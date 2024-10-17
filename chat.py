import sys

def chatbot_response(user_message):
    if "hello" in user_message.lower():
        return "Hello! How can I assist you today?"
    elif "bye" in user_message.lower():
        return "Goodbye! Have a great day!"
    else:
        return "This is Test!"

if __name__ == '__main__':
    user_message = sys.argv[1]
    print(chatbot_response(user_message))
