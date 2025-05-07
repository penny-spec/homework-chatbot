import re
import random

class HomeworkChatBot:
    def __init__(self):
        self.responses = {
            r"\byour name\b": ["I'm HomeworkBot, your study assistant!"],
            r"\bhelp\b": [
                "Sure, what subject do you need help with?",
                "I'm here to assist you. Which topic are you studying?",
                "How can I help you with your homework today?"
            ],
            r"\bmath\b": [
                "I can help with math problems! What do you need assistance with?",
                "Math is fun! What topic are you working on?"
            ],
            r"\bart\b": [
                "I can help with art! Do you want to draw something? Should I give you some ideas on what to draw?",
                "Art is fun! What can I assist you with?"
            ],
            r"\bscience\b": [
                "Let's dive into science! What topic are you studying?",
                "Science is fascinating! Which area are you focusing on?"
            ],
            r"\bhistory\b": [
                "History is fascinating! What period are you focusing on?",
                "Let's explore history! Which era are you studying?"
            ],
            r"\benglish\b": [
                "English literature or grammar? I can assist with both!",
                "Let's work on English! What aspect are you focusing on?"
            ],
            r"\bgeography\b": [
                "Geography is all about the Earth! What aspect are you studying?",
                "Let's explore the world! Which region are you focusing on?"
            ],
            r"\bliterature\b": [
                "Literature is the study of written works. What genre interests you?",
                "Let's delve into literature! Which author or genre are you exploring?"
            ],
            r"\bcomputer science\b": [
                "Computer Science is the study of computers and computational systems. What topic are you exploring?",
                "Let's dive into Computer Science! Which area are you studying?"
            ],
            r"\b(thank you|thanks)\b": ["You're welcome! Happy to help."],
            r"\bbye\b": ["Goodbye! Good luck with your studies."]
        }

    def get_response(self, user_input):
        user_input = user_input.lower()
        for pattern, response_list in self.responses.items():
            if re.search(pattern, user_input):
                return random.choice(response_list)
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

def main():
    print("Hello! I'm HomeworkBot. How can I assist you with your homework today?")
    chatbot = HomeworkChatBot()
    while True:
        user_input = input("You: ")
        if re.search(r"\bbye\b", user_input.lower()):
            print("HomeworkBot: Goodbye! Good luck with your studies.")
            break
        response = chatbot.get_response(user_input)
        print(f"HomeworkBot: {response}")

if __name__ == "__main__":
    main()
