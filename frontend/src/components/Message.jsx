export default function Message({ from, text }) {
  const isUser = from === "user";

  return (
    <div className={`mb-2 ${isUser ? "text-right" : "text-left"}`}>
      <span
        className={`inline-block p-2 rounded ${
          isUser ? "bg-blue-200" : "bg-gray-200"
        }`}
      >
        {text}
      </span>
    </div>
  );
}
