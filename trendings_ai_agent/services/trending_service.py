from services.base_http_client import BaseHTTPClient 
from dotenv import load_dotenv 
import os 

load_dotenv()

class TrendingService:
    def __init__(self):
        self.client = BaseHTTPClient(os.environ["TRENDING_BASE_URL"])

    def getTrendingRepos(self):
        try:
            response = self.client.getCall("repos.json")
            results = []
            for data in response:
                obj = {}
                if "slug" in data:
                    slugParts = data["slug"].split("/")
                    obj["owner"] = slugParts[0]
                    obj["repoId"] = slugParts[1]
                    results.append(obj)
            return results 
        except Exception as e:
            return self.client.handleError(e)

    def getOpenSourceAlternatives(self):
        try:
            response = self.client.getCall("alternatives.json")
            return response 
        except Exception as e:
            return self.client.handleError(e)

    def getGithubTopics(self):
        try:
            response = self.client.getCall("topics.json")
            return response
        except Exception as e:
            return self.client.handleError(e)

    def getGithubStats(self):
        try:
            response = self.client.getCall("stats.json")
            return response 
        except Exception as e:
            return self.client.handleError(e)

    def getRepoGrowthDetails(self, ownerId : str, repoId : str):
        try:
            response = self.client.getCall(f"repos/{ownerId}/{repoId}")
            return response 
        except Exception as e:
            return self.client.handleError(e)
 
