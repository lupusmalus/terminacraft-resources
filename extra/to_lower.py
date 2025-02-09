from pathlib import Path
import os


path = Path(__file__).parent.parent.absolute().joinpath('assets')
files = os.listdir(path)

for pardir, dirs, files in os.walk(path):
    os.chdir(pardir)
    for file in files:
        os.rename(file, file.lower())


for _, dirname, files in os.walk(path):
    print(files)