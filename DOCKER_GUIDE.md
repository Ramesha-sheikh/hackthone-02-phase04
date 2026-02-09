# 🐳 Docker Setup Guide - Urdu/English

## ✅ Pre-requisites (Zarurat)

1. **Docker Desktop** install hona chahiye aur **running** hona chahiye
2. **Terminal/CMD** admin mode mein open karen

---

## 🚀 Quick Start - Docker Containers Banaye

### Step 1: Project folder mein jayen
```bash
cd "D:\hacthone-02 giaic\Hackthone02-phase-04"
```

### Step 2: Environment Files Check Karen

**AI Agent Environment File:**
```bash
# Check if exists
type ai-agent\.env
```
Agar file nahi hai to banayein:
```bash
echo OPENAI_API_KEY=your-openai-api-key-here > ai-agent\.env
```

**MCP Server Environment File:**
```bash
# Check if exists
type mcp-server\.env
```
Agar file nahi hai to banayein:
```bash
echo BACKEND_URL=https://rameesha12123214-todophase02-backend.hf.space > mcp-server\.env
```

---

## 🏗️ Docker Containers Build Karen

### Option 1: Automated Script (EASIEST! ⭐)
Simply double-click karo:
```
docker-build-run.bat
```
Yeh script automatically:
- ✅ Docker check karega
- ✅ Images build karega
- ✅ Containers start karega
- ✅ Browser open karega

### Option 2: Manual Commands

**Sab Kuch Ek Saath Build Karen:**
```bash
docker-compose build
```
Yeh command **3 containers** build karega:
- ✅ `todo-mcp-server` (Port 8003)
- ✅ `todo-ai-agent` (Port 8002)
- ✅ `todo-frontend` (Port 3000)

**Individual Containers Build Karen:**

MCP Server:
```bash
docker build -t todo-mcp-server ./mcp-server
```

AI Agent:
```bash
docker build -t todo-ai-agent ./ai-agent
```

Frontend:
```bash
docker build -t todo-frontend ./frontend
```

---

## ▶️ Containers Run Karen

### Option 1: Docker Compose se Sab Kuch Start Karen (EASY)
```bash
docker-compose up -d
```

Yeh command:
- ✅ Sab containers start karega
- ✅ Background mein run karega (`-d` flag)
- ✅ Automatically network banayega
- ✅ Ports map karega

### Option 2: Individual Containers Run Karen

**MCP Server:**
```bash
docker run -d --name todo-mcp-server -p 8003:8003 ^
  -e BACKEND_URL=https://rameesha12123214-todophase02-backend.hf.space ^
  todo-mcp-server
```

**AI Agent:**
```bash
docker run -d --name todo-ai-agent -p 8002:8002 ^
  --env-file ai-agent/.env ^
  todo-ai-agent
```

**Frontend:**
```bash
docker run -d --name todo-frontend -p 3000:3000 ^
  -e NEXT_PUBLIC_AI_AGENT_URL=http://localhost:8002 ^
  -e NEXT_PUBLIC_BACKEND_URL=https://rameesha12123214-todophase02-backend.hf.space ^
  todo-frontend
```

---

## 🔍 Check Karen - Containers Running Hain?

### Terminal mein check karen:
```bash
docker ps
```

Output kuch aisa hoga:
```
CONTAINER ID   IMAGE              STATUS         PORTS                    NAMES
abc123def456   todo-frontend      Up 2 minutes   0.0.0.0:3000->3000/tcp   todo-frontend
def456ghi789   todo-ai-agent      Up 2 minutes   0.0.0.0:8002->8002/tcp   todo-ai-agent
ghi789jkl012   todo-mcp-server    Up 2 minutes   0.0.0.0:8003->8003/tcp   todo-mcp-server
```

### Docker Desktop mein check karen:
1. Docker Desktop open karen
2. **Containers** tab pe click karen
3. Aapko 3 containers dikhne chahiye:
   - ✅ `todo-frontend` (green = running)
   - ✅ `todo-ai-agent` (green = running)
   - ✅ `todo-mcp-server` (green = running)

---

## 🌐 Test Karen - Services Working Hain?

### Browser mein test karen:

1. **Frontend:** http://localhost:3000
2. **AI Agent Health:** http://localhost:8002
3. **MCP Server Health:** http://localhost:8003

### Terminal se test karen:
```bash
curl http://localhost:3000
curl http://localhost:8002
curl http://localhost:8003
```

---

## 📋 Logs Dekhna (Agar Error Aaye)

### Sab containers ke logs:
```bash
docker-compose logs -f
```

### Individual container logs:
```bash
docker logs todo-frontend
docker logs todo-ai-agent
docker logs todo-mcp-server
```

### Live logs (real-time):
```bash
docker logs -f todo-frontend
```

---

## 🛑 Containers Stop Karen

### Sab containers stop karen:
```bash
docker-compose down
```

### Individual container stop karen:
```bash
docker stop todo-frontend
docker stop todo-ai-agent
docker stop todo-mcp-server
```

---

## 🗑️ Containers Delete Karen

### Stop + Delete (docker-compose):
```bash
docker-compose down --volumes --remove-orphans
```

### Individual container delete:
```bash
docker rm -f todo-frontend
docker rm -f todo-ai-agent
docker rm -f todo-mcp-server
```

### Images bhi delete karen:
```bash
docker rmi todo-frontend todo-ai-agent todo-mcp-server
```

---

## 🔄 Rebuild Karen (Code Change Ke Baad)

### Poora rebuild:
```bash
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

### Single service rebuild:
```bash
docker-compose build --no-cache frontend
docker-compose up -d frontend
```

---

## 🐛 Common Issues & Solutions

### Issue 1: Port already in use
```
Error: Bind for 0.0.0.0:3000 failed: port is already allocated
```
**Solution:**
```bash
# Port use kar rahi service find karen
netstat -ano | findstr :3000

# Ya port change karen docker-compose.yml mein
ports:
  - "3001:3000"  # Host port 3001 pe map karo
```

### Issue 2: Docker daemon not running
```
Error: Cannot connect to the Docker daemon
```
**Solution:**
- Docker Desktop open karen
- Wait until it's fully started (whale icon green hoga)

### Issue 3: Container crash ho raha hai
```bash
# Logs check karen
docker logs todo-frontend

# Container restart karen
docker restart todo-frontend
```

### Issue 4: Build fail ho raha hai
```bash
# Cache clear karke rebuild karen
docker-compose build --no-cache

# Ya individual service
docker build --no-cache -t todo-frontend ./frontend
```

### Issue 5: Network error
```bash
# Network recreate karen
docker network rm todo-network
docker-compose up -d
```

---

## 📊 Docker Desktop Mein Kya Dikhega

```
Docker Desktop
│
├── Containers (Tab)
│   ├── 📦 todo-frontend (Port 3000) ✅ Running
│   ├── 📦 todo-ai-agent (Port 8002) ✅ Running
│   └── 📦 todo-mcp-server (Port 8003) ✅ Running
│
├── Images (Tab)
│   ├── 🖼️ todo-frontend:latest
│   ├── 🖼️ todo-ai-agent:latest
│   └── 🖼️ todo-mcp-server:latest
│
└── Volumes (Tab)
    └── hackthone02-phase-04_postgres_data
```

---

## ✨ Complete Workflow (Step by Step)

### 🎬 Pehli Baar Setup (First Time)

```bash
# 1. Project folder mein jayen
cd "D:\hacthone-02 giaic\Hackthone02-phase-04"

# 2. Environment files check karen
type ai-agent\.env
type mcp-server\.env

# 3. Build karen (5-10 minutes lagega)
docker-compose build

# 4. Start karen
docker-compose up -d

# 5. Check karen
docker ps

# 6. Browser mein open karen
start http://localhost:3000
```

### 🔄 Daily Use

```bash
# Start karen
docker-compose up -d

# Stop karen (kaam khatam hone ke baad)
docker-compose down
```

### 🔧 Debugging

```bash
# Logs dekhein
docker-compose logs -f

# Specific container logs
docker logs -f todo-frontend

# Container restart karen
docker-compose restart frontend

# Container ke andar jayen (debugging)
docker exec -it todo-frontend sh
```

---

## 🎯 Production Deployment

### Docker Hub pe push karen:
```bash
# 1. Login karen
docker login

# 2. Tag karen
docker tag todo-frontend yourusername/todo-frontend:latest
docker tag todo-ai-agent yourusername/todo-ai-agent:latest
docker tag todo-mcp-server yourusername/todo-mcp-server:latest

# 3. Push karen
docker push yourusername/todo-frontend:latest
docker push yourusername/todo-ai-agent:latest
docker push yourusername/todo-mcp-server:latest
```

### Kubernetes Deployment:
```bash
# Helm charts available hain helm/ folder mein
cd helm
helm install todo-app .
```

---

## 📝 Important Notes

1. **Environment Variables**: `.env` files zaroori hain, bina is ke containers crash honge
2. **Ports**: Make sure ports 3000, 8002, 8003 free hain
3. **Docker Desktop**: Running hona chahiye before any command
4. **Build Time**: First build 5-10 minutes lag sakta hai (internet speed pe depend)
5. **Disk Space**: Kam se kam 2GB free space chahiye
6. **Windows Users**: Commands `^` se multi-line hain, Linux/Mac pe `\` use karen

---

## 🎉 Success Criteria

Agar sab kuch theek hai to:

✅ Docker Desktop mein 3 green containers dikhenge
✅ `docker ps` mein 3 containers running dikhenge
✅ `http://localhost:3000` pe app open hoga
✅ `http://localhost:8002` pe AI agent response dega
✅ `http://localhost:8003` pe MCP server response dega
✅ Chatbot kaam karega dashboard mein
✅ Tasks add/delete kar saktay hain

---

## 📞 Help & Support

### Quick Commands Cheatsheet:

```bash
# Build
docker-compose build

# Start
docker-compose up -d

# Stop
docker-compose down

# Logs
docker-compose logs -f

# Restart
docker-compose restart

# Status
docker ps

# Remove everything
docker-compose down --volumes --rmi all
```

---

**Happy Dockerizing! 🐳**

**Ab aap Docker Desktop mein apne containers dekh saktay hain!** ✨
