from services.trending_service import TrendingService 

ts = TrendingService()

def getTrendingRepoStats():
    print("Calling getTrendingRepoStats tool")
    return ts.getGithubStats()

def getTrendingRepos():
    print("Calling getTrendingRepos tool")
    return ts.getTrendingRepos()

def getGithubTopics():
    print("Calling getGithubTopics tool")
    return ts.getGithubTopics()

def getOpenSourceAlternatives():
    print("Calling getOpenSourceAlternatives tool")
    return ts.getOpenSourceAlternatives()

def getRepoGrowthDetails(ownerId : str, repoId : str):
    print(f"Calling getRepoGrowthDetails tool for {ownerId} {repoId}")
    return ts.getRepoGrowthDetails(ownerId=ownerId, repoId=repoId)

def writeHTML(htmlStr : str, fileName : str):
    print(f"Calling writeHTML tool for {fileName}")
    with open(fileName, "w") as f:
        f.write(htmlStr)
    return {
        "status": "success",
        "message": f"writeHTML on {fileName}"
    }

def getAvailableTools():
    return [
        getTrendingRepoStats,
        getTrendingRepos,
        getGithubTopics,
        getOpenSourceAlternatives,
        getRepoGrowthDetails,
        writeHTML
    ]