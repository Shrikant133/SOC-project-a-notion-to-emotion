from pathlib import Path

file= Path("emails")
print(file.exists())

file.mkdir()
print(file.exists())

file.rmdir()
print(file.exists())


for i in file.glob('*'):
    print(i)