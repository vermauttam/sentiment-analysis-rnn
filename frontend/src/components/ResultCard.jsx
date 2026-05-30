// src/components/ResultCard.jsx
function ResultCard({ result }) {
  if (!result) return null;

  const label = result.label ?? result.sentiment ?? "unknown";
  const isPositive = label.toLowerCase() === "positive";
  const confidence =
    result.confidence != null
      ? (result.confidence * 100).toFixed(1) + "%"
      : null;

  return (
    <div className={`result-card ${isPositive ? "positive" : "negative"}`}>
      <h2>{isPositive ? "😊 Positive" : "😞 Negative"}</h2>
      {confidence && <p>Confidence: {confidence}</p>}
    </div>
  );
}

export default ResultCard;
