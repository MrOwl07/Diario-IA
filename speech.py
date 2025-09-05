
import speech_recognition as speech_recog
#### V1 - función
def speech_es():
    mic = speech_recog.Microphone()
    recog = speech_recog.Recognizer()

    with mic as audio_file:
        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)
        return recog.recognize_google(audio, language="es-MX")

def prueba():
    #### V2 - script
    mic = speech_recog.Microphone()
    recog = speech_recog.Recognizer()

    with mic as audio_file:
        print("Por favor, hable")

        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)

        print("Conversión de voz a texto...")
        print(f"Usted dijo: {recog.recognize_google(audio, language='es-MX')}")
        
prueba()
