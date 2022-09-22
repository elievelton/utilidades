import os
from pathlib2 import Path

all_files = open("musica_juntos.txt", "w+")


for root, dirs, files in os.walk("./sons"):
    for name in files:
        fileContent = Path(root, name).read_text()
        all_files.write(fileContent + '\n')

all_files.close()
print("juntou os textos com sucesso!")