import os
import shutil
import glob

# Sozdat papki musik images text
# sortirovka

# print(os.getcwd())
# C:\Users\\016_ Mi_SQL_Conekter  C:\Users\aivin\PycharmProjects\pythonProject\016_ Mi_SQL_Conekter
try:
    os.mkdir('musik'),
except:
    print('ok musik')
try:
    os.mkdir('images'),
except:
    print('ok images')
try:
    os.mkdir('doks'),
except:
    print('ok doks')

sort_folder = r'needs_sorting'
#C:\\016_ Mi_SQL_Conekter\needs_sorting  ./

extention = {
    "mp3": "musik",
    "txt": "doks",
    "png": "images",
    "jpg": "images",
    "html": "doks",
}

for extention, folder_name in extention.items():
    files = glob.glob(os.path.join(sort_folder, f"*.{extention}"))
    for file in files:
        basename = os.path.basename(file)
        dst = os.path.join(folder_name,basename)
        shutil.move(file, dst)


# musik_folder = r'C:\Users\aivin\PycharmProjects\pythonProject\016_ Mi_SQL_Conekter\images'
# images_folder = r'C:\Users\aivin\PycharmProjects\pythonProject\016_ Mi_SQL_Conekter\doks'
# doks_folder = r'C:\Users\aivin\PycharmProjects\pythonProject\016_ Mi_SQL_Conekter\musik'

# for dir_path, dir_name, file_name in sort_folder:
#     print('path ',dir_path)
#     print('direkt ', dir_name)
#     print('file name ', file_name)
#
#
# print(os.environ.get('HOMEPAhs'))
#
# # os.rename()
#
# # os.path.splitext
#
# file_path = "/my/directory/filename.txt"
# directory = os.path.dirname(file_path)
# try: os.stat(directory)
# except: os.mkdir(directory)
# f = file(filename)