import subprocess
from database.schemas.info import InfoResponse
from database.schemas.scheme import SchemeResponse


def call_mistral(prompt: str) -> str:
    """
    Calls local Mistral via Ollama.
    """
    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt,
        text=True,
        capture_output=True,
        timeout=60,  # safer for local CPU
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr)

    return result.stdout.strip()


def explain_scheme_with_llm(scheme: SchemeResponse) -> str:
    """
    LLM is ONLY allowed to explain the given facts.
    """

    eligibility_lines = "\n".join(
        f"- {e.condition}" for e in scheme.eligibility_checks
    )

    prompt = f"""
You are VoiceAid AI.

RULES:
- Use ONLY the information provided below.
- Do NOT add new facts.
- Do NOT invent schemes.
- Explain in simple language for rural users.

SCHEME NAME:
{scheme.scheme_name}

BENEFITS:
{", ".join(scheme.benefits)}

ELIGIBILITY CONDITIONS:
{eligibility_lines}

USER ELIGIBLE:
{"Yes" if scheme.eligible else "No"}

Explain clearly:
"""

    try:
        return call_mistral(prompt)
    except Exception:
        return (
            "This eligibility result is based on official scheme rules. "
            "A detailed explanation is currently unavailable."
        )


def llm_fallback(query: str) -> InfoResponse:
    """
    Used ONLY when routing finds nothing.
    """

    prompt = f"""
You are VoiceAid AI.

RULES:
- You may give general guidance.
- Do NOT invent government scheme names.
- If unsure, say so.
- Keep response short and clear.

USER QUESTION:
{query}

Answer:
"""

    try:
        answer = call_mistral(prompt)
    except Exception:
        answer = (
            "I am unable to provide a detailed answer right now. "
            "Please try again later or ask about a specific government scheme."
        )

    return InfoResponse(
        success=True,
        source="llm",
        title="General Guidance",
        message=answer,
        summary="This response is AI-generated and not from verified government data.",
    )
