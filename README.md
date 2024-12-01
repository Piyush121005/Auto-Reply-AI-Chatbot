# Automated Chat Responder with DialoGPT and PyAutoGUI

This project automates the process of responding to chat messages using Microsoft's DialoGPT model for natural language understanding. It integrates with a GUI-based application to fetch chat messages, process them, and send AI-generated responses based on context.

## Features

- Automatically reads the latest chat messages from the screen.
- Checks if the last message is from a specific sender.
- Cleans and preprocesses chat messages for better response generation.
- Uses DialoGPT, a transformer-based conversational AI model, to generate responses.
- Automates GUI interactions (copying, pasting, and sending responses) using PyAutoGUI.

## Requirements

- Python 3.8 or above
- The following Python libraries:
  - `transformers`
  - `torch`
  - `pyautogui`
  - `pyperclip`
  - `re`

## Setup Instructions

### 1. Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/your-username/automated-chat-responder.git
cd automated-chat-responder

2. Install Dependencies
Ensure you have pip installed. Then, run the following command to install the required libraries:
pip install transformers torch pyautogui pyperclip

3. Download the DialoGPT Model
The project uses the Microsoft DialoGPT-medium model. Run the following command to download the model:
python -c "from transformers import AutoModelForCausalLM, AutoTokenizer; AutoTokenizer.from_pretrained('microsoft/DialoGPT-medium'); AutoModelForCausalLM.from_pretrained('microsoft/DialoGPT-medium')"


Here's the full README content for your project, which you can copy and paste into your README.md file. This provides clear setup instructions and details on how to get your automated chat responder working:

markdown
Copy code
# Automated Chat Responder with DialoGPT and PyAutoGUI

This project automates the process of responding to chat messages using Microsoft's DialoGPT model for natural language understanding. It integrates with a GUI-based application to fetch chat messages, process them, and send AI-generated responses based on context.

## Features

- Automatically reads the latest chat messages from the screen.
- Checks if the last message is from a specific sender.
- Cleans and preprocesses chat messages for better response generation.
- Uses DialoGPT, a transformer-based conversational AI model, to generate responses.
- Automates GUI interactions (copying, pasting, and sending responses) using PyAutoGUI.

## Requirements

- Python 3.8 or above
- The following Python libraries:
  - `transformers`
  - `torch`
  - `pyautogui`
  - `pyperclip`
  - `re`

## Setup Instructions

### 1. Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/your-username/automated-chat-responder.git
cd automated-chat-responder
2. Install Dependencies
Ensure you have pip installed. Then, run the following command to install the required libraries:

bash
Copy code
pip install transformers torch pyautogui pyperclip
3. Download the DialoGPT Model
The project uses the Microsoft DialoGPT-medium model. Run the following command to download the model:

bash
Copy code
python -c "from transformers import AutoModelForCausalLM, AutoTokenizer; AutoTokenizer.from_pretrained('microsoft/DialoGPT-medium'); AutoModelForCausalLM.from_pretrained('microsoft/DialoGPT-medium')"
4. Adjust Coordinates
Open the script and locate the pyautogui.click() and pyautogui.moveTo() calls. Modify the coordinates (x, y) to match your screen layout. You can use pyautogui.position() in an interactive Python session to find the exact screen coordinates.

5. Run the Script
After setting up the environment and adjusting coordinates, run the script using:
python automated_chat_responder.py
