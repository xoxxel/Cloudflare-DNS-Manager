"""
Cloudflare DNS Management Application
Main application demonstrating all features from app.feature package
"""

import sys
import os
from typing import Optional, List, Dict, Any

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.feature import (
    add_record_service,
    delete_record_service,
    edit_record_service,
    query_record_service
)
from app.log.logger import logger


class CloudflareDNSManager:
    """
    Main DNS management class that orchestrates all DNS operations
    """
    
    def __init__(self):
        self.add_service = add_record_service
        self.delete_service = delete_record_service
        self.edit_service = edit_record_service
        self.query_service = query_record_service
        logger.info("Cloudflare DNS Manager initialized")
    
    def display_menu(self):
        """Display the main menu options"""
        print("\n" + "="*50)
        print("🌐 Cloudflare DNS Management System")
        print("="*50)
        print("1.  📋 List all DNS records")
        print("2.  🔍 Search record by name")
        print("3.  🔎 Search record by ID")
        print("4.  📊 List records by type")
        print("5.  ➕ Add A record (subdomain)")
        print("6.  ➕ Add CNAME record")
        print("7.  ✏️  Edit A record IP")
        print("8.  ✏️  Edit CNAME target")
        print("9.  ⏱️  Update record TTL")
        print("10. 🔄 Toggle proxy status")
        print("11. ❌ Delete record by ID")
        print("12. ❌ Delete record by name")
        print("13. 📈 Show DNS statistics")
        print("14. 🔧 Bulk operations")
        print("0.  🚪 Exit")
        print("="*50)
    
    def list_all_records(self):
        """List all DNS records with formatted output"""
        print("\n📋 Fetching all DNS records...")
        records = self.query_service.list_all_records()
        
        if not records:
            print("❌ No records found or error occurred")
            return
        
        self._display_records_table(records)
    
    def search_record_by_name(self):
        """Search for a specific record by name"""
        name = input("\n🔍 Enter record name to search: ").strip()
        if not name:
            print("❌ Record name cannot be empty")
            return
        
        print(f"🔍 Searching for record: {name}")
        record = self.query_service.get_record_by_name(name)
        
        if record:
            self._display_single_record(record)
        else:
            print(f"❌ Record '{name}' not found")
    
    def search_record_by_id(self):
        """Search for a specific record by ID"""
        record_id = input("\n🔎 Enter record ID to search: ").strip()
        if not record_id:
            print("❌ Record ID cannot be empty")
            return
        
        print(f"🔎 Searching for record ID: {record_id}")
        record = self.query_service.get_record_by_id(record_id)
        
        if record:
            self._display_single_record(record)
        else:
            print(f"❌ Record with ID '{record_id}' not found")
    
    def list_records_by_type(self):
        """List records filtered by type"""
        print("\n📊 Available record types: A, AAAA, CNAME, MX, TXT, SRV, NS, etc.")
        record_type = input("Enter record type: ").strip().upper()
        
        if not record_type:
            print("❌ Record type cannot be empty")
            return
        
        print(f"📊 Fetching {record_type} records...")
        records = self.query_service.list_records_by_type(record_type)
        
        if not records:
            print(f"❌ No {record_type} records found")
            return
        
        self._display_records_table(records)
    
    def add_a_record(self):
        """Add a new A record (subdomain)"""
        print("\n➕ Adding new A record")
        name = input("Enter subdomain name: ").strip()
        ip = input("Enter IP address: ").strip()
        
        if not name or not ip:
            print("❌ Name and IP address are required")
            return
        
        # Optional parameters
        ttl_input = input("Enter TTL (default 3600): ").strip()
        ttl = int(ttl_input) if ttl_input.isdigit() else 3600
        
        proxy_input = input("Enable Cloudflare proxy? (y/N): ").strip().lower()
        proxied = proxy_input in ['y', 'yes']
        
        print(f"➕ Adding A record: {name} -> {ip}")
        success = self.add_service.add_subdomain(name, ip, ttl, proxied)
        
        if success:
            print("✅ A record added successfully!")
        else:
            print("❌ Failed to add A record")
    
    def add_cname_record(self):
        """Add a new CNAME record"""
        print("\n➕ Adding new CNAME record")
        name = input("Enter record name: ").strip()
        target = input("Enter target domain: ").strip()
        
        if not name or not target:
            print("❌ Name and target are required")
            return
        
        # Optional parameters
        ttl_input = input("Enter TTL (default 3600): ").strip()
        ttl = int(ttl_input) if ttl_input.isdigit() else 3600
        
        proxy_input = input("Enable Cloudflare proxy? (y/N): ").strip().lower()
        proxied = proxy_input in ['y', 'yes']
        
        print(f"➕ Adding CNAME record: {name} -> {target}")
        success = self.add_service.add_cname_record(name, target, ttl, proxied)
        
        if success:
            print("✅ CNAME record added successfully!")
        else:
            print("❌ Failed to add CNAME record")
    
    def edit_a_record(self):
        """Edit an existing A record"""
        print("\n✏️ Editing A record")
        record_id = input("Enter record ID: ").strip()
        new_ip = input("Enter new IP address: ").strip()
        
        if not record_id or not new_ip:
            print("❌ Record ID and new IP are required")
            return
        
        # Optional parameters
        ttl_input = input("Enter TTL (default 3600): ").strip()
        ttl = int(ttl_input) if ttl_input.isdigit() else 3600
        
        proxy_input = input("Enable Cloudflare proxy? (y/N): ").strip().lower()
        proxied = proxy_input in ['y', 'yes']
        
        print(f"✏️ Updating A record {record_id} -> {new_ip}")
        success = self.edit_service.edit_subdomain(record_id, new_ip, ttl, proxied)
        
        if success:
            print("✅ A record updated successfully!")
        else:
            print("❌ Failed to update A record")
    
    def edit_cname_record(self):
        """Edit an existing CNAME record"""
        print("\n✏️ Editing CNAME record")
        record_id = input("Enter record ID: ").strip()
        new_target = input("Enter new target domain: ").strip()
        
        if not record_id or not new_target:
            print("❌ Record ID and new target are required")
            return
        
        # Optional parameters
        ttl_input = input("Enter TTL (default 3600): ").strip()
        ttl = int(ttl_input) if ttl_input.isdigit() else 3600
        
        proxy_input = input("Enable Cloudflare proxy? (y/N): ").strip().lower()
        proxied = proxy_input in ['y', 'yes']
        
        print(f"✏️ Updating CNAME record {record_id} -> {new_target}")
        success = self.edit_service.edit_cname_record(record_id, new_target, ttl, proxied)
        
        if success:
            print("✅ CNAME record updated successfully!")
        else:
            print("❌ Failed to update CNAME record")
    
    def update_record_ttl(self):
        """Update TTL for a DNS record"""
        print("\n⏱️ Updating record TTL")
        record_id = input("Enter record ID: ").strip()
        ttl_input = input("Enter new TTL (seconds): ").strip()
        
        if not record_id or not ttl_input.isdigit():
            print("❌ Valid record ID and TTL are required")
            return
        
        ttl = int(ttl_input)
        print(f"⏱️ Updating TTL for record {record_id} to {ttl} seconds")
        success = self.edit_service.update_record_ttl(record_id, ttl)
        
        if success:
            print("✅ TTL updated successfully!")
        else:
            print("❌ Failed to update TTL")
    
    def toggle_proxy_status(self):
        """Toggle proxy status for a DNS record"""
        print("\n🔄 Toggling proxy status")
        record_id = input("Enter record ID: ").strip()
        
        if not record_id:
            print("❌ Record ID is required")
            return
        
        # Get current record to show current status
        current_record = self.query_service.get_record_by_id(record_id)
        if current_record:
            current_status = "enabled" if current_record.get('proxied') else "disabled"
            print(f"Current proxy status: {current_status}")
        
        proxy_input = input("Enable proxy? (y/N): ").strip().lower()
        proxied = proxy_input in ['y', 'yes']
        
        print(f"🔄 {'Enabling' if proxied else 'Disabling'} proxy for record {record_id}")
        success = self.edit_service.toggle_proxy(record_id, proxied)
        
        if success:
            print("✅ Proxy status updated successfully!")
        else:
            print("❌ Failed to update proxy status")
    
    def delete_record_by_id(self):
        """Delete a DNS record by ID"""
        print("\n❌ Deleting record by ID")
        record_id = input("Enter record ID to delete: ").strip()
        
        if not record_id:
            print("❌ Record ID is required")
            return
        
        # Show record details before deletion
        record = self.query_service.get_record_by_id(record_id)
        if record:
            print(f"Record to delete: {record.get('name')} ({record.get('type')}) -> {record.get('content')}")
            confirm = input("Are you sure? (y/N): ").strip().lower()
            
            if confirm in ['y', 'yes']:
                print(f"❌ Deleting record {record_id}")
                success = self.delete_service.delete_subdomain(record_id)
                
                if success:
                    print("✅ Record deleted successfully!")
                else:
                    print("❌ Failed to delete record")
            else:
                print("Deletion cancelled")
        else:
            print(f"❌ Record with ID '{record_id}' not found")
    
    def delete_record_by_name(self):
        """Delete a DNS record by name"""
        print("\n❌ Deleting record by name")
        record_name = input("Enter record name to delete: ").strip()
        
        if not record_name:
            print("❌ Record name is required")
            return
        
        # Show record details before deletion
        record = self.query_service.get_record_by_name(record_name)
        if record:
            print(f"Record to delete: {record.get('name')} ({record.get('type')}) -> {record.get('content')}")
            confirm = input("Are you sure? (y/N): ").strip().lower()
            
            if confirm in ['y', 'yes']:
                print(f"❌ Deleting record {record_name}")
                success = self.delete_service.delete_record_by_name(record_name)
                
                if success:
                    print("✅ Record deleted successfully!")
                else:
                    print("❌ Failed to delete record")
            else:
                print("Deletion cancelled")
        else:
            print(f"❌ Record '{record_name}' not found")
    
    def show_dns_statistics(self):
        """Show DNS statistics and summary"""
        print("\n📈 DNS Statistics")
        print("="*40)
        
        records = self.query_service.list_all_records()
        if not records:
            print("❌ No records found")
            return
        
        # Count records by type
        type_counts = {}
        proxy_enabled = 0
        total_records = len(records)
        
        for record in records:
            record_type = record.get('type', 'Unknown')
            type_counts[record_type] = type_counts.get(record_type, 0) + 1
            
            if record.get('proxied'):
                proxy_enabled += 1
        
        print(f"📊 Total Records: {total_records}")
        print(f"🔄 Proxy Enabled: {proxy_enabled}")
        print(f"🔄 Proxy Disabled: {total_records - proxy_enabled}")
        print("\n📋 Records by Type:")
        
        for record_type, count in sorted(type_counts.items()):
            print(f"   {record_type}: {count}")
        
        print("="*40)
    
    def bulk_operations(self):
        """Perform bulk operations"""
        print("\n🔧 Bulk Operations")
        print("1. Export all records to file")
        print("2. Enable proxy for all A records")
        print("3. Disable proxy for all A records")
        print("4. Update TTL for all records of specific type")
        
        choice = input("Select bulk operation (1-4): ").strip()
        
        if choice == "1":
            self._export_records()
        elif choice == "2":
            self._bulk_toggle_proxy("A", True)
        elif choice == "3":
            self._bulk_toggle_proxy("A", False)
        elif choice == "4":
            self._bulk_update_ttl()
        else:
            print("❌ Invalid choice")
    
    def _export_records(self):
        """Export all records to a file"""
        records = self.query_service.list_all_records()
        if not records:
            print("❌ No records to export")
            return
        
        filename = f"dns_records_{self._get_timestamp()}.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("Cloudflare DNS Records Export\n")
                f.write("="*50 + "\n\n")
                
                for record in records:
                    f.write(f"Name: {record.get('name', 'N/A')}\n")
                    f.write(f"Type: {record.get('type', 'N/A')}\n")
                    f.write(f"Content: {record.get('content', 'N/A')}\n")
                    f.write(f"TTL: {record.get('ttl', 'N/A')}\n")
                    f.write(f"Proxied: {record.get('proxied', False)}\n")
                    f.write(f"ID: {record.get('id', 'N/A')}\n")
                    f.write("-" * 30 + "\n")
            
            print(f"✅ Records exported to {filename}")
            
        except Exception as e:
            print(f"❌ Failed to export records: {str(e)}")
    
    def _bulk_toggle_proxy(self, record_type: str, enable: bool):
        """Bulk toggle proxy for records of specific type"""
        records = self.query_service.list_records_by_type(record_type)
        if not records:
            print(f"❌ No {record_type} records found")
            return
        
        action = "enable" if enable else "disable"
        print(f"🔄 Found {len(records)} {record_type} records")
        confirm = input(f"Confirm {action} proxy for all {record_type} records? (y/N): ").strip().lower()
        
        if confirm not in ['y', 'yes']:
            print("Operation cancelled")
            return
        
        success_count = 0
        for record in records:
            record_id = record.get('id')
            if record_id:
                if self.edit_service.toggle_proxy(record_id, enable):
                    success_count += 1
        
        print(f"✅ Successfully updated {success_count}/{len(records)} records")
    
    def _bulk_update_ttl(self):
        """Bulk update TTL for records of specific type"""
        record_type = input("Enter record type: ").strip().upper()
        ttl_input = input("Enter new TTL (seconds): ").strip()
        
        if not record_type or not ttl_input.isdigit():
            print("❌ Valid record type and TTL are required")
            return
        
        ttl = int(ttl_input)
        records = self.query_service.list_records_by_type(record_type)
        
        if not records:
            print(f"❌ No {record_type} records found")
            return
        
        print(f"⏱️ Found {len(records)} {record_type} records")
        confirm = input(f"Confirm update TTL to {ttl} for all {record_type} records? (y/N): ").strip().lower()
        
        if confirm not in ['y', 'yes']:
            print("Operation cancelled")
            return
        
        success_count = 0
        for record in records:
            record_id = record.get('id')
            if record_id:
                if self.edit_service.update_record_ttl(record_id, ttl):
                    success_count += 1
        
        print(f"✅ Successfully updated {success_count}/{len(records)} records")
    
    def _display_records_table(self, records: List[Dict[str, Any]]):
        """Display records in a formatted table"""
        if not records:
            return
        
        print(f"\n📋 Found {len(records)} records:")
        print("-" * 100)
        print(f"{'Name':<25} {'Type':<8} {'Content':<30} {'TTL':<8} {'Proxy':<8} {'ID':<20}")
        print("-" * 100)
        
        for record in records:
            name = record.get('name', 'N/A')[:24]
            record_type = record.get('type', 'N/A')
            content = record.get('content', 'N/A')[:29]
            ttl = str(record.get('ttl', 'N/A'))
            proxied = "Yes" if record.get('proxied') else "No"
            record_id = record.get('id', 'N/A')[:19]
            
            print(f"{name:<25} {record_type:<8} {content:<30} {ttl:<8} {proxied:<8} {record_id:<20}")
        
        print("-" * 100)
    
    def _display_single_record(self, record: Dict[str, Any]):
        """Display detailed information for a single record"""
        print("\n📄 Record Details:")
        print("="*40)
        print(f"Name: {record.get('name', 'N/A')}")
        print(f"Type: {record.get('type', 'N/A')}")
        print(f"Content: {record.get('content', 'N/A')}")
        print(f"TTL: {record.get('ttl', 'N/A')}")
        print(f"Proxied: {'Yes' if record.get('proxied') else 'No'}")
        print(f"ID: {record.get('id', 'N/A')}")
        print(f"Zone ID: {record.get('zone_id', 'N/A')}")
        print(f"Created: {record.get('created_on', 'N/A')}")
        print(f"Modified: {record.get('modified_on', 'N/A')}")
        print("="*40)
    
    def _get_timestamp(self) -> str:
        """Get current timestamp for file naming"""
        from datetime import datetime
        return datetime.now().strftime("%Y%m%d_%H%M%S")
    
    def run(self):
        """Main application loop"""
        print("🚀 Starting Cloudflare DNS Manager...")
        
        try:
            while True:
                self.display_menu()
                choice = input("\n🎯 Enter your choice (0-14): ").strip()
                
                if choice == "0":
                    print("👋 Goodbye!")
                    break
                elif choice == "1":
                    self.list_all_records()
                elif choice == "2":
                    self.search_record_by_name()
                elif choice == "3":
                    self.search_record_by_id()
                elif choice == "4":
                    self.list_records_by_type()
                elif choice == "5":
                    self.add_a_record()
                elif choice == "6":
                    self.add_cname_record()
                elif choice == "7":
                    self.edit_a_record()
                elif choice == "8":
                    self.edit_cname_record()
                elif choice == "9":
                    self.update_record_ttl()
                elif choice == "10":
                    self.toggle_proxy_status()
                elif choice == "11":
                    self.delete_record_by_id()
                elif choice == "12":
                    self.delete_record_by_name()
                elif choice == "13":
                    self.show_dns_statistics()
                elif choice == "14":
                    self.bulk_operations()
                else:
                    print("❌ Invalid choice. Please try again.")
                
                input("\n⏸️ Press Enter to continue...")
        
        except KeyboardInterrupt:
            print("\n\n👋 Application terminated by user")
        except Exception as e:
            logger.error(f"Application error: {str(e)}")
            print(f"❌ An error occurred: {str(e)}")


def main():
    """Application entry point"""
    try:
        manager = CloudflareDNSManager()
        manager.run()
    except Exception as e:
        logger.error(f"Failed to start application: {str(e)}")
        print(f"❌ Failed to start application: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()