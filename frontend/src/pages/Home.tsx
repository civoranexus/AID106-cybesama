import { useState } from "react";
import TextInput from "../components/TextInput";
import VoiceInput from "../components/VoiceInput";
import AudioPlayer from "../components/AudioPlayer";
import { sendVoiceText } from "../api/voiceaid";

type UIState =
  | "idle"
  | "listening"
  | "processing"
  | "speaking"
  | "error";

export default function Home() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState<any>(null);
  const [audio, setAudio] = useState<string | null>(null);
  const [uiState, setUIState] = useState<UIState>("idle");
  const [error, setError] = useState<string | null>(null);

  const handleQuery = async (text: string) => {
    if (!text || !text.trim()) {
      setUIState("idle");
      return;
    }

    setQuery(text); // 🔑 mic text appears in input

    try {
      setUIState("processing");
      setError(null);

      const data = await sendVoiceText(text);

      setResponse(data.text_response);
      setAudio(data.audio_response);
      setUIState("speaking");
    } catch (err: any) {
  console.error(err);

  if (!navigator.onLine) {
    setError("No internet connection. Please check your network.");
  } else {
    setError("Service is temporarily unavailable. Please try again.");
  }

  setUIState("error");
}

  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>VoiceAid AI</h1>

      <TextInput
        value={query}
        onChange={setQuery}
        onSubmit={handleQuery}
      />

      <VoiceInput
      onResult={handleQuery}
      onListeningStart={() => setUIState("listening")}
      onListeningStop={() => setUIState("idle")}
      onError={(msg) => {
        setError(msg);
        setUIState("error");
      }}
      disabled={uiState !== "idle"}
      />


      {/* STATUS MESSAGE */}
      <div style={{ marginTop: "10px", minHeight: "24px" }}>
        {uiState === "listening" && "🎤 Listening..."}
        {uiState === "processing" && "⏳ Processing your request..."}
        {uiState === "speaking" && "🔊 Speaking response..."}
        {uiState === "error" && `❌ ${error}`}
      </div>

      <AudioPlayer
        audioBase64={audio}
        onEnd={() => setUIState("idle")}
      />
    </div>
  );
}
