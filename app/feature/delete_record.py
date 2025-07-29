"""
DNS Record Deletion Module
Handles deleting DNS records from Cloudflare
"""
from .base_api import CloudflareAPIClient


class DeleteRecord(CloudflareAPIClient):
    """Handle DNS record deletion operations"""
    
    def delete_subdomain(self, subdomain_id):
        """
        Delete a DNS record by its ID
        
        Args:
            subdomain_id (str): The DNS record ID to delete
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            response = self._make_request("DELETE", f"/{subdomain_id}")
            
            if response.status_code == 200:
                self._log_success("deleted subdomain", f"ID: {subdomain_id}")
                return True
            else:
                self._log_error("deleting subdomain", response)
                return False
                
        except Exception as e:
            self._log_error("deleting subdomain", error=e)
            return False
    
    def delete_record_by_name(self, record_name):
        """
        Delete a DNS record by its name (requires fetching ID first)
        
        Args:
            record_name (str): The DNS record name to delete
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # First, get the record ID by name
            record_id = self._get_record_id_by_name(record_name)
            
            if not record_id:
                self._log_error("deleting record", error=f"Record '{record_name}' not found")
                return False
            
            return self.delete_subdomain(record_id)
            
        except Exception as e:
            self._log_error("deleting record by name", error=e)
            return False
    
    def _get_record_id_by_name(self, record_name):
        """
        Get DNS record ID by name
        
        Args:
            record_name (str): The DNS record name
            
        Returns:
            str: Record ID if found, None otherwise
        """
        try:
            response = self._make_request("GET", f"?name={record_name}")
            
            if response.status_code == 200:
                records = response.json().get('result', [])
                if records:
                    return records[0]['id']
            
            return None
            
        except Exception as e:
            self._log_error("fetching record ID", error=e)
            return None


# Create instance for easy importing
delete_record_service = DeleteRecord()