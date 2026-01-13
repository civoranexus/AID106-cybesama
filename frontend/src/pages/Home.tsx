import { useState } from "react";
import TextInput from "../components/TextInput";
import VoiceInput from "../components/VoiceInput";
import SchemeCard from "../components/SchemeCard";
import AudioPlayer from "../components/AudioPlayer";
import { sendVoiceText } from "../api/voiceaid";

export default function Home() {
  const [response, setResponse] = useState<any>(null);
  const [audio, setAudio] = useState<string | null>(null);

  const handleQuery = async (text: string) => {
    const data = await sendVoiceText(text);
    setResponse(data.text_response);
    setAudio(data.audio_response);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>VoiceAid AI</h1>

      <TextInput onSubmit={handleQuery} />
      <VoiceInput onResult={handleQuery} />

      {response?.data && <SchemeCard scheme={response.data} />}

      <AudioPlayer audioBase64={audio} />
    </div>
  );
}

