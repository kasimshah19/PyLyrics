# 🎶 PyLyrics: Audio-Synced Terminal Lyrics Player

**PyLyrics** is an elegant, high-precision, terminal-based lyrics player written in Python. Instead of relying on flawed, drift-prone timers (`time.sleep`), it uses the **Audio Master Clock Architecture** to ensure that what you see on the screen is *exactly* what the singer is singing at that very millisecond.

---

## 📖 The Vibe (About)
*Because music isn't just heard, it's felt.*

PyLyrics was born out of the love for those late-night coding sessions where the terminal is your only companion, and a song hits just right. It transforms your cold command line into a soulful, synchronized karaoke experience. The lyrics don't just print—they breathe with the audio, fading in and highlighting word by word, exactly as the artist sings them. 

No messy logs, no out-of-sync lines. Just you, your favorite track, and the poetry of music beautifully painted across your terminal.

---
## 🌟 Features

- **Master Clock Synchronization**: UI updates are tightly bound to the exact audio position (`pygame.mixer.music.get_pos()`), ensuring 100% accuracy with zero drift over long playback sessions.
- **Word-Level Karaoke Highlighting**: Future words are dimmed, past words get colored, and the currently spoken word is highlighted in a vibrant gold.
- **In-Place Terminal Rendering**: Flawless command-line UI using ANSI escape sequences. New lines don't spam the terminal; it redraws active text seamlessly in place.
- **Clean Aesthetic UI**: Emojis, custom colors (Soul Purple, Deep Red, Golden Warm), and elegant whitespace mimic a premium music player in your terminal.
- **AI-Powered Timestamps**: Includes a script (`align_audio.py`) leveraging OpenAI's Whisper model to auto-generate timestamp JSON files for your songs.
- **Debug Mode**: A clean production UI by default. Set `DEBUG_MODE = True` in `ishaq.py` to pipe all synchronization logs to `lyrics_debug.log` without destroying the visual layout.

---

## 🛠️ Architecture

Instead of the common mistake of making the UI delay logic control the music, **PyLyrics inverses the control**:

```
Audio Playback Position (Pygame)
       ↓
Fetch Current Timestamp in MS
       ↓
Determine Active Line / Active Word from JSON
       ↓
Redraw Terminal Line (In-Place)
```

This guarantees lyrics will never fall out of sync, even if the system stutters.

---

## 🚀 Getting Started

### 1. Requirements

Make sure you have Python 3 installed. Install the dependencies:
```bash
pip install pygame
```
*(If you plan to auto-generate timestamps, you will also need `openai-whisper` and `torch`)*

### 2. Run the Player

Play the default song by executing:
```bash
python ishaq.py
```
*(Ensure `Ishaq Karne Ki.mp3` and `ishaq_timestamps.json` are in the same folder)*

### 3. Add Your Own Songs

1. Place your MP3 file in the project directory.
2. Update the `song_path` in the code.
3. Create a JSON file (e.g., `timestamps.json`) with your lyrics and their exact start/end times in milliseconds.
4. Enjoy your custom synced karaoke!

---

## 📝 Timestamp JSON Format

PyLyrics reads lyrics and timing metadata from a structured JSON file:
```json
[
    {
        "line": "Main likh doon aasmaan par ye...",
        "start": 5000,
        "end": 8000,
        "words": [
             {"text": "Main", "start": 5000, "end": 5500},
             {"text": "likh", "start": 5500, "end": 6000}
        ]
    }
]
```

---
*Created by [Kasim Shah](https://github.com/kasimshah19)*
