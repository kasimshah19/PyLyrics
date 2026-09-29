import os
import sys
import json
import warnings
import whisper

# Suppress warnings
warnings.filterwarnings("ignore")

# Add current directory to PATH so whisper finds ffmpeg.exe
os.environ["PATH"] += os.pathsep + os.path.dirname(os.path.abspath(__file__))

def align_song(song_path, output_json):
    print(f"Loading Whisper model (base)... This might take a minute.")
    model = whisper.load_model("base")

    print(f"Aligning {song_path}...")
    print("This will extract exact word-level and line-level timestamps.")
    
    # Transcribe with word-level timestamps and initial prompt
    initial_text = "Main likh doon aasmaan par ye... ke padh lega jahaan saara..."
    result = model.transcribe(song_path, word_timestamps=True, language="hi", initial_prompt=initial_text)
    
    formatted_data = []
    
    for segment in result["segments"]:
        line_text = segment["text"].strip()
        line_start = segment["start"] * 1000  # Convert to ms
        line_end = segment["end"] * 1000
        
        words = []
        if "words" in segment:
            for w in segment["words"]:
                words.append({
                    "text": w["word"].strip(),
                    "start": w["start"] * 1000,
                    "end": w["end"] * 1000
                })
        
        formatted_data.append({
            "line": line_text,
            "start": line_start,
            "end": line_end,
            "words": words
        })

    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(formatted_data, f, indent=4, ensure_ascii=False)
        
    print(f"\nAlignment complete! Timestamps saved to {output_json}")

if __name__ == "__main__":
    song_file = "Ishaq Karne Ki.mp3"
    json_file = "ishaq_timestamps.json"
    
    if not os.path.exists(song_file):
        print(f"Error: Could not find {song_file}")
        sys.exit(1)
        
    align_song(song_file, json_file)
