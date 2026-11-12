"""Assistant conversationnel local utilisant l'API Ollama."""

import json
import os
import urllib.error
import urllib.request

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434").rstrip("/")
MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:3b")
SYSTEM_PROMPT = (
    "Tu es un assistant utile, clair et pédagogique. "
    "Réponds en français sauf si l'utilisateur demande une autre langue."
)


def ask_ollama(messages):
    """Envoie l'historique à Ollama et renvoie la réponse du modèle."""
    url = f"{OLLAMA_HOST}/api/chat"
    payload = {
        "model": MODEL,
        "messages": messages,
        "stream": False,
    }
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=180) as response:
            result = json.loads(response.read().decode("utf-8"))
        return result["message"]["content"]
    except urllib.error.URLError as exc:
        raise RuntimeError(
            "Impossible de joindre Ollama. Vérifiez qu'il est installé "
            "et démarré, puis réessayez."
        ) from exc
    except (KeyError, json.JSONDecodeError) as exc:
        raise RuntimeError("La réponse reçue d'Ollama est invalide.") from exc


def main():
    print("=== Assistant IA local ===")
    print(f"Modèle : {MODEL}")
    print("Tapez /quit pour quitter.\n")

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    while True:
        try:
            user_text = input("Vous : ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nÀ bientôt !")
            break

        if not user_text:
            continue
        if user_text.lower() in {"/quit", "/exit"}:
            print("À bientôt !")
            break

        messages.append({"role": "user", "content": user_text})

        try:
            answer = ask_ollama(messages)
        except RuntimeError as exc:
            print(f"Erreur : {exc}\n")
            messages.pop()
            continue

        messages.append({"role": "assistant", "content": answer})
        print(f"Assistant : {answer}\n")


if __name__ == "__main__":
    main()
