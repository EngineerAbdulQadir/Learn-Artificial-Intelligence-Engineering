!pip install python-dotenv -q
!pip install langchain-community -U -q
!pip install google-generativeai -U -q
!pip install langchain -U -q
!pip install langchain_google_genai -U -q

"""# Import API keys"""

from google.colab import userdata
userdata.get('GOOGLE_API_KEY')
api_key = userdata.get('GOOGLE_API_KEY')

"""# Define the Calculator Tool"""

class Calculator:
    def calculate(self, expression: str) -> str:
        try:
            # Use Python's eval to compute the result safely
            result = eval(expression, {"__builtins__": None}, {})
            return str(result)
        except Exception as e:
            return f"Error: {e}"

"""# Create the Tool Wrapper"""

from langchain.tools import tool

# Define the tool using a decorator
@tool
def calculator(expression: str) -> str:
    """
    Perform arithmetic calculations.
    Input: A mathematical expression as a string (e.g., "2 + 2").
    Output: Result of the calculation as a string.
    """
    calc = Calculator()
    return calc.calculate(expression)

"""# Set Up the Google Gemini Flash Model"""

import os
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain.chains.conversation.memory import ConversationBufferMemory

# Initialize the Google Gemini Flash model
gemini_model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-exp",  # Specify the model name, e.g., 'gemini-1.5-flash'
    api_key=userdata.get('GOOGLE_API_KEY'),
    temperature=0.7
)
print("Google Gemini Flash model initialized.")

from langchain.agents import initialize_agent, AgentType
from langchain.tools import tool


# Create a list of tools
tools = [calculator]

# Initialize the agent
agent = initialize_agent(
    tools=tools,
    llm=gemini_model,
    agent_type="openai-function-calling"
)

# Example usage
response = agent.invoke("What is 12 * 15?")
print(response)

"""# Build the Conversational Chain"""

from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# Set up memory to maintain conversation context
memory = ConversationBufferMemory()

# Build the conversational chain
chain = ConversationChain(
    llm=gemini_model,
    memory=memory,
    verbose=True
)

# Example usage
response = chain.invoke("What is 12 * 15?")
print(response)

"""# Test the Calculator Tool"""

query = "What is 15 divided by 3?"
response = chain.invoke(query)
print(response)

queries = [
    "What is 25 multiplied by 4?",
    "Now divide the result by 5.",
    "Add 10 to that."
]

for q in queries:
    print("Query:", q)
    print("Response:", chain.invoke(q))
    print("-" * 40)

"""# The End..."""