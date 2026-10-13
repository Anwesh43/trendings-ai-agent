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