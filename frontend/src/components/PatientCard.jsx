export default function PatientCard({ data }) {
  return (
    <div className="mt-4 bg-green-100 p-4 rounded">
      <h2 className="font-bold mb-2">Patient Summary</h2>
      <p><b>Name:</b> {data.name}</p>
      <p><b>Age:</b> {data.age}</p>
      <p><b>Problem:</b> {data.query}</p>
      <p><b>Ward:</b> {data.ward}</p>
    </div>
  );
}
