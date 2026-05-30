// src/components/InputBox.jsx
function InputBox({ text, setText, onSubmit, loading }) {
  return (
    <div className="input-box">
      <textarea
        rows={5}
        placeholder="Type a movie review here..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <button onClick={onSubmit} disabled={loading || !text.trim()}>
        {loading ? "Analyzing..." : "Analyze Sentiment"}
      </button>
    </div>
  );
}

export default InputBox;
