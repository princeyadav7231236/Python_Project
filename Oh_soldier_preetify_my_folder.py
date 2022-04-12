import os

def soldier(path, file_name, format_type):
    i = 1
    os.chdir(path)
    files = os.listdir(path)
    with open(file_name) as f:
        a = f.read().split("\n")

    for file_name in files:
        if file_name not in a:
            os.rename(file_name, file_name.capitalize())

        if os.path.splitext(file_name)[1] == format_type:
            os.rename(file_name, f"{i}{format_type}")
            i += 1

soldier(r"C:\Users\Bansh\PycharmProjects\python_tutorials", "Dictionary_of_items", ".jpg")