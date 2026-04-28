# Auto Type Bot
> A Python-based automation tool for maintaining perfect indentation and WPM (words per minute) in web or app based code editors.

## 🚀 Overview
**Auto Type Bot** is designed to bypass the aggressive auto-indentation behaviors of online IDE's. By resetting the margin and manually applying tabs based on the source file's structure, it ensures your code is formatted exactly as intended.

## 🛠️ Installation
Before running the script, ensure you have the required libraries installed:
```bash
pip install keyboard pyautogui
```
## ⚙️ Configuration
The script is configured to be plug-and-play on Windows machines. It dynamically locates your user profile and looks for the source file (type me.txt) at:
`Downloads/my drive/.code/Pyhton Projects/Auto Type/type me.txt`

## 🎮 How to Use
Prepare your code: Place the code you want to type into the `type me.txt` file.

Run the bot: Launch easytype.py from your terminal or VS Code.

Activate: Navigate to your target editor and press the ` (Activate) key.

Position: You have 2 seconds to click into the line where you want the typing to start.

Emergency Stop: If things go wrong, slam your mouse cursor into the top-left corner of your screen to kill the script.

## 📜 License
Distributed under the MIT License. See LICENSE for more information.

Developed by CaptainEXE / Slayd