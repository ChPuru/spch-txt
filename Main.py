import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os

r = sr.Recognizer()
translator = Translator()

while True:
    with sr.Microphone() as source:
        print("Speak now!")
        audio = r.listen(source)
        try:
            speech_text = r.recognize_google(audio)
            print(speech_text)
            if speech_text.lower() == "exit":
                break

            # Translate the speech_text from English to French
            translation = translator.translate(
                speech_text, src='en', dest='fr')
            translated_text = translation.text
            print(translated_text)

            # Convert translated text to French speech
            voice = gTTS(translated_text, lang='fr')
            voice.save("voice.mp3")

            # Play the translated text as audio and wait for it to finish
            audio_file = AudioSegment.from_mp3("voice.mp3")
            play(audio_file)

            # Remove the temporary audio file
            os.remove("voice.mp3")
        except sr.UnknownValueError:
            print("Could not understand")
        except sr.RequestError:
            print("Could not request result from Google")
