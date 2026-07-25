"""
食品添加剂知识库
包含有害添加剂和有益成分的数据
"""

ADDITIVES = [
    # ========== 有害添加剂 ==========
    {
        "name": "亚硝酸钠",
        "aliases": ["亚硝酸盐", "硝酸钠", "sodium nitrite", "nitrite"],
        "category": "harmful",
        "risk_level": "high",
        "description": "防腐剂和护色剂，常用于加工肉制品。在体内可转化为致癌物亚硝胺，长期摄入增加胃癌、食道癌风险。",
        "related_diseases": ["高血压", "心脏病", "胃病"],
        "common_in": "火腿、香肠、培根、腊肉、罐头肉制品",
        "advice": "尽量避免食用。维生素C可抑制亚硝胺的形成。"
    },
    {
        "name": "苯甲酸钠",
        "aliases": ["苯甲酸", "sodium benzoate", "benzoate"],
        "category": "harmful",
        "risk_level": "medium",
        "description": "常见防腐剂，在酸性环境下可能与维生素C反应生成苯（致癌物）。可能引起过敏反应。",
        "related_diseases": ["过敏体质", "哮喘"],
        "common_in": "碳酸饮料、果汁、酱油、酱菜、果酱",
        "advice": "尽量选择不含苯甲酸钠的产品，特别是儿童食品。"
    },
    {
        "name": "山梨酸钾",
        "aliases": ["山梨酸", "potassium sorbate", "sorbate"],
        "category": "harmful",
        "risk_level": "low",
        "description": "防腐剂，相对安全性较高，但过量摄入可能引起胃肠道不适和过敏反应。",
        "related_diseases": ["过敏体质", "胃病"],
        "common_in": "乳制品、烘焙食品、饮料、果酱、腌制食品",
        "advice": "相对安全的防腐剂，但仍建议适量摄入。"
    },
    {
        "name": "阿斯巴甜",
        "aliases": ["阿斯巴坦", "aspartame", "蛋白糖"],
        "category": "harmful",
        "risk_level": "medium",
        "description": "人工合成甜味剂，甜度为蔗糖的200倍。苯丙酮尿症患者禁用。部分研究认为可能与头痛、情绪问题有关。",
        "related_diseases": ["苯丙酮尿症", "糖尿病", "偏头痛"],
        "common_in": "无糖饮料、口香糖、低糖食品、餐桌甜味剂",
        "advice": "苯丙酮尿症患者严格禁用。普通人群建议适量摄入。"
    },
    {
        "name": "糖精钠",
        "aliases": ["糖精", "saccharin", "saccharin sodium"],
        "category": "harmful",
        "risk_level": "medium",
        "description": "最古老的人工甜味剂，甜度为蔗糖的300-500倍。动物实验显示大剂量可能致癌，但人体证据不足。",
        "related_diseases": ["糖尿病", "肥胖"],
        "common_in": "无糖饮料、蜜饯、果冻、牙膏",
        "advice": "建议孕妇和儿童避免摄入。"
    },
    {
        "name": "安赛蜜",
        "aliases": ["乙酰磺胺酸钾", "acesulfame K", "AK糖", "acesulfame potassium"],
        "category": "harmful",
        "risk_level": "low",
        "description": "人工合成甜味剂，不被人体代谢。长期大量摄入的安全性存在争议。",
        "related_diseases": ["糖尿病"],
        "common_in": "无糖饮料、烘焙食品、口香糖、糖果",
        "advice": "适量摄入，不要过度依赖无糖产品。"
    },
    {
        "name": "三氯蔗糖",
        "aliases": ["蔗糖素", "sucralose", "splenda"],
        "category": "harmful",
        "risk_level": "low",
        "description": "以蔗糖为原料的氯化甜味剂，甜度为蔗糖的600倍。高温烹饪时可能产生有害物质。",
        "related_diseases": ["糖尿病", "肠道疾病"],
        "common_in": "无糖饮料、蛋白棒、烘焙食品、调味品",
        "advice": "避免高温加热使用。"
    },
    {
        "name": "柠檬黄",
        "aliases": ["酒石黄", "tartrazine", "FD&C Yellow 5", "黄色4号"],
        "category": "harmful",
        "risk_level": "medium",
        "description": "合成食用色素。可能引起儿童多动症、注意力不集中。过敏体质者可能出现荨麻疹、哮喘。",
        "related_diseases": ["过敏体质", "哮喘", "ADHD"],
        "common_in": "糖果、饮料、冰淇淋、果冻、零食、调味酱",
        "advice": "儿童应尽量避免摄入。过敏体质者需注意。"
    },
    {
        "name": "日落黄",
        "aliases": ["sunset yellow", "FD&C Yellow 6", "黄色5号"],
        "category": "harmful",
        "risk_level": "medium",
        "description": "合成食用色素。可能引起过敏反应、儿童多动症。部分国家已限制使用。",
        "related_diseases": ["过敏体质", "ADHD"],
        "common_in": "糖果、饮料、糕点、零食、果冻",
        "advice": "尽量选择天然色素的食品。"
    },
    {
        "name": "胭脂红",
        "aliases": ["ponceau 4R", "cochineal red A", "红色7号", "丽春红"],
        "category": "harmful",
        "risk_level": "medium",
        "description": "合成食用色素。可能引起过敏反应、哮喘。动物实验显示可能有致癌风险。",
        "related_diseases": ["过敏体质", "哮喘"],
        "common_in": "糖果、饮料、果冻、肉制品、调味酱",
        "advice": "尽量选择天然色素替代产品。"
    },
    {
        "name": "诱惑红",
        "aliases": ["allura red", "FD&C Red 40", "红色40号"],
        "category": "harmful",
        "risk_level": "medium",
        "description": "合成食用色素。可能引起儿童多动症和注意力问题。过敏体质者可能出现反应。",
        "related_diseases": ["过敏体质", "ADHD"],
        "common_in": "糖果、饮料、零食、甜点、早餐麦片",
        "advice": "儿童应尽量避免。"
    },
    {
        "name": "亮蓝",
        "aliases": ["brilliant blue", "FD&C Blue 1", "蓝色1号"],
        "category": "harmful",
        "risk_level": "low",
        "description": "合成食用色素。吸收率低，大部分随粪便排出。但仍有过敏反应的报道。",
        "related_diseases": ["过敏体质"],
        "common_in": "糖果、饮料、冰淇淋、烘焙食品",
        "advice": "相对较安全的合成色素，但仍建议适量。"
    },
    {
        "name": "味精",
        "aliases": ["谷氨酸钠", "MSG", "monosodium glutamate", "味之素"],
        "category": "harmful",
        "risk_level": "low",
        "description": "增味剂，广泛使用。部分人群可能出现「味精综合征」：头痛、口渴、心悸等。但科学证据表明适量摄入对多数人安全。",
        "related_diseases": ["高血压", "偏头痛", "心脏病"],
        "common_in": "调味品、方便面、零食、酱料、冷冻食品、汤料",
        "advice": "高血压患者注意钠含量。敏感人群出现不适应减少摄入。"
    },
    {
        "name": "5'-呈味核苷酸二钠",
        "aliases": ["呈味核苷酸二钠", "I+G", "disodium 5'-ribonucleotide"],
        "category": "harmful",
        "risk_level": "low",
        "description": "增味剂，常与味精配合使用增强鲜味。痛风患者需注意嘌呤代谢问题。",
        "related_diseases": ["痛风", "高尿酸血症"],
        "common_in": "方便面、调味料、零食、酱料、鸡精",
        "advice": "痛风和高尿酸患者需限量摄入。"
    },
    {
        "name": "亚铁氰化钾",
        "aliases": ["potassium ferrocyanide", "黄血盐"],
        "category": "harmful",
        "risk_level": "low",
        "description": "食盐抗结剂。正常使用下安全，但与酸反应或在高温下可能产生氰化物。",
        "related_diseases": ["肾脏病"],
        "common_in": "食盐、调味盐",
        "advice": "选择无抗结剂的天然海盐或岩盐。"
    },
    {
        "name": "二氧化钛",
        "aliases": ["钛白粉", "titanium dioxide", "TiO2", "E171"],
        "category": "harmful",
        "risk_level": "medium",
        "description": "白色素和增白剂。欧盟已禁止在食品中使用（2022年）。纳米级二氧化钛可能损害肠道健康和DNA。",
        "related_diseases": ["肠道疾病", "免疫系统疾病"],
        "common_in": "糖果、口香糖、糖霜、白色酱料、咖啡伴侣",
        "advice": "尽量选择不含二氧化钛的产品。"
    },
    {
        "name": "BHA",
        "aliases": ["丁基羟基茴香醚", "butylated hydroxyanisole", "叔丁基对羟基茴香醚"],
        "category": "harmful",
        "risk_level": "high",
        "description": "抗氧化剂（防腐）。国际癌症研究机构(IARC)将其列为可能的人类致癌物（2B类）。",
        "related_diseases": ["过敏体质", "肝脏疾病"],
        "common_in": "油炸食品、烘焙食品、方便面、零食、油脂",
        "advice": "建议避免摄入。寻找使用天然抗氧化剂（如维生素E）的产品。"
    },
    {
        "name": "BHT",
        "aliases": ["二丁基羟基甲苯", "butylated hydroxytoluene", "2,6-二叔丁基对甲酚"],
        "category": "harmful",
        "risk_level": "medium",
        "description": "抗氧化剂（防腐）。与BHA类似，大剂量动物实验显示可能影响肝脏和甲状腺功能。",
        "related_diseases": ["肝脏疾病", "甲状腺问题"],
        "common_in": "油炸食品、麦片、零食、油脂、口香糖",
        "advice": "尽量选择不含BHT的产品。"
    },
    {
        "name": "亚硫酸盐",
        "aliases": ["二氧化硫", "sulfites", "sulfur dioxide", "亚硫酸钠", "焦亚硫酸钠", "低亚硫酸钠"],
        "category": "harmful",
        "risk_level": "medium",
        "description": "防腐剂和漂白剂。哮喘患者可能产生严重过敏反应。破坏维生素B1。",
        "related_diseases": ["哮喘", "过敏体质", "维生素B1缺乏"],
        "common_in": "果干、葡萄酒、果汁、腌制品、冷冻海鲜",
        "advice": "哮喘患者严格注意。食用前可用水浸泡果干以减少残留。"
    },
    {
        "name": "磷酸盐",
        "aliases": ["磷酸钠", "磷酸钾", "磷酸钙", "phosphates", "三聚磷酸钠", "六偏磷酸钠"],
        "category": "harmful",
        "risk_level": "medium",
        "description": "水分保持剂和膨松剂。过量摄入影响钙吸收，增加肾脏负担。慢性肾病患者需严格控制。",
        "related_diseases": ["肾脏病", "骨质疏松", "心血管疾病"],
        "common_in": "加工肉制品、加工奶酪、碳酸饮料、烘焙食品、方便面",
        "advice": "肾病患者严格限制。健康人群也应注意不要过量。"
    },
    {
        "name": "反式脂肪酸",
        "aliases": ["反式脂肪", "trans fat", "氢化植物油", "部分氢化油", "起酥油", "人造黄油", "植脂末"],
        "category": "harmful",
        "risk_level": "high",
        "description": "增加坏胆固醇(LDL)，降低好胆固醇(HDL)，显著增加心血管疾病风险。WHO建议完全消除工业反式脂肪。",
        "related_diseases": ["心脏病", "高血压", "糖尿病", "肥胖", "高血脂"],
        "common_in": "油炸食品、烘焙食品、人造奶油、饼干、薯片、奶茶、咖啡伴侣",
        "advice": "严格避免摄入。查看配料表中的「氢化」、「部分氢化」、「起酥油」等字样。"
    },
    {
        "name": "高果糖玉米糖浆",
        "aliases": ["果葡糖浆", "高果糖浆", "HFCS", "high fructose corn syrup", "玉米糖浆", "葡萄糖果糖浆"],
        "category": "harmful",
        "risk_level": "high",
        "description": "工业生产的甜味剂，果糖含量高。过量摄入导致脂肪肝、胰岛素抵抗、肥胖、痛风风险增加。",
        "related_diseases": ["脂肪肝", "糖尿病", "肥胖", "痛风", "高血脂", "心脏病"],
        "common_in": "碳酸饮料、果汁饮料、调味酸奶、酱料、烘焙食品、零食",
        "advice": "严格限制摄入。注意配料表中的「果葡糖浆」、「玉米糖浆」等。"
    },
    {
        "name": "卡拉胶",
        "aliases": ["角叉菜胶", "carrageenan", "鹿角菜胶"],
        "category": "harmful",
        "risk_level": "medium",
        "description": "增稠剂和稳定剂。降解型卡拉胶可能引起肠道炎症。部分研究认为与炎症性肠病有关。",
        "related_diseases": ["肠道疾病", "炎症性肠病", "甲状腺问题"],
        "common_in": "冰淇淋、巧克力牛奶、豆奶、椰奶、果冻、宠物食品",
        "advice": "肠道敏感人群建议选择不含卡拉胶的产品。"
    },
    {
        "name": "溴酸钾",
        "aliases": ["potassium bromate", "溴酸钾盐"],
        "category": "harmful",
        "risk_level": "high",
        "description": "面粉处理剂和面团改良剂。已被IARC列为可能致癌物（2B类）。中国、欧盟、加拿大等多国已禁用。",
        "related_diseases": ["肾脏病", "甲状腺问题"],
        "common_in": "面包、烘焙食品（进口产品中可能出现）",
        "advice": "购买面包时选择正规品牌。中国已禁止使用。"
    },
    {
        "name": "铝",
        "aliases": ["硫酸铝钾", "硫酸铝铵", "明矾", "aluminum", "钾明矾", "铵明矾"],
        "category": "harmful",
        "risk_level": "high",
        "description": "膨松剂。铝在体内蓄积可能损害神经系统，与阿尔茨海默病有关。影响钙磷代谢。",
        "related_diseases": ["肾脏病", "骨质疏松", "神经系统疾病"],
        "common_in": "油条、粉条、粉丝、膨化食品、发酵粉",
        "advice": "尽量选择无铝膨松剂产品。传统油条含铝量高，建议少食。"
    },
    {
        "name": "甜蜜素",
        "aliases": ["环己基氨基磺酸钠", "cyclamate", "sodium cyclamate"],
        "category": "harmful",
        "risk_level": "medium",
        "description": "人工合成甜味剂。美国因动物实验显示可能致癌而禁用。中国允许限量使用。",
        "related_diseases": ["糖尿病", "肝脏疾病"],
        "common_in": "蜜饯、果冻、饮料、冰淇淋、糕点",
        "advice": "孕妇和儿童建议避免。"
    },
    {
        "name": "脱氢乙酸钠",
        "aliases": ["脱氢醋酸钠", "sodium dehydroacetate"],
        "category": "harmful",
        "risk_level": "medium",
        "description": "防腐剂。中国2025年起已在淀粉制品、烘焙食品等中禁用。长期过量摄入可能影响肝肾功能。",
        "related_diseases": ["肝脏疾病", "肾脏病"],
        "common_in": "糕点、面包、月饼、酱菜（需注意产品日期）",
        "advice": "尽量选择新鲜烘焙食品，避免含此添加剂的产品。"
    },

    # ========== 有益成分 ==========
    {
        "name": "维生素C",
        "aliases": ["抗坏血酸", "vitamin C", "ascorbic acid", "VC", "L-抗坏血酸"],
        "category": "beneficial",
        "description": "强效抗氧化剂，增强免疫力，促进铁吸收，帮助胶原蛋白合成，保护细胞免受氧化损伤。",
        "benefits": ["增强免疫力", "抗氧化", "促进铁吸收", "皮肤健康", "伤口愈合"],
        "common_in": "柑橘类水果、猕猴桃、草莓、西兰花、彩椒、番茄"
    },
    {
        "name": "维生素D",
        "aliases": ["vitamin D", "维生素D3", "胆钙化醇", "cholecalciferol", "VD"],
        "category": "beneficial",
        "description": "促进钙吸收和骨骼健康，调节免疫功能，改善情绪。多数中国人缺乏维生素D。",
        "benefits": ["骨骼健康", "增强免疫力", "改善情绪", "促进钙吸收", "预防骨质疏松"],
        "common_in": "蛋黄、肝类、富含脂肪的鱼类、强化牛奶、蘑菇"
    },
    {
        "name": "维生素E",
        "aliases": ["生育酚", "vitamin E", "tocopherol", "VE", "混合生育酚"],
        "category": "beneficial",
        "description": "天然抗氧化剂，保护细胞膜，延缓衰老，保护心血管健康。",
        "benefits": ["抗氧化", "延缓衰老", "心血管保护", "皮肤健康", "护发"],
        "common_in": "坚果、种子、植物油、牛油果、菠菜、全谷物"
    },
    {
        "name": "维生素B族",
        "aliases": ["维生素B1", "维生素B2", "维生素B6", "维生素B12", "vitamin B", "硫胺素", "核黄素", "烟酸", "叶酸"],
        "category": "beneficial",
        "description": "参与能量代谢，维持神经系统健康，帮助红血球生成，预防贫血。",
        "benefits": ["能量代谢", "神经系统健康", "预防贫血", "皮肤健康", "减轻疲劳"],
        "common_in": "全谷物、瘦肉、鸡蛋、豆类、绿叶蔬菜、坚果"
    },
    {
        "name": "钙",
        "aliases": ["calcium", "碳酸钙", "乳酸钙", "磷酸钙", "钙质", "Ca"],
        "category": "beneficial",
        "description": "骨骼和牙齿的主要成分，参与神经传导和肌肉收缩。中国人缺钙较为普遍。",
        "benefits": ["骨骼健康", "牙齿健康", "神经传导", "肌肉功能", "预防骨质疏松"],
        "common_in": "牛奶、酸奶、奶酪、豆腐、芝麻酱、小鱼干、绿叶蔬菜"
    },
    {
        "name": "铁",
        "aliases": ["iron", "铁质", "Fe", "富马酸亚铁", "硫酸亚铁", "血红素铁"],
        "category": "beneficial",
        "description": "血红蛋白的关键成分，运输氧气至全身。缺铁性贫血是全球最常见的营养缺乏症。",
        "benefits": ["预防贫血", "增强体力", "改善注意力", "增强免疫力", "促进生长发育"],
        "common_in": "红肉、动物肝脏、动物血、菠菜、红枣、黑木耳、豆类"
    },
    {
        "name": "锌",
        "aliases": ["zinc", "锌元素", "Zn", "葡萄糖酸锌", "氧化锌"],
        "category": "beneficial",
        "description": "参与300多种酶的活性，支持免疫系统、伤口愈合和味觉。",
        "benefits": ["增强免疫力", "伤口愈合", "味觉维持", "皮肤健康", "生长发育"],
        "common_in": "牡蛎、牛肉、南瓜子、腰果、蛋黄、全谷物"
    },
    {
        "name": "膳食纤维",
        "aliases": ["纤维素", "dietary fiber", "fiber", "聚葡萄糖", "菊粉", "低聚果糖", "抗性糊精"],
        "category": "beneficial",
        "description": "促进肠道蠕动，预防便秘，降低胆固醇，稳定血糖，增加饱腹感。益生元纤维还能滋养肠道有益菌。",
        "benefits": ["肠道健康", "降低胆固醇", "稳定血糖", "增加饱腹感", "预防便秘", "滋养益生菌"],
        "common_in": "全谷物、燕麦、豆类、蔬菜、水果、坚果、种子"
    },
    {
        "name": "蛋白质",
        "aliases": ["protein", "乳清蛋白", "大豆蛋白", "豌豆蛋白", "胶原蛋白", "氨基酸"],
        "category": "beneficial",
        "description": "身体组织的基本构建块。维持肌肉、骨骼、皮肤、头发和酶的正常功能。",
        "benefits": ["肌肉生长", "组织修复", "增强免疫力", "维持饱腹感", "骨骼健康"],
        "common_in": "肉类、鱼类、鸡蛋、牛奶、豆类、坚果、豆腐"
    },
    {
        "name": "Omega-3",
        "aliases": ["欧米伽3", "ω-3", "DHA", "EPA", "α-亚麻酸", "omega-3 fatty acids", "鱼油"],
        "category": "beneficial",
        "description": "必需脂肪酸，抗炎作用，保护心脑血管，促进大脑和视力发育。",
        "benefits": ["心血管保护", "抗炎", "大脑健康", "视力保护", "降低甘油三酯", "改善情绪"],
        "common_in": "深海鱼（三文鱼、沙丁鱼）、亚麻籽、奇亚籽、核桃、藻油"
    },
    {
        "name": "益生菌",
        "aliases": ["probiotics", "乳酸菌", "双歧杆菌", "嗜酸乳杆菌", "乳双歧杆菌", "鼠李糖乳杆菌"],
        "category": "beneficial",
        "description": "活的微生物，改善肠道菌群平衡，增强消化功能和免疫力。",
        "benefits": ["肠道健康", "增强免疫力", "改善消化", "缓解便秘", "改善过敏"],
        "common_in": "酸奶、泡菜、味噌、康普茶、酸菜、韩国泡菜"
    },
    {
        "name": "叶酸",
        "aliases": ["folic acid", "folate", "维生素B9", "叶酸盐"],
        "category": "beneficial",
        "description": "对细胞分裂和DNA合成至关重要。孕妇补充叶酸可预防胎儿神经管缺陷。",
        "benefits": ["胎儿发育", "预防贫血", "心血管健康", "细胞生长", "预防神经管缺陷"],
        "common_in": "深绿色蔬菜、豆类、动物肝脏、橘子、强化谷物"
    },
    {
        "name": "镁",
        "aliases": ["magnesium", "Mg", "氧化镁", "柠檬酸镁"],
        "category": "beneficial",
        "description": "参与300多种生化反应，帮助肌肉放松、改善睡眠、缓解焦虑。现代饮食中常缺乏。",
        "benefits": ["改善睡眠", "缓解焦虑", "肌肉放松", "骨骼健康", "能量代谢", "预防偏头痛"],
        "common_in": "深绿色蔬菜、坚果、种子、全谷物、黑巧克力、香蕉"
    },
    {
        "name": "钾",
        "aliases": ["potassium", "K", "氯化钾", "柠檬酸钾"],
        "category": "beneficial",
        "description": "维持体液平衡、神经信号传导和肌肉收缩。有助于降低血压。",
        "benefits": ["降低血压", "维持电解质平衡", "肌肉功能", "神经传导", "预防抽筋"],
        "common_in": "香蕉、土豆、番茄、橙子、菠菜、豆类、牛油果"
    },
    {
        "name": "多酚",
        "aliases": ["polyphenols", "茶多酚", "花青素", "儿茶素", "白藜芦醇", "黄酮类", "原花青素"],
        "category": "beneficial",
        "description": "植物来源的强效抗氧化剂。抗炎、抗癌、保护心血管、延缓衰老。",
        "benefits": ["抗氧化", "抗炎", "心血管保护", "延缓衰老", "抗癌潜力", "改善认知"],
        "common_in": "绿茶、红酒、蓝莓、黑巧克力、石榴、橄榄油、苹果"
    },
    {
        "name": "虾青素",
        "aliases": ["astaxanthin", "虾红素"],
        "category": "beneficial",
        "description": "超强天然抗氧化剂（抗氧化能力是维生素C的6000倍）。保护皮肤、眼睛和大脑。",
        "benefits": ["超强抗氧化", "皮肤保护", "眼睛健康", "抗疲劳", "延缓衰老"],
        "common_in": "三文鱼、虾、蟹、微藻"
    },
    {
        "name": "姜黄素",
        "aliases": ["curcumin", "姜黄", "turmeric"],
        "category": "beneficial",
        "description": "姜黄中的活性成分，强效抗炎和抗氧化。可能有助于预防和缓解关节炎、改善消化。",
        "benefits": ["抗炎", "抗氧化", "关节健康", "改善消化", "护肝", "增强脑功能"],
        "common_in": "咖喱、姜黄粉、姜黄饮料、功能性食品"
    },
    {
        "name": "辅酶Q10",
        "aliases": ["CoQ10", "coenzyme Q10", "泛醌", "ubiquinone"],
        "category": "beneficial",
        "description": "细胞能量产生必需的辅酶。强抗氧化剂，保护心脏。随年龄增长体内水平下降。",
        "benefits": ["心脏健康", "能量代谢", "抗氧化", "延缓衰老", "改善偏头痛"],
        "common_in": "牛肉、鸡心、沙丁鱼、西兰花、花生、大豆油"
    },
]


# 疾病与添加剂的关联
DISEASE_ADDITIVE_MAP = {
    "高血压": {
        "harmful": ["味精", "磷酸盐", "反式脂肪酸", "亚硝酸钠", "高果糖玉米糖浆"],
        "warning": "高血压患者应严格限制钠含量高的添加剂，注意配料表中的味精、磷酸盐等含钠添加剂。"
    },
    "糖尿病": {
        "harmful": ["高果糖玉米糖浆", "阿斯巴甜", "糖精钠", "安赛蜜", "甜蜜素", "三氯蔗糖", "反式脂肪酸"],
        "warning": "糖尿病患者需特别注意各种形式的糖和甜味剂。虽然人工甜味剂不升血糖，但可能影响肠道菌群和胰岛素敏感性。"
    },
    "心脏病": {
        "harmful": ["反式脂肪酸", "高果糖玉米糖浆", "亚硝酸钠", "味精", "磷酸盐", "BHA"],
        "warning": "心脏病患者应严格避免反式脂肪酸，限制钠含量和含磷添加剂。"
    },
    "高血脂": {
        "harmful": ["反式脂肪酸", "高果糖玉米糖浆", "BHA", "BHT"],
        "warning": "高血脂患者应严格避免反式脂肪酸和过量糖类添加剂。"
    },
    "脂肪肝": {
        "harmful": ["高果糖玉米糖浆", "反式脂肪酸", "阿斯巴甜", "甜蜜素"],
        "warning": "脂肪肝患者应严格限制果糖和人工甜味剂摄入，选择天然食品。"
    },
    "肥胖": {
        "harmful": ["高果糖玉米糖浆", "反式脂肪酸", "糖精钠", "阿斯巴甜"],
        "warning": "肥胖人群应避免高热量添加剂和可能干扰代谢的人工甜味剂。"
    },
    "肾脏病": {
        "harmful": ["磷酸盐", "亚铁氰化钾", "铝", "溴酸钾", "脱氢乙酸钠", "卡拉胶"],
        "warning": "慢性肾病患者必须严格控制磷、钾、铝等元素的摄入。磷酸盐是加工食品中最常见的含磷添加剂。"
    },
    "痛风": {
        "harmful": ["5'-呈味核苷酸二钠", "高果糖玉米糖浆", "味精"],
        "warning": "痛风患者应避免嘌呤相关添加剂和果糖。高果糖玉米糖浆会增加尿酸生成。"
    },
    "高尿酸血症": {
        "harmful": ["5'-呈味核苷酸二钠", "高果糖玉米糖浆"],
        "warning": "高尿酸患者应限制核苷酸类增味剂和果糖的摄入。"
    },
    "过敏体质": {
        "harmful": ["苯甲酸钠", "山梨酸钾", "柠檬黄", "日落黄", "胭脂红", "诱惑红", "亮蓝", "亚硫酸盐", "BHA", "卡拉胶"],
        "warning": "过敏体质者需特别注意防腐剂、合成色素和亚硫酸盐，这些是常见的过敏原。"
    },
    "哮喘": {
        "harmful": ["亚硫酸盐", "苯甲酸钠", "柠檬黄", "胭脂红"],
        "warning": "哮喘患者应严格避免亚硫酸盐类添加剂，可能诱发严重哮喘发作。"
    },
    "胃病": {
        "harmful": ["山梨酸钾", "亚硝酸钠", "苯甲酸钠", "卡拉胶", "甜蜜素"],
        "warning": "胃病患者应尽量选择新鲜食品，减少含防腐剂和刺激性添加剂的食品。"
    },
    "肠道疾病": {
        "harmful": ["卡拉胶", "二氧化钛", "三氯蔗糖", "高果糖玉米糖浆"],
        "warning": "肠道疾病患者（如炎症性肠病、肠易激综合征）应避免卡拉胶、二氧化钛等可能刺激肠道的添加剂。"
    },
    "肝脏疾病": {
        "harmful": ["BHA", "BHT", "脱氢乙酸钠", "甜蜜素"],
        "warning": "肝脏疾病患者需要减轻肝脏代谢负担，应避免人工抗氧化剂和防腐剂。"
    },
    "甲状腺问题": {
        "harmful": ["BHT", "卡拉胶", "溴酸钾", "亚硝酸钠"],
        "warning": "甲状腺功能异常者注意BHT和卡拉胶等可能干扰甲状腺功能的添加剂。"
    },
    "骨质疏松": {
        "harmful": ["磷酸盐", "铝", "苯甲酸钠"],
        "warning": "骨质疏松患者应限制磷摄入（影响钙吸收），避免含铝添加剂。"
    },
    "偏头痛": {
        "harmful": ["味精", "阿斯巴甜", "亚硝酸钠"],
        "warning": "偏头痛患者需注意味精、阿斯巴甜等可能诱发头痛的添加剂。"
    },
    "苯丙酮尿症": {
        "harmful": ["阿斯巴甜"],
        "warning": "苯丙酮尿症患者严格禁止摄入阿斯巴甜（含苯丙氨酸）！"
    },
    "ADHD": {
        "harmful": ["柠檬黄", "日落黄", "诱惑红", "胭脂红", "苯甲酸钠"],
        "warning": "ADHD（注意力缺陷多动障碍）患者建议避免合成色素和苯甲酸钠。"
    },
}


# 常见忌口与添加剂关联
DIETARY_RESTRICTION_MAP = {
    "素食": {
        "harmful": [],
        "note": "素食者需注意配料表中的动物来源成分（如明胶、虫胶、胭脂红等）。胭脂红来源于昆虫。"
    },
    "清真": {
        "harmful": [],
        "note": "清真饮食需注意酒精类添加剂、明胶来源等。"
    },
    "无麸质": {
        "harmful": [],
        "note": "无麸质饮食需注意配料表中的小麦、大麦、黑麦及其衍生物。注意麦芽糖浆、麦芽糊精等。"
    },
    "低钠饮食": {
        "harmful": ["味精", "苯甲酸钠", "亚硝酸钠", "磷酸盐", "5'-呈味核苷酸二钠"],
        "note": "低钠饮食需注意所有含「钠」字的添加剂，以及味精等增味剂。"
    },
    "低糖饮食": {
        "harmful": ["高果糖玉米糖浆", "甜蜜素", "糖精钠", "阿斯巴甜", "安赛蜜", "三氯蔗糖"],
        "note": "低糖/生酮饮食需注意各种形式的糖和甜味剂。建议选择天然无糖食品。"
    },
    "无乳糖": {
        "harmful": [],
        "note": "无乳糖饮食需注意配料表中的牛奶、乳清、乳糖、酪蛋白等成分。"
    },
    "孕妇": {
        "harmful": ["糖精钠", "甜蜜素", "阿斯巴甜", "亚硝酸钠", "BHA", "BHT", "反式脂肪酸"],
        "note": "孕妇应尽量避免人工甜味剂、防腐剂和反式脂肪酸。选择天然新鲜食材最为安全。"
    },
    "儿童": {
        "harmful": ["柠檬黄", "日落黄", "诱惑红", "胭脂红", "苯甲酸钠", "阿斯巴甜", "糖精钠", "甜蜜素", "BHA"],
        "note": "儿童食品应尽量选择不含合成色素和防腐剂的天然食品。人工甜味剂不建议儿童长期摄入。"
    },
    "老年人": {
        "harmful": ["磷酸盐", "铝", "亚硝酸钠", "反式脂肪酸", "高果糖玉米糖浆"],
        "note": "老年人应选择低钠、低磷、富含钙和蛋白质的天然食品。"
    },
}
