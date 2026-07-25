@echo off
chcp 65001 >nul
title 食品配料分析网站

echo ============================================
echo    食品配料分析网站 - 启动中...
echo ============================================
echo.

REM 检查 Flask 是否已经在运行
curl -s http://127.0.0.1:5000 >nul 2>&1
if %errorlevel% neq 0 (
    echo [1/2] 启动后端服务...
    start "Flask" /min python app.py
    timeout /t 5 /nobreak >nul
) else (
    echo [1/2] 后端服务已在运行
)

echo [2/2] 获取公网地址...
echo.
echo 请稍等，正在连接...
echo.

ssh -o StrictHostKeyChecking=no -R 80:localhost:5000 nokey@localhost.run 2>&1 | findstr /C:"lhr.life"

echo.
echo ============================================
echo   复制上面的 https:// 开头的地址发给朋友!
echo   本机访问: http://127.0.0.1:5000
echo ============================================
echo.
echo 按任意键关闭隧道（网站将不可访问）
pause >nul
