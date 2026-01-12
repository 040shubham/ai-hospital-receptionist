# 🏥 AI Hospital Receptionist System

An AI-powered full-stack web application that automates the hospital front-desk process by interacting with patients through a chat-based interface. The system collects patient details step-by-step, classifies medical queries into appropriate hospital wards, securely stores patient data, and supports webhook-based automation.

---

## 📌 Project Overview

The **AI Hospital Receptionist System** simulates a real-world hospital reception workflow. Instead of a human receptionist, the system interacts with patients using a conversational interface, gathers essential medical information, and routes the case to the appropriate hospital department.

This project demonstrates **full-stack development**, **API integration**, **environment configuration**, and **real-world debugging**.

---

## 🎯 Objectives

- Build a chat-based patient interaction system
- Collect patient details step-by-step
- Automatically classify patients into hospital wards
- Store patient data securely in a cloud database
- Enable external automation using webhooks
- Handle real-world frontend–backend integration challenges

---

## 🧱 Tech Stack

| Layer | Technology |
|-----|-----------|
| Frontend | React (Vite) |
| Styling | Tailwind CSS |
| Backend | FastAPI (Python) |
| Database | Supabase (PostgreSQL) |
| API | REST |
| Configuration | dotenv (.env) |
| Automation | Webhooks (optional) |

---

## 📁 Project Structure

ai-hospital-receptionist/
│
├── frontend/
│ ├── src/
│ │ ├── App.jsx
│ │ ├── index.css
│ │ └── components/
│ │ ├── ChatBox.jsx
│ │ └── Message.jsx
│ ├── package.json
│ └── vite.config.js
│
└── backend/
├── main.py
├── state.py
├── webhook.py
├── requirements.txt
└── .env


---

## 🚀 Application Flow

1. Patient opens the web application
2. Patient interacts via chat interface
3. System asks questions step-by-step:
   - Greeting
   - Age
   - Health problem
4. System classifies the patient into a ward:
   - Emergency
   - General
   - Mental Health
5. Patient data is stored in the database
6. Optional webhook is triggered for automation
7. System confirms completion

---

## 🖥️ Frontend Details

- Built using **React with Vite** for fast development
- Styled using **Tailwind CSS**
- Chat-style UI for better user experience
- Real-time message rendering
- API calls handled using `fetch()`

---

## 🧠 Backend & Chat Logic

- Backend built with **FastAPI**
- `/chat` endpoint handles all conversation logic
- Session-based state management
- Input validation using Pydantic
- Ward classification based on keywords
- CORS enabled for frontend communication

---

## 🗄️ Database Integration (Supabase)

- Uses Supabase (PostgreSQL) for data storage
- Stores patient details:
  - Name
  - Age
  - Medical query
  - Assigned ward
- Secure access using environment variables

---

## 🔐 Environment Configuration

Create a `.env` file inside the `backend` directory:

SUPABASE_URL = os.geten("https://hqieeqrbkrsczyccoffg.supabase.co")
SUPABASE_KEY = os.geten("YeyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhxaWVlcXJia3JzY3p5Y2NvZmZnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Njc3MDU1NTMsImV4cCI6MjA4MzI4MTU1M30.sbznD9FNBK100ty3Mmbg9dECSoYy6cLEJARNW7jZi84BASE_ANON_KEY")  


Load environment variables in `main.py` using `python-dotenv`.

---

## 🧪 Local Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/ai-hospital-receptionist.git
cd ai-hospital-receptionist


2️⃣ Frontend Setup
cd frontend
npm install
npm run dev

Frontend runs at:

http://localhost:5173

3️⃣ Backend Setup
cd backend
pip install -r requirements.txt
uvicorn main:app --reload


Backend runs at:

http://127.0.0.1:8000


Swagger API Docs:

http://127.0.0.1:8000/docs

🐞 Issues Faced & Solutions

Issue	Solution
Tailwind PostCSS error	Used .cjs PostCSS config
PowerShell npm blocked	Updated execution policy
CORS error	Added CORSMiddleware
API mismatch	Synced frontend & backend
Supabase 401 error	Fixed invalid API key
JSON decode error	Corrected request body

✅ Final Output

Fully functional chat-based UI

Stable backend API

Secure database integration

Real-world debugging experience

Production-ready project structure

📈 Learning Outcomes

Full-stack application development

REST API design

Environment variable handling

Debugging configuration-level issues

Cloud database integration

System architecture design

🔮 Future Enhancements

NLP-based intent detection

Multi-language support

User authentication

Appointment scheduling

Admin dashboard

📄 License

This project is created for educational and demonstration purposes.

⭐ If you like this project, feel free to star the repository!


---

## ✅ NEXT STEPS

1. Paste this into `README.md`
2. Save file
3. Run:
```bash
git add README.md
git commit -m "Add detailed project README"
git push