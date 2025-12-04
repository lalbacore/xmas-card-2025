#!/usr/bin/env python3
"""
Simple QR Code generator for the greeting card.
Creates an SVG QR code pointing to the GitHub repository.
"""

# For now, we'll create a placeholder QR code SVG
# In a real deployment, you'd use a QR library or online generator

def create_placeholder_qr():
    """Creates a simple placeholder QR code SVG"""
    svg = '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="400" height="400" viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
  <!-- Placeholder QR Code - Replace with actual generated QR -->
  <rect width="400" height="400" fill="white"/>
  
  <!-- QR Corner markers (simplified) -->
  <g fill="black">
    <!-- Top-left corner -->
    <rect x="20" y="20" width="80" height="80"/>
    <rect x="30" y="30" width="60" height="60" fill="white"/>
    <rect x="40" y="40" width="40" height="40" fill="black"/>
    
    <!-- Top-right corner -->
    <rect x="300" y="20" width="80" height="80"/>
    <rect x="310" y="30" width="60" height="60" fill="white"/>
    <rect x="320" y="40" width="40" height="40" fill="black"/>
    
    <!-- Bottom-left corner -->
    <rect x="20" y="300" width="80" height="80"/>
    <rect x="30" y="310" width="60" height="60" fill="white"/>
    <rect x="40" y="320" width="40" height="40" fill="black"/>
    
    <!-- Center pattern (simplified) -->
    <rect x="180" y="180" width="40" height="40"/>
    
    <!-- Some random QR-like patterns -->
    <rect x="120" y="40" width="20" height="20"/>
    <rect x="160" y="40" width="20" height="20"/>
    <rect x="240" y="40" width="20" height="20"/>
    <rect x="120" y="80" width="20" height="20"/>
    <rect x="200" y="80" width="20" height="20"/>
    <rect x="240" y="80" width="20" height="20"/>
    
    <rect x="40" y="120" width="20" height="20"/>
    <rect x="120" y="120" width="20" height="20"/>
    <rect x="240" y="120" width="20" height="20"/>
    <rect x="320" y="120" width="20" height="20"/>
    
    <rect x="80" y="160" width="20" height="20"/>
    <rect x="160" y="160" width="20" height="20"/>
    <rect x="280" y="160" width="20" height="20"/>
    <rect x="360" y="160" width="20" height="20"/>
    
    <rect x="40" y="200" width="20" height="20"/>
    <rect x="120" y="200" width="20" height="20"/>
    <rect x="240" y="200" width="20" height="20"/>
    <rect x="320" y="200" width="20" height="20"/>
    
    <rect x="80" y="240" width="20" height="20"/>
    <rect x="160" y="240" width="20" height="20"/>
    <rect x="280" y="240" width="20" height="20"/>
    <rect x="360" y="240" width="20" height="20"/>
    
    <rect x="120" y="320" width="20" height="20"/>
    <rect x="160" y="320" width="20" height="20"/>
    <rect x="240" y="320" width="20" height="20"/>
    <rect x="320" y="320" width="20" height="20"/>
    
    <rect x="120" y="360" width="20" height="20"/>
    <rect x="200" y="360" width="20" height="20"/>
    <rect x="280" y="360" width="20" height="20"/>
  </g>
  
  <!-- URL text for reference -->
  <text x="200" y="410" text-anchor="middle" font-family="monospace" font-size="12" fill="black">
    github.com/lalbacore/xmas-card-2025
  </text>
</svg>'''
    
    with open('qr-code.svg', 'w') as f:
        f.write(svg)
    print("Placeholder QR code created: qr-code.svg")
    print("\nTo create a real QR code:")
    print("1. Visit https://www.qr-code-generator.com/")
    print("2. Enter: https://github.com/lalbacore/xmas-card-2025")
    print("3. Download as SVG")
    print("4. Replace qr-code.svg with the downloaded file")

if __name__ == "__main__":
    create_placeholder_qr()
