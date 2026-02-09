#!/usr/bin/env python3
"""
Test script to verify the chatbot system is working correctly
"""

import requests
import json
import time
import sys

# Configuration
MCP_SERVER_URL = "http://localhost:8003"
AI_AGENT_URL = "http://localhost:8002"
BACKEND_URL = "https://rameesha12123214-todophase02-backend.hf.space"

def check_service(name, url):
    """Check if a service is running"""
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"✅ {name} is running at {url}")
            return True
        else:
            print(f"❌ {name} returned status code {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ {name} is not accessible at {url}")
        print(f"   Error: {e}")
        return False

def test_mcp_server():
    """Test MCP Server health"""
    print("\n🧪 Testing MCP Server...")
    return check_service("MCP Server", MCP_SERVER_URL)

def test_ai_agent():
    """Test AI Agent health"""
    print("\n🧪 Testing AI Agent...")
    return check_service("AI Agent", AI_AGENT_URL)

def test_backend():
    """Test Backend API health"""
    print("\n🧪 Testing Backend API...")
    return check_service("Backend API", f"{BACKEND_URL}/docs")

def test_chatbot_conversation():
    """Test a complete chatbot conversation flow"""
    print("\n🧪 Testing Chatbot Conversation...")

    try:
        # Send a test message
        test_message = {
            "message": "List my tasks",
            "user_id": "test_user"
        }

        print(f"   Sending message: '{test_message['message']}'")
        response = requests.post(
            f"{AI_AGENT_URL}/chat",
            json=test_message,
            timeout=30
        )

        if response.status_code == 200:
            data = response.json()
            print("✅ Chatbot responded successfully!")
            print(f"   Response: {data.get('response', 'No response')[:100]}...")
            print(f"   Conversation ID: {data.get('conversation_id', 'N/A')}")
            print(f"   Tool calls: {len(data.get('tool_calls', []))}")
            return True
        else:
            print(f"❌ Chatbot returned status code {response.status_code}")
            print(f"   Response: {response.text}")
            return False

    except requests.exceptions.Timeout:
        print("❌ Request timed out (took longer than 30 seconds)")
        print("   This might indicate an issue with the OpenAI API or MCP server")
        return False
    except Exception as e:
        print(f"❌ Error testing chatbot: {e}")
        return False

def test_mcp_tool_execution():
    """Test MCP Server tool execution"""
    print("\n🧪 Testing MCP Server Tool Execution...")

    try:
        # Test the get_tasks tool
        tool_request = {
            "tool_name": "get_tasks",
            "parameters": {
                "session_token": ""
            }
        }

        print("   Calling 'get_tasks' tool...")
        response = requests.post(
            f"{MCP_SERVER_URL}/call_tool",
            json=tool_request,
            timeout=10
        )

        if response.status_code == 200:
            data = response.json()
            print("✅ MCP tool executed successfully!")
            print(f"   Result: {data.get('result', 'No result')[:100]}...")
            return True
        else:
            print(f"❌ MCP tool execution failed with status {response.status_code}")
            print(f"   Response: {response.text}")
            return False

    except Exception as e:
        print(f"❌ Error testing MCP tool: {e}")
        return False

def main():
    """Run all tests"""
    print("=" * 60)
    print("AI Chatbot System Test Suite")
    print("=" * 60)

    results = {
        "MCP Server": test_mcp_server(),
        "AI Agent": test_ai_agent(),
        "Backend API": test_backend(),
        "MCP Tool Execution": test_mcp_tool_execution(),
        "Chatbot Conversation": test_chatbot_conversation(),
    }

    print("\n" + "=" * 60)
    print("Test Results Summary")
    print("=" * 60)

    for test_name, passed in results.items():
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{test_name:.<40} {status}")

    print("=" * 60)

    total_tests = len(results)
    passed_tests = sum(1 for passed in results.values() if passed)

    print(f"\nTotal: {passed_tests}/{total_tests} tests passed")

    if passed_tests == total_tests:
        print("\n🎉 All tests passed! The chatbot system is working correctly.")
        return 0
    else:
        print("\n⚠️  Some tests failed. Please check the errors above.")
        print("\nTroubleshooting tips:")
        print("1. Make sure all services are running (use start-chatbot-services.bat)")
        print("2. Check that your .env files have the correct configuration")
        print("3. Verify your OpenAI API key is valid and has credits")
        print("4. Ensure the backend API is accessible")
        return 1

if __name__ == "__main__":
    sys.exit(main())
