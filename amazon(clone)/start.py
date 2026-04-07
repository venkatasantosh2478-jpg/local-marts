#!/usr/bin/env python3
"""
Amazon Clone - Startup Script
Run this from the amazon(clone) folder: python start.py
"""

import os
import sys
import subprocess
import platform

def check_python():
    """Check if Python version is correct"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ ERROR: Python 3.8+ required!")
        print(f"Your version: {version.major}.{version.minor}")
        return False
    return True

def check_dependencies():
    """Check if required packages are installed"""
    required = ['flask', 'flask_sqlalchemy', 'flask_login']
    missing = []
    
    for package in required:
        try:
            __import__(package.replace('_', '-'))
        except ImportError:
            missing.append(package)
    
    if missing:
        print("❌ Missing dependencies!")
        print(f"Run: pip install -r requirements.txt")
        return False
    return True

def seed_database():
    """Create database if it doesn't exist"""
    db_path = os.path.join(os.path.dirname(__file__), 'app', 'amazon_clone.db')
    
    if not os.path.exists(db_path):
        print("\n📦 Creating database with sample data...")
        try:
            # Run seed script
            seed_file = os.path.join(os.path.dirname(__file__), 'seed.py')
            exec(open(seed_file).read())
            print("✅ Database created successfully!")
        except Exception as e:
            print(f"⚠️  Could not auto-seed: {e}")
            print("Run manually: python seed.py")
            return False
    else:
        print("✅ Database already exists")
    return True

def start_app():
    """Start the Flask application"""
    app_dir = os.path.join(os.path.dirname(__file__), 'app')
    
    if not os.path.exists(app_dir):
        print("❌ ERROR: app/ folder not found!")
        return False
    
    print("\n" + "="*50)
    print("🚀 Starting Amazon Clone...")
    print("="*50)
    print("📱 Server: http://localhost:5000")
    print("👤 Admin: admin / admin123")
    print("👤 User: testuser / test123")
    print("="*50 + "\n")
    
    try:
        # Change to app directory
        os.chdir(app_dir)
        
        # Import and run Flask app
        sys.path.insert(0, app_dir)
        from run import app, db
        
        # Create tables
        with app.app_context():
            db.create_all()
        
        # Run Flask
        print("Starting Flask server...\n")
        app.run(debug=True, host='127.0.0.1', port=5000)
        
    except Exception as e:
        print(f"❌ Error starting app: {e}")
        print("\nTroubleshooting:")
        print("1. Make sure you're in amazon(clone) folder")
        print("2. Run: pip install -r requirements.txt")
        print("3. Run: python seed.py")
        return False

def main():
    """Main startup sequence"""
    print("\n" + "="*50)
    print("   AMAZON CLONE - E-COMMERCE APPLICATION")
    print("="*50 + "\n")
    
    # Check Python version
    print("✓ Checking Python version...")
    if not check_python():
        return False
    print(f"  Python {sys.version_info.major}.{sys.version_info.minor} ✅\n")
    
    # Check dependencies
    print("✓ Checking dependencies...")
    if not check_dependencies():
        return False
    print("  All dependencies installed ✅\n")
    
    # Seed database
    print("✓ Checking database...")
    if not seed_database():
        print("  ⚠️  Could not auto-seed database")
    print()
    
    # Start application
    return start_app()

if __name__ == '__main__':
    try:
        success = main()
        if not success:
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n👋 Server stopped!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        sys.exit(1)
