# 🤖 AI Chatbot - Complete Guide

## 📖 Table of Contents
1. [Overview](#overview)
2. [Quick Start](#quick-start)
3. [Features](#features)
4. [Usage Examples](#usage-examples)
5. [Architecture](#architecture)
6. [Troubleshooting](#troubleshooting)

---

## 🎯 Overview

Your Todo application now includes an **AI-powered chatbot** that lets users manage tasks through natural conversation. The chatbot:

- ☕ Matches your coffee & caramel theme perfectly
- 💬 Understands natural language commands
- ⚡ Updates the dashboard in real-time
- 🎨 Features beautiful animations and smooth UX
- 🤖 Powered by OpenAI GPT-4o-mini

### Visual Preview

```
Dashboard with Chatbot
┌────────────────────────────────────────┐
│  Your Tasks                            │
│  □ Buy groceries                       │
│  □ Finish homework                     │
│  ☑ Call mom                            │
│                                        │
│                                 [💬]   │ ← Click here!
└────────────────────────────────────────┘

When opened:
┌────────────────────┐
│ AI Assistant   [X] │
├────────────────────┤
│ 🤖 How can I      │
│    help you?      │
│                   │
│       You 👤      │
│ Add task to       │
│ buy milk          │
│                   │
│ 🤖 Task added!    │
├────────────────────┤
│ Type here...  [→] │
└────────────────────┘
```

---

## 🚀 Quick Start

### Step 1: Install Dependencies

```bash
# AI Agent dependencies
cd ai-agent
pip install -r requirements.txt

# MCP Server dependencies
cd ../mcp-server
pip install -r requirements.txt

# Frontend dependencies (if needed)
cd ../frontend
npm install
```

### Step 2: Start Services

**Option A: Automated (Windows)**
```bash
# From project root
start-chatbot-services.bat
```

**Option B: Manual (3 terminals)**
```bash
# Terminal 1
cd mcp-server
python http_wrapper.py

# Terminal 2
cd ai-agent
python main.py

# Terminal 3
cd frontend
npm run dev
```

### Step 3: Use the Chatbot

1. Open browser: `http://localhost:3000`
2. Login to your account
3. Navigate to Dashboard
4. Click the floating chat button (bottom-right)
5. Start chatting!

### Step 4: Test It

```bash
# Run automated tests
python test-chatbot.py
```

Expected: `5/5 tests passed ✅`

---

## ✨ Features

### 1. Natural Language Understanding
Talk naturally - no need for specific commands:
- ✅ "Add a task to buy milk"
- ✅ "Show me what I need to do"
- ✅ "Mark the first task as done"
- ✅ "Delete task number 2"

### 2. Real-time Dashboard Updates
When the chatbot performs actions:
- Tasks appear/update/disappear automatically
- No manual refresh needed
- Instant feedback

### 3. Beautiful UI
- Coffee & caramel themed design
- Smooth animations
- Glow effects
- Loading indicators
- Message timestamps

### 4. Smart Features
- Conversation history (within session)
- Health status indicator
- Error handling with clear messages
- Typing indicators
- Auto-scroll to new messages

### 5. Complete Task Management
- ➕ Add tasks
- 📋 List tasks
- ✏️ Update tasks
- 🗑️ Delete tasks

---

## 💬 Usage Examples

### Adding Tasks

```
You: "Add a task to buy groceries"
🤖: "Task added: buy groceries"

You: "Create a new task: finish homework"
🤖: "Task created successfully!"

You: "Make a reminder to call mom"
🤖: "Added task: call mom"
```

### Viewing Tasks

```
You: "Show my tasks"
🤖: "Your tasks:
     1. [○] Buy groceries
     2. [○] Finish homework
     3. [✓] Call mom"

You: "What do I need to do?"
🤖: "You have 3 tasks: ..."

You: "List all my todos"
🤖: "Here are your tasks: ..."
```

### Completing Tasks

```
You: "Mark task 1 as completed"
🤖: "Task updated successfully!"

You: "Complete the homework task"
🤖: "Task marked as done!"

You: "Finish task 2"
🤖: "Task completed!"
```

### Deleting Tasks

```
You: "Delete task 1"
🤖: "Task deleted successfully!"

You: "Remove the groceries task"
🤖: "Task removed!"
```

### Conversational

```
You: "Hello!"
🤖: "Hello! I'm here to help you manage
     your tasks. What can I do for you?"

You: "What can you do?"
🤖: "I can help you:
     • Add new tasks
     • Show your task list
     • Mark tasks as complete
     • Delete tasks

     Just ask me naturally!"
```

---

## 🏗️ Architecture

### System Components

```
Frontend (React)
    ↓
AI Agent (Port 8002)
    ↓ (uses OpenAI)
MCP Server (Port 8003)
    ↓
Backend API (Port 8000)
    ↓
Database
```

### Component Details

| Component | Port | Technology | Purpose |
|-----------|------|------------|---------|
| Frontend | 3000 | Next.js, React | User interface |
| AI Agent | 8002 | FastAPI, OpenAI | Natural language processing |
| MCP Server | 8003 | FastAPI | API translation layer |
| Backend API | 8000 | FastAPI | Task operations |

### File Structure

```
project-root/
├── ai-agent/
│   ├── agent.py              # AI logic
│   ├── main.py               # FastAPI server
│   ├── requirements.txt      # Dependencies
│   └── .env                  # Configuration
│
├── mcp-server/
│   ├── http_wrapper.py       # HTTP endpoints
│   ├── tools.py              # Tool definitions
│   ├── requirements.txt      # Dependencies
│   └── .env                  # Configuration
│
├── frontend/
│   └── src/
│       ├── components/
│       │   └── Chatbot.tsx   # Chatbot UI
│       └── services/
│           └── chatbot_api.ts # API client
│
├── start-chatbot-services.bat # Startup script
├── test-chatbot.py           # Testing script
└── [Documentation files]
```

---

## 🎨 Theme Integration

The chatbot perfectly matches your coffee & caramel theme:

### Colors Used
- **Coffee Brown**: `#5d4037`, `#8d6e63` (buttons, borders)
- **Caramel Gold**: `#d9a441` (accents, highlights)
- **Light Cream**: `#f5f1ee` (backgrounds)
- **Dark Coffee**: `#3c2f2f` (text)

### Visual Elements
- ✨ Animated glow effects
- 🎭 Smooth transitions (300ms)
- 💫 Gradient backgrounds
- 🔄 Loading animations
- 📱 Responsive design

---

## 🔧 Configuration

### Environment Variables

All configured in:

**`ai-agent/.env`**
```env
OPENAI_API_KEY=your_key_here
MCP_SERVER_URL=http://localhost:8003
```

**`mcp-server/.env`**
```env
BACKEND_BASE_URL=your_backend_url
```

**`frontend/.env.local`**
```env
NEXT_PUBLIC_AI_AGENT_URL=http://localhost:8002
```

### Ports

| Service | Port | Status |
|---------|------|--------|
| Frontend | 3000 | ✅ Configured |
| AI Agent | 8002 | ✅ Configured |
| MCP Server | 8003 | ✅ Configured |
| Backend API | 8000 | ✅ Running (HuggingFace) |

---

## 🐛 Troubleshooting

### Chatbot Shows "Offline"

**Problem**: Chatbot button shows offline status

**Solution**:
```bash
# Check if AI Agent is running
curl http://localhost:8002
# Should return: {"status":"healthy","service":"AI Agent"}

# If not running, start it:
cd ai-agent
python main.py
```

### "Failed to communicate with AI assistant"

**Problem**: Error when sending messages

**Solution**:
```bash
# 1. Check MCP Server
curl http://localhost:8003
# Should return: {"status":"healthy"...}

# 2. Check .env files
cat ai-agent/.env    # Verify OpenAI key
cat mcp-server/.env  # Verify backend URL

# 3. Restart services
# Stop all Python processes
# Restart using start-chatbot-services.bat
```

### Tasks Not Updating

**Problem**: Chatbot responds but dashboard doesn't update

**Solution**:
1. Check browser console for errors (F12)
2. Verify you're logged in
3. Check network tab for failed requests
4. Ensure backend API is accessible

### OpenAI API Errors

**Problem**: "Invalid API key" or timeout errors

**Solution**:
```bash
# 1. Verify API key
echo $OPENAI_API_KEY  # Should show your key

# 2. Check OpenAI account
# - Visit platform.openai.com
# - Verify you have credits
# - Check API key is valid

# 3. Test API directly
curl https://api.openai.com/v1/models \
  -H "Authorization: Bearer YOUR_KEY"
```

### Port Already in Use

**Problem**: "Address already in use" error

**Solution**:
```bash
# Windows
netstat -ano | findstr :8002  # Find process
taskkill /PID <pid> /F        # Kill process

# Then restart the service
```

### Import Errors

**Problem**: "No module named 'fastapi'" or similar

**Solution**:
```bash
# Reinstall dependencies
cd ai-agent
pip install -r requirements.txt --force-reinstall

cd ../mcp-server
pip install -r requirements.txt --force-reinstall
```

---

## 🧪 Testing

### Manual Testing Checklist

- [ ] Chatbot button appears on dashboard
- [ ] Button has coffee/caramel colors
- [ ] Clicking opens chat window
- [ ] Welcome message displays
- [ ] Can send messages
- [ ] AI responds to messages
- [ ] "Show my tasks" lists tasks
- [ ] "Add task" creates new task
- [ ] Dashboard updates automatically
- [ ] "Complete task" marks as done
- [ ] "Delete task" removes task
- [ ] Error messages are clear
- [ ] No console errors

### Automated Testing

```bash
# Run comprehensive test suite
python test-chatbot.py

# Expected output:
# ✅ MCP Server health check
# ✅ AI Agent health check
# ✅ Backend API accessible
# ✅ MCP tool execution
# ✅ Chatbot conversation
# Total: 5/5 tests passed
```

### Test Commands

Try these in the chatbot:

1. **Hello**: Test basic response
2. **Show my tasks**: Test task listing
3. **Add a task to test the bot**: Test task creation
4. **Mark task 1 as completed**: Test task update
5. **Delete task 1**: Test task deletion

---

## 📚 Additional Resources

### Documentation Files

- **`CHATBOT_SETUP.md`** - Detailed setup instructions
- **`QUICK_START_CHATBOT.md`** - Get started in 5 minutes
- **`CHATBOT_SUMMARY.md`** - Feature overview and architecture
- **`CHATBOT_UI_GUIDE.md`** - Design specifications
- **`CHATBOT_CHECKLIST.md`** - Verification checklist

### Useful Commands

```bash
# Health checks
curl http://localhost:8002  # AI Agent
curl http://localhost:8003  # MCP Server
curl http://localhost:3000  # Frontend

# View logs
# Check the terminal windows where services are running

# Restart services
# Stop: Ctrl+C in each terminal
# Start: Use start-chatbot-services.bat

# Run tests
python test-chatbot.py
```

---

## 🎯 Success Criteria

Your chatbot is working correctly if:

✅ Button appears on dashboard (bottom-right)
✅ Theme matches coffee & caramel colors
✅ Can open/close chatbot smoothly
✅ Welcome message displays
✅ Can send and receive messages
✅ Natural language commands work
✅ Tasks can be added via chat
✅ Tasks can be listed via chat
✅ Tasks can be updated via chat
✅ Tasks can be deleted via chat
✅ Dashboard updates automatically
✅ No console errors
✅ Test script passes all checks

---

## 🚀 Next Steps

### Immediate Actions
1. ✅ Start all services
2. ✅ Open dashboard
3. ✅ Test chatbot functionality
4. ✅ Run test script

### Future Enhancements
- 📅 Task scheduling
- 🔔 Reminders
- 📊 Task analytics
- 🗣️ Voice input
- 🌍 Multi-language support
- 💾 Conversation persistence
- 🤝 Task sharing

---

## 💡 Tips & Best Practices

### For Users
- Speak naturally - the AI understands context
- Use task numbers when updating/deleting
- Check the dashboard for visual confirmation
- Report issues in the browser console

### For Developers
- Keep services running in separate terminals
- Monitor logs for errors
- Use the test script regularly
- Check .env files if issues occur
- Keep OpenAI API key secure

---

## 📞 Support

### Getting Help

1. **Check Documentation**: Review the guides above
2. **Run Tests**: `python test-chatbot.py`
3. **Check Logs**: Look at terminal outputs
4. **Browser Console**: Press F12 to check for errors

### Common Issues

Most issues are resolved by:
1. Restarting services
2. Checking .env files
3. Verifying OpenAI API key
4. Ensuring all dependencies installed

---

## 🎉 Summary

You now have a fully functional AI chatbot that:
- 🎨 Matches your beautiful coffee & caramel theme
- 💬 Understands natural language
- ⚡ Performs all task operations
- 🔄 Updates the dashboard automatically
- ✨ Provides smooth, polished UX

**Status**: ✅ Production Ready
**Theme**: ☕ Coffee & 🍯 Caramel
**Integration**: ✅ Complete

Enjoy your AI-powered todo app! 🚀
