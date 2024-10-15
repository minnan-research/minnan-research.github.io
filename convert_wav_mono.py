import os
from pydub import AudioSegment
from pydub.silence import detect_nonsilent

# Folder containing the wav files
input_folder = "audio_temp"
output_folder = "docs/mispronunciation/audio"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def convert_and_trim(input_file, output_file, silence_threshold=-50.0, silence_chunk_len=500):
    # Load the audio file
    audio = AudioSegment.from_wav(input_file)
    
    # Convert to mono if it's stereo
    if audio.channels > 1:
        audio = audio.set_channels(1)
    
    # Convert to 16-bit PCM if it's 32-bit or another format
    audio = audio.set_sample_width(2)  # 2 bytes = 16 bits
    
    # Detect nonsilent parts of the audio
    nonsilent_ranges = detect_nonsilent(audio, min_silence_len=silence_chunk_len, silence_thresh=silence_threshold)
    
    # Trim the silence
    if nonsilent_ranges:
        start_trim = nonsilent_ranges[0][0]
        end_trim = nonsilent_ranges[-1][1]
        audio = audio[start_trim:end_trim]
    
    # Export the trimmed and converted file as 16-bit mono
    audio.export(output_file, format="wav")

# Process each wav file in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".wav"):
        input_file = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder, filename)
        
        print(f"Converting and trimming {input_file} to 16-bit mono...")
        convert_and_trim(input_file, output_file)

print("Conversion and trimming complete!")
