// src/pages/Home.jsx
import { useState } from "react";
import InputBox from "../components/InputBox";
import ResultCard from "../components/ResultCard";
import { predictSentiment } from "../services/api";

function Home() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async () => {
    setLoading(true);
    setError("");
    setResult(null);
    try {
      const data = await predictSentiment(text);
      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="home">
      <h1>🎬 Movie Review Sentiment Analyzer</h1>
      <InputBox
        text={text}
        setText={setText}
        onSubmit={handleSubmit}
        loading={loading}
      />
      {error && <p className="error">⚠️ {error}</p>}
      <ResultCard result={result} />
    </div>
  );
}

export default Home;
