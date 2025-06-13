from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()  

model = ChatAnthropic(model="claude-2", temperature=0.5, max_completion_tokens=10)
result = model.invoke("What is the capital of Nepal?")
print(result)