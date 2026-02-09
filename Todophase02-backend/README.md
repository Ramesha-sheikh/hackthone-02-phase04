---
title: Todophase02 Backend
emoji: 📈
colorFrom: red
colorTo: green
sdk: docker
sdk_version: "latest"
app_file: app.py
pinned: false
---

# Todo App Backend

A FastAPI-based backend for a todo application with user authentication and task management capabilities.

## Features
- User authentication with JWT tokens
- Task CRUD operations with user authorization
- PostgreSQL database with SQLModel
- Secure password hashing with bcrypt
- Modern Python web development practices

## Deployment
This backend is configured for deployment on Hugging Face Spaces using Docker.

### Environment Variables
Set the following environment variables in your Hugging Face Space settings:


### Ports
The application runs on port **7860** as required by Hugging Face Spaces.

### Endpoints
- `GET /` – Welcome message  
- `POST /api/auth/signup` – User registration  
- `POST /api/auth/signin` – User login  
- `GET /api/tasks/` – Get user's tasks  
- `POST /api/tasks/` – Create a new task  
- `PUT /api/tasks/{id}` – Update a task  
- `DELETE /api/tasks/{id}` – Delete a task  

All endpoints (except signup, signin, and root) require a valid JWT token in the `Authorization` header.
