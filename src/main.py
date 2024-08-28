from assistant.recognizer import listen
import keyboard
from assistant.tts import speak
from assistant.command_handler import handle_command

def main():
    print("Presiona la tecla 'v' para comenzar a hablar.")
    while True:
        if keyboard.is_pressed('v'):  # Verifica si la tecla 'v' está presionada
            print("Calibrando micrófono...")
            command = listen()
            handle_command(command)
        else:
            # Si la tecla 'v' no está presionada, puedes agregar un pequeño retraso
            # para evitar usar demasiado CPU en el loop
            keyboard.wait('v')  # Espera hasta que la tecla 'v' sea presionada

if __name__ == "__main__":
    main()