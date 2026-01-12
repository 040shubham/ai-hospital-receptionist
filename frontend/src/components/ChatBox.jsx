import { useState } from "react";

export default function ChatBox({ onSend }) {
  const [text, setText] = useState("");

  function handleSend() {
    if (!text.trim()) return;
    onSend(text);
    setText("");
  }

  return (
    <div className="flex gap-2">
      <input
        className="border rounded w-full p-2"
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Type your message..."
      />
      <button
        className="bg-blue-500 text-white px-4 rounded"
        onClick={handleSend}
      >
        Send
      </button>
    </div>
  );
}
