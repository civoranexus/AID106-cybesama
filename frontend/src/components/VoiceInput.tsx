import { useState } from "react";

declare global {
  interface Window {
    webkitSpeechRecognition: any;
  }
}

type Props = {
  onResult: (text: string) => void;
  onListeningStart: () => void;
  onListeningStop: () => void;
  onError: (message: string) => void;
  disabled?: boolean;
};


export default function VoiceInput({
  onResult,
  onListeningStart,
  onListeningStop,
  onError, 
  disabled,
}: Props) {
  const [listening, setListening] = useState(false);

  const startListening = () => {
    if (disabled || listening) return;

    if (!("webkitSpeechRecognition" in window)) {
      alert("Speech recognition not supported");
      return;
    }

    const recognition = new window.webkitSpeechRecognition();
    recognition.lang = "en-IN";
    recognition.continuous = false;
    recognition.interimResults = false;

    recognition.onstart = () => {
      setListening(true);
      onListeningStart();
    };

    recognition.onresult = (event: any) => {
      const transcript = event.results[0][0].transcript;
      setListening(false);
      onResult(transcript); // processing starts here
    };

    recognition.onerror = (event: any) => {
  setListening(false);
  onListeningStop();

  if (event.error === "not-allowed") {
    onError("Microphone permission denied. Please allow mic access.");
  } else if (event.error === "no-speech") {
    onError("I didn’t hear anything. Please try speaking again.");
  } else {
    onError("Speech recognition failed. Please try again.");
  }
};


    recognition.onend = () => {
      if (listening) {
  onError("I didn’t catch that. Please speak clearly.");
}

      setListening(false);
      onListeningStop(); // 🔑 EXIT listening

    };

    recognition.start();
  };

  return (
    <button onClick={startListening} disabled={disabled || listening}>
      {listening ? "🎤 Listening..." : "🎤 Speak"}
    </button>
  );
}
