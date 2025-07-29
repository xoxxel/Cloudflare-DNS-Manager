"""
DNS Record Query Module
Handles querying and listing DNS records from Cloudflare
"""
from .base_api import CloudflareAPIClient


class QueryRecord(CloudflareAPIClient):
    """Handle DNS record query operations"""
    
    def list_all_records(self):
        """
        List all DNS records in the zone
        
        Returns:
            list: List of DNS records if successful, empty list otherwise
        """
        try:
            response = self._make_request("GET", "")
            
            if response.status_code == 200:
                records = response.json().get('result', [])
                self._log_success("retrieved all records", f"found {len(records)} records")
                return records
            else:
                self._log_error("listing records", response)
                return []
                
        except Exception as e:
            self._log_error("listing records", error=e)
            return []
    
    def get_record_by_name(self, record_name):
        """
        Get a specific DNS record by name
        
        Args:
            record_name (str): The DNS record name to search for
            
        Returns:
            dict: Record data if found, None otherwise
        """
        try:
            response = self._make_request("GET", f"?name={record_name}")
            
            if response.status_code == 200:
                records = response.json().get('result', [])
                if records:
                    self._log_success("found record", f"name: {record_name}")
                    return records[0]
                else:
                    self._log_error("finding record", error=f"Record '{record_name}' not found")
                    return None
            else:
                self._log_error("finding record", response)
                return None
                
        except Exception as e:
            self._log_error("finding record", error=e)
            return None
    
    def get_record_by_id(self, record_id):
        """
        Get a specific DNS record by ID
        
        Args:
            record_id (str): The DNS record ID to search for
            
        Returns:
            dict: Record data if found, None otherwise
        """
        try:
            response = self._make_request("GET", f"/{record_id}")
            
            if response.status_code == 200:
                record = response.json().get('result')
                self._log_success("found record", f"ID: {record_id}")
                return record
            else:
                self._log_error("finding record by ID", response)
                return None
                
        except Exception as e:
            self._log_error("finding record by ID", error=e)
            return None
    
    def list_records_by_type(self, record_type):
        """
        List DNS records filtered by type
        
        Args:
            record_type (str): DNS record type (A, CNAME, MX, etc.)
            
        Returns:
            list: List of DNS records of specified type
        """
        try:
            response = self._make_request("GET", f"?type={record_type}")
            
            if response.status_code == 200:
                records = response.json().get('result', [])
                self._log_success("retrieved records by type", f"found {len(records)} {record_type} records")
                return records
            else:
                self._log_error("listing records by type", response)
                return []
                
        except Exception as e:
            self._log_error("listing records by type", error=e)
            return []


# Create instance for easy importing
query_record_service = QueryRecord()
