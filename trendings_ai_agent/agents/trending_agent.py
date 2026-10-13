from pydantic_ai import Agent 
from tools.trending_tools import getAvailableTools
from prompts.trending_prompt import SYSTEM_PROMPT 
from dotenv import load_dotenv 

load_dotenv()

agent = Agent(
    tools = getAvailableTools(),
    model = "openai:gpt-5.2",
    system_prompt = SYSTEM_PROMPT 
)

async def analyseTrendingRepos(prompt : str):
    async with agent.run_stream(prompt) as result:
        async for token in result.stream_text(delta=True):
            print(token, end = '')