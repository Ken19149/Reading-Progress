import datetime
import pyperclip

today = str(datetime.date.today()).split(" ")[0].replace("-","")

input("press enter to start: ")
start = datetime.datetime.now()
startTime = str(start).split(" ")[1].split(".")[0].replace(":","")[0:4]
print(f"start time: {start}\n")

input("press enter again to pause: ")
end = datetime.datetime.now()
endTime = str(end).split(" ")[1].split(".")[0].replace(":","")[0:4]
print(f"end time: {end}\n")

dif = (end - start)
difMin = (int(str(dif).split(":")[0]) * 60) + int(str(dif).split(":")[1])
difSec = float(str(dif).split(":")[2])
if difSec >= 30: difMin+=1

print(f"dif: {dif}\n")
format = f"{difMin} {today} {startTime} {endTime}"
pyperclip.copy(format)
print(f"Format: {format} \nCopied to Clipboard")