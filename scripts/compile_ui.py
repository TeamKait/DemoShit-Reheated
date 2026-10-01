import os
import subprocess

PATH = "./app/windows"

for file in os.listdir(PATH):
    if file.endswith('.ui'):
        filename_without_ext = os.path.splitext(file)[0]

        ui_path = os.path.join(PATH, f"{filename_without_ext}.ui")
        py_path = os.path.join(PATH, f"{filename_without_ext}.py")

        print(f"{file} -> {filename_without_ext}.py")
        subprocess.run(f'pyside6-uic "{ui_path}" -o "{py_path}"', shell=True)
