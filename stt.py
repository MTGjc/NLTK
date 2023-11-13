import speech_recognition
import pyttsx3

#recognizer => r
r = speech_recognition.Recognizer()

r.energy_threshold -= 20 

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

while True:

    try:

        with speech_recognition.Microphone() as mic:
            r.adjust_for_ambient_noise(mic, duration=0.2)
            audio = r.listen(mic, timeout= 5)

            text = r.recognize_google(audio)
            text = text.lower()
           
            print("Recognized"+ text)
            SpeakText(text)

    except speech_recognition.UnknownValueError:
        print("Speech Recognition timed out. No speech detected within the specified time.")
        r = speech_recognition.Recognizer()
        continue

    except speech_recognition.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        break  # Exit the loop if there's a request error or other exception


