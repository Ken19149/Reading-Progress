import datetime
import pyperclip
import io

# timer

print("\nReading Progress Timer Activated\n")

today = str(datetime.date.today()).split(" ")[0].replace("-","")

pageBegin = (input("input start page: "))
print(f"page begin: {pageBegin}")
start = datetime.datetime.now()
startTime = str(start).split(" ")[1].split(".")[0].replace(":","")[0:4]
print(f"start time: {start}\n")

pageEnd = (input("input end page when finish reading: "))
end = datetime.datetime.now()
endTime = str(end).split(" ")[1].split(".")[0].replace(":","")[0:4]
print(f"end time: {end}\n")

pageOffset = (input("type page offset (default=0): "))
pageCount = int(pageEnd) - int(pageBegin) + int(pageOffset)
print(f"page count: {pageCount}")

dif = (end - start)
difHour = int(str(dif).split(":")[0])
difMin = int(str(dif).split(":")[1])
difSec = float(str(dif).split(":")[2])
difFormat = (difHour * 60) + difMin
if difSec >= 30: difFormat+=1
print(f"dif: {dif}\n")

speed_ppm = pageCount/(((difHour*60*60) + (difMin*60) + difSec)/60) # pages per min
speed_mpp = 1/speed_ppm # mins per page
speed_spp = speed_mpp*60 # seconds per page
print(f"speed:\n{speed_ppm} pages/min\n{speed_mpp} mins/page\n{speed_spp} seconds/page\n")

format = f"{pageEnd} {pageCount} {difFormat} {today} {startTime} {endTime}"
pyperclip.copy(format)
print(f"Format: {format} \nCopied to Clipboard")

# stats updater

path = open("path", "r").read()
print(path)
data = io.open(path, "r", encoding="utf-8").read()
