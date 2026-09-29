"""
🎵 TIMESTAMP FINDER TOOL
─────────────────────────
Song sunao aur jab bhi nayi line gayi jaaye, ENTER daba do.
Yeh tool har ENTER ka timestamp print karega.
Woh timestamps copy karke song.py mein daalna.

Press ENTER to start song, then press ENTER on each lyric line.
Press Ctrl+C to stop.
"""
import time
import sys
import os

os.environ["PYTHONIOENCODING"] = "utf-8"
if sys.platform == "win32":
    os.system("chcp 65001 >nul 2>&1")
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

import pygame

SONG_START = 25  # Same as song.py

lyrics_text = [
    "Hua hain aaj pehli baar...",
    "jo aisa mujhe laga hain...",
    "Hua hain aaj pehli baar...",
    "jo aisa mujhe laga hain...",
    "Jaise kisi ne mujhe...",
    "chhua hain dil ke taar...",
    "Hua hain aaj pehli baar...",
    "--- MUSIC BREAK ---",
    "Teri nazron ne kuch aisa...",
    "jadoo kar diya...",
    "Har dhadkan mein tera hi...",
    "chehra bas gaya...",
    "Sapno mein bhi ab to tera...",
    "saaya rehta hain...",
    "Har pal tujhe sochta hain...",
    "ye dil deewana...",
    "--- MUSIC BREAK ---",
    "Hua hain aaj pehli baar...",
    "jo aisa mujhe laga hain...",
    "Jaise kisi ne mujhe...",
    "chhua hain dil ke taar...",
    "Hua hain aaj pehli baar...",
    "--- MUSIC BREAK ---",
    "Zindagi mein koi aaya hain...",
    "pehli dafa aisa...",
    "Khushiyon ka mausam laaya hain...",
    "pehli dafa aisa...",
    "Dil ko chu jaaye woh...",
    "aise baat karta hain...",
    "Hasi bhi aati hain aur...",
    "aankhein bhar aati hain...",
    "--- MUSIC BREAK ---",
    "Hua hain aaj pehli baar...",
    "jo aisa mujhe laga hain...",
    "Jaise kisi ne mujhe...",
    "chhua hain dil ke taar...",
    "Hua hain aaj pehli baar...",
]

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    song_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Hua Hain Aaj Pehli Baar.mp3")
    if not os.path.exists(song_path):
        print(f"  ❌ Song not found!")
        return

    print("=" * 55)
    print("  🎵 TIMESTAMP FINDER TOOL")
    print("=" * 55)
    print()
    print("  Song sunao aur jab line gayi jaaye tab ENTER daba do.")
    print("  Yeh har line ka SAHI timestamp record karega.")
    print()
    print(f"  Song {SONG_START}s se start hoga.")
    print()
    input("  >>> ENTER daba ke song start karo >>> ")

    pygame.mixer.init()
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play(start=SONG_START)

    start_time = time.time()
    timestamps = []

    print()
    print("  Song chal raha hai... Jab line suno tab ENTER daba do!")
    print("-" * 55)
    print()

    try:
        for i, lyric in enumerate(lyrics_text):
            input(f"  [{i+1:2d}] {lyric}  >>> ")
            elapsed = time.time() - start_time
            actual_timestamp = SONG_START + elapsed
            timestamps.append(actual_timestamp)
            print(f"       ⏱️  Timestamp: {actual_timestamp:.1f}s")
            print()

    except KeyboardInterrupt:
        pass

    pygame.mixer.music.stop()
    pygame.mixer.quit()

    print()
    print("=" * 55)
    print("  ✅ SAHI TIMESTAMPS - Yeh copy karo song.py mein:")
    print("=" * 55)
    print()

    for i, (ts, lyric) in enumerate(zip(timestamps, lyrics_text)):
        if "MUSIC BREAK" in lyric:
            print(f'        ({ts:.0f},  "", ""),')
        else:
            print(f'        ({ts:.0f},  "{lyric}", COLOR),')

    print()
    print("  ☝️  Yeh timestamps copy karke song.py mein daalna!")
    print()

if __name__ == "__main__":
    main()
