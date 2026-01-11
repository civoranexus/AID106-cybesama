import { useState } from "react";

declare global {
  interface Window {
    webkitSpeechRecognition: any;
  }
}

export default function VoiceInput({ onResult }: { onResult: (text: string) => void }) {
  const [listening, setListening] = useState(false);

  const startListening = () => {
    if (!("webkitSpeechRecognition" in window)) {
      alert("Speech recognition not supported in this browser");
      return;
    }

    const recognition = new window.webkitSpeechRecognition();
    recognition.lang = "en-IN";
    recognition.continuous = false;
    recognition.interimResults = false;

    recognition.onstart = () => setListening(true);

    recognition.onresult = (event: any) => {
      const transcript = event.results[0][0].transcript;
      onResult(transcript);
      setListening(false);
    };

    recognition.onerror = () => {
      setListening(false);
      alert("Voice recognition failed");
    };

    recognition.start();
  };

  return (
    <div>
      <button onClick={startListening}>
        {listening ? "Listening..." : "🎤 Speak"}
      </button>
    </div>
  );
}
