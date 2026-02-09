# Quick Start Guide - AI Chatbot

## 🚀 Quick Setup (3 Steps)

### Step 1: Install Dependencies

```bash
# Install AI Agent dependencies
cd ai-agent
pip install -r requirements.txt

# Install MCP Server dependencies
cd ../mcp-server
pip install -r requirements.txt

# Install Frontend dependencies (if not already done)
cd ../frontend
npm install
```

### Step 2: Start Services

**Option A: Use the automated script (Windows)**
```bash
# From the project root
start-chatbot-services.bat
```

**Option B: Start services manually**

Open 3 separate terminals:

```bash
# Terminal 1: MCP Server
cd mcp-server
python http_wrapper.py

# Terminal 2: AI Agent
cd ai-agent
python main.py

# Terminal 3: Frontend
cd frontend
npm run dev
```

### Step 3: Test the Chatbot

1. Open browser: `http://localhost:3000`
2. Login to your account
3. Go to Dashboard
4. Click the floating chat button (bottom-right)
5. Try: "Show my tasks" or "Add a task to test chatbot"

## 🧪 Run Tests

```bash
python test-chatbot.py
```

This will verify:
- ✅ MCP Server is running
- ✅ AI Agent is running
- ✅ Backend API is accessible
- ✅ Chatbot can process messages
- ✅ Tasks can be managed via chatbot

## 💬 Example Commands

| Command | What it does |
|---------|-------------|
| "Add a task to buy milk" | Creates a new task |
| "Show my tasks" | Lists all your tasks |
| "List all tasks" | Lists all your tasks |
| "Mark task 1 as completed" | Completes task #1 |
| "Delete task 2" | Deletes task #2 |
| "Update task 3 to done" | Marks task #3 as complete |

## 🎨 Chatbot Features

- **Coffee & Caramel Theme**: Matches your website design
- **Real-time Updates**: Dashboard refreshes automatically
- **Natural Language**: Talk naturally, no need for commands
- **Error Handling**: Clear messages if something goes wrong
- **Health Indicator**: Shows if AI is online/offline

## 📱 Chatbot UI Location

The chatbot appears as a **floating button** on the bottom-right of the dashboard:

```
Dashboard Page
┌─────────────────────────────────────┐
│  Tasks List                         │
│  [Add Task Form]                    │
│                                     │
│  Your Tasks:                        │
│  □ Task 1                           │
│  □ Task 2                           │
│                              [💬]   │ ← Chatbot Button
└─────────────────────────────────────┘
```

## 🔧 Ports Used

| Service | Port | URL |
|---------|------|-----|
| Frontend | 3000 | http://localhost:3000 |
| AI Agent | 8002 | http://localhost:8002 |
| MCP Server | 8003 | http://localhost:8003 |
| Backend API | 8000 | https://rameesha12123214-todophase02-backend.hf.space |

## ⚠️ Troubleshooting

### Chatbot shows offline
```bash
# Check if AI Agent is running
curl http://localhost:8002
# Should return: {"status":"healthy","service":"AI Agent"}
```

### Can't add/delete tasks
```bash
# Check if MCP Server is running
curl http://localhost:8003
# Should return: {"status":"healthy","service":"HTTP-based MCP Server"}
```

### "Failed to communicate"
1. Verify all services are running
2. Check console for error messages
3. Run `python test-chatbot.py` to diagnose

## 📝 Environment Variables

Already configured in:
- `ai-agent/.env` - OpenAI API key and MCP server URL
- `mcp-server/.env` - Backend API URL
- `frontend/.env.local` - AI Agent URL

## 🎯 Success Checklist

- [ ] Can open chatbot by clicking the button
- [ ] Chatbot shows welcome message
- [ ] "Show my tasks" displays tasks
- [ ] "Add a task" creates a new task
- [ ] Dashboard updates automatically
- [ ] Tasks can be deleted via chatbot
- [ ] Chatbot responds naturally

## 🆘 Need Help?

1. Check `CHATBOT_SETUP.md` for detailed setup
2. Run `python test-chatbot.py` for diagnostics
3. Check terminal logs for errors
4. Verify .env files have correct values

---

**Made with ☕ Coffee & 🍯 Caramel theme**
