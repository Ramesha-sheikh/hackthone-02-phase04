# 🚀 QUICK REFERENCE - Docker Todo App

## ✅ STATUS: ALL 4 CONTAINERS RUNNING

---

## 📦 YOUR CONTAINERS:

```
1. todo-backend       http://localhost:8000
2. todo-frontend      http://localhost:3000  ← OPEN THIS!
3. todo-ai-agent      http://localhost:8002
4. todo-mcp-server    http://localhost:8003
```

---

## ⚡ MOST USED COMMANDS:

```bash
# CHECK STATUS
docker ps

# START ALL
docker start todo-backend todo-frontend todo-ai-agent todo-mcp-server

# STOP ALL
docker stop todo-backend todo-frontend todo-ai-agent todo-mcp-server

# VIEW LOGS
docker logs todo-frontend

# RESTART ALL
docker restart todo-backend todo-frontend todo-ai-agent todo-mcp-server
```

---

## 🔍 QUICK CHECKS:

```bash
# Are containers running?
docker ps

# Are images present?
docker images | grep hackthone02

# Check logs if error
docker logs todo-backend
docker logs todo-frontend
docker logs todo-ai-agent
docker logs todo-mcp-server
```

---

## 🌐 URLS TO REMEMBER:

| Service | URL |
|---------|-----|
| **Main App** | http://localhost:3000 |
| **Backend API** | http://localhost:8000 |
| **AI Chatbot** | http://localhost:8002 |
| **MCP Server** | http://localhost:8003 |

---

## 🐳 DOCKER DESKTOP:

1. Open Docker Desktop
2. Click **Containers** tab
3. Should see **4 GREEN** containers
4. Click **Images** tab
5. Should see **4 images**

---

## 🆘 IF SOMETHING WRONG:

```bash
# Restart everything
docker restart todo-backend todo-frontend todo-ai-agent todo-mcp-server

# Stop and start fresh
docker stop todo-backend todo-frontend todo-ai-agent todo-mcp-server
docker start todo-backend todo-frontend todo-ai-agent todo-mcp-server

# Check what's wrong
docker ps -a
docker logs <container-name>
```

---

## 📚 DETAILED DOCS:

- **COMPLETE_4_CONTAINERS_SUCCESS.md** - Full guide
- **DOCKER_GUIDE.md** - Docker complete guide
- **SIMPLE_DOCKER_STEPS.md** - Urdu guide

---

## 🎯 DAILY WORKFLOW:

**Morning:**
```bash
docker start todo-backend todo-frontend todo-ai-agent todo-mcp-server
# Wait 30 seconds, then open http://localhost:3000
```

**Evening:**
```bash
docker stop todo-backend todo-frontend todo-ai-agent todo-mcp-server
```

---

**Keep this file handy for quick reference!** 📌
