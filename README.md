# Password-Strength-Analyzer---Elevate-Labs-
A Python-based Password Strength Analyzer and Wordlist Generator with a modern Tkinter GUI using zxcvbn for entropy-based analysis.
# Password Strength Analyzer & Wordlist Generator

**One-line description:** Password Strength Analyzer & Wordlist Generator — GUI tool to evaluate password strength and create personalized wordlists.

## Overview
A small Python-based GUI that analyzes password strength (using `zxcvbn-python`) and generates targeted wordlists from user inputs (name, pet name, years, leet variants, etc.). Built with Tkinter (ttk) and designed to be non-destructive of your original project files.

## Features
- Entropy-based strength scoring (zxcvbn)
- Visual strength meter and suggestions
- Optional HaveIBeenPwned breach check (k-anonymity)
- Wordlist generator with leet and year variations
- Export results and wordlists

## Quick start
1. Create a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate      # Windows PowerShell
   source venv/bin/activate     # macOS / Linux
