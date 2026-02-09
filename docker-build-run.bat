@echo off
echo ========================================
echo   Docker Build and Run Script
echo   Todo App with AI Chatbot
echo ========================================
echo.

REM Check if Docker is running
docker info >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Docker Desktop running nahi hai!
    echo Please Docker Desktop start karen aur phir se try karen.
    pause
    exit /b 1
)

echo [SUCCESS] Docker Desktop running hai!
echo.

REM Change to project directory
cd /d "%~dp0"

echo ========================================
echo Step 1: Building Docker Images...
echo ========================================
echo.
echo Yeh kuch time le sakta hai (5-10 minutes)...
echo.

docker-compose build

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Build fail ho gaya!
    echo Logs check karen aur phir se try karen.
    pause
    exit /b 1
)

echo.
echo [SUCCESS] Sab images build ho gayi!
echo.

echo ========================================
echo Step 2: Starting Containers...
echo ========================================
echo.

docker-compose up -d

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Containers start nahi huay!
    pause
    exit /b 1
)

echo.
echo [SUCCESS] Sab containers start ho gaye!
echo.

echo ========================================
echo Step 3: Checking Container Status...
echo ========================================
echo.

docker ps --filter "name=todo-"

echo.
echo ========================================
echo   SUCCESS! Sab kuch ready hai!
echo ========================================
echo.
echo Ab aap in URLs pe ja saktay hain:
echo.
echo   Frontend:    http://localhost:3000
echo   AI Agent:    http://localhost:8002
echo   MCP Server:  http://localhost:8003
echo.
echo ========================================
echo.

REM Wait for services to start
echo Services start ho rahi hain, wait karen...
timeout /t 10 /nobreak >nul

REM Try to open browser
echo Browser open ho raha hai...
start http://localhost:3000

echo.
echo ========================================
echo Commands:
echo   - Stop:    docker-compose down
echo   - Logs:    docker-compose logs -f
echo   - Restart: docker-compose restart
echo ========================================
echo.

pause
