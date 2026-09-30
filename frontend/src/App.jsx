import { useState } from "react";
import "./App.css";

function App() {
  const [question, setQuestion] = useState("");
  const [context, setContext] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const askQuestion = async () => {
    if (!question.trim()) return;

    setLoading(true);
    setAnswer("");
    setContext("");
    setError("");

    try {
      const response = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question }),
      });

      const data = await response.json();
      setContext(data.context || []);
      setAnswer(data.answer || "");
    } catch (err) {
      setError("Error connecting to backend.");
    }

    setLoading(false);
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && e.ctrlKey) askQuestion();
  };

  return (
    <div className="app-container">
      <header className="app-header">
        <h1>EBM Medical Research Assistant</h1>
        <p className="subtitle">Evidence-based oncology insights powered by AI</p>
      </header>

      <div className="input-section">
        <textarea
          id="question-input"
          rows="4"
          className="question-textarea"
          placeholder="Ask an oncology research question… (Ctrl+Enter to submit)"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          onKeyDown={handleKeyDown}
        />
        <button
          id="ask-btn"
          className="ask-btn"
          onClick={askQuestion}
          disabled={loading}
        >
          {loading ? (
            <span className="loading-dots">
              <span>.</span><span>.</span><span>.</span>
            </span>
          ) : (
            "Ask"
          )}
        </button>
      </div>

      {error && <p className="error-msg">{error}</p>}

      {context && (
        <section className="result-section" id="context-section">
          <h2 className="section-title">
            <span className="section-icon">📄</span> Retrieved Context
          </h2>
          <div className="answer-box">
            <pre className="answer-text" style={{whiteSpace: "pre-wrap", fontFamily: "inherit"}}>{context}</pre>
          </div>
        </section>
      )}

      {answer && (
        <section className="result-section" id="answer-section">
          <h2 className="section-title">
            <span className="section-icon">🧠</span> Final Answer
          </h2>
          <div className="answer-box">
            <p className="answer-text">{answer}</p>
          </div>
        </section>
      )}
    </div>
  );
}

export default App;