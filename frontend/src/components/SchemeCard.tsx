import type { SchemeResponse } from "../types/scheme";


export default function SchemeCard({ scheme }: { scheme: SchemeResponse }) {
  return (
    <div>
      <h2>{scheme.name}</h2>

      <h4>Eligibility</h4>
      <ul>
        {scheme.eligibility_checks.map((e, i) => (
          <li key={i}>
            {e.condition} ✅
          </li>
        ))}
      </ul>

      <h4>Benefits</h4>
      <p>{scheme.benefits}</p>
    </div>
  );
}
