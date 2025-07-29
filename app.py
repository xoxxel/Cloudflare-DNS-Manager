#!/usr/bin/env python3
"""
Cloudflare DNS Management Application - Simple Launcher
Entry point that launches the appropriate module

Usage:
    python app.py                    # Run interactive DNS manager (default)
    python app.py --examples         # Run usage examples
    python app.py --test             # Run system tests
    python app.py --version          # Show version
"""

import sys
import os
import argparse

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Application metadata
APP_NAME = "Cloudflare DNS Manager"
APP_VERSION = "2.0.0"


def main():
    """Simple launcher - delegates to appropriate modules"""
    parser = argparse.ArgumentParser(
        description=f"{APP_NAME} v{APP_VERSION} - Simple Launcher",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python app.py            # Run main application (default)
  python app.py --examples # Run code examples
  python app.py --test     # Run system tests
  python app.py --version  # Show version info
        """
    )
    
    parser.add_argument('--examples', '-e', action='store_true', 
                       help='Run usage examples')
    parser.add_argument('--test', '-t', action='store_true', 
                       help='Run system tests')
    parser.add_argument('--version', '-v', action='store_true', 
                       help='Show version information')
    
    args = parser.parse_args()
    
    try:
        # Handle version
        if args.version:
            print(f"{APP_NAME} v{APP_VERSION}")
            print(f"Python: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
            return 0
        
        # Handle examples
        if args.examples:
            print("🧪 Running Usage Examples...")
            from app.examples import main as examples_main
            examples_main()
            return 0
        
        # Handle tests
        if args.test:
            print("🔬 Running System Tests...")
            from test_app import main as test_main
            return 0 if test_main() else 1
        
        # Default: Run main application
        print("🚀 Starting Cloudflare DNS Manager...")
        from app.main import main as app_main
        app_main()
        return 0
        
    except ImportError as e:
        print(f"❌ Import Error: {e}")
        print("Please ensure all required files are present and dependencies are installed.")
        return 1
    except KeyboardInterrupt:
        print("\n👋 Application terminated by user")
        return 0
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
