import sys
import json
import csv


def json_to_csv(json_file, csv_file):
    # Open the JSON file and load data
    with open(json_file, "r") as f:
        data = json.load(f)

    # Open the CSV file and create a CSV writer
    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        # Write header (assuming all objects have the same keys)
        writer.writerow(data[0].keys())

        # Write data
        for item in data:
            writer.writerow(item.values())


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <json_file>")
        sys.exit(1)

    json_file = sys.argv[1]
    csv_file = json_file.split(".")[0] + ".csv"

    json_to_csv(json_file, csv_file)
