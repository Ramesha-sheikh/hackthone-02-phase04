# 🐳 Docker Containers Kaise Banaye - Bilkul Simple Steps

## ⚠️ IMPORTANT: Docker Desktop sirf open karne se containers NAHI bante!

Aapko commands run karni parengi to containers banenge aur Docker Desktop mein dikhai denge.

---

## 📋 Pre-Check (Pehle Ye Confirm Karen)

### 1. Docker Desktop Running Hai?
- Docker Desktop open karen
- Bottom-left corner mein **GREEN** whale icon dekhen 🐳
- Agar RED hai to wait karen

### 2. CMD/PowerShell Admin Mode Mein Open Karen
- **Windows Key** + **X** press karen
- "Windows PowerShell (Admin)" select karen
- Ya "Command Prompt (Admin)" select karen

---

## 🚀 Step-by-Step: Containers Banaye

### Step 1: Docker Version Check (Confirm Docker Working Hai)

CMD mein paste karen:
```bash
docker --version
```

**Expected Output:**
```
Docker version 24.0.x, build xxxxx
```

Agar error aaye = Docker Desktop properly installed nahi hai.

---

### Step 2: Project Folder Mein Jayen

CMD mein paste karen (EXACTLY ye path):
```bash
cd "D:\hacthone-02 giaic\Hackthone02-phase-04"
```

**Confirm Karen:**
```bash
dir
```

Aapko ye files dikhni chahiye:
- docker-compose.yml ✅
- frontend (folder) ✅
- ai-agent (folder) ✅
- mcp-server (folder) ✅

---

### Step 3: Build Karen - Containers Banayenge (First Time: 5-10 Minutes)

CMD mein paste karen:
```bash
docker-compose build
```

**Kya Hoga:**
- Screen pe bahut saari lines ayengi
- "Downloading...", "Building..." dikhai dega
- 5-10 minutes lagenge (internet speed pe depend)
- Agar koi error aaye to STOP karen aur mujhe batayein

**Success Message:**
```
Successfully built [container_id]
Successfully tagged todo-frontend:latest
Successfully tagged todo-ai-agent:latest
Successfully tagged todo-mcp-server:latest
```

---

### Step 4: Check Karen - Images Ban Gayi?

CMD mein paste karen:
```bash
docker images
```

**Aapko Ye Dikhna Chahiye:**
```
REPOSITORY         TAG       IMAGE ID       SIZE
todo-frontend      latest    abc123def...   500MB
todo-ai-agent      latest    def456ghi...   200MB
todo-mcp-server    latest    ghi789jkl...   200MB
```

**Ab Docker Desktop Mein Check Karen:**
- Docker Desktop open karen
- **Images** tab pe click karen
- Aapko **3 images** dikhni chahiye! 🖼️

---

### Step 5: Containers Run Karen (Start Karen)

CMD mein paste karen:
```bash
docker-compose up -d
```

**Kya Hoga:**
- "Creating network..." dikhai dega
- "Creating todo-frontend..." dikhai dega
- "Creating todo-ai-agent..." dikhai dega
- "Creating todo-mcp-server..." dikhai dega
- Kuch seconds mein done ho jayega

**Success Message:**
```
✔ Container todo-mcp-server   Started
✔ Container todo-ai-agent     Started
✔ Container todo-frontend     Started
```

---

### Step 6: Check Karen - Containers Running Hain?

**CMD Mein:**
```bash
docker ps
```

**Expected Output:**
```
CONTAINER ID   IMAGE           STATUS         PORTS                    NAMES
abc123...      todo-frontend   Up 10 seconds  0.0.0.0:3000->3000/tcp   todo-frontend
def456...      todo-ai-agent   Up 10 seconds  0.0.0.0:8002->8002/tcp   todo-ai-agent
ghi789...      todo-mcp-server Up 10 seconds  0.0.0.0:8003->8003/tcp   todo-mcp-server
```

**Docker Desktop Mein:**
1. **Containers** tab pe click karen
2. Aapko **3 GREEN containers** dikhne chahiye! 📦✅

```
📦 todo-frontend       ● Running    3000:3000
📦 todo-ai-agent       ● Running    8002:8002
📦 todo-mcp-server     ● Running    8003:8003
```

---

### Step 7: Browser Mein Test Karen

Ye URLs open karen:

1. **http://localhost:3000** - Main App
2. **http://localhost:8002** - AI Agent (JSON response dikhai dega)
3. **http://localhost:8003** - MCP Server (JSON response dikhai dega)

---

## ✅ Success Checklist

- [ ] Docker Desktop running hai (green whale)
- [ ] `docker images` mein 3 images dikhai di
- [ ] `docker ps` mein 3 containers running dikhai diye
- [ ] Docker Desktop > Containers tab mein 3 green containers hain
- [ ] http://localhost:3000 khul raha hai
- [ ] http://localhost:8002 response de raha hai
- [ ] http://localhost:8003 response de raha hai

---

## 🛑 Stop Karen (Jab Kaam Khatam Ho)

```bash
docker-compose down
```

Ye command:
- Sab containers band kar degi
- Network remove kar degi
- Images rahenge (next time fast start hoga)

---

## 🔄 Next Time Start Karen (Fast - Sirf 10 Seconds)

Agli baar sirf ye command run karen:
```bash
cd "D:\hacthone-02 giaic\Hackthone02-phase-04"
docker-compose up -d
```

Build dobara nahi karna padega! ✅

---

## 🐛 Common Errors & Solutions

### Error 1: "docker: command not found"
**Problem:** Docker Desktop properly install nahi hai
**Solution:**
1. Docker Desktop uninstall karen
2. Fresh install karen from: https://www.docker.com/products/docker-desktop
3. Restart karen computer

---

### Error 2: "Cannot connect to Docker daemon"
**Problem:** Docker Desktop running nahi hai
**Solution:**
1. Docker Desktop open karen
2. Wait karen until GREEN whale icon dikhai de
3. Phir commands run karen

---

### Error 3: "Port already in use"
**Problem:** Port 3000, 8002, ya 8003 pehle se use ho raha hai
**Solution:**
```bash
# Pehle running process check karen
netstat -ano | findstr :3000
netstat -ano | findstr :8002
netstat -ano | findstr :8003

# Ya containers stop karen
docker-compose down

# Phir start karen
docker-compose up -d
```

---

### Error 4: Build fail ho raha hai
**Problem:** Internet slow hai ya dependency download nahi ho rahi
**Solution:**
```bash
# Internet check karen
# Phir clean build karen
docker-compose build --no-cache
```

---

### Error 5: Container crash ho raha hai
**Problem:** Environment variables missing hain
**Solution:**
```bash
# Logs check karen
docker logs todo-frontend

# .env files check karen
type ai-agent\.env
type mcp-server\.env

# Agar missing hain to create karen
echo OPENAI_API_KEY=your-key-here > ai-agent\.env
echo BACKEND_URL=https://rameesha12123214-todophase02-backend.hf.space > mcp-server\.env
```

---

## 📞 Quick Commands Reference

```bash
# Build (first time only)
docker-compose build

# Start containers
docker-compose up -d

# Stop containers
docker-compose down

# Check running containers
docker ps

# Check all containers (including stopped)
docker ps -a

# Check images
docker images

# Logs dekhein
docker-compose logs -f

# Specific container logs
docker logs todo-frontend

# Restart containers
docker-compose restart

# Remove everything (fresh start)
docker-compose down --volumes --rmi all
```

---

## 🎯 Summary

### Pehli Baar:
```bash
cd "D:\hacthone-02 giaic\Hackthone02-phase-04"
docker-compose build        # 5-10 minutes
docker-compose up -d         # Start containers
docker ps                    # Check containers
```

### Har Baar (After First Time):
```bash
cd "D:\hacthone-02 giaic\Hackthone02-phase-04"
docker-compose up -d         # Just 10 seconds!
```

### Stop Karen:
```bash
docker-compose down
```

---

## 🎉 Expected Result

Jab sab theek hoga to:

✅ Docker Desktop > **Containers** tab mein:
```
📦 todo-frontend       ● Running
📦 todo-ai-agent       ● Running
📦 todo-mcp-server     ● Running
```

✅ Docker Desktop > **Images** tab mein:
```
🖼️ todo-frontend:latest
🖼️ todo-ai-agent:latest
🖼️ todo-mcp-server:latest
```

✅ Browser mein:
- http://localhost:3000 - App chal raha hai
- Dashboard pe chatbot kaam kar raha hai

---

**Ab bas commands copy-paste karen aur containers ban jayenge!** 🐳✨
