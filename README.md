![Slayd Development Shutdown](https://img.shields.io/badge/Slayd%20Development%20Has%20Been%20Shutdown-%20Migrated%20to%20CaptainEXE%20Studios-red?style=for-the-badge)

# ⌨️ Auto Type Bot

A Python-based automation tool designed to simulate controlled typing behavior and maintain consistent formatting when working inside web-based or desktop code editors.

The tool focuses on structured, predictable input automation rather than raw speed, ensuring indentation and layout remain intact when injecting prewritten code into editors.

---

## 🚀 Overview

Auto Type Bot helps automate text injection into code editors while preserving formatting integrity.

It is designed to:

* Maintain consistent indentation
* Respect source file structure
* Avoid broken auto-formatting in online IDEs
* Provide controlled, manual-feel typing simulation

Instead of relying on raw paste behavior, it simulates structured typing to reduce formatting distortion caused by aggressive editor auto-indentation systems.

---

## 🛠️ Installation

Before running the script, install required dependencies:

```bash
pip install keyboard pyautogui
```

---

## ⚙️ Configuration

The script is designed for Windows-based environments and assumes a local file structure for input sourcing.

Default input path:

```txt
Downloads/my drive/.code/Pyhton Projects/Auto Type/type me.txt
```

Ensure your input file is placed correctly before execution.

---

## 🎮 How to Use

### 1. Prepare Input

Place the code or text you want to auto-type into:

`type me.txt`

### 2. Run Script

Launch the main script:

```bash
easytype.py
```

### 3. Activate Bot

* Open your target editor or input field
* Press the activation key (`` ` ``)
* The bot will begin typing after a short delay

### 4. Positioning Window

You have a short buffer window (approx. 2 seconds) to focus the correct input field before automation begins.

### 5. Emergency Stop

Move your mouse to the top-left corner of the screen to immediately stop execution.

---

## ⚠️ Safety Notes

* Only use in environments you control or have permission to automate
* Avoid using in protected or anti-bot systems
* Always test on safe files before real usage

---

## 📦 Use Cases

* Code formatting automation
* Controlled typing simulations
* Educational scripting experiments
* UI/automation testing
* Productivity tooling prototypes

---

## 📜 License

This project is released under the MIT License.

---

## 👨‍💻 Developed By

**CaptainEXE**
