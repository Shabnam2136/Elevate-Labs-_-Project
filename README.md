Here you go Shabnam — a **clean, professional, combined GitHub README** for BOTH projects together.
This README introduces the repo, explains both tools clearly, and keeps everything developer-friendly.

---

# ⭐ **Cybersecurity Tools – Combined Repository**

**Encrypted Keylogger POC (Safe Simulation) + Password Strength Analyzer & Wordlist Generator**

This repository contains **two educational cybersecurity projects** developed for learning, research, and ethical demonstrations.
Both tools are safe, local, and intended for **defensive security understanding** only.

---

# 📌 **Project 1: Encrypted Keylogger POC (Safe & Ethical Simulation)**

### ✔ Overview

A **safe Proof-of-Concept** simulating how an encrypted keylogger works — **without capturing real keystrokes**.
It demonstrates how malware encrypts logs, stores them locally, and sends them to a server for decryption.

### ✔ Key Features

* Fully **simulated fake keystrokes** (no real logging)
* **AES-based Fernet encryption**
* Local encrypted log storage
* Flask server for receiving & decrypting logs
* Client-side fake data generation and upload
* Safe for academic use

### ✔ Folder Structure

```
encrypted_logger_poc/
├── gen_key.py
├── fernet_key.txt
├── server.py
├── client_sim.py
├── local_encrypted_logs/
└── received_logs/
```

### ✔ How It Works

1. `gen_key.py` generates a Fernet key.
2. `client_sim.py` creates fake keystrokes → encrypts → stores locally → uploads to server.
3. `server.py` receives encrypted logs → decrypts → stores in `received_logs/`.

### ✔ Install Dependencies

```bash
pip install cryptography flask requests
```

### ✔ Run Instructions

```bash
python gen_key.py
python server.py
python client_sim.py
```

---

# 📌 **Project 2: Password Strength Analyzer & Wordlist Generator**

### ✔ Overview

A GUI-based tool for:

* Evaluating password strength using entropy & pattern analysis
* Generating **custom wordlists** for ethical password testing
* Teaching users how attackers build targeted dictionaries

### ✔ Features

* Real-time password strength analysis (via `zxcvbn-python`)
* Entropy, pattern match, crack-time estimation
* Personalized wordlist creation using:

  * Name
  * Birth year
  * Pet name
  * Nicknames
  * Special dates
* Automatically adds:

  * Leet speak
  * Special-character variations
  * Number/year combinations
* Clean Tkinter GUI

### ✔ Tools Used

* Python 3
* Tkinter
* zxcvbn-python
* Custom logic for wordlist generation
* Virtual environment (venv)

### ✔ How to Run

```bash
pip install zxcvbn-python
python main.py     # or whichever file contains the GUI
```

---

# 📂 **Repository Structure (Combined)**

```
/Encrypted_Keylogger_POC/
    ├── gen_key.py
    ├── client_sim.py
    ├── server.py
    ├── fernet_key.txt
    ├── local_encrypted_logs/
    └── received_logs/

 /Password_Strength_Analyzer/
    ├── main.py
    ├── ui_components/
    ├── wordlist_generator.py
    ├── requirements.txt
    └── assets/
```

---

# 📜 **Purpose of This Repository**

This repo helps students and cybersecurity learners understand:

### 🔐 **1. How encrypted data exfiltration works (safely simulated)**

* Encryption
* Local log storage
* Client → server secure communication

### 🔑 **2. How password weaknesses are detected**

* Entropy measurement
* Pattern recognition
* Crack-time estimation

### 🧠 **3. How attackers generate targeted password lists**

* OSINT-style personal data combinations
* Leet transformations and variations

---

# ⚠️ **Ethical Use Disclaimer**

These projects are strictly for:
✔ Learning
✔ Research
✔ Educational demonstrations
✔ Improving personal cybersecurity






