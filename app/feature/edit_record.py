"""
DNS Record Editing Module
Handles editing existing DNS records in Cloudflare
"""
from .base_api import CloudflareAPIClient


class EditRecord(CloudflareAPIClient):
    """Handle DNS record editing operations"""
    
    def edit_subdomain(self, subdomain_id, new_ip_address, ttl=3600, proxied=False):
        """
        Edit an existing DNS A record
        
        Args:
            subdomain_id (str): The DNS record ID to edit
            new_ip_address (str): New IP address
            ttl (int): Time to live in seconds (default: 3600)
            proxied (bool): Whether to proxy through Cloudflare (default: False)
            
        Returns:
            bool: True if successful, False otherwise
        """
        data = {
            "type": "A",
            "content": new_ip_address,
            "ttl": ttl,
            "proxied": proxied
        }

        try:
            response = self._make_request("PUT", f"/{subdomain_id}", data)
            
            if response.status_code == 200:
                self._log_success("edited subdomain", f"ID: {subdomain_id} with new IP: {new_ip_address}")
                return True
            else:
                self._log_error("editing subdomain", response)
                return False
                
        except Exception as e:
            self._log_error("editing subdomain", error=e)
            return False

    def toggle_proxy(self, subdomain_id, proxied):
        """
        Toggle proxy status for a DNS record
        
        Args:
            subdomain_id (str): The DNS record ID
            proxied (bool): Whether to enable or disable proxy
            
        Returns:
            bool: True if successful, False otherwise
        """
        data = {
            "proxied": proxied
        }
        
        try:
            response = self._make_request("PUT", f"/{subdomain_id}", data)
            
            if response.status_code == 200:
                status = "enabled" if proxied else "disabled"
                self._log_success(f"proxy {status}", f"subdomain ID: {subdomain_id}")
                return True
            else:
                self._log_error("toggling proxy", response)
                return False
                
        except Exception as e:
            self._log_error("toggling proxy", error=e)
            return False
    
    def update_record_ttl(self, subdomain_id, new_ttl):
        """
        Update TTL for a DNS record
        
        Args:
            subdomain_id (str): The DNS record ID
            new_ttl (int): New TTL value in seconds
            
        Returns:
            bool: True if successful, False otherwise
        """
        data = {
            "ttl": new_ttl
        }
        
        try:
            response = self._make_request("PUT", f"/{subdomain_id}", data)
            
            if response.status_code == 200:
                self._log_success("updated TTL", f"subdomain ID: {subdomain_id} to {new_ttl} seconds")
                return True
            else:
                self._log_error("updating TTL", response)
                return False
                
        except Exception as e:
            self._log_error("updating TTL", error=e)
            return False
    
    def edit_cname_record(self, record_id, new_target, ttl=3600, proxied=False):
        """
        Edit an existing CNAME record
        
        Args:
            record_id (str): The DNS record ID to edit
            new_target (str): New target domain/subdomain
            ttl (int): Time to live in seconds (default: 3600)
            proxied (bool): Whether to proxy through Cloudflare (default: False)
            
        Returns:
            bool: True if successful, False otherwise
        """
        data = {
            "type": "CNAME",
            "content": new_target,
            "ttl": ttl,
            "proxied": proxied
        }

        try:
            response = self._make_request("PUT", f"/{record_id}", data)
            
            if response.status_code == 200:
                self._log_success("edited CNAME record", f"ID: {record_id} with new target: {new_target}")
                return True
            else:
                self._log_error("editing CNAME record", response)
                return False
                
        except Exception as e:
            self._log_error("editing CNAME record", error=e)
            return False


# Create instance for easy importing
edit_record_service = EditRecord()