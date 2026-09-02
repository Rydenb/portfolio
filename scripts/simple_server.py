#!/usr/bin/env python3
"""
Simple HTTP server for local development when Jekyll is not available.
Serves the _site directory if it exists, otherwise serves the repository root.
"""

import os
import sys
import http.server
import socketserver
from pathlib import Path

def run_server(host="localhost", port=4500):
    """Run a simple HTTP server."""
    
    # Determine serving directory
    serve_dir = "_site" if os.path.isdir("_site") else "."
    
    # Change to serving directory
    original_dir = os.getcwd()
    os.chdir(serve_dir)
    
    # Create request handler with the directory
    Handler = http.server.SimpleHTTPRequestHandler
    
    try:
        with socketserver.TCPServer((host, int(port)), Handler) as httpd:
            print(f"📁 Serving from: {os.path.abspath('.')}")
            print(f"🚀 Server running at http://{host}:{port}/")
            print(f"✓ Press Ctrl+C to stop")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n✓ Server stopped")
    except OSError as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
    finally:
        os.chdir(original_dir)

if __name__ == "__main__":
    host = sys.argv[1] if len(sys.argv) > 1 else "localhost"
    port = sys.argv[2] if len(sys.argv) > 2 else "4500"
    run_server(host, port)
