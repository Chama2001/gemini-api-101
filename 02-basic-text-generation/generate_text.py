import google.generativeai as genai

# 1. Setup your API key
# Replace "YOUR_API_KEY" with your actual Gemini API key
genai.configure(api_key="YOUR_API_KEY")

# 2. Initialize the model
# We are using 'gemini-pro' which is optimized for text generation
model = genai.GenerativeModel('gemini-pro')

# 3. Create a prompt (the question you want to ask)
prompt = "Explain what Artificial Intelligence is in exactly 3 simple sentences."

print("Asking Gemini: ", prompt)
print("-" * 50)

# 4. Generate the response
response = model.generate_content(prompt)

# 5. Print the result
print(response.text)
