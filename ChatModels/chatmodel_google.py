from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.5, max_completion_tokens=10)
result = model.invoke("What is the capital of Nepal?")
print(result)
print(result.content)