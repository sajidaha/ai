# chatbot_basic.py
def get_response(user_input):
    user_input = user_input.lower()
    if "crop" in user_input:
        return "Which crop do you want information about?"
    elif "weather" in user_input:
        return "Please provide your location for weather updates."
    elif "pest" in user_input:
        return "For pest management, consider natural predators or pesticides suitable for your crop."
    else:
        return "Sorry, I didn't understand that. Can you please rephrase?"

def main():
    print("Agricultural Assistant Chatbot (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = get_response(user_input)
        print("inibot:", response)

if __name__ == "__main__":
    main()
