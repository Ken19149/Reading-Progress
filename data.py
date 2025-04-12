import json
from pathlib import Path
import matplotlib.pyplot as plt
from datetime import datetime

def convert_md_to_json(md_path, json_path):
    with open(md_path, encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()][2:]

    books = []
    current_book = None

    for line in lines:
        if line.startswith('---'):
            if current_book:
                current_book["total_time"] = sum(
                    entry["time"] for entry in current_book["entries"] if entry["time"] is not None
                )
            current_book = None
            continue

        if not line[0].isdigit():
            current_book = {
                "title": line,
                "entries": [],
                "total_time": 0  # will update later
            }
            books.append(current_book)
            continue

        parts = line.split()

        page = int(parts[0])
        page_count = int(parts[1])
        time = None if parts[2] == "x" else int(parts[2])
        speed = round(time / page_count, 2) if time is not None and page_count > 0 else None

        entry = {
            "page": page,
            "page_count": page_count,
            "time": time,
            "date": parts[3][:4] + "-" + parts[3][4:6] + "-" + parts[3][6:],
            "start": None,
            "end": None,
            "speed": speed
        }

        if len(parts) >= 6:
            entry["start"] = parts[4][:2] + ":" + parts[4][2:]
            entry["end"] = parts[5][:2] + ":" + parts[5][2:]

        current_book["entries"].append(entry)

    # Handle last book
    if current_book:
        current_book["total_time"] = sum(
            entry["time"] for entry in current_book["entries"] if entry["time"] is not None
        )

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(books, f, ensure_ascii=False, indent=2)

    print(f"Converted and saved to {json_path}")

convert_md_to_json("output/data.md", "output/data.json")

# visualizing day-pageRead data

with open("output/data.json", "r", encoding="utf-8") as f:
    books = json.load(f)

# Flatten the data: one list of (date, page_count) across all books
dates = []
pages_read = []

for book in books:
    for entry in book["entries"]:
        if entry["date"] and entry["page_count"] != "x":
            try:
                # Convert to readable date
                dt = datetime.strptime(entry["date"], "%Y-%m-%d")
                dates.append(dt)
                pages_read.append(int(entry["page_count"]))
            except ValueError:
                continue
            
# Sort by date
sorted_data = sorted(zip(dates, pages_read))
dates, pages_read = zip(*sorted_data)

# Plot
plt.figure(figsize=(10, 5))
plt.plot(dates, pages_read, marker="o", linestyle="-", color="royalblue")
plt.title("Reading Progress (Pages per Day)")
plt.xlabel("Date")
plt.ylabel("Pages Read")
plt.grid(True)
plt.tight_layout()
plt.xticks(rotation=45)

# Save as image for README
plt.savefig("output/reading_progress.png", dpi=300)
print("Saved: reading_progress.png")