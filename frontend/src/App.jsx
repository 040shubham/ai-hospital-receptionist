import { useState } from "react";
import ChatBox from "./components/ChatBox";
import Message from "./components/Message";
import PatientCard from "./components/PatientCard";
import WardBadge from "./components/WardBadge";

function App() {
  const [messages, setMessages] = useState([]);
  const [state, setState] = useState({});

  async function sendMessage(text) {
    setMessages((prev) => [...prev, { from: "user", text }]);

    const res = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        message: text,
        session_id: "demo-session-1"
      }),
    });

    const data = await res.json();

    console.log("API RESPONSE:", data);

   setMessages((prev) => [
  ...prev,
  { from: "ai", text: data.reply },
]);

setState((prev) => ({
  ...prev,
  ward: data.ward || prev.ward,
}));

  }

  return (
    <div className="min-h-screen bg-gray-100 p-4">
      <h1 className="text-xl font-bold mb-4">
        🏥 AI Hospital Receptionist
      </h1>

      {state.ward && <WardBadge ward={state.ward} />}

      <div className="bg-white rounded p-4 h-96 overflow-y-auto mb-4">
        {messages.map((m, i) => (
          <Message key={i} from={m.from} text={m.text} />
        ))}
      </div>

      <ChatBox onSend={sendMessage} />

      {state.completed && <PatientCard data={state} />}
    </div>
  );
}

export default App;
