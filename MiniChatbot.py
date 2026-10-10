# Mini Chatbot
print("Hello! I am a mini chatbot. How can I assist you today?")
print("You can ask me basic questions or type 'bye' to exit.")

#chatbot memory creation
responses = {
    'hello': 'Hello! How can I help you?',
    'how are you': 'I am just a program, but I am functioning as expected!',
    'what is your name': 'I am a mini chatbot created to assist you.',
    'motivate me': 'Believe in yourself! You can achieve anything you set your mind to.',
    'nice': 'Thank you! I appreciate your kind words.',
    'busy': 'I am always here to assist you, no matter how busy I am.',

}
#Method function to get response from chatbot
def get_response(user_input):
    user_input = user_input.lower()
    for each_key in responses.keys():
        if each_key in user_input:
            return responses[each_key]
    return responses.get(user_input, "I'm sorry, I don't understand that. Can you ask something else?")
#Output of the chatbot
while True:
    user_input=input("Please enter your question: ")
    reply = get_response(user_input)
    print("Bot response: " + reply)
    if user_input.lower() == 'bye':
        print("Goodbye! Have a great day!")
        break