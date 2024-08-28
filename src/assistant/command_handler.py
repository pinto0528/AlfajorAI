from assistant.ai import get_ai_response

def handle_command(command):
    if command:
        response = get_ai_response(command)
        print(f"AI Response: {response}")
        return response
    return "Comando no reconocido."

