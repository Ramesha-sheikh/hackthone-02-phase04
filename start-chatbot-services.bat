@echo off
echo ========================================
echo Starting AI Chatbot Services
echo ========================================
echo.

echo Starting MCP Server on port 8003...
start "MCP Server" cmd /k "cd mcp-server && python http_wrapper.py"
timeout /t 3 /nobreak > nul

echo Starting AI Agent on port 8002...
start "AI Agent" cmd /k "cd ai-agent && python main.py"
timeout /t 3 /nobreak > nul

echo Starting Frontend on port 3000...
start "Frontend" cmd /k "cd frontend && npm run dev"

echo.
echo ========================================
echo All services are starting...
echo ========================================
echo.
echo MCP Server:  http://localhost:8003
echo AI Agent:    http://localhost:8002
echo Frontend:    http://localhost:3000
echo.
echo Press any key to stop all services...
pause > nul

taskkill /FI "WindowTitle eq MCP Server*" /T /F
taskkill /FI "WindowTitle eq AI Agent*" /T /F
taskkill /FI "WindowTitle eq Frontend*" /T /F

echo All services stopped.
pause
