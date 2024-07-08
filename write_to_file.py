import os


def write_text(folder_name, file_name, input):
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    path = f"{folder_name}/{file_name}"
    with open(f"{path}", "w", encoding="utf=8") as file:
        file.write(f"{input}")
