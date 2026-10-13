import requests 
from typing import Dict 
from urllib.parse import urlencode 

class BaseHTTPClient:
    def __init__(self, baseURL : str):
        self.baseURL = baseURL 

    def _handleError(self, e):
        print("Error", e)
        return {
            "status": "Error",
            "message": str(e)
        }
    
    def getCall(self, endpoint : str, qpParams : Dict = {}): 
        try:
            response = requests.get(f"{self.baseURL}/{endpoint}?{urlencode(qpParams)}")
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return self._handleError(e)

