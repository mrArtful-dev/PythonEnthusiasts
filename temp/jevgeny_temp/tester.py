import os
import shutil

source_folder = r'needs_sorting'

music_folder = r'needs_sorting\music'
images_folder = r'needs_sorting\pictures'
text_folder = r'needs_sorting\text'

for filename in os.listdir(source_folder):
    source_file = os.path.join(source_folder, filename)
    if os.path.isfile(source_file):
        file_extension = os.path.splitext(filename)[1].lower()
        if file_extension in ('.mp3'):
            destination_folder = music_folder
        elif file_extension in ('.jpg', '.png'):
            destination_folder = images_folder
        elif file_extension in ('.txt', '.docx'):
            destination_folder = text_folder
        else:
            destination_folder = source_folder

        destination_file = os.path.join(destination_folder, filename)
        shutil.move(source_file, destination_file)
        print(f"File '{filename}' moved to '{destination_folder}'")

print("Sorting completed!")