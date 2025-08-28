#!/usr/bin/env python3

import sys
print("Python executable:", sys.executable)
print("Python version:", sys.version)
print("Python path:")
for path in sys.path:
    print(f"  {path}")

print("\nTrying to import Flask...")
try:
    import flask
    print("Flask module found at:", flask.__file__)
    print("Flask version:", flask.__version__)
    
    from flask import Flask
    print("Flask class imported successfully!")
    
except ImportError as e:
    print(f"Import error: {e}")
    
except Exception as e:
    print(f"Other error: {e}")
    import traceback
    traceback.print_exc()
