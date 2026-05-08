import os
import glob
import whisper

# load Whisper large model
model = whisper.load_model("large")

# root folder containing the wav files
root_dir = "dataset"

# find all wav files recursively
wav_files = glob.glob(os.path.join(root_dir, "**", "*.wav"), recursive=True)

print(f"Found {len(wav_files)} wav files.")

for wav_path in wav_files:
    print(f"Transcribing: {wav_path}")

    # run whisper
    result = model.transcribe(wav_path, language="en")

    # transcription text
    text = result["text"].strip()

    # make a .lab path with same basename
    lab_path = os.path.splitext(wav_path)[0] + ".lab"

    # save transcription
    with open(lab_path, "w", encoding="utf-8") as f:
        f.write(text + "\n")

    print(f"Saved transcription to {lab_path}")
