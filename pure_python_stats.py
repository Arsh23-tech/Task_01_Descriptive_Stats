import csv
import math
from collections import Counter

DATA_FILE = "fb_ads_president_scored_anon.csv"


# ---------- Utility Functions ----------

def is_number(value):
    try:
        float(value)
        return True
    except:
        return False


def mean(values):
    return sum(values) / len(values)


def median(values):
    values = sorted(values)
    n = len(values)

    if n % 2 == 0:
        return (values[n//2 - 1] + values[n//2]) / 2
    else:
        return values[n//2]


def std_dev(values):
    m = mean(values)
    variance = sum((x - m) ** 2 for x in values) / len(values)
    return math.sqrt(variance)


# ---------- Load Dataset ----------

with open(DATA_FILE, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = list(reader)

rows = len(data)
columns = list(data[0].keys())

print("\nDATASET OVERVIEW")
print("-----------------")
print("Total Rows:", rows)
print("Total Columns:", len(columns))


# ---------- Missing Values ----------

print("\nMISSING VALUES")
print("-----------------")

for col in columns:
    missing = sum(1 for row in data if row[col] == "" or row[col] is None)
    print(f"{col}: {missing}")


# ---------- Column Analysis ----------

print("\nCOLUMN STATISTICS")
print("-----------------")


for col in columns:

    values = [row[col] for row in data if row[col] != "" and row[col] is not None]

    if not values:
        continue

    # Determine if numeric
    numeric_values = [float(v) for v in values if is_number(v)]

    print(f"\nColumn: {col}")

    if len(numeric_values) == len(values):

        print("Type: Numeric")
        print("Count:", len(numeric_values))
        print("Mean:", mean(numeric_values))
        print("Median:", median(numeric_values))
        print("Min:", min(numeric_values))
        print("Max:", max(numeric_values))
        print("Std Dev:", std_dev(numeric_values))

    else:

        print("Type: Categorical")

        counter = Counter(values)

        print("Count:", len(values))
        print("Unique Values:", len(counter))
        print("Mode:", counter.most_common(1)[0][0])

        print("Top 5 Most Frequent Values:")
        for value, count in counter.most_common(5):
            print(value, count)