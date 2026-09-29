import time
import sys
import os
import random
import json
import pygame
import logging

# --- Environment & Setup ---
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
os.environ["PYTHONIOENCODING"] = "utf-8"
if sys.platform == "win32":
    os.system("chcp 65001 >nul 2>&1")
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

# --- Config ---
SYNC_OFFSET_MS = 0  
POLL_INTERVAL = 0.03  # 30ms polling for high precision
DEBUG_MODE = False

if DEBUG_MODE:
    logging.basicConfig(
        filename="lyrics_debug.log",
        level=logging.DEBUG,
        format="%(asctime)s %(message)s"
    )

# --- Colors ---
DEEP_RED     = '\033[38;5;88m'
SOUL_PURPLE  = '\033[38;5;54m'
GOLDEN_WARM  = '\033[38;5;136m'
MIST_BLUE    = '\033[38;5;24m'
MIST_WHITE   = '\033[38;5;251m'
BOLD         = '\033[1m'
RESET        = '\033[0m'
HIGHLIGHT    = '\033[38;5;220m' # Gold/Yellow for active word
DIM_WHITE    = '\033[38;5;245m' # For upcoming words

def get_emoji(text):
    text = text.lower()
    if "aasmaan" in text: return " 🌌"
    if "jahaan" in text: return " 🌍"
    if "hum do" in text: return " 💑"
    if "sajde" in text or "ijaazat" in text: return " 🙏"
    return " ❤️"

def get_line_color(idx):
    colors = [GOLDEN_WARM, GOLDEN_WARM, MIST_BLUE, MIST_BLUE, DEEP_RED, DEEP_RED, SOUL_PURPLE, SOUL_PURPLE]
    return colors[idx % len(colors)]

def run_ishaq_code():
    os.system('cls' if os.name == 'nt' else 'clear')

    json_file = "ishaq_timestamps.json"
    if not os.path.exists(json_file):
        print(f"Error: {json_file} not found. Please wait for align_audio.py to finish.")
        sys.exit(1)

    with open(json_file, "r", encoding="utf-8") as f:
        timestamps = json.load(f)

    song_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Ishaq Karne Ki.mp3")
    if not os.path.exists(song_path):
        print(f"Error: {song_path} not found.")
        return

    pygame.mixer.init()
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()

    active_line_idx = -1
    active_word_idx = -1
    
    print(f"\n {MIST_WHITE}       ♪ Now Playing ♪{RESET}")
    print(f" {GOLDEN_WARM}       Main Likh Doon Aasmaan Par {RESET}\n\n")

    if DEBUG_MODE:
        logging.debug("Waiting for audio to reach first lyric...")

    try:
        while pygame.mixer.music.get_busy():
            # 1. READ ACTUAL AUDIO POSITION
            raw_pos_ms = pygame.mixer.music.get_pos()
            pos = raw_pos_ms - SYNC_OFFSET_MS

            # 2. FIND ACTIVE LINE
            new_line_idx = -1
            for i, line in enumerate(timestamps):
                # Using line['start'] to line['end'] might be too strict if there are gaps
                # We'll make a line active as soon as we cross its start, until the next line starts
                next_start = timestamps[i+1]['start'] if i+1 < len(timestamps) else line['end'] + 5000
                if line['start'] <= pos < next_start:
                    new_line_idx = i
                    break
            
            # Transition to a new line
            if new_line_idx != active_line_idx:
                if active_line_idx != -1:
                    # Finalize the previous line so it stays on screen cleanly
                    sys.stdout.write("\n\n")
                    sys.stdout.flush()
                
                active_line_idx = new_line_idx
                active_word_idx = -1
                
                if active_line_idx != -1:
                    line_data = timestamps[active_line_idx]
                    
                    if DEBUG_MODE:
                        mins = int(pos // 60000)
                        secs = (pos % 60000) / 1000
                        next_lyric = timestamps[active_line_idx+1]['line'] if active_line_idx+1 < len(timestamps) else 'End'
                        logging.debug(f"[AUDIO {mins:02d}:{secs:05.2f}]")
                        logging.debug(f"ACTIVE: {line_data['line']}")
                        logging.debug(f"NEXT: {next_lyric}")

            # 3. FIND ACTIVE WORD (KARAOKE)
            if active_line_idx != -1:
                line_data = timestamps[active_line_idx]
                words = line_data.get('words', [])
                
                new_word_idx = -1
                for w_idx, w in enumerate(words):
                    # Word becomes active at w['start']
                    if pos >= w['start']:
                        new_word_idx = w_idx
                        
                if new_word_idx != active_word_idx or len(words) == 0:
                    active_word_idx = new_word_idx
                    line_color = get_line_color(active_line_idx)
                    
                    # Redraw the current line in place
                    sys.stdout.write('\r\033[K') # Clear line
                    indent = " " * 8
                    sys.stdout.write(indent)
                    
                    if len(words) == 0:
                        # Fallback if no word-level timestamps exist
                        sys.stdout.write(f"{BOLD}{line_color}{line_data['line']}{RESET}")
                    else:
                        for w_idx, w in enumerate(words):
                            if w_idx == active_word_idx:
                                # Currently singing word
                                sys.stdout.write(f"{BOLD}{HIGHLIGHT}{w['text']}{RESET} ")
                            elif w_idx < active_word_idx:
                                # Already sung word
                                sys.stdout.write(f"{line_color}{w['text']}{RESET} ")
                            else:
                                # Future word
                                sys.stdout.write(f"{DIM_WHITE}{w['text']}{RESET} ")
                    
                    sys.stdout.write(get_emoji(line_data['line']))
                    sys.stdout.flush()

            time.sleep(POLL_INTERVAL)
            
    except KeyboardInterrupt:
        pass
    finally:
        if pygame.mixer.get_init():
            pygame.mixer.music.stop()
            pygame.mixer.quit()
        
        sys.stdout.write("\n\n")
        print(f" {MIST_WHITE}       ♪ Song Finished ♪{RESET}\n")

if __name__ == "__main__":
    run_ishaq_code()