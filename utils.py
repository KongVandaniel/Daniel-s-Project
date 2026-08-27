"""
Utility helpers for Python Text-Based Games.
Includes ANSI colors, typewriter printing effect, robust user input,
and cross-platform Text-To-Speech (macOS, Windows, Linux).
"""

import os
import platform
import subprocess
import sys
import time

# ANSI Escape Color Codes
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
GRAY = "\033[90m"

DEFAULT_DELAY = 0.00 if (any('test_games' in arg for arg in sys.argv) or os.environ.get('TESTING') == '1') else 0.02


def colorize(text: str, color_code: str) -> str:
    """Wraps text in ANSI color codes for rich terminal styling."""
    return f"{color_code}{text}{RESET}"


def typewriter_print(text: str, delay: float = None, end: str = '\n'):
    """
    Prints text character by character to produce a smooth typewriter animation.
    Handles ANSI color escape codes seamlessly without slowing down on invisible codes.
    """
    if delay is None or not isinstance(delay, (int, float)):
        if isinstance(delay, str):
            try:
                delay = float(delay)
            except ValueError:
                delay = 0.00 if (any('test_games' in arg for arg in sys.argv) or os.environ.get('TESTING') == '1') else 0.02
        else:
            delay = 0.00 if (any('test_games' in arg for arg in sys.argv) or os.environ.get('TESTING') == '1') else 0.02
    in_ansi = False
    for char in str(text):
        if char == '\033':
            in_ansi = True
        
        sys.stdout.write(char)
        sys.stdout.flush()

        if in_ansi:
            if char == 'm':
                in_ansi = False
        else:
            time.sleep(delay)
            
    sys.stdout.write(end)
    sys.stdout.flush()


def get_safe_input(prompt: str = '> ') -> str:
    """
    Safely prompts user for input using try-except to catch KeyboardInterrupt 
    (Ctrl+C) and EOFError (Ctrl+D), preventing unhandled crash exceptions.
    
    Returns:
        str: Cleaned user input, or 'EXIT' if an interrupt exception occurs.
    """
    try:
        user_input = input(prompt)
        return user_input.strip()
    except (KeyboardInterrupt, EOFError):
        typewriter_print(colorize("\n[Input Interrupted] Returning to menu/exiting gracefully...", RED))
        return 'EXIT'
    except Exception as e:
        typewriter_print(colorize(f"\n[Input Error] An unexpected error occurred: {e}", RED))
        return ''


def speak(text: str):
    """
    Cross-platform Text-to-Speech function:
    - macOS: Native `say` binary (built-in)
    - Windows: Native PowerShell System.Speech / SAPI.SpVoice (built-in, zero dependencies)
    - Linux/Other: Falls back to `pyttsx3` package if installed
    """
    if not text:
        return
    
    os_name = platform.system()
    
    if os_name == 'Darwin':
        subprocess.Popen(['say', text])
    elif os_name == 'Windows':
        clean_text = text.replace("'", "''")
        cmd = f'powershell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{clean_text}\')"'
        subprocess.Popen(cmd, shell=True)
    else:
        try:
            import pyttsx3
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
        except Exception:
            pass
