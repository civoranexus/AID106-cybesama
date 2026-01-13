import { useState } from "react";

export default function TextInput({ onSubmit }: any) {
  const [value, setValue] = useState("");

  return (
    <div>
      <input
        placeholder="Enter scheme name"
        value={value}
        onChange={(e) => setValue(e.target.value)}
      />
      <button onClick={() => onSubmit(value)}>Search</button>
    </div>
  );
}
