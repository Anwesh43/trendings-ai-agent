from tools.trending_tools import getRepoGrowthDetails, getOpenSourceAlternatives, getGithubTopics, getTrendingRepos, getTrendingRepoStats
from typing import Dict 
import json 

def writeFile(data : Dict, fileName : str):
    with open(fileName, "w") as f:
        f.write(json.dumps(data))
    print(f"Writing data to {fileName}")

if __name__ == "__main__":
    writeFile(getTrendingRepoStats(), "trending_repo_stats.json")
    writeFile(getOpenSourceAlternatives(), "open_source_alternatives.json")
    writeFile(getTrendingRepos(), "tending_repo_stats.json")
    writeFile(getGithubTopics(), "github_topics.json")
    writeFile(getRepoGrowthDetails("01mf02", "jaq"), "growth_repo.json")