print("=" * 40)
print("🤖 Welcome to DecodeBot")
print("Type 'bye' to exit")
print("=" * 40)

name = input("Enter your name: ")
print(f"Hello {name}! Nice to meet you.\n")

while True:
    user = input("You: ").lower()

    if user in ["hello", "hi", "hey"]:
        print("Bot: Hello! How can I help you?")

    elif user == "how are you":
        print("Bot: I am doing great!")

    elif user == "what is your name":
        print("Bot: My name is DecodeBot.")

    elif user == "who created you":
        print("Bot: I was created by an AI Intern.")

    elif user == "tell me a joke":
        print("Bot: Why do programmers hate bugs? Because they take forever to debug!")

    elif user == "thank you":
        print("Bot: You're welcome!")

    elif user in ["bye", "exit", "quit"]:
        print(f"Bot: Goodbye {name}! Have a great day.")
        break

    else:
        print("Bot: Sorry, I don't understand that command.")