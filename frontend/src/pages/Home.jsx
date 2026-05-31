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
    if (!text.trim()) {
      setError("Please enter a movie review first.");
      setResult(null);
      return;
    }

    setLoading(true);
    setError("");
    setResult(null);

    try {
      const data = await predictSentiment(text);
      setResult(data);
    } catch (err) {
      console.error(err);
      setError("Failed to analyze sentiment. Please check backend connection.");
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

      {result && <ResultCard result={result} />}
    </div>
  );
}

export default Home;
