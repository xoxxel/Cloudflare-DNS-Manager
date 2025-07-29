"""
DNS Record Addition Module
Handles adding new DNS records to Cloudflare
"""
from .base_api import CloudflareAPIClient


class AddRecord(CloudflareAPIClient):
    """Handle DNS record addition operations"""
    
    def add_subdomain(self, name, ip_address, ttl=3600, proxied=False):
        """
        Add a new subdomain (A record) to Cloudflare DNS
        
        Args:
            name (str): Subdomain name
            ip_address (str): IP address for the A record
            ttl (int): Time to live in seconds (default: 3600)
            proxied (bool): Whether to proxy through Cloudflare (default: False)
            
        Returns:
            bool: True if successful, False otherwise
        """
        data = {
            "type": "A",
            "name": name,
            "content": ip_address,
            "ttl": ttl,
            "proxied": proxied
        }
        
        try:
            response = self._make_request("POST", "", data)
            
            if response.status_code == 201:
                self._log_success("added subdomain", f"{name} with IP: {ip_address}")
                return True
            else:
                self._log_error("adding subdomain", response)
                return False
                
        except Exception as e:
            self._log_error("adding subdomain", error=e)
            return False
    
    def add_cname_record(self, name, target, ttl=3600, proxied=False):
        """
        Add a new CNAME record to Cloudflare DNS
        
        Args:
            name (str): Record name
            target (str): Target domain/subdomain
            ttl (int): Time to live in seconds (default: 3600)
            proxied (bool): Whether to proxy through Cloudflare (default: False)
            
        Returns:
            bool: True if successful, False otherwise
        """
        data = {
            "type": "CNAME",
            "name": name,
            "content": target,
            "ttl": ttl,
            "proxied": proxied
        }
        
        try:
            response = self._make_request("POST", "", data)
            
            if response.status_code == 201:
                self._log_success("added CNAME record", f"{name} -> {target}")
                return True
            else:
                self._log_error("adding CNAME record", response)
                return False
                
        except Exception as e:
            self._log_error("adding CNAME record", error=e)
            return False


# Create instance for easy importing
add_record_service = AddRecord()