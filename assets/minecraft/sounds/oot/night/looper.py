from pydub import AudioSegment
import os

def concatenate_and_append(input_folder, sound_file, n_loops=20):
    # Construct the paths to the input audio files
    loop_sound_path = os.path.join(input_folder, f"{sound_file}_loop.ogg")
    fade_sound_path = os.path.join(input_folder, f"{sound_file}_fade.ogg")

    # Load the sound files
    AudioSegment.converter = "C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe"  # Specify ffmpeg executable path
    loop_sound = AudioSegment.from_file(loop_sound_path, format="ogg")
    fade_sound = AudioSegment.from_file(fade_sound_path, format="ogg")

    # Concatenate the loop sound 20 times
    concatenated_sound = loop_sound * n_loops

    # Append the fade sound at the end
    final_sound = concatenated_sound + fade_sound

    # Extract the relative folder structure from the input folder
    relative_folder = os.path.relpath(input_folder)

    # Construct the output folder path
    output_folder = os.path.join("output", relative_folder)

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Construct the output file path
    output_file = os.path.join(output_folder, sound_file + ".ogg")

    # Export the final sound to the output file
    final_sound.export(output_file, format="ogg")

# Specify the input folder containing the audio files
input_folder = os.getcwd()

# Replace "<sound>" with the actual name of your sound file
sound_file = "cicada2"

for i in range(1, 6):
    sound_file = f"cicada{i}"
    concatenate_and_append(input_folder, sound_file, 25)
