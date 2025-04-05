import io

path = open("path", "r").read()
print(path)
data = io.open(path, "r", encoding="utf-8").read()
print(f"test{data[-1]}test")
print(data[-1]=="\n")
