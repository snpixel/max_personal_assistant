# Voice Assistant - Max

This is a simple voice assistant named "Max," which can perform various tasks such as searching on Google, opening applications, playing music, telling jokes, and more.

## Features

- Greet users based on the time of day.
- Open websites like YouTube, Google, and GitHub.
- Search for information on Wikipedia.
- Open local applications like Spotify, Visual Studio Code, and Blender (paths need to be configured).
- Tell the current time.
- Tell jokes using `pyjokes`.
- Execute Google searches.
- Perform tasks based on voice commands.

## How It Works

The assistant uses voice commands captured through the microphone and processed by Google’s speech recognition service. Based on the recognized commands, it performs various tasks.

### Commands Supported:
- **Wikipedia Search**: Searches for any topic on Wikipedia and reads out a short summary.
- **Open Websites**: Opens YouTube, Google, and GitHub.
- **Play Music**: Opens the local music application (configurable).
- **Tell the Time**: Reads out the current time.
- **Open Applications**: Opens VS Code, Blender, and Godot (paths need to be configured).
- **Search on Google**: Opens a web browser to search for the specified query.
- **Jokes**: Tells a joke using the `pyjokes` library.
- **Go Offline**: Stops listening and exits the program.

## Installation

1. Clone the repository.
   ```bash
   git clone <repository_url>
   cd <repository_name>
    ```
2. Install the required libraries or run the requirements file:
    ```bash
    pip install pyttsx3 speechRecognition wikipedia pyjokes
    ```
    or
    ```bash
    pip install -r requirements.txt
    ```

3. Customize the file paths in the main script (e.g., for opening Spotify, VS Code, or Blender).
4. python main.py


## Requirements

- Python 3.x
- Libraries: pyttsx3, speechRecognition, wikipedia, pyjokes

## Customization

- You can add or modify the voice commands in the main.py file.
- The application paths for Spotify, VS Code, Godot, etc., should be updated in the script based on your system.

## Future Improvments

- Add more voice commands.
- Improve the joke-telling feature to be more engaging.
- Add AI in the convo.
- Add more day to day functionality


