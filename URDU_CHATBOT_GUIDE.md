# 🤖 AI Chatbot - Urdu/Roman Urdu Guide

## ✅ Services Running!

### URLs:

1. **MCP Server**: `http://localhost:8003`
   - Status: ✅ Running
   - Health Check: `http://localhost:8003/`

2. **AI Agent**: `http://localhost:8002`
   - Status: ✅ Running
   - Health Check: `http://localhost:8002/`

3. **Frontend**: `http://localhost:3000`
   - Dashboard pe chatbot button milega (bottom-right corner)

---

## 🚀 Kaise Run Karein?

### Option 1: Automated Script (Recommended)
```bash
start-chatbot-services.bat
```

### Option 2: Manual (3 Terminals)

**Terminal 1 - MCP Server:**
```bash
cd mcp-server
python http_wrapper.py
```

**Terminal 2 - AI Agent:**
```bash
cd ai-agent
python main.py
```

**Terminal 3 - Frontend:**
```bash
cd frontend
npm run dev
```

---

## 💬 Custom Commands Kaise Use Karein?

### Method 1: Frontend Chatbot (Easiest)

1. Browser mein jayen: `http://localhost:3000`
2. Login karein
3. Dashboard pe jayen
4. Bottom-right corner mein coffee color ka button dikhega ☕
5. Us button pe click karein
6. Ab natural language mein type karein:

#### Examples:
```
"Mujhe mere tasks dikhao"
"Add a task to buy groceries"
"Pehla task complete kar do"
"Task number 2 delete kar do"
```

### Method 2: Direct API Call (For Testing)

#### curl se:
```bash
# Chatbot se baat karein
curl -X POST http://localhost:8002/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Show my tasks",
    "user_id": "test_user"
  }'
```

#### PowerShell se:
```powershell
$body = @{
    message = "Show my tasks"
    user_id = "test_user"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8002/chat" `
  -Method Post `
  -ContentType "application/json" `
  -Body $body
```

---

## 📋 Supported Commands (Natural Language)

### Task Add Karne Ke Liye:
```
"Add a task to buy milk"
"Create a new task: finish homework"
"Nayi task banao: call doctor"
"Make a task to clean room"
```

### Tasks Dekhne Ke Liye:
```
"Show my tasks"
"List all tasks"
"Mere tasks dikhao"
"What tasks do I have?"
"Display my todos"
```

### Task Complete Karne Ke Liye:
```
"Mark task 1 as completed"
"Complete task 2"
"Task 3 ko done kar do"
"Finish task number 1"
```

### Task Delete Karne Ke Liye:
```
"Delete task 1"
"Remove task 2"
"Task 3 ko delete kar do"
"Clear task number 1"
```

---

## 🔧 MCP Server Direct API Calls

Agar aap directly MCP server ke tools use karna chahte hain:

### Get Tasks:
```bash
curl -X POST http://localhost:8003/call_tool \
  -H "Content-Type: application/json" \
  -d '{
    "tool_name": "get_tasks",
    "parameters": {
      "session_token": "YOUR_AUTH_TOKEN"
    }
  }'
```

### Create Task:
```bash
curl -X POST http://localhost:8003/call_tool \
  -H "Content-Type: application/json" \
  -d '{
    "tool_name": "create_task",
    "parameters": {
      "title": "Buy groceries",
      "description": "Milk, eggs, bread",
      "session_token": "YOUR_AUTH_TOKEN"
    }
  }'
```

### Update Task:
```bash
curl -X POST http://localhost:8003/call_tool \
  -H "Content-Type: application/json" \
  -d '{
    "tool_name": "update_task",
    "parameters": {
      "task_id": 1,
      "status": "completed",
      "session_token": "YOUR_AUTH_TOKEN"
    }
  }'
```

### Delete Task:
```bash
curl -X POST http://localhost:8003/call_tool \
  -H "Content-Type: application/json" \
  -d '{
    "tool_name": "delete_task",
    "parameters": {
      "task_id": 1,
      "session_token": "YOUR_AUTH_TOKEN"
    }
  }'
```

---

## 🎨 UI Mein Kaise Dikhega?

### Dashboard:
```
┌─────────────────────────────────────┐
│  Your Tasks                         │
│  □ Buy groceries                    │
│  □ Finish homework                  │
│  ☑ Call mom                         │
│                                     │
│                              [💬]   │ ← Yahan click karein
└─────────────────────────────────────┘
```

### Chatbot Open:
```
┌────────────────────┐
│ AI Assistant   [X] │ ← Coffee color theme
├────────────────────┤
│ 🤖 Hello! How     │
│    can I help?    │
│                   │
│         You 👤    │
│ Show my tasks     │
│                   │
│ 🤖 You have 3     │
│    tasks:         │
│    1. Task 1      │
│    2. Task 2      │
│    3. Task 3      │
├────────────────────┤
│ Type here...  [→] │
└────────────────────┘
```

---

## 🧪 Test Kaise Karein?

### Quick Test:
```bash
# Ye command run karein
python test-chatbot.py
```

Expected Output:
```
✅ MCP Server health check
✅ AI Agent health check
✅ Backend API accessible
✅ MCP tool execution
✅ Chatbot conversation
Total: 5/5 tests passed
```

### Manual Test Commands:

1. **Health Check:**
```bash
curl http://localhost:8002
curl http://localhost:8003
```

2. **Simple Chat:**
```bash
curl -X POST http://localhost:8002/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello", "user_id": "test"}'
```

3. **Task Operation:**
```bash
curl -X POST http://localhost:8002/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Show my tasks", "user_id": "test"}'
```

---

## 🎯 Step-by-Step Tutorial

### Step 1: Services Start Karein
```bash
# Ye script run karein
start-chatbot-services.bat
```
Ya phir manually 3 terminals mein run karein (upar dekhen)

### Step 2: Browser Mein Dashboard Kholein
```
http://localhost:3000
```

### Step 3: Login Karein
Apna email/password enter karein

### Step 4: Dashboard Pe Jayen
Login ke baad automatically dashboard pe jaoge

### Step 5: Chatbot Button Click Karein
Bottom-right corner mein coffee color ka gol button dikhega - us pe click karein

### Step 6: Commands Try Karein

**Example 1 - Tasks Dekhna:**
```
Type: "Show my tasks"
Result: Aapke saare tasks list ho jayenge
```

**Example 2 - Task Add Karna:**
```
Type: "Add a task to buy milk"
Result: Nayi task ban jayegi aur dashboard mein dikhegi
```

**Example 3 - Task Complete Karna:**
```
Type: "Mark task 1 as completed"
Result: Task complete ho jayega
```

**Example 4 - Task Delete Karna:**
```
Type: "Delete task 1"
Result: Task delete ho jayega
```

---

## 🔍 Troubleshooting

### Problem 1: Chatbot "Offline" Dikha Raha Hai

**Solution:**
```bash
# Check karein AI Agent chal raha hai ya nahi
curl http://localhost:8002

# Agar nahi chal raha, to start karein
cd ai-agent
python main.py
```

### Problem 2: "Failed to communicate" Error

**Solution:**
```bash
# MCP Server check karein
curl http://localhost:8003

# Agar nahi chal raha, to start karein
cd mcp-server
python http_wrapper.py
```

### Problem 3: Tasks Update Nahi Ho Rahe

**Solution:**
1. Browser console check karein (F12 press karein)
2. Ensure karein ke aap login hain
3. Backend API accessible hai ya nahi check karein

### Problem 4: OpenAI API Error

**Solution:**
```bash
# Check karein .env file mein API key sahi hai
cd ai-agent
notepad .env

# API key verify karein OpenAI website pe
# Credits available hain ya nahi check karein
```

---

## 📊 Response Format

### Successful Response:
```json
{
  "conversation_id": "abc123",
  "response": "Task added successfully!",
  "tool_calls": [
    {
      "name": "create_task",
      "arguments": {
        "title": "Buy milk"
      }
    }
  ]
}
```

### Error Response:
```json
{
  "detail": "Error message here"
}
```

---

## 💡 Tips & Tricks

### Tip 1: Natural Language Use Karein
```
❌ Ye mat likhen: "create_task buy milk"
✅ Ye likhen: "Add a task to buy milk"
```

### Tip 2: Task Numbers Use Karein
```
✅ "Complete task 1"
✅ "Delete task number 2"
```

### Tip 3: Multiple Commands
Ek ek karke commands send karein, sab ek saath nahi

### Tip 4: Dashboard Auto-Refresh
Chatbot se task operations ke baad dashboard automatically update hoga

---

## 🎨 Theme Colors (Coffee & Caramel)

Chatbot ki design:
- ☕ Coffee Brown: #5d4037, #8d6e63
- 🍯 Caramel Gold: #d9a441
- ☁️ Light Cream: #f5f1ee
- 🌑 Dark Coffee: #3c2f2f

---

## 📱 Keyboard Shortcuts

- **Enter**: Message send karein
- **Esc**: Chatbot close karein (future feature)
- **Tab**: Input field pe focus karein

---

## 🚀 Quick Commands Summary

| Command Type | Example | Result |
|--------------|---------|--------|
| Add | "Add task X" | New task created |
| List | "Show my tasks" | All tasks displayed |
| Complete | "Mark task 1 done" | Task marked complete |
| Delete | "Delete task 1" | Task removed |
| Help | "What can you do?" | Help message |

---

## 📞 Common Questions

**Q: Kya Urdu mein type kar sakte hain?**
A: Haan! Natural language AI hai, Urdu/Hindi bhi samajh leta hai.

**Q: Kitne tasks add kar sakte hain?**
A: Unlimited! Jitne chahein utne.

**Q: Offline kaam karega?**
A: Nahi, internet chahiye for OpenAI API.

**Q: API calls paid hain?**
A: Haan, OpenAI API paid hai, lekin bahut sasta (gpt-4o-mini use kar rahe hain).

**Q: Mobile pe kaam karega?**
A: Haan! Responsive design hai.

---

## ✅ Final Checklist

- [x] MCP Server running (Port 8003)
- [x] AI Agent running (Port 8002)
- [ ] Frontend running (Port 3000) - Aap start karein
- [ ] Browser mein test karein
- [ ] Dashboard pe chatbot button dikhe
- [ ] Commands kaam kar rahe hain

---

**Sab kuch ready hai! Ab aap chatbot use kar sakte hain.** 🎉

**URLs:**
- Frontend: http://localhost:3000
- AI Agent: http://localhost:8002
- MCP Server: http://localhost:8003

**Services Status:**
- ✅ MCP Server: Running
- ✅ AI Agent: Running
- ⏳ Frontend: Start karein (`cd frontend && npm run dev`)

**Enjoy your AI-powered todo app!** ☕🍯🤖
