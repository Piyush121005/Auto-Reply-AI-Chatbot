Automated Chat Responder with DialoGPT and PyAutoGUI
This project automates the process of responding to chat messages using Microsoft's DialoGPT model for natural language understanding. It integrates with a GUI-based application to fetch chat messages, process them, and send AI-generated responses based on context.

Features
Automatically reads the latest chat messages from the screen.
Checks if the last message is from a specific sender.
Cleans and preprocesses chat messages for better response generation.
Uses DialoGPT, a transformer-based conversational AI model, to generate responses.
Automates GUI interactions (copying, pasting, and sending responses) using PyAutoGUI.
Requirements
Python 3.8 or above
The following Python libraries:
transformers
torch
pyautogui
pyperclip
re
Setup Instructions
1. Clone the Repository

git clone https://github.com/your-username/automated-chat-responder.git
cd automated-chat-responder

Below is a complete and detailed README file for your project, ready for GitHub. Simply copy and paste the content into a README.md file. It includes instructions, setup, and usage details to ensure anyone can implement the project on their machine.

Automated Chat Responder with DialoGPT and PyAutoGUI
This project automates the process of responding to chat messages using Microsoft's DialoGPT model for natural language understanding. It integrates with a GUI-based application to fetch chat messages, process them, and send AI-generated responses based on context.

Features
Automatically reads the latest chat messages from the screen.
Checks if the last message is from a specific sender.
Cleans and preprocesses chat messages for better response generation.
Uses DialoGPT, a transformer-based conversational AI model, to generate responses.
Automates GUI interactions (copying, pasting, and sending responses) using PyAutoGUI.
Requirements
Python 3.8 or above
The following Python libraries:
transformers
torch
pyautogui
pyperclip
re
Setup Instructions

1. Clone the Repository
git clone https://github.com/your-username/automated-chat-responder.git
cd automated-chat-responder

3. Install Dependencies
Ensure you have pip installed. Then, run the following command to install the required libraries:
pip install transformers torch pyautogui pyperclip

3. Download the DialoGPT Model
The project uses the Microsoft DialoGPT-medium model:
python -c "from transformers import AutoModelForCausalLM, AutoTokenizer; AutoTokenizer.from_pretrained('microsoft/DialoGPT-medium'); AutoModelForCausalLM.from_pretrained('microsoft/DialoGPT-medium')"

4. Adjust Coordinates
Open the script and locate the pyautogui.click() and pyautogui.moveTo() calls.
Modify the coordinates (x, y) to match your screen layout.
You can use pyautogui.position() in an interactive Python session to find the exact screen coordinates.
5. Run the Script
python automated_chat_responder.py

