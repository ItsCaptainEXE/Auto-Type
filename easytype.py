# Be sure to use `pip install` for these libarys!
import keyboard
import pyautogui
import os
import time

# --- DYNAMIC PATHING ---
# This automatically finds C:\Users\<YourUser>\
USER_HOME = os.path.expanduser("~")
TARGET_FILE = os.path.join(USER_HOME, "Downloads", "Python-Playground", "Auto Type", "type me.txt")

# --- PERFORMANCE CONFIG ---
pyautogui.PAUSE = 0 # Edit this if the script freezes/ glitchs (Common with large files)

def force_indent_writer():
    if not os.path.exists(TARGET_FILE):
        print(f"[!] Error: File not found at {TARGET_FILE}")
        return

    print(f"[*] Starting in 2 seconds... Click on where you want to type!")
    time.sleep(1.0)
    print(f"[*] Starting in 1 seconds... Click on where you want to type!")
    time.sleep(1.0)

    try:
        with open(TARGET_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        print(f"[*] Forcing indents to ensure exact format from: {os.path.basename(TARGET_FILE)}")

        for line in lines:
            stripped_line = line.lstrip()
            
            if not stripped_line.strip(): 
                pyautogui.press('enter')
                continue
            
            # Calculate Indentation (4 spaces)
            indent_count = (len(line) - len(stripped_line)) // 4
            
            # Reset Margin
            with pyautogui.hold('shift'):
                pyautogui.press(['tab', 'tab', 'tab', 'tab'])
            
            # Apply Forced Indents
            for _ in range(indent_count):
                pyautogui.press('tab')
            
            # Write Content
            keyboard.write(stripped_line.rstrip('\n'), delay=0.01)
            pyautogui.press('enter')
            
        print("[*] Typing Finished.")
    except Exception as e:
        print(f"[!] Error: {e}")

print("--- Easy Auto Type Bot ---")
print(f"Detecting Path: {TARGET_FILE}")
print("Hotkey: ` (Use to activate the bot to type from the text file)")
print("QUICK SCRIPT KILLER: Move your mouse to the top left corner to end typing")

keyboard.add_hotkey('`', force_indent_writer)
keyboard.wait()