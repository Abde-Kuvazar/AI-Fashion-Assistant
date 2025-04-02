import React, { useState } from "react";
import axios from "axios";
import "./App.css";


function App() {
  const [prompt, setPrompt] = useState("");
  const [image, setImage] = useState(null);
  const [loading, setLoading] = useState(false);

  const generateImage = async () => {
    if (!prompt) {
      alert("Please enter a prompt!");
      return;
    }

    setLoading(true);
    try {
      const response = await axios.post("http://127.0.0.1:5000/generate", { prompt });
      setImage(response.data.image);
    } catch (error) {
      console.error("Error generating image:", error);
      alert("Error generating image. Check console for details.");
    }
    setLoading(false);
  };

  return (
    <div className="App">
      <h1>AI Fashion Assistant</h1>
      <input
        type="text"
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Enter garment description..."
      />
      <button onClick={generateImage} disabled={loading}>
        {loading ? "Generating..." : "Generate Design"}
      </button>
      {image && (
        <img
          src={`data:image/png;base64,${image}`}
          alt="Generated Fashion Design"
          style={{ width: "300px", height: "auto", marginTop: "20px" }}
        />
      )}
    </div>
  );
}

export default App;
