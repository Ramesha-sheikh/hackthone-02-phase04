@echo off
echo ========================================
echo   Starting Todo App - Quick Start
echo ========================================
echo.

echo Containers already running:
docker ps --filter "name=todo-"

echo.
echo ========================================
echo Starting Frontend Locally...
echo ========================================
echo.

cd frontend
start cmd /k "npm run dev"

echo.
echo ========================================
echo   All Services Started!
echo ========================================
echo.
echo Services:
echo   - AI Agent:    http://localhost:8002 (Docker)
echo   - MCP Server:  http://localhost:8003 (Docker)
echo   - Frontend:    http://localhost:3000 (Local)
echo.
echo Opening browser in 10 seconds...
timeout /t 10
start http://localhost:3000
echo.
echo Done!
pause
