import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import sys
import os

# Utilisez load_env pour tracer le chemin de .env:
destination = os.environ.get("destinationimportcollab")

data = pd.read_csv(destination + '\\' + sys.argv[1])
print(data)
# df = pd.DataFrame({'team': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B'],
#                    'assists': [5, 7, 7, 9, 12, 9, 9, 4],
#                    'points': [11, 8, 10, 6, 6, 5, 9, 12]})
# # default_text = 'Some Text'
# print("Original 'input.csv' CSV Data: \n")
# print(data)
# a = df.drop(['team', 'assists'], axis=1)
# print(a)
# data['Nombre de pics'] = df['points']/df['assists']

# dataFrame = pd.DataFrame.drop(labels='Last name', axis=1)
# print("\nCSV Data after deleting the column 'year':\n")
# print(dataFrame)
# print(data)
print("rrrrrrrrrrrrrr")
print("First name: " + sys.argv[1])

# with open(r'C:\ecommerce\username.csv.csv', 'r') as read_obj, \
#         open('output_1.csv', 'w', newline='') as write_obj:
#     # Create a csv.reader object from the input file object
#     csv_reader = reader(read_obj)
#     # Create a csv.writer object from the output file object
#     csv_writer = writer(write_obj)
#     # Read each row of the input csv file as list
#     for row in csv_reader:
#         # Append the default text in the row / list
#         row.append(default_text)
#         # Add the updated row / list to the output file
#         csv_writer.writerow(row)
# # import random

# def generate():
#     return random.randint(0, 9)
