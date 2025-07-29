# Migration Guide: From Legacy to Modular Structure


### Option 1: Using convenience functions (same interface as before)
```python
from app.feature import add_subdomain, delete_subdomain, edit_subdomain, toggle_proxy

# Same function calls as before
add_subdomain("test", "192.168.1.1")
delete_subdomain("record_id_123")
edit_subdomain("record_id_123", "192.168.1.2")
toggle_proxy("record_id_123", True)
```

### Option 2: Using service instances (recommended for new code)
```python
from app.feature import add_record_service, delete_record_service, edit_record_service, query_record_service

# Add operations
add_record_service.add_subdomain("test", "192.168.1.1")
add_record_service.add_cname_record("www", "example.com")

# Query operations
all_records = query_record_service.list_all_records()
record = query_record_service.get_record_by_name("test")

# Edit operations  
edit_record_service.edit_subdomain("record_id", "192.168.1.2")
edit_record_service.toggle_proxy("record_id", True)
edit_record_service.update_record_ttl("record_id", 7200)

# Delete operations
delete_record_service.delete_subdomain("record_id")
delete_record_service.delete_record_by_name("test")
```

### Option 3: Using classes directly (for advanced usage)
```python
from app.feature import AddRecord, DeleteRecord, EditRecord, QueryRecord

# Create instances
add_service = AddRecord()
query_service = QueryRecord()

# Use methods
add_service.add_subdomain("api", "192.168.1.10")
records = query_service.list_records_by_type("A")
```

## New Features Available:

1. **Enhanced Query Operations**: 
   - List all records
   - Get record by name or ID
   - Filter records by type

2. **Additional Record Types**:
   - CNAME record support
   - Easy to extend for other types

3. **Better Error Handling**:
   - Consistent return values (True/False)
   - Detailed logging
   - Exception handling

4. **Modular Architecture**:
   - Separate concerns
   - Easy to test individual components
   - Extensible design

## File Structure:
```
app/feature/
├── __init__.py          # Main exports and convenience functions
├── base_api.py          # Base API client with common functionality
├── add_record.py        # DNS record addition operations
├── delete_record.py     # DNS record deletion operations  
├── edit_record.py       # DNS record editing operations
└── query_record.py      # DNS record query operations
```
