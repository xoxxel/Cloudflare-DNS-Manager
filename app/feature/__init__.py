"""
Cloudflare DNS Management Feature Module
Provides modular access to DNS record operations
"""

# Import base classes
from .base_api import CloudflareAPIClient

# Import service instances
from .add_record import AddRecord, add_record_service
from .delete_record import DeleteRecord, delete_record_service
from .edit_record import EditRecord, edit_record_service
from .query_record import QueryRecord, query_record_service

# Expose all functionality
__all__ = [
    # Base classes
    'CloudflareAPIClient',
    
    # Feature classes
    'AddRecord',
    'DeleteRecord', 
    'EditRecord',
    'QueryRecord',
    
    # Service instances (for direct use)
    'add_record_service',
    'delete_record_service',
    'edit_record_service',
    'query_record_service',
]

# Convenience functions that mirror the original cloudflare_api.py interface
def add_subdomain(name, ip_address, ttl=3600, proxied=False):
    """Add a new subdomain (A record) - convenience function"""
    return add_record_service.add_subdomain(name, ip_address, ttl, proxied)

def delete_subdomain(subdomain_id):
    """Delete a subdomain by ID - convenience function"""
    return delete_record_service.delete_subdomain(subdomain_id)

def edit_subdomain(subdomain_id, new_ip_address, ttl=3600, proxied=False):
    """Edit an existing subdomain - convenience function"""
    return edit_record_service.edit_subdomain(subdomain_id, new_ip_address, ttl, proxied)

def toggle_proxy(subdomain_id, proxied):
    """Toggle proxy status - convenience function"""
    return edit_record_service.toggle_proxy(subdomain_id, proxied)