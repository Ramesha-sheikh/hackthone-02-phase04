@echo off
echo ========================================
echo   Docker Status Check
echo ========================================
echo.

echo === Running Containers ===
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

echo.
echo === All Images ===
docker images | findstr hackthone02

echo.
echo === Test Services ===
echo.
echo Testing AI Agent (8002):
curl -s http://localhost:8002 || echo [NOT RESPONDING]

echo.
echo Testing MCP Server (8003):
curl -s http://localhost:8003 || echo [NOT RESPONDING]

echo.
echo Testing Frontend (3000):
curl -s http://localhost:3000 || echo [NOT RESPONDING]

echo.
pause
