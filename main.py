import pyautogui
import pyperclip
import time
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the model and tokenizer
model_name = "microsoft/DialoGPT-medium"  # You can also use 'small' or 'large'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Set pad token if not already defined
tokenizer.pad_token = tokenizer.eos_token
model.config.pad_token_id = tokenizer.pad_token_id

# Function to truncate input text to fit model limits
def truncate_text(text, max_length=512):
    tokens = tokenizer.encode(text, return_tensors="pt")
    if tokens.size(1) > max_length:
        text = tokenizer.decode(tokens[0, -max_length:], skip_special_tokens=True)
    return text

# Function to clean text (removes timestamps, emojis, etc.)
def clean_text(text):
    import re
    text = re.sub(r"(\[.*?\])", "", text)  # Remove timestamps
    text = re.sub(r"[^a-zA-Z0-9\s.,!?]", "", text)  # Remove emojis and special characters
    return text.strip()

# Generate a response for a given input
def generate_response(user_input):
    try:
        # Clean and truncate the input
        user_input = truncate_text(clean_text(user_input))
        
        # Tokenize the input
        inputs = tokenizer(user_input + tokenizer.eos_token, return_tensors="pt", padding=True)
        print("Tokenized Input IDs:", inputs["input_ids"])
        
        # Generate a response
        response_ids = model.generate(
            inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_length=300,
            pad_token_id=tokenizer.pad_token_id
        )
        print("Generated Response IDs:", response_ids)
        
        # Decode the response
        response = tokenizer.decode(response_ids[:, inputs["input_ids"].shape[-1]:][0], skip_special_tokens=True)
        print("Decoded Response:", response)
        return response
    except Exception as e:
        return f"Error generating response: {str(e)}"

# Function to check if the last message is from a specific sender
def is_last_message_from_sender(chat_log, sender_name="Rohan Das"):
    try:
        # Split the chat log into individual messages
        messages = chat_log.strip().split("\n")
        last_message = messages[-1] if messages else ""
        return sender_name in last_message
    except Exception as e:
        print(f"Error in is_last_message_from_sender: {str(e)}")
        return False

# Add a delay to switch to the desired application (optional)
time.sleep(3)  # Adjust as needed

try:
    # Step 1: Click on the icon at coordinates (135, 412)
    pyautogui.click(135, 412)
    time.sleep(1)  # Small delay to ensure the application responds

    # Step 2: Drag from (546, 184) to (851, 682) to select the text
    pyautogui.moveTo(546, 184)
    pyautogui.dragTo(851, 682, duration=1, button='left')  # Adjust duration if needed
    time.sleep(1.5)  # Small delay to ensure text is selected

    # Step 3: Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)  # Small delay to ensure the text is copied
    pyautogui.click(851, 682)
    
    # Step 4: Retrieve the text from the clipboard
    copied_text = pyperclip.paste()
    if not copied_text.strip():
        raise ValueError("Clipboard is empty. Ensure the text was copied successfully.")

    # Check if the last message is from the sender
    if is_last_message_from_sender(copied_text, sender_name="Rohan Das"):
        # Step 5: Generate and print the response
        response = generate_response(copied_text)

        print("Copied text:", copied_text)
        print("Response from response generator:", response)

        # Step 6: Copy the response to clipboard
        pyperclip.copy(response)

        # Step 7: Click at coordinates (1808, 1328) to focus the input box
        pyautogui.click(1808, 1328)
        time.sleep(0.5)  # Small delay

        # Step 8: Paste the response and press Enter
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
    else:
        print("The last message is not from the specified sender.")

except Exception as e:
    print(f"An error occurred: {str(e)}")
