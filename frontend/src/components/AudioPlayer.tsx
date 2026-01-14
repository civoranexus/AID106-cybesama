import { useEffect } from "react";

type Props = {
  audioBase64: string | null;
  onEnd?: () => void;
};

export default function AudioPlayer({ audioBase64, onEnd }: Props) {
  useEffect(() => {
    if (!audioBase64) return;

    const audio = new Audio(`data:audio/wav;base64,${audioBase64}`);

    audio.onended = () => {
      onEnd?.();
    };

    audio.play();
  }, [audioBase64]);

  return null;
}
