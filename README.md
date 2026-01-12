# ai-hospital-receptionist
An AI-powered full-stack web application that automates hospital front-desk interactions by collecting patient details, classifying medical queries into appropriate wards, and securely storing patient information.
🏥 AI Hospital Receptionist System

A full-stack AI-powered hospital receptionist application that automates patient intake using a conversational chat interface. The system collects patient details step-by-step, classifies medical queries into appropriate hospital wards, stores records securely in a database, and supports webhook-based automation.

📌 Project Goals

Simulate a hospital front-desk using a chat interface

Collect patient details interactively

Classify patients into wards automatically

Store patient data securely

Handle real-world frontend–backend integration issues

Demonstrate production-level debugging and configuration
| Layer      | Technology                 |
| ---------- | -------------------------- |
| Frontend   | React (Vite), Tailwind CSS |
| Backend    | FastAPI (Python)           |
| Database   | Supabase (PostgreSQL)      |
| Styling    | Tailwind CSS               |
| API        | REST                       |
| Config     | `.env`, dotenv             |
| Automation | Webhooks (Optional)        |


📁 Project Structure
ai-hospital-receptionist/
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   └── components/
│   ├── index.css
│   └── package.json
│
└── backend/
    ├── main.py
    ├── state.py
    ├── webhook.py
    ├── .env
    └── requirements.txt
🚀 Step-by-Step Setup Process
1️⃣ Clone the Repository
git clone https://github.com/your-username/ai-hospital-receptionist.git
cd ai-hospital-receptionist

2️⃣ Frontend Setup (React + Vite)
cd frontend
npm install
npm run dev


If PowerShell blocks npm scripts:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser


Frontend runs at:

http://localhost:5173

3️⃣ Backend Setup (FastAPI)
cd backend
pip install -r requirements.txt
uvicorn main:app --reload


Backend runs at:

http://127.0.0.1:8000


Swagger UI:

http://127.0.0.1:8000/docs

4️⃣ Tailwind CSS Configuration

Installed Tailwind manually due to CLI conflicts

Resolved PostCSS ES module issue by using:

postcss.config.cjs

module.exports = {
  plugins: {
    "@tailwindcss/postcss": {},
    autoprefixer: {},
  },
};

5️⃣ Environment Variables Setup

Create .env inside backend/:

SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your_supabase_anon_key


Load env in main.py:

from dotenv import load_dotenv
import os

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

6️⃣ CORS Configuration
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

7️⃣ Chat Flow Logic

User sends greeting

System asks for age

User enters age (validated)

User describes health problem

System classifies ward:

Emergency

General

Mental Health

Data stored in Supabase

Optional webhook triggered

🐞 Issues Faced & Fixes
Issue	Resolution
Tailwind PostCSS errors	Switched to .cjs config
PowerShell npm blocked	Changed execution policy
CORS error	Added CORSMiddleware
API mismatch	Synced request/response
Supabase 401 error	Fixed invalid API key
JSON decode error	Corrected request body
🧪 Final Testing
API Test (Swagger)
{
  "message": "Hello",
  "session_id": "test-session"
}


Expected:

{
  "reply": "Thank you. Please tell your age."
}

✅ Final Result

Frontend chat UI fully functional

Backend API stable

Secure database storage

Real-world debugging experience

Production-ready architecture

📈 Learning Outcomes

Full-stack integration

API contract management

Environment variable handling

Debugging production-level issues

Cloud database usage

System architecture design

🔮 Future Enhancements

NLP-based intent detection

Multi-language support

Authentication

Appointment scheduling

Admin dashboard

📄 License

This project is for educational and demonstration purposes.
