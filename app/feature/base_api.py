"""
Base API client for Cloudflare DNS operations
"""
import requests
import json
from config import API_TOKEN, ZONE_ID
from app.log.logger import logger


class CloudflareAPIClient:
    """Base class for Cloudflare API operations"""
    
    def __init__(self):
        self.api_token = API_TOKEN
        self.zone_id = ZONE_ID
        self.base_url = "https://api.cloudflare.com/client/v4"
        self.headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }
    
    def _make_request(self, method, endpoint, data=None):
        """
        Make HTTP request to Cloudflare API
        
        Args:
            method (str): HTTP method (GET, POST, PUT, DELETE)
            endpoint (str): API endpoint
            data (dict): Request data (optional)
            
        Returns:
            requests.Response: HTTP response object
        """
        url = f"{self.base_url}/zones/{self.zone_id}/dns_records{endpoint}"
        
        try:
            if method.upper() == "GET":
                response = requests.get(url, headers=self.headers)
            elif method.upper() == "POST":
                response = requests.post(url, headers=self.headers, data=json.dumps(data))
            elif method.upper() == "PUT":
                response = requests.put(url, headers=self.headers, data=json.dumps(data))
            elif method.upper() == "DELETE":
                response = requests.delete(url, headers=self.headers)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
                
            return response
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Network error during {method} request to {url}: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error during {method} request: {str(e)}")
            raise
    
    def _log_success(self, operation, details=""):
        """Log successful operation"""
        logger.info(f"Successfully {operation}: {details}")
    
    def _log_error(self, operation, response=None, error=None):
        """Log failed operation"""
        if response:
            logger.error(f"Error {operation}: {response.json()}")
        elif error:
            logger.error(f"Exception occurred while {operation}: {str(error)}")
