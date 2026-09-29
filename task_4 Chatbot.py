def get_reply(msg):
    msg = msg.lower().strip()

    if msg == "hello" or msg == "hi":
        return "Hi!"
    elif msg == "how are you":
        return "I'm fine, thanks!"
    elif msg == "what is your name":
        return "I'm a simple chatbot."
    elif msg == "help":
        return "Try saying: hello, how are you, what is your name, or bye."
    elif msg == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."


print("Chatbot: Hi! Type 'bye' to exit.")

while True:
    user = input("You: ")
    reply = get_reply(user)
    print("Chatbot:", reply)

    # stop the loop when the user says bye
    if user.lower().strip() == "bye":
        break