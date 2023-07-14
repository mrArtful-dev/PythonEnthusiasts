
# C:\Users\Roman\PycharmProjects\PythonEnthusiasts\007_working_with_files\text_files\tester.txt

# 007_working_with_files/text_files/tester.txt

# 'r' - read
# 'a' - append
# 'w' - write
# 'x' - create
# 'r+' - read and write


with open('text_files/python.jpg', 'rb') as file:
    with open('text_files/python_copy.jpg', 'wb') as wfile:
        chunk = 25000
        data = file.read(chunk)
        # while len(data) > 0:
        #     wfile.write(data)
        #     data = file.read(chunk)
        wfile.write(data)