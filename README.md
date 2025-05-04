# 🎨 ASCII Art Text Generator

[![Python Version](https://img.shields.io/badge/python-3.6+-brightgreen.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Text Art](https://img.shields.io/badge/art-ASCII-blue.svg)](https://github.com/yourusername/ascii-art-generator)

Transform your text into beautiful ASCII art with multiple font styles, borders, and effects. Perfect for creating eye-catching terminal banners, signatures, and decorative text.

```
  WHAT  YOU  CAN  CREATE
 ╔═══════════════════════╗
 ║  AAAAA  RRRR  TTTTT  ║
 ║  A   A  R   R   T    ║
 ║  AAAAA  RRRR    T    ║
 ║  A   A  R  R    T    ║
 ║  A   A  R   R   T    ║
 ╚═══════════════════════╝
```

## ✨ Features

- 🔤 **Multiple Fonts**: Choose from standard, banner, and small font styles
- 🖼️ **Border Options**: Add decorative borders (plain, fancy, or rounded)
- 🌟 **Shadow Effect**: Add depth to your ASCII art with shadows
- 📐 **Text Alignment**: Center your ASCII art easily
- 💾 **File Export**: Save your creations to text files
- 🎯 **Simple CLI**: Easy command-line interface
- 🚀 **Zero Dependencies**: Pure Python implementation

## 🔧 Requirements

- 🐍 Python 3.6+
- No external libraries required!

## 📥 Installation

1. Clone this repository:
```bash
git clone https://github.com/0xG4sl3ss/ascii-art-generator.git
cd ascii-art-generator
```

2. 🎉 That's it! You're ready to create ASCII art!

## 🚀 Quick Start

### Basic Usage

```bash
# Generate simple ASCII art
python main.py "HELLO"
```

```bash
# Use a different font
python main.py "HELLO" --font banner
```

```bash
# Add a fancy border
python main.py "HELLO" --border fancy
```

```bash
# Add shadow effect
python main.py "HELLO" --shadow
```

```bash
# Center the text
python main.py "HELLO" --center
```

### Advanced Combinations

```bash
# Create a fancy banner with shadow
python main.py "WELCOME" --font banner --border fancy --shadow --center
```

```bash
# Save to file
python main.py "HELLO" --output greeting.txt
```

```bash
# See all available fonts
python main.py --list-fonts
```

```bash
# View font demonstrations
python main.py --demo
```

## 🎨 Font Styles

| Font Style | Example | Best For |
|------------|---------|----------|
| **standard** | <pre>  A  <br> A A <br>AAAAA<br>A   A<br>A   A</pre> | General purpose, clear text |
| **banner** | <pre>  #  <br> # # <br>#   #<br>#####<br>#   #</pre> | Bold statements, headers |
| **small** | <pre> _ <br>/_\</pre> | Compact text, signatures |

## 🎭 Border Options

<pre>
Plain Border:          Fancy Border:          Round Border:
+--------------------+╔════════════════════╗╭────────────────────╮
|  HELLO             |||  HELLO             ||  HELLO             |
+--------------------+╚════════════════════╝╰────────────────────╯
</pre>

## 💡 Examples

### Create a Logo

```bash
python main.py "PYTHON" --font banner --border fancy --center
```

Output:
<pre>
╔════════════════════════════════════════════════════════════════════╗
║     #### #   # ##### #   #  ####  #   #                            ║
║     #   ##  #    #   #   # #    # ##  #                            ║
║     ####  # #    #   ##### #    # # # #                            ║
║     #     ##     #   #   # #    # #  ##                            ║
║     #     #      #   #   #  ####  #   #                            ║
╚════════════════════════════════════════════════════════════════════╝
</pre>

### Make a Banner

```bash
python main.py "WELCOME TO MY GITHUB" --font standard --shadow --border round
```

### Create Terminal Art

```bash
python main.py "LOADING..." --font small --border plain --output loading.txt
```

## 🖥️ Command Line Options

| Option | Description | Example |
|--------|-------------|---------|
| `-f`, `--font` | Font style (standard, banner, small) | `--font banner` |
| `-b`, `--border` | Border style (plain, fancy, round) | `--border fancy` |
| `-s`, `--shadow` | Add shadow effect | `--shadow` |
| `-c`, `--center` | Center the text | `--center` |
| `-o`, `--output` | Save to file | `--output logo.txt` |
| `--list-fonts` | Show available fonts | `--list-fonts` |
| `--demo` | Show font examples | `--demo` |

## 🛡️ Supported Characters

- Letters: A-Z
- Numbers: 0-9
- Spaces are supported
- Other characters are converted to spaces

## 🚀 Future Enhancements

- [ ] Add more font styles
- [ ] Support for lowercase letters
- [ ] Color option for terminals
- [ ] Custom character mapping
- [ ] Gradient effects
- [ ] Unicode character support

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs
- 💡 Suggest new features
- 🎨 Add new font styles
- 📝 Improve documentation

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🎯 Use Cases

- 🖥️ Terminal splash screens
- 📝 README decorations  
- 💌 ASCII art signatures
- 🎮 Game ASCII art displays
- 🎉 Celebration banners
- 🚀 ASCII logos

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by classic ASCII art generators
- Built with ❤️ for the command-line community

---

<div align="center">
  <h3>🌟 If you like this project, give it a star on GitHub! 🌟</h3>
  
  ```
     THANK  YOU!
    ╔═══════════╗
    ║ ♥ ASCII ♥ ║
    ╚═══════════╝
  ```
</div>
