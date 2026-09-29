import time
import sys
import os
import random

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
os.environ["PYTHONIOENCODING"] = "utf-8"
if sys.platform == "win32":
    os.system("chcp 65001 >nul 2>&1")
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

import pygame

DEEP_ROSE    = '\033[38;5;204m'
SOFT_GOLD    = '\033[38;5;180m'
SOUL_PURPLE  = '\033[38;5;134m'
MIST_BLUE    = '\033[38;5;110m'
MIST_WHITE   = '\033[38;5;251m'
BOLD         = '\033[1m'
RESET        = '\033[0m'

def soulful_typing(text, color):
    for char in text:
        sys.stdout.write(f"{BOLD}{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(0.078)

def run_song():
    os.system('cls' if os.name == 'nt' else 'clear')

    # ─── Play Audio ───
    song_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Hua Hain Aaj Pehli Baar.mp3")
    if os.path.exists(song_path):
        pygame.mixer.init()
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play(start=32)

    print(f"\n {MIST_WHITE}  🌸  Hua hain aaj pehli baar...{RESET}")
    time.sleep(1.7)
    print(f" {SOFT_GOLD}  🎶 Hua Hain Aaj Pehli Baar {RESET}\n")
    time.sleep(1.3)

    lyrics = [
        ("Hua hain aaj pehli baar...", SOFT_GOLD),
        ("jo aisa mujhe laga hain...", SOFT_GOLD),
        ("Hua hain aaj pehli baar...", MIST_BLUE),
        ("jo aisa mujhe laga hain...", MIST_BLUE),
        ("Jaise kisi ne mujhe...", SOUL_PURPLE),
        ("chhua hain dil ke taar...", SOUL_PURPLE),
        ("Hua hain aaj pehli baar...", SOFT_GOLD),
        ("Teri nazron ne kuch aisa...", DEEP_ROSE),
        ("jadoo kar diya...", DEEP_ROSE),
        ("Har dhadkan mein tera hi...", SOUL_PURPLE),
        ("chehra bas gaya...", SOUL_PURPLE),
        ("Sapno mein bhi ab to tera...", MIST_BLUE),
        ("saaya rehta hain...", MIST_BLUE),
        ("Har pal tujhe sochta hain...", DEEP_ROSE),
        ("ye dil deewana...", DEEP_ROSE),
        ("Hua hain aaj pehli baar...", SOFT_GOLD),
        ("jo aisa mujhe laga hain...", SOFT_GOLD),
        ("Jaise kisi ne mujhe...", MIST_BLUE),
        ("chhua hain dil ke taar...", MIST_BLUE),
        ("Hua hain aaj pehli baar...", SOFT_GOLD),
        ("Zindagi mein koi aaya hain...", DEEP_ROSE),
        ("pehli dafa aisa...", DEEP_ROSE),
        ("Khushiyon ka mausam laaya hain...", SOUL_PURPLE),
        ("pehli dafa aisa...", SOUL_PURPLE),
        ("Dil ko chu jaaye woh...", MIST_BLUE),
        ("aise baat karta hain...", MIST_BLUE),
        ("Hasi bhi aati hain aur...", DEEP_ROSE),
        ("aankhein bhar aati hain...", DEEP_ROSE),
        ("Hua hain aaj pehli baar...", SOFT_GOLD),
        ("jo aisa mujhe laga hain...", SOFT_GOLD),
        ("Jaise kisi ne mujhe...", MIST_BLUE),
        ("chhua hain dil ke taar...", MIST_BLUE),
        ("Hua hain aaj pehli baar...", SOFT_GOLD),
    ]

    for line, color in lyrics:
        indent = " " * random.randint(3, 14)
        sys.stdout.write(indent)

        soulful_typing(line, color)

        if "pehli baar" in line.lower():
            sys.stdout.write(" 🌸")
        elif "dil" in line.lower():
            sys.stdout.write(" 💕")
        elif "nazron" in line.lower() or "jadoo" in line.lower():
            sys.stdout.write(" 🪄")
        elif "sapno" in line.lower() or "saaya" in line.lower():
            sys.stdout.write(" 🌙")
        elif "khushiyon" in line.lower() or "hasi" in line.lower():
            sys.stdout.write(" 😊")
        elif "aankhein" in line.lower():
            sys.stdout.write(" 🥹")
        elif "zindagi" in line.lower():
            sys.stdout.write(" 🦋")
        elif "dhadkan" in line.lower() or "chehra" in line.lower():
            sys.stdout.write(" 💓")
        else:
            sys.stdout.write(" ✨")

        print("\n")
        time.sleep(1.6)

    print(f"\n {BOLD}{SOFT_GOLD}    [ Hua hain aaj pehli baar... 🌸 ]{RESET}")
    print(f" {MIST_WHITE}    Jaise kisi ne chhua hain dil ke taar...{RESET}\n")

    if pygame.mixer.get_init():
        pygame.mixer.music.stop()
        pygame.mixer.quit()

if __name__ == "__main__":
    run_song()
