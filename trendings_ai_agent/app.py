from agents.trending_agent import analyseTrendingRepos
import sys 
import asyncio 

if __name__ == "__main__" and len(sys.argv) > 1:
    prompt = " ".join(sys.argv[1:])
    asyncio.run(analyseTrendingRepos(prompt = prompt))