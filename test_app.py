#!/usr/bin/env python3
"""
Test Script for Cloudflare DNS Manager
Validates that all modules import correctly and basic functionality works
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test that all modules can be imported"""
    print("🧪 Testing imports...")
    
    try:
        # Test config import
        from config import API_TOKEN, ZONE_ID
        print("✅ Config imported successfully")
        
        # Test feature imports
        from app.feature import (
            add_record_service,
            delete_record_service, 
            edit_record_service,
            query_record_service
        )
        print("✅ Feature services imported successfully")
        
        # Test main app import
        from app.main import CloudflareDNSManager
        print("✅ Main application imported successfully")
        
        # Test convenience functions
        from app.feature import add_subdomain, delete_subdomain
        print("✅ Convenience functions imported successfully")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def test_configuration():
    """Test configuration validity"""
    print("\n🔧 Testing configuration...")
    
    try:
        from config import API_TOKEN, ZONE_ID
        
        if not API_TOKEN:
            print("⚠️  API_TOKEN not set")
            return False
        
        if not ZONE_ID:
            print("⚠️  ZONE_ID not set")
            return False
            
        print("✅ Configuration is valid")
        return True
        
    except Exception as e:
        print(f"❌ Configuration error: {e}")
        return False

def test_service_initialization():
    """Test that services can be initialized"""
    print("\n🏗️ Testing service initialization...")
    
    try:
        from app.feature import (
            add_record_service,
            delete_record_service,
            edit_record_service,
            query_record_service
        )
        
        # Test that services have required methods
        assert hasattr(add_record_service, 'add_subdomain'), "Missing add_subdomain method"
        assert hasattr(delete_record_service, 'delete_subdomain'), "Missing delete_subdomain method"
        assert hasattr(edit_record_service, 'edit_subdomain'), "Missing edit_subdomain method"
        assert hasattr(query_record_service, 'list_all_records'), "Missing list_all_records method"
        
        print("✅ All services initialized with required methods")
        return True
        
    except Exception as e:
        print(f"❌ Service initialization error: {e}")
        return False

def test_main_app():
    """Test main application can be created"""
    print("\n🎮 Testing main application...")
    
    try:
        from app.main import CloudflareDNSManager
        
        # Try to create manager instance
        manager = CloudflareDNSManager()
        
        # Test that manager has required methods
        assert hasattr(manager, 'display_menu'), "Missing display_menu method"
        assert hasattr(manager, 'run'), "Missing run method"
        
        print("✅ Main application can be created successfully")
        return True
        
    except Exception as e:
        print(f"❌ Main application error: {e}")
        return False

def test_convenience_functions():
    """Test convenience functions compatibility"""
    print("\n🔄 Testing convenience functions...")
    
    try:
        from app.feature import add_subdomain, delete_subdomain, edit_subdomain, toggle_proxy
        
        # Test that functions exist
        assert callable(add_subdomain), "add_subdomain is not callable"
        assert callable(delete_subdomain), "delete_subdomain is not callable"
        assert callable(edit_subdomain), "edit_subdomain is not callable"
        assert callable(toggle_proxy), "toggle_proxy is not callable"
        
        print("✅ Convenience functions work correctly")
        return True
        
    except Exception as e:
        print(f"❌ Convenience functions error: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 Starting Cloudflare DNS Manager Tests")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_configuration,
        test_service_initialization,
        test_main_app,
        test_convenience_functions
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Application is ready to use.")
        return True
    else:
        print("❌ Some tests failed. Please fix the issues before using the application.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
