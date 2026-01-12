export default function WardBadge({ ward }) {
  const colors = {
    Emergency: "bg-red-500",
    General: "bg-blue-500",
    "Mental Health": "bg-purple-500",
  };

  return (
    <span
      className={`inline-block text-white px-3 py-1 rounded mb-2 ${colors[ward]}`}
    >
      Ward: {ward}
    </span>
  );
}
