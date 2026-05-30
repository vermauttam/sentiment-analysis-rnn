// src/services/api.js
const API_URL = "http://127.0.0.1:8000/predict";

export async function predictSentiment(text) {
  const response = await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text }),
  });

  if (!response.ok) {
    throw new Error(`Server error: ${response.status}`);
  }

  return await response.json(); // { label, confidence } or whatever app.py returns
}
