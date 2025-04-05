import io

path = open("path", "r").read()
print(path)
data = io.open(path, "r", encoding="utf-8").read()
print(data)