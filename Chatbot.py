print("Chatbot started type bye to exit")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hello how can I help you")
    elif user == "how are you":
        print("Bot: I am fine thank you")
    elif user == "who are you":
        print("Bot: I am a chatbot developed by Monty")
    elif user == "bye":
        print("Bot: Goodbye")
        break
    else:
        print("Bot: Sorry I do not understand")
