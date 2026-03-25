import os
from pathlib import Path
from uuid import uuid4

from dotenv import load_dotenv
from flask import Flask, jsonify, request, send_from_directory, session
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import AssistantV2

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR.parent / "frontend"

load_dotenv(BASE_DIR / ".env")

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "cardioia_secret_key_dev")


def get_env_var(name: str, required: bool = True) -> str:
    value = os.getenv(name, "").strip()
    if required and not value:
        raise RuntimeError(f"Variável de ambiente obrigatória ausente: {name}")
    return value


def get_assistant_client() -> AssistantV2:
    api_key = get_env_var("WATSON_API_KEY")
    service_url = get_env_var("WATSON_SERVICE_URL")

    authenticator = IAMAuthenticator(api_key)
    assistant = AssistantV2(
        version="2024-08-25",
        authenticator=authenticator
    )
    assistant.set_service_url(service_url)
    return assistant


def create_watson_session() -> str:
    assistant_id = get_env_var("WATSON_ASSISTANT_ID")
    environment_id = get_env_var("WATSON_ENVIRONMENT_ID")
    assistant = get_assistant_client()

    created_session = assistant.create_session(
        assistant_id=assistant_id,
        environment_id=environment_id
    ).get_result()

    return created_session["session_id"]


def ensure_watson_session_id() -> str:
    watson_session_id = session.get("watson_session_id")
    if watson_session_id:
        return watson_session_id

    watson_session_id = create_watson_session()
    session["watson_session_id"] = watson_session_id
    return watson_session_id


def reset_watson_session() -> str:
    session.pop("watson_session_id", None)
    new_session_id = create_watson_session()
    session["watson_session_id"] = new_session_id
    return new_session_id


def ensure_user_id() -> str:
    user_id = session.get("cardioia_user_id")
    if not user_id:
        user_id = f"user_{uuid4()}"
        session["cardioia_user_id"] = user_id
    return user_id


def extract_reply_and_options(response_data: dict) -> tuple[str, list[str]]:
    output = response_data.get("output", {})
    generic = output.get("generic", [])

    text_parts: list[str] = []
    options_list: list[str] = []

    for item in generic:
        response_type = item.get("response_type")

        if response_type == "text":
            text = item.get("text", "").strip()
            if text:
                text_parts.append(text)

        elif response_type == "option":
            title = item.get("title", "").strip()
            if title:
                text_parts.append(title)

            for option in item.get("options", []):
                label = option.get("label", "").strip()
                if label:
                    options_list.append(label)

    reply_text = "\n\n".join(text_parts).strip()
    if not reply_text:
        reply_text = "O assistente respondeu, mas não retornou texto legível nesta etapa."

    return reply_text, options_list


@app.route("/", methods=["GET"])
def home():
    index_file = FRONTEND_DIR / "index.html"

    if index_file.exists():
        return send_from_directory(FRONTEND_DIR, "index.html")

    return jsonify({
        "status": "ok",
        "message": "Backend do CardioIA rodando com sucesso."
    })


@app.route("/health", methods=["GET"])
def health():
    try:
        api_key_ok = bool(get_env_var("WATSON_API_KEY"))
        service_url_ok = bool(get_env_var("WATSON_SERVICE_URL"))
        assistant_id_ok = bool(get_env_var("WATSON_ASSISTANT_ID"))
        environment_id_ok = bool(get_env_var("WATSON_ENVIRONMENT_ID"))

        return jsonify({
            "status": "ok",
            "service": "CardioIA Backend",
            "watson_configured": (
                api_key_ok and service_url_ok and assistant_id_ok and environment_id_ok
            ),
            "details": {
                "WATSON_API_KEY": api_key_ok,
                "WATSON_SERVICE_URL": service_url_ok,
                "WATSON_ASSISTANT_ID": assistant_id_ok,
                "WATSON_ENVIRONMENT_ID": environment_id_ok,
            }
        })
    except Exception as exc:
        return jsonify({
            "status": "error",
            "message": str(exc)
        }), 500


@app.route("/api/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json(silent=True) or {}
        user_message = (data.get("message") or "").strip()

        if not user_message:
            return jsonify({"error": "Mensagem vazia."}), 400

        assistant_id = get_env_var("WATSON_ASSISTANT_ID")
        environment_id = get_env_var("WATSON_ENVIRONMENT_ID")
        assistant = get_assistant_client()
        user_id = ensure_user_id()

        watson_session_id = ensure_watson_session_id()

        try:
            response = assistant.message(
                assistant_id=assistant_id,
                environment_id=environment_id,
                session_id=watson_session_id,
                user_id=user_id,
                input={
                    "message_type": "text",
                    "text": user_message
                }
            ).get_result()

        except Exception as inner_exc:
            if "Invalid Session" in str(inner_exc):
                watson_session_id = reset_watson_session()

                response = assistant.message(
                    assistant_id=assistant_id,
                    environment_id=environment_id,
                    session_id=watson_session_id,
                    user_id=user_id,
                    input={
                        "message_type": "text",
                        "text": user_message
                    }
                ).get_result()
            else:
                raise inner_exc

        print("\n=== RESPOSTA BRUTA DO WATSON ===")
        print(response)
        print("================================\n")

        reply_text, options = extract_reply_and_options(response)

        return jsonify({
            "reply": reply_text,
            "options": options
        })

    except Exception as exc:
        print("=== ERRO AO COMUNICAR COM O WATSON ===")
        print(str(exc))

        return jsonify({
            "error": "Erro ao comunicar com o Watson Assistant",
            "details": str(exc)
        }), 502


@app.route("/api/session/reset", methods=["POST"])
def reset_session():
    session.clear()
    return jsonify({
        "status": "ok",
        "message": "Sessão resetada com sucesso."
    })


@app.route("/<path:filename>", methods=["GET"])
def serve_frontend_files(filename: str):
    file_path = FRONTEND_DIR / filename

    if file_path.exists():
        return send_from_directory(FRONTEND_DIR, filename)

    return jsonify({
        "status": "error",
        "message": f"Arquivo '{filename}' não encontrado."
    }), 404


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)




    