# Libraries
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo

# Recipe Lookup Agent
recipe_agent = Agent(
    name="Recipe AI Agent",
    model=Groq(id="llama-3.2-3b-preview"),  # Updated model
    tools=[
        DuckDuckGo()  # Use this for web searches related to recipes or cooking tips
    ],
    instructions=[
        "Find recipes based on the query.",
        "Provide a list of ingredients with quantities.",
        "Explain step-by-step cooking instructions clearly.",
        "Include preparation and cooking time if available.",
        "Always include sources for the recipes.",
    ],
    show_tool_calls=True,
    markdown=True,
)

# Multi-Modal Agent with Recipe Integration
multi_ai_agent = Agent(
    model=Groq(id="llama-3.2-3b-preview"),  # Updated model
    team=[recipe_agent],  # Add the recipe agent to the team
    instructions=["Provide detailed responses and include sources."],
    show_tool_calls=True,
    markdown=True,
)

# Example Query to the Recipe Agent
multi_ai_agent.print_response(
    "Find a recipe for chocolate chip cookies and explain how to make them step-by-step.", 
    stream=True
)
