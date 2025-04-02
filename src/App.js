import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [prompt, setPrompt] = useState("");
  const [image, setImage] = useState(null);
  const [loading, setLoading] = useState(false);

  const generateImage = async () => {
    setLoading(true);
    try {
      const response = await axios.post("http://127.0.0.1:5000/generate", {
        prompt,
      });
      setImage(response.data.image_url);
    } catch (error) {
      console.error("Error generating image:", error);
    }
    setLoading(false);
  };

  return (
    <div className="App">
      <h1>AI Fashion Assistant 👗</h1>
      <input
        type="text"
        placeholder="Describe your fashion idea..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />
      <button onClick={generateImage} disabled={loading}>
        {loading ? "Generating..." : "Generate Design"}
      </button>
      {image && (
        <div>
          <h3>Generated Design:</h3>
          <img src={`data:image/png;base64,${image}`} alt="Generated Design" />
        </div>
      )}
    </div>
  );
}

export default App;
