Omega Voice Assistant
Omega is a voice-activated assistant built using Python. It can execute various commands such as playing music, performing web searches, and providing information. The assistant uses libraries such as speech_recognition, pyttsx3, webbrowser, pywhatkit, and wikipedia to accomplish its tasks.

Features
Voice Recognition: Listens to your voice commands and processes them.

Voice Responses: Provides spoken feedback using pyttsx3.

Web Search: Searches Google for your queries.

YouTube Playback: Plays songs or videos on YouTube using pywhatkit.

Wikipedia Integration: Fetches summaries from Wikipedia.

Joke Teller: Tells jokes using pyjokes.

Date and Time: Provides the current date and time.

Instagram Profile: Opens Instagram profiles in the browser.

Custom Commands: Additional commands can be added easily.

Installation
Clone the repository:

bash
git clone https://github.com/VedantPandey10/omega-voice-assistant.git
cd omega-voice-assistant
Install the required dependencies:

bash
pip install -r requirements.txt
Usage
Run the Assistant:

bash
python main.py
Voice Commands:

Say "hello" to greet the assistant.

Say "play [song name]" to play a song on YouTube.

Say "search [query]" or "google [query]" to perform a web search.

Say "who is [person]" or "what is [topic]" to get information from Wikipedia.

Say "joke" to hear a joke.

Say "time" to get the current time.

Say "date" to get the current date.

Say "open Instagram [username]" to open an Instagram profile.[Can only open previously logged in acccount]

Customization
You can customize the voice settings in the main.py file:

python
engine.setProperty('voice', voices[0].id)  # Change to voices[1].id for a female voice
Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgements
Special thanks to all the libraries and resources used in this project:

speech_recognition

pyttsx3

webbrowser

pywhatkit

wikipedia

pyjokes

datetime

googlesearch
