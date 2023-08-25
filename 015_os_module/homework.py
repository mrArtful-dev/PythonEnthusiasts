import os

files = os.walk('needs_sorting')
file_names = list(files)[0][2]

for folder in ['images', 'text', 'music']:
    if not os.path.isdir(folder):
        os.mkdir(folder)


for name in file_names:
    file_ext = os.path.splitext(name)[1]
    if file_ext in ['.png', '.jpg']:
        os.rename(f'needs_sorting/{name}', f'images/{name}')
    elif file_ext in ['.txt', '.html']:
        os.rename(f'needs_sorting/{name}', f'text/{name}')
    elif file_ext == '.mp3':
        os.rename(f'needs_sorting/{name}', f'music/{name}')
