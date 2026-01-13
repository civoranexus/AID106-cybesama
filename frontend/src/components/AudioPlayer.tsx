import { useEffect } from "react";

type Props = {
  audioBase64: string | null;
};

export default function AudioPlayer({ audioBase64 }: Props) {
  useEffect(() => {
    if (!audioBase64) return;

    try {
      const audio = new Audio(`data:audio/wav;base64,${audioBase64}`);
      audio.play();
    } catch (err) {
      console.error("Audio playback failed", err);
    }
  }, [audioBase64]);

  return null;
}
