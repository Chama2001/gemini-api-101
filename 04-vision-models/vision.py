import google.generativeai as genai
import PIL.Image

# 1. Setup your API key
genai.configure(api_key="YOUR_API_KEY")

# 2. Initialize the multimodal model (gemini-1.5-flash is best for images)
model = genai.GenerativeModel('gemini-1.5-flash')

print("Make sure you have an image named 'sample.jpg' in this folder!")

try:
    # 3. Load the image from your computer
    img = PIL.Image.open('sample.jpg')
    
    # 4. Ask a question about the image
    prompt = "Describe what is in this picture in detail."
    
    print(f"Asking Gemini: {prompt}")
    print("-" * 50)
    
    # Send the picture and the question to Gemini
    response = model.generate_content([prompt, img])
    
    # 5. Print the response
    print(response.text)
    
except FileNotFoundError:
    print("Error: Could not find 'sample.jpg'. Please add a picture with this name to the folder and try again.")
