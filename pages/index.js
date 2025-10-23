import { useState } from "react";

export default function Home() {
  const [message, setMessage] = useState("");

  async function fetchAPI() {
    try {
      const res = await fetch("/api/hello");
      const data = await res.json();
      setMessage(data.message);
    } catch (error) {
      setMessage("Erro ao chamar a API");
    }
  }

  return (
    <div style={{ padding: 20 }}>
      <h1>Front-end React/Next.js</h1>
      <button onClick={fetchAPI}>Chamar API</button>
      {message && <p>Resposta da API: {message}</p>}
    </div>
  );
}
