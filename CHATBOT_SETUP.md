# AI Chatbot Setup Guide

This guide will help you set up and test the AI chatbot integrated with your Todo application.

## Architecture Overview

The chatbot system consists of three main components:

1. **AI Agent** (Port 8002) - FastAPI service that processes natural language using OpenAI
2. **MCP Server** (Port 8003) - HTTP wrapper that connects the AI agent to the backend API
3. **Frontend Chatbot UI** - React component integrated into the dashboard

## Prerequisites

- Python 3.8+ installed
- Node.js 16+ installed
- OpenAI API key
- Backend API running on port 8000

## Setup Instructions

### 1. Install Python Dependencies

#### AI Agent
```bash
cd ai-agent
pip install -r requirements.txt
```

#### MCP Server
```bash
cd mcp-server
pip install -r requirements.txt
```

### 2. Configure Environment Variables

#### AI Agent (.env)
Edit `ai-agent/.env`:
```
OPENAI_API_KEY=your_actual_openai_api_key_here
MCP_SERVER_URL=http://localhost:8003
```

#### MCP Server (.env)
Edit `mcp-server/.env`:
```
BACKEND_BASE_URL=http://localhost:8000
```

#### Frontend (.env.local)
Already configured in `frontend/.env.local`:
```
NEXT_PUBLIC_AI_AGENT_URL=http://localhost:8002
```

### 3. Start All Services

You need to run these services in separate terminal windows:

#### Terminal 1: Backend API (if not already running)
```bash
cd Todophase02-backend
uvicorn main:app --reload --port 8000
```

#### Terminal 2: MCP Server
```bash
cd mcp-server
python http_wrapper.py
```

#### Terminal 3: AI Agent
```bash
cd ai-agent
python main.py
```

#### Terminal 4: Frontend
```bash
cd frontend
npm run dev
```

## Testing the Chatbot

### 1. Access the Dashboard
- Open your browser and navigate to `http://localhost:3000`
- Log in to your account
- Go to the Dashboard page

### 2. Open the Chatbot
- Look for the floating chat button in the bottom-right corner of the screen
- Click it to open the chatbot interface

### 3. Test Commands

Try these natural language commands:

#### Add Tasks
- "Add a task to buy groceries"
- "Create a new task: finish homework"
- "Make a task called prepare presentation"

#### List Tasks
- "Show my tasks"
- "List all tasks"
- "What tasks do I have?"
- "Display my todos"

#### Update Tasks
- "Mark task 1 as completed"
- "Update task 2 to done"
- "Complete task 3"

#### Delete Tasks
- "Delete task 1"
- "Remove task 2"

### 4. Expected Behavior

When you use the chatbot:
1. The chatbot should respond naturally to your commands
2. Task operations should be performed automatically
3. The task list on the dashboard should update in real-time
4. The chatbot will confirm each action

## Troubleshooting

### Chatbot shows "offline" status
- Check if AI Agent is running on port 8002
- Verify `NEXT_PUBLIC_AI_AGENT_URL` in frontend/.env.local

### "Failed to communicate with AI assistant"
- Ensure MCP Server is running on port 8003
- Check MCP_SERVER_URL in ai-agent/.env

### "Failed to add/update/delete task"
- Verify backend API is running on port 8000
- Check BACKEND_BASE_URL in mcp-server/.env
- Make sure you're logged in and have a valid auth token

### OpenAI API errors
- Verify your OpenAI API key is correct
- Check if you have sufficient credits in your OpenAI account
- Ensure you're using a valid model (gpt-4o-mini)

## Architecture Flow

```
User Input (Frontend)
    ↓
Chatbot Component (React)
    ↓
AI Agent (Port 8002) - Processes natural language with OpenAI
    ↓
MCP Server (Port 8003) - Translates to API calls
    ↓
Backend API (Port 8000) - Performs database operations
    ↓
Response flows back through the same chain
```

## Features

### Coffee & Caramel Theme Integration
- The chatbot UI matches the website's coffee and caramel color scheme
- Smooth animations and transitions
- Floating chat button with glow effects
- Message bubbles with proper styling

### Real-time Updates
- When the chatbot performs task operations, the dashboard automatically refreshes
- No need to manually reload the page

### Conversation Context
- The chatbot maintains conversation history within each session
- Each conversation has a unique ID for tracking

### Error Handling
- Graceful error messages for offline services
- Clear feedback when operations fail
- Health check indicators

## Development Notes

### File Structure
```
ai-agent/
  ├── agent.py          # Core AI logic with OpenAI integration
  ├── main.py           # FastAPI server
  └── requirements.txt  # Python dependencies

mcp-server/
  ├── http_wrapper.py   # HTTP endpoint wrapper
  ├── tools.py          # MCP tool definitions
  └── requirements.txt  # Python dependencies

frontend/src/
  ├── components/
  │   └── Chatbot.tsx   # Main chatbot UI component
  └── services/
      └── chatbot_api.ts # API client for AI agent
```

### Customization

To modify the chatbot behavior:
1. Edit `ai-agent/agent.py` to change natural language processing logic
2. Modify `frontend/src/components/Chatbot.tsx` to change UI appearance
3. Update `mcp-server/http_wrapper.py` to add new tool capabilities

## Security Notes

- Never commit `.env` files with actual API keys
- The `.env` files are already in `.gitignore`
- In production, use proper environment variable management
- Implement rate limiting for the chatbot endpoint

## Next Steps

1. Test all chatbot commands thoroughly
2. Add more sophisticated natural language understanding
3. Implement conversation memory across sessions
4. Add support for more complex task operations
5. Deploy all services to production environment
