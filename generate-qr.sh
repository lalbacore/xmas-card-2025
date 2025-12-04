#!/bin/bash
# Generate QR code for custom URL

URL="${1:-https://github.com/lalbacore/xmas-card-2025}"

echo "==================================="
echo "QR Code Generator for Greeting Card"
echo "==================================="
echo ""
echo "Target URL: $URL"
echo ""

# Check if we have qrencode installed
if command -v qrencode &> /dev/null; then
    echo "✓ Generating QR code with qrencode..."
    qrencode -t SVG -o qr-code.svg "$URL"
    echo "✓ QR code saved to: qr-code.svg"
elif command -v python3 &> /dev/null; then
    echo "⚠ qrencode not found, using Python fallback..."
    python3 -c "
try:
    import qrcode
    import qrcode.image.svg
    
    factory = qrcode.image.svg.SvgPathImage
    img = qrcode.make('$URL', image_factory=factory)
    with open('qr-code.svg', 'wb') as f:
        img.save(f)
    print('✓ QR code saved to: qr-code.svg')
except ImportError:
    print('⚠ Python qrcode library not installed')
    print('')
    print('Install with: pip install qrcode[pil]')
    print('Or use an online generator:')
    print('  1. Visit: https://www.qr-code-generator.com/')
    print('  2. Enter URL: $URL')
    print('  3. Download as SVG and save as qr-code.svg')
    exit(1)
"
else
    echo "⚠ No QR code generators found"
    echo ""
    echo "Options:"
    echo "  1. Install qrencode: sudo apt-get install qrencode"
    echo "  2. Install Python library: pip install qrcode[pil]"
    echo "  3. Use online generator:"
    echo "     - Visit: https://www.qr-code-generator.com/"
    echo "     - Enter URL: $URL"
    echo "     - Download as SVG and save as qr-code.svg"
    exit 1
fi

echo ""
echo "✓ Done! Open card.html to see your updated card."
echo ""
