import google.generativeai as genai

# Insert your API key here
genai.configure(api_key="YOUR_API_KEY")

# Select the Gemini model
model = genai.GenerativeModel('gemini-pro')

# Ask a simple question
response = model.generate_content("Hello, Gemini! Say hi to my new GitHub project.")
print(response.text)
