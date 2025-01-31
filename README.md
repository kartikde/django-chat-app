# Django Chat Application

A simple chat application built with Django and Channels that allows users to sign up, log in, and chat with each other in real-time using WebSockets.

## Features

- User authentication (Sign up and Login).
- Real-time chat using WebSockets.
- Chat rooms where users can send and receive messages.
- Collapsible left menu with a list of registered users.
- Responsive and user-friendly chat interface.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher installed.
- Django 5.0 or higher.
- Channels installed (`channels` for WebSocket support).
- An AWS account (for the Lambda tasks).

### Installing Dependencies

1. Clone the repository (if you haven't already).
   
   If you're using Git, run:
   ```bash
   git clone https://github.com/yourusername/chat-app.git
   ```

2. Navigate to the project directory:
   ```bash
   cd chatapp
   ```

3. Create a virtual environment (recommended) and activate it:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # For Windows
   ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` is not available, install the necessary packages manually:
   ```bash
   pip install django channels
   ```

---

## Setting Up the Project

1. **Create Database**:
   - Migrate the database to create necessary tables.
   ```bash
   python manage.py migrate
   ```

2. **Create a Superuser**:
   - Create an admin user to access the Django admin panel.
   ```bash
   python manage.py createsuperuser
   ```

3. **Run the Server**:
   - Start the Django development server.
   ```bash
   python manage.py runserver
   ```

   Now you can access the app at `http://127.0.0.1:8000/`.

---

## Usage

1. **Sign Up**:
   - Visit `/accounts/signup/` to create a new user.

2. **Log In**:
   - After signing up, visit `/accounts/login/` to log in.

3. **Chat**:
   - After logging in, you will be redirected to the chat room page.
   - On the left side, you will see a collapsible list of registered users.
   - Click on a user’s name to initiate a chat.

4. **WebSockets**:
   - The chat interface uses WebSockets for real-time communication. Once you send a message, it will be immediately displayed on the other user's screen.

---

## Project Structure

```
chatapp/
│
├── chat/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── consumers.py  # WebSocket consumers
│   ├── models.py
│   ├── routing.py    # WebSocket routing
│   ├── templates/
│   │   └── chat/
│   │       └── chat_room.html  # Chat interface
│   ├── urls.py
│   ├── views.py
│   └── ...
│
├── chatapp/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py         # ASGI for Channels
│   ├── wsgi.py
│   └── ...
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

---


1. **Add Lambda Function**:
   - For instructions on how to set up AWS Lambda functions, refer to the AWS Lambda documentation or [Lambda setup instructions](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html).

---

Let me know if you need any additional help!
