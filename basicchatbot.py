# Enhanced Rule-Based Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input in ["hello", "hi", "hey"]:
        return "Hi there! How can I help you?"
    elif user_input in ["how are you", "how are you doing"]:
        return "I'm doing great, thank you! What about you?"
    elif user_input in ["i am fine", "i'm fine", "doing well", "good"]:
        return "Glad to hear that!"
    elif user_input in ["what is your name", "who are you"]:
        return "I'm a simple chatbot created to talk with you."
    elif user_input in ["what can you do", "help me"]:
        return "I can chat with you! Try saying 'hello' or ask how I am."
    elif user_input in ["bye", "goodbye", "see you"]:
        return "Goodbye! Have a nice day!"
    elif user_input in ["thanks", "thank you"]:
        return "You're welcome!"
    else:
        return "Sorry, I don't understand that. Try saying something else."

def run_chatbot():
    print("🤖 Welcome to the Enhanced Chatbot!")
    print("Type 'bye' anytime to end the conversation.\n")

    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Bot:", response)

        if user_input.lower() in ["bye", "goodbye", "see you"]:
            break

# Start the chatbot
run_chatbot()
