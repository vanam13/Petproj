#!/usr/bin/env python3
"""
Flask Application Startup Script
Run this file to start your Flask application
"""

from app import app

if __name__ == '__main__':
    print("🚀 Starting Flask Application...")
    print("📍 Server will be available at: http://localhost:5000")
    print("🔄 Press Ctrl+C to stop the server")
    print("-" * 50)
    
    try:
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n🛑 Flask application stopped by user")
    except Exception as e:
        print(f"❌ Error starting Flask application: {e}")
