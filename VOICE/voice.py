import speech_recognition as sr
import pyttsx3 as tts
from neuralintents import GenericAssistant
recognizer = sr.Recognizer()
speaker = tts.init()
speaker.setProperty('rate', 140)


def start():
    print("Hey!How are you?")
    speak("Hey!How are you?")
    print("How can i help u today?")
    speak("How can i help u today?")
def greet():
    print("Hello! How can I assist you today?")
    speak("Hello! How can I assist you today?")
def end():
    print("Goodbyeee!")
    speak("Goodbyeee!")
    exit()

def read():
    print("Please tell file name")
    speak("Please tell file name")
    fname=listen()+".txt"
    f=open(fname,"r")
    print(f.readline())
    speak(f.readline())
def create_file():
    print("Sure! What would u like to write in file Sir?")
    speak("Sure! What would u like to write in file Sir?")
    note_content = listen()

    if note_content != "unknown":
        print("Please tell file name:")
        speak("Please tell file name:")
        filename = listen()
        print("filename: "+filename)
        with open(filename + '.txt', 'w') as f:
            f.write(note_content)
        print(f"Successfully created with the filename {filename}")
        speak(f"Successfully created with the filename {filename}")

def speak(text):
    speaker.say(text)
    speaker.runAndWait()
def listen():
    with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=0.5)
        audio = recognizer.listen(mic)
        try:
            user_input = recognizer.recognize_google(audio).lower()
            return user_input
        except sr.UnknownValueError:
            speak("Can't understand")
            return listen()
        except sr.RequestError:
            return "error"
todo_list = []

def add_task_to_todo():
    print("What task would you like to add to the to-do list?")
    speak("What task would you like to add to the to-do list?")
    task = listen()

    if task != "unknown":
        todo_list.append(task)
        print(f"I added {task} to the to-do list!")
        speak(f"I added {task} to the to-do list!")

def show_todo():
    if todo_list:
        print("Here are the items on your to-do list:")
        speak("Here are the items on your to-do list:")
        for idx, item in enumerate(todo_list, 1):
            print(f"{idx}. {item}")
            speak(f"{idx}. {item}")
    else:
        print("Your to-do list is empty!")
        speak("Your to-do list is empty!")

keymatches = {
    "hi": start,
    "create file": create_file,
    "remeber this": create_file,
    "make note": create_file,
    "add to do": add_task_to_todo,
    "show to do": show_todo,
    "exit": end,
    "open":read
}
def main():
    print("Powering on mark")
    speak("Powering on mark")

    while True:
        inpt=listen()
        user_input = listen()
        print(user_input)
        if user_input == "error":
            print("Sorry, there was an error with the microphone.")
            speak("Sorry, there was an error with the microphone.")
        else:
            if user_input in keymatches:
                keymatches[user_input]()
            else:
                print("Sorry, I didn't understand that. Please try again.")
                speak("Sorry, I didn't understand that. Please try again.")


if __name__ == "__main__":
    main()
