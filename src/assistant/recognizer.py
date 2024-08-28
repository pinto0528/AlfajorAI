import speech_recognition as sr
import time

def listen():
    recognizer = sr.Recognizer()
    mic = sr.Microphone(device_index=2)  # Usar el índice del micrófono identificado
    with mic as source:
        print("Listening...")
        try:
            start_time = time.time()
            audio = recognizer.listen(source, timeout=5)
            end_time = time.time()
            print(f"Audio capturado en {end_time - start_time:.2f} segundos")
            try:
                # Transcribe el audio a texto en español
                command = recognizer.recognize_google(audio, language='es-ES')
                print(f"Command received: {command}")
                return command
            except sr.UnknownValueError:
                print("No se pudo entender el audio.")
                return None
            except sr.RequestError as e:
                print(f"No se pudo conectar con el servicio de reconocimiento de voz: {e}")
                return None
        except sr.WaitTimeoutError:
            print("No se detectó ninguna palabra en el tiempo límite.")
            return None