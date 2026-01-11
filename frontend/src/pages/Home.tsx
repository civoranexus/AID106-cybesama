import { useState } from "react";
import { fetchScheme } from "../api/voiceaid";
import TextInput from "../components/TextInput";
import VoiceInput from "../components/VoiceInput";
import SchemeCard from "../components/SchemeCard";

export default function Home() {
  const [scheme, setScheme] = useState<any>(null);

  const handleSearch = async (query: string) => {
    const data = await fetchScheme(query);
    setScheme(data);
  };

  return (
    <div>
      <h1>VoiceAid AI</h1>

      <TextInput onSubmit={handleSearch} />
      <VoiceInput onResult={handleSearch} />

      {scheme && <SchemeCard scheme={scheme} />}
    </div>
  );
}
