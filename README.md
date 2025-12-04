# 🎄 Season's Greetings Card 2025

A customizable HTML-based greeting card with personalized parameter layouts and QR code integration.

## 📋 Features

- Print-ready HTML/CSS card template
- Standard A7 (5" × 7") folded card format
- Customizable parameter layouts for two recipients
- QR code generation pointing to this repository (or your custom URL)
- Easy to modify and version control

## 🚀 Quick Start

### Prerequisites
- A modern web browser (Chrome, Firefox, Safari, Edge)
- Optional: Node.js for QR code generation

### Basic Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/lalbacore/xmas-card-2025.git
   cd xmas-card-2025
   ```

2. Open `card.html` in your web browser

3. Print using your browser:
   - File → Print
   - Set to Letter/A4 paper
   - Landscape orientation
   - No margins
   - Save as PDF or print directly

4. Fold the printed card:
   - Fold horizontally (long edge to long edge)
   - Fold vertically (short edge to short edge)
   - Result: Front has "Season's Greetings", inside has Bob/Alice, back has QR code

## 🎨 Customization

### Change Recipient Names
Edit `card.html` and find:
```html
<h2>Bob</h2>
<!-- and -->
<h2>Alice</h2>
```

### Change QR Code URL
The default QR code points to: `https://github.com/lalbacore/xmas-card-2025`

To generate a new QR code with your custom URL:
```bash
./generate-qr.sh "https://your-custom-url.com"
```

### Modify Card Colors/Fonts
Edit `styles.css` - all styling is centralized there.

## 📐 Card Layout

The card uses a standard 4-panel layout on letter-size (8.5" × 11") paper:

```
┌─────────────┬─────────────┐
│   Panel 4   │   Panel 1   │
│   (Front)   │   (Back)    │
│  Season's   │   QR Code   │
│  Greetings  │             │
├─────────────┼─────────────┤
│   Panel 2   │   Panel 3   │
│ (Inside L)  │ (Inside R)  │
│    Bob      │    Alice    │
│ Parameters  │ Parameters  │
└─────────────┴─────────────┘
```

## 🎁 Easter Egg Ideas

Want to track who scans the QR code? Consider setting up a redirect service:
- Use a URL shortener with analytics (bit.ly, tinyurl with stats)
- Host a simple redirect on your own domain
- Add fun surprises (first 10 scans get one message, rest get another)

## 📝 License

MIT License - feel free to fork, modify, and share!

## 🤝 Contributing

Found a bug or want to add features? PRs welcome!

---

Made with ❤️ for the holidays
