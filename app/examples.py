"""
Example Usage: Cloudflare DNS Management Features
Demonstrates how to use the app.feature package programmatically
"""

import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.feature import (
    add_record_service,
    delete_record_service,
    edit_record_service,
    query_record_service
)


def example_usage():
    """Demonstrate various DNS operations"""
    print("🌐 Cloudflare DNS Management Examples")
    print("="*50)
    
    # 1. Query Operations
    print("\n📋 1. Listing all DNS records:")
    all_records = query_record_service.list_all_records()
    print(f"Found {len(all_records)} total records")
    
    # 2. Filter by type
    print("\n📊 2. Getting A records:")
    a_records = query_record_service.list_records_by_type("A")
    print(f"Found {len(a_records)} A records")
    
    # 3. Search by name
    print("\n🔍 3. Searching for specific record:")
    record = query_record_service.get_record_by_name("example.com")
    if record:
        print(f"Found: {record['name']} -> {record['content']}")
    else:
        print("Record not found")
    
    # 4. Add new A record
    print("\n➕ 4. Adding new A record:")
    success = add_record_service.add_subdomain(
        name="api.example.com",
        ip_address="192.168.1.100",
        ttl=3600,
        proxied=True
    )
    print(f"Add operation: {'✅ Success' if success else '❌ Failed'}")
    
    # 5. Add CNAME record
    print("\n➕ 5. Adding CNAME record:")
    success = add_record_service.add_cname_record(
        name="www.example.com",
        target="example.com",
        ttl=3600,
        proxied=False
    )
    print(f"CNAME add operation: {'✅ Success' if success else '❌ Failed'}")
    
    # 6. Edit record (you'll need a real record ID)
    print("\n✏️ 6. Editing record (example - requires real ID):")
    # success = edit_record_service.edit_subdomain("RECORD_ID", "192.168.1.101")
    print("Edit operation example shown in code")
    
    # 7. Toggle proxy
    print("\n🔄 7. Toggling proxy (example - requires real ID):")
    # success = edit_record_service.toggle_proxy("RECORD_ID", True)
    print("Proxy toggle example shown in code")
    
    # 8. Update TTL
    print("\n⏱️ 8. Updating TTL (example - requires real ID):")
    # success = edit_record_service.update_record_ttl("RECORD_ID", 7200)
    print("TTL update example shown in code")
    
    # 9. Delete record
    print("\n❌ 9. Deleting record (example - requires real ID):")
    # success = delete_record_service.delete_subdomain("RECORD_ID")
    # success = delete_record_service.delete_record_by_name("api.example.com")
    print("Delete operation examples shown in code")


def advanced_example():
    """Advanced usage patterns"""
    print("\n🚀 Advanced Usage Examples")
    print("="*50)
    
    # Batch operations
    print("\n📦 Batch Operations:")
    
    # Get all A records and update their TTL
    a_records = query_record_service.list_records_by_type("A")
    updated_count = 0
    
    for record in a_records[:3]:  # Limit to first 3 for example
        record_id = record.get('id')
        if record_id:
            success = edit_record_service.update_record_ttl(record_id, 7200)
            if success:
                updated_count += 1
    
    print(f"Updated TTL for {updated_count} A records")
    
    # Find and modify records with specific pattern
    print("\n🔍 Pattern-based Operations:")
    all_records = query_record_service.list_all_records()
    
    api_records = [r for r in all_records if 'api' in r.get('name', '').lower()]
    print(f"Found {len(api_records)} records containing 'api'")
    
    # Statistics and analysis
    print("\n📊 DNS Statistics:")
    type_counts = {}
    proxy_enabled = 0
    
    for record in all_records:
        record_type = record.get('type', 'Unknown')
        type_counts[record_type] = type_counts.get(record_type, 0) + 1
        
        if record.get('proxied'):
            proxy_enabled += 1
    
    print(f"Total records: {len(all_records)}")
    print(f"Proxy enabled: {proxy_enabled}")
    print("Record types:")
    for rtype, count in type_counts.items():
        print(f"  {rtype}: {count}")


def error_handling_example():
    """Demonstrate error handling"""
    print("\n🛡️ Error Handling Examples")
    print("="*50)
    
    # Attempt to get non-existent record
    print("\n❌ Testing error handling:")
    
    record = query_record_service.get_record_by_name("non-existent-record.example.com")
    if record is None:
        print("✅ Properly handled non-existent record")
    
    # Attempt to delete non-existent record
    success = delete_record_service.delete_subdomain("invalid-id-12345")
    if not success:
        print("✅ Properly handled invalid record deletion")
    
    print("All error scenarios handled gracefully")


def main():
    """Main entry point for examples"""
    try:
        example_usage()
        advanced_example()
        error_handling_example()
        
        print("\n✅ All examples completed successfully!")
        
    except Exception as e:
        print(f"❌ Error running examples: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
