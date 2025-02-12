#!/usr/bin/python3
"""
module csv and json
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    data = []
    try:
        with open(csv_filename, 'r', encoding='utf-8') as csvfile:
            """
            csv reader read csv file and convert line in dictionary
            """
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                data.append(row)

        with open('data.json', "w", encoding='utf-8') as jsonfile:
            """
            Writes the data list to the JSON file using 4-space indentation
            """
            json.dump(data, jsonfile, indent=4)
            return True
    except FileNotFoundError:
        return False
