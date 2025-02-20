import speech_recognition as sr
import pyttsx3
import webbrowser
import pywhatkit
import wikipedia
import pyjokes
import datetime
from PyQt6 import QtWidgets, QtCore
from googlesearch import search
import threading
import logging

# Initializing speech recognition
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Change to voices[1].id for female voice and [0] for male voice

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            logging.info('Listening...')
            listener.adjust_for_ambient_noise(source, duration=1)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'assistant' in command:
                command = command.replace('assistant', '')
    except sr.UnknownValueError:
        logging.error("Sorry, I did not understand that.")
        talk("Sorry, I did not understand that.")
    except sr.RequestError as e:
        logging.error(f"Could not request results; {e}")
        talk(f"Could not request results; {e}")
    except Exception as e:
        logging.error(f"Error: {e}")
    return command

def google_search(query):
    try:
        # Perform Google search and get the top result
        top_result = next(search(query, num_results=1))
        return top_result
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return f"An error occurred: {e}"

def open_instagram_profile(username):
    try:
        url = f"https://www.instagram.com/{username}/"
        webbrowser.open(url)
        return f"Opened Instagram profile for {username}"
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return f"An error occurred: {e}"

def run_assistant(command):
    if 'hello' in command:
        talk("Hi I'm Omega, your voice assistant")
        logging.info("Hi I'm Omega, your voice assistant")
    elif 'play' in command:
        song = command.replace('play', '').strip()
        talk('Playing ' + song)
        try:
            pywhatkit.playonyt(song)
            logging.info(f"Attempting to play {song} on YouTube using pywhatkit.")
        except Exception as e:
            logging.error(f"pywhatkit failed: {e}. Falling back to webbrowser.")
            search_url = f"https://www.youtube.com/results?search_query={song.replace(' ', '+')}"
            try:
                webbrowser.open(search_url)
                logging.info(f"Attempting to open {search_url} in your browser.")
            except Exception as e:
                logging.error(f"Fallback also failed: {e}")
                talk(f"An error occurred while trying to play {song}.")
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        logging.info('Current time is: - ' + time)
    elif 'who is' in command or 'what is' in command:
        person = command.replace('who is', '').strip()
        gist = command.replace('what is','').strip()
        info = wikipedia.summary(person, sentences=2)
        venture = wikipedia.summary(gist, sentences=2)
        logging.info(info)
        talk(info)
    elif 'date' in command:
        date = datetime.datetime.now().strftime('%d %m %Y')
        talk('Date is ' + date)
        logging.info('Date is :- ' + date)
    elif 'who made you' in command:
        talk('Vedant Pandey')
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)
        logging.info(joke)
    elif 'ipc' in command or 'law' in command:
        code = command.replace('ipc', '').replace('law', '').strip()
        info = google_search(f"Indian Penal Code {code} site:indiacode.nic.in")
        logging.info(info)
        talk(info)
    elif 'search' in command or 'google' in command:
        query = command.replace('search', '').replace('google', '').strip()
        talk(f"Searching for {query}")
        top_result = google_search(query)
        if "An error occurred" in top_result:
            logging.error(top_result)
            talk(top_result)
        else:
            logging.info(f"Opening top search result: {top_result}")
            webbrowser.open(top_result)
            talk(f"Here is what I found for {query}")
    elif 'open instagram' in command:
        username = command.replace('open instagram', '').strip()
        result = open_instagram_profile(username)
        logging.info(result)
        talk(result)
    else:
        talk('Please say the command again.')

def handle_voice_command():
    threading.Thread(target=take_command).start()

class ChatBox(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle('Omega Assistant')
        self.setGeometry(100, 100, 480, 320)
        
        self.text_area = QtWidgets.QTextEdit(self)
        self.text_area.setReadOnly(True)
        self.text_area.setGeometry(10, 10, 460, 240)
        
        self.input_line = QtWidgets.QLineEdit(self)
        self.input_line.setGeometry(10, 260, 360, 40)
        self.input_line.setPlaceholderText('Type your commands or queries here...')
        
        self.send_button = QtWidgets.QPushButton('Execute', self)
        self.send_button.setGeometry(380, 260, 90, 40)
        self.send_button.clicked.connect(self.handle_text_command)
        
        self.voice_button = QtWidgets.QPushButton('Voice Input', self)
        self.voice_button.setGeometry(380, 210, 90, 40)
        self.voice_button.clicked.connect(handle_voice_command)
        
        self.show()
        
    def handle_text_command(self):
        command = self.input_line.text()
        self.text_area.append(f'You: {command}')
        run_assistant(command)
        self.input_line.clear()

def main():
    app = QtWidgets.QApplication([])
    chat_box = ChatBox()
    app.exec()

if __name__ == "__main__":
    main()