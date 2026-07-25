"""
食品配料分析网站 - Flask 后端
"""
import json
import re
import sqlite3
import os
from datetime import datetime
from functools import wraps
from flask import Flask, render_template, request, jsonify, session, redirect, url_for, g
from werkzeug.security import generate_password_hash, check_password_hash
from additives_data import ADDITIVES, DISEASE_ADDITIVE_MAP, DIETARY_RESTRICTION_MAP

app = Flask(__name__)
app.secret_key = 'food-additive-analyzer-secret-key-2024'

DATABASE = 'food_analyzer.db'


# ==================== 数据库操作 ====================

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA journal_mode=WAL")
        g.db.execute("PRAGMA foreign_keys=ON")
    return g.db


@app.teardown_appcontext
def close_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db():
    """初始化数据库表"""
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            age INTEGER,
            gender TEXT,
            diseases TEXT DEFAULT '[]',
            allergies TEXT DEFAULT '[]',
            dietary_restrictions TEXT DEFAULT '[]',
            custom_notes TEXT DEFAULT '',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scan_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            food_name TEXT DEFAULT '',
            ingredients_text TEXT NOT NULL,
            result_json TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')

    # 创建索引
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_scan_user ON scan_history(user_id)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_scan_date ON scan_history(created_at)')

    db.commit()
    db.close()


# ==================== 认证装饰器 ====================

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            if request.is_json:
                return jsonify({"error": "请先登录"}), 401
            return redirect(url_for('login_page'))
        return f(*args, **kwargs)
    return decorated_function


# ==================== 页面路由 ====================

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login_page'))


@app.route('/login')
def login_page():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')


@app.route('/register')
def register_page():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return render_template('register.html')


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/profile')
@login_required
def profile_page():
    return render_template('profile.html')


@app.route('/history')
@login_required
def history_page():
    return render_template('history.html')


@app.route('/result/<int:scan_id>')
@login_required
def result_page(scan_id):
    return render_template('result.html', scan_id=scan_id)


# ==================== API - 认证 ====================

@app.route('/api/register', methods=['POST'])
def api_register():
    data = request.get_json()
    if not data:
        return jsonify({"error": "无效的请求数据"}), 400

    username = data.get('username', '').strip()
    password = data.get('password', '').strip()

    if not username or not password:
        return jsonify({"error": "用户名和密码不能为空"}), 400
    if len(username) < 2 or len(username) > 20:
        return jsonify({"error": "用户名长度应为2-20个字符"}), 400
    if len(password) < 6:
        return jsonify({"error": "密码长度至少6个字符"}), 400

    db = get_db()
    existing = db.execute('SELECT id FROM users WHERE username = ?', (username,)).fetchone()
    if existing:
        return jsonify({"error": "该用户名已被注册"}), 400

    password_hash = generate_password_hash(password, method='pbkdf2:sha256')

    diseases = json.dumps(data.get('diseases', []), ensure_ascii=False)
    allergies = json.dumps(data.get('allergies', []), ensure_ascii=False)
    dietary_restrictions = json.dumps(data.get('dietary_restrictions', []), ensure_ascii=False)

    db.execute('''
        INSERT INTO users (username, password_hash, age, gender, diseases, allergies, dietary_restrictions, custom_notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        username,
        password_hash,
        data.get('age'),
        data.get('gender', ''),
        diseases,
        allergies,
        dietary_restrictions,
        data.get('custom_notes', '')
    ))
    db.commit()

    return jsonify({"success": True, "message": "注册成功！请登录。"})


@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.get_json()
    if not data:
        return jsonify({"error": "无效的请求数据"}), 400

    username = data.get('username', '').strip()
    password = data.get('password', '').strip()

    if not username or not password:
        return jsonify({"error": "用户名和密码不能为空"}), 400

    db = get_db()
    user = db.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()

    if not user or not check_password_hash(user['password_hash'], password):
        return jsonify({"error": "用户名或密码错误"}), 401

    session['user_id'] = user['id']
    session['username'] = user['username']

    return jsonify({"success": True, "message": "登录成功！"})


@app.route('/api/logout', methods=['POST'])
def api_logout():
    session.clear()
    return jsonify({"success": True, "message": "已退出登录"})


# ==================== API - 用户资料 ====================

@app.route('/api/user/profile', methods=['GET'])
@login_required
def api_get_profile():
    db = get_db()
    user = db.execute('SELECT * FROM users WHERE id = ?', (session['user_id'],)).fetchone()
    if not user:
        session.clear()
        return jsonify({"error": "用户不存在"}), 404

    return jsonify({
        "username": user['username'],
        "age": user['age'],
        "gender": user['gender'],
        "diseases": json.loads(user['diseases']),
        "allergies": json.loads(user['allergies']),
        "dietary_restrictions": json.loads(user['dietary_restrictions']),
        "custom_notes": user['custom_notes'],
        "created_at": user['created_at']
    })


@app.route('/api/user/profile', methods=['PUT'])
@login_required
def api_update_profile():
    data = request.get_json()
    if not data:
        return jsonify({"error": "无效的请求数据"}), 400

    db = get_db()
    db.execute('''
        UPDATE users SET
            age = ?,
            gender = ?,
            diseases = ?,
            allergies = ?,
            dietary_restrictions = ?,
            custom_notes = ?
        WHERE id = ?
    ''', (
        data.get('age'),
        data.get('gender', ''),
        json.dumps(data.get('diseases', []), ensure_ascii=False),
        json.dumps(data.get('allergies', []), ensure_ascii=False),
        json.dumps(data.get('dietary_restrictions', []), ensure_ascii=False),
        data.get('custom_notes', ''),
        session['user_id']
    ))
    db.commit()

    return jsonify({"success": True, "message": "个人资料更新成功！"})


# ==================== API - 配料分析 ====================

def normalize_text(text):
    """标准化文本：去标点、转小写"""
    # 移除常见标点符号，但保留中文
    text = re.sub(r'[，,、。\.；;：:！!？?\s（）()\[\]【】""''「」『』《》—…·/|@#$%^&*+=-]', ' ', text)
    # 规范化空格
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def extract_ingredients(text):
    """从配料文本中提取配料列表"""
    text = text.strip()

    # 尝试多个分隔符
    separators = ['，', ',', '、', '；', ';', '\n', '\r']

    # 检测主要分隔符
    ingredients = [text]
    for sep in separators:
        if sep in text:
            # 使用最常见的分隔符
            if sep in [',', '，', '、']:
                parts = re.split(r'[,，、]', text)
                ingredients = [p.strip() for p in parts if p.strip()]
                break

    # 如果以换行为主
    if len(ingredients) == 1 and '\n' in text:
        ingredients = [p.strip() for p in text.split('\n') if p.strip()]

    # 过滤太短或太长的
    ingredients = [i for i in ingredients if 1 < len(i) < 200]

    # 如果没有明确分隔符，也尝试按句号分割
    if len(ingredients) <= 1:
        ingredients = [i.strip() for i in re.split(r'[，,、。；;]', text) if i.strip() and len(i.strip()) > 1]

    return ingredients


def match_additives(ingredients_list):
    """在配料列表中匹配已知添加剂"""
    found_harmful = []
    found_beneficial = []
    all_found_set = set()

    for ingredient in ingredients_list:
        ingredient_lower = ingredient.lower().strip()

        for add in ADDITIVES:
            # 检查主名称
            if add['name'].lower() in ingredient_lower or ingredient_lower in add['name'].lower():
                if add['category'] == 'harmful':
                    if add['name'] not in all_found_set:
                        found_harmful.append({
                            "name": add['name'],
                            "risk_level": add['risk_level'],
                            "description": add['description'],
                            "common_in": add.get('common_in', ''),
                            "advice": add.get('advice', ''),
                            "matched_ingredient": ingredient
                        })
                        all_found_set.add(add['name'])
                else:
                    if add['name'] not in all_found_set:
                        found_beneficial.append({
                            "name": add['name'],
                            "description": add['description'],
                            "benefits": add.get('benefits', []),
                            "common_in": add.get('common_in', ''),
                            "matched_ingredient": ingredient
                        })
                        all_found_set.add(add['name'])
                break

            # 检查别名
            for alias in add.get('aliases', []):
                if alias.lower() in ingredient_lower or ingredient_lower in alias.lower():
                    if add['category'] == 'harmful':
                        if add['name'] not in all_found_set:
                            found_harmful.append({
                                "name": add['name'],
                                "risk_level": add['risk_level'],
                                "description": add['description'],
                                "common_in": add.get('common_in', ''),
                                "advice": add.get('advice', ''),
                                "matched_ingredient": ingredient
                            })
                            all_found_set.add(add['name'])
                    else:
                        if add['name'] not in all_found_set:
                            found_beneficial.append({
                                "name": add['name'],
                                "description": add['description'],
                                "benefits": add.get('benefits', []),
                                "common_in": add.get('common_in', ''),
                                "matched_ingredient": ingredient
                            })
                            all_found_set.add(add['name'])
                    break

    return found_harmful, found_beneficial


def analyze_suitability(user_diseases, user_restrictions, harmful_list):
    """分析食品是否适合该用户"""
    warnings = []
    high_risk_items = []
    disease_warnings = []

    # 检查疾病相关警告
    for disease in user_diseases:
        if disease in DISEASE_ADDITIVE_MAP:
            disease_info = DISEASE_ADDITIVE_MAP[disease]
            conflict_additives = []

            for item in harmful_list:
                if item['name'] in disease_info['harmful']:
                    conflict_additives.append(item)

            if conflict_additives:
                disease_warnings.append({
                    "disease": disease,
                    "warning": disease_info['warning'],
                    "conflict_additives": conflict_additives
                })
                # 收集高风险项
                for item in conflict_additives:
                    if item['risk_level'] == 'high':
                        high_risk_items.append(f"{item['name']}（{disease}风险）")

    # 检查忌口相关警告
    for restriction in user_restrictions:
        if restriction in DIETARY_RESTRICTION_MAP:
            restriction_info = DIETARY_RESTRICTION_MAP[restriction]
            conflict_additives = []

            for item in harmful_list:
                if item['name'] in restriction_info.get('harmful', []):
                    conflict_additives.append(item)

            if conflict_additives:
                warnings.append({
                    "type": "restriction",
                    "restriction": restriction,
                    "message": restriction_info.get('note', ''),
                    "conflict_additives": conflict_additives
                })

    # 确定适合度
    all_high_risk = [h for h in harmful_list if h['risk_level'] == 'high']
    all_medium_risk = [h for h in harmful_list if h['risk_level'] == 'medium']

    if disease_warnings:
        high_disease_conflicts = any(
            any(item['risk_level'] == 'high' for item in dw['conflict_additives'])
            for dw in disease_warnings
        )
        if high_disease_conflicts:
            suitability = "not_recommended"
            suitability_text = "⚠️ 不建议食用"
            suitability_detail = "该食品含有的添加剂与您的健康状况存在显著冲突，建议避免食用。"
        else:
            suitability = "caution"
            suitability_text = "⚠️ 谨慎食用"
            suitability_detail = "该食品含有的添加剂与您的健康状况存在一定关联，建议少量食用或咨询医生。"
    elif len(all_high_risk) >= 2 and not user_diseases:
        suitability = "caution"
        suitability_text = "⚡ 需注意"
        suitability_detail = "该食品含有多种高风险添加剂，即使您没有相关疾病史，也建议谨慎食用。"
    elif len(all_high_risk) >= 1 and not user_diseases:
        suitability = "moderate"
        suitability_text = "🔶 一般"
        suitability_detail = "该食品含有高风险添加剂，但未发现与您健康状况的直接冲突。建议适量食用。"
    else:
        suitability = "safe"
        suitability_text = "✅ 可以食用"
        suitability_detail = "该食品未发现与您健康状况冲突的有害添加剂。"

    return {
        "suitability": suitability,
        "suitability_text": suitability_text,
        "suitability_detail": suitability_detail,
        "disease_warnings": disease_warnings,
        "dietary_warnings": warnings,
        "high_risk_count": len(all_high_risk),
        "medium_risk_count": len(all_medium_risk)
    }


@app.route('/api/analyze', methods=['POST'])
@login_required
def api_analyze():
    data = request.get_json()
    if not data:
        return jsonify({"error": "无效的请求数据"}), 400

    ingredients_text = data.get('ingredients', '').strip()
    food_name = data.get('food_name', '').strip()

    if not ingredients_text:
        return jsonify({"error": "请输入配料表内容"}), 400

    if len(ingredients_text) < 3:
        return jsonify({"error": "配料表内容太短，请输入完整的配料表"}), 400

    # 获取用户信息
    db = get_db()
    user = db.execute('SELECT * FROM users WHERE id = ?', (session['user_id'],)).fetchone()
    if not user:
        return jsonify({"error": "用户不存在"}), 404

    user_diseases = json.loads(user['diseases'])
    user_allergies = json.loads(user['allergies'])
    user_restrictions = json.loads(user['dietary_restrictions'])

    # 提取配料
    ingredients_list = extract_ingredients(ingredients_text)

    # 匹配添加剂
    harmful_list, beneficial_list = match_additives(ingredients_list)

    # 分析适合度
    suitability = analyze_suitability(user_diseases, user_restrictions, harmful_list)

    # 构建结果
    result = {
        "food_name": food_name or "未命名食品",
        "ingredients_text": ingredients_text,
        "ingredients_count": len(ingredients_list),
        "ingredients_list": ingredients_list,
        "harmful_additives": harmful_list,
        "harmful_count": len(harmful_list),
        "beneficial_ingredients": beneficial_list,
        "beneficial_count": len(beneficial_list),
        "suitability": suitability,
        "user_diseases": user_diseases,
        "user_restrictions": user_restrictions,
        "user_allergies": user_allergies,
        "analyzed_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    # 保存扫描历史
    result_json = json.dumps(result, ensure_ascii=False)
    db.execute('''
        INSERT INTO scan_history (user_id, food_name, ingredients_text, result_json)
        VALUES (?, ?, ?, ?)
    ''', (session['user_id'], food_name or "未命名食品", ingredients_text, result_json))
    db.commit()

    scan_id = db.execute('SELECT last_insert_rowid()').fetchone()[0]
    result['scan_id'] = scan_id

    return jsonify(result)


@app.route('/api/scan/<int:scan_id>', methods=['GET'])
@login_required
def api_get_scan(scan_id):
    db = get_db()
    scan = db.execute(
        'SELECT * FROM scan_history WHERE id = ? AND user_id = ?',
        (scan_id, session['user_id'])
    ).fetchone()

    if not scan:
        return jsonify({"error": "扫描记录不存在"}), 404

    result = json.loads(scan['result_json'])
    result['scan_id'] = scan['id']
    result['food_name'] = scan['food_name']
    result['created_at'] = scan['created_at']
    return jsonify(result)


@app.route('/api/scans', methods=['GET'])
@login_required
def api_get_scans():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    offset = (page - 1) * per_page

    db = get_db()
    scans = db.execute('''
        SELECT id, food_name, ingredients_text,
               json_extract(result_json, '$.harmful_count') as harmful_count,
               json_extract(result_json, '$.beneficial_count') as beneficial_count,
               json_extract(result_json, '$.suitability.suitability') as suitability,
               created_at
        FROM scan_history
        WHERE user_id = ?
        ORDER BY created_at DESC
        LIMIT ? OFFSET ?
    ''', (session['user_id'], per_page, offset)).fetchall()

    total = db.execute(
        'SELECT COUNT(*) FROM scan_history WHERE user_id = ?',
        (session['user_id'],)
    ).fetchone()[0]

    return jsonify({
        "scans": [dict(row) for row in scans],
        "total": total,
        "page": page,
        "per_page": per_page,
        "total_pages": max(1, (total + per_page - 1) // per_page)
    })


@app.route('/api/scan/<int:scan_id>', methods=['DELETE'])
@login_required
def api_delete_scan(scan_id):
    db = get_db()
    db.execute('DELETE FROM scan_history WHERE id = ? AND user_id = ?', (scan_id, session['user_id']))
    db.commit()
    return jsonify({"success": True, "message": "记录已删除"})


# ==================== API - 选项数据 ====================

@app.route('/api/options', methods=['GET'])
def api_get_options():
    """返回前端下拉选项"""
    return jsonify({
        "diseases": [
            {"value": "高血压", "label": "高血压"},
            {"value": "糖尿病", "label": "糖尿病"},
            {"value": "心脏病", "label": "心脏病"},
            {"value": "高血脂", "label": "高血脂"},
            {"value": "脂肪肝", "label": "脂肪肝"},
            {"value": "肥胖", "label": "肥胖/超重"},
            {"value": "肾脏病", "label": "肾脏病"},
            {"value": "痛风", "label": "痛风"},
            {"value": "高尿酸血症", "label": "高尿酸血症"},
            {"value": "过敏体质", "label": "过敏体质"},
            {"value": "哮喘", "label": "哮喘"},
            {"value": "胃病", "label": "胃病/胃炎"},
            {"value": "肠道疾病", "label": "肠道疾病（肠炎/IBS等）"},
            {"value": "肝脏疾病", "label": "肝脏疾病"},
            {"value": "甲状腺问题", "label": "甲状腺功能异常"},
            {"value": "骨质疏松", "label": "骨质疏松"},
            {"value": "偏头痛", "label": "偏头痛"},
            {"value": "苯丙酮尿症", "label": "苯丙酮尿症（PKU）"},
            {"value": "ADHD", "label": "注意力缺陷多动障碍（ADHD）"},
        ],
        "allergies": [
            {"value": "花生", "label": "花生"},
            {"value": "坚果", "label": "坚果（杏仁、核桃等）"},
            {"value": "牛奶", "label": "牛奶/乳制品"},
            {"value": "鸡蛋", "label": "鸡蛋"},
            {"value": "大豆", "label": "大豆"},
            {"value": "小麦", "label": "小麦/麸质"},
            {"value": "海鲜", "label": "海鲜/贝类"},
            {"value": "鱼类", "label": "鱼类"},
            {"value": "芝麻", "label": "芝麻"},
            {"value": "亚硫酸盐", "label": "亚硫酸盐"},
            {"value": "味精", "label": "味精/MSG"},
            {"value": "食用色素", "label": "合成食用色素"},
            {"value": "防腐剂", "label": "防腐剂"},
        ],
        "dietary_restrictions": [
            {"value": "素食", "label": "素食"},
            {"value": "清真", "label": "清真饮食"},
            {"value": "无麸质", "label": "无麸质饮食"},
            {"value": "低钠饮食", "label": "低钠饮食"},
            {"value": "低糖饮食", "label": "低糖/戒糖"},
            {"value": "无乳糖", "label": "无乳糖饮食"},
            {"value": "孕妇", "label": "孕期饮食注意"},
            {"value": "儿童", "label": "儿童饮食注意"},
            {"value": "老年人", "label": "老年人饮食注意"},
        ],
        "genders": [
            {"value": "male", "label": "男"},
            {"value": "female", "label": "女"},
            {"value": "other", "label": "其他"},
        ]
    })


# ==================== 启动 ====================

if __name__ == '__main__':
    init_db()
    print("=" * 60)
    print("  食品配料分析网站已启动！")
    print("  请在浏览器访问: http://127.0.0.1:5000")
    print("=" * 60)
    app.run(debug=True, host='0.0.0.0', port=5000)
