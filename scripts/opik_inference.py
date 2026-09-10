"""
opik_inference.py — Run inference on ANY LLM and trace it in your local Opik.

Why LiteLLM? It gives one uniform API for 100+ providers (OpenAI, Anthropic,
Google, Mistral, Ollama, Together, ...). You switch models with an env var —
no code changes. Every call is auto-logged to your self-hosted Opik instance.

--------------------------------------------------------------------------
Setup (once):
    pip install opik litellm
    opik configure --use_local      # points the SDK at http://localhost:5173

Pick a model + key, then run:

    # OpenAI
    export LLM_MODEL="gpt-5.6-luna"
    export OPENAI_API_KEY="sk-..."

    # Google (Gemini)
    export LLM_MODEL="gemini/gemini-3.6-flash"
    export GEMINI_API_KEY="..."

    # Local, no API key (Ollama — run `ollama run llama3` first)
    export LLM_MODEL="ollama/llama3"

    python scripts/opik_inference.py "Explain what an LLM trace is in one sentence."
--------------------------------------------------------------------------
"""

import os
import sys

import litellm
from opik import track


# 1. Send every LiteLLM call to your local Opik instance.
# Register by name (not OpikLogger()) so LiteLLM builds the logger lazily inside
# its own event loop -- instantiating it here would raise "no running event loop".
litellm.callbacks = ["opik"]

# Group these traces under a readable project name in the Opik UI.
os.environ.setdefault("OPIK_PROJECT_NAME", "quickstart")


@track  # 2. @track wraps our function so nested calls show up as one trace.
def ask_llm(prompt: str) -> str:
    model = os.environ.get("LLM_MODEL", "gpt-5.6-luna")
    print(f"→ Model: {model}")

    response = litellm.completion(
        model=model,
        messages=[
            {"role": "system", "content": "You are a concise, helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content


def main() -> None:
    # Prompt from the command line, or a sensible default.
    prompt = " ".join(sys.argv[1:]) or "Say hello and tell me you are being traced by Opik."

    print(f"→ Prompt: {prompt}\n")
    answer = ask_llm(prompt)

    print("\n─── Answer ───────────────────────────────")
    print(answer)
    print("──────────────────────────────────────────")
    print("\n✅ Traced! Open http://localhost:5173 → project 'quickstart' to view it.")


if __name__ == "__main__":
    main()
