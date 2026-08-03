import google.generativeai as genai

# 1. Setup your API key
genai.configure(api_key="YOUR_API_KEY")

# 2. Initialize the model
model = genai.GenerativeModel('gemini-pro')

# 3. Start a chat session (this keeps track of the conversation history)
chat = model.start_chat(history=[])

print("Welcome to the Gemini Chatbot! Type 'quit' to exit.\n")

# 4. Create a simple loop to talk to the bot continuously
while True:
    user_message = input("You: ")
    
    if user_message.lower() == 'quit':
        print("Chat ended. Goodbye!")
        break
        
    # Send the message to the model
    response = chat.send_message(user_message)
    
    # Print the response
    print(f"Gemini: {response.text}\n")
