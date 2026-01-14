type Props = {
  value: string;
  onChange: (v: string) => void;
  onSubmit: (v: string) => void;
};

export default function TextInput({ value, onChange, onSubmit }: Props) {
  return (
    <div>
      <input
        placeholder="Enter scheme name"
        value={value}
        onChange={(e) => onChange(e.target.value)}
      />
      <button onClick={() => onSubmit(value)}>Search</button>
    </div>
  );
}

