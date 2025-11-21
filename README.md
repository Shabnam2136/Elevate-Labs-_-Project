# Password Strength Analyzer & Wordlist Generator

A powerful tool to analyze password strength and generate custom wordlists for security testing purposes.

## Features

### Password Analyzer
- Analyze password strength using zxcvbn
- Get detailed feedback and suggestions
- View estimated time to crack
- Visual strength indicator

### Wordlist Generator
- Generate custom wordlists based on personal information
- Support for leet speak variations
- Combine multiple words with different separators
- Add special characters and number combinations
- Export wordlists in .txt format

## Requirements
- Python 3.6+
- Required packages listed in `requirements.txt`

## Installation

1. Clone this repository
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

### GUI Mode (Recommended)
Run the application with:
```
python password_analyzer.py
```

### Features
1. **Password Analyzer Tab**:
   - Enter a password to analyze
   - View detailed strength analysis
   - Get improvement suggestions

2. **Wordlist Generator Tab**:
   - Enter personal information (name, pet name, birth year)
   - Customize word generation options
   - Preview generated wordlist
   - Save wordlist to a file

## Security Note
This tool is intended for educational and security testing purposes only. Always ensure you have proper authorization before testing any system.

## License
MIT License - Feel free to use and modify as needed.
