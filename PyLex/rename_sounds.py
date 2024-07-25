#!/usr/bin/env python3
import pandas as pd
import os
import glob
import openpyxl

folder_path = os.path.join("Griechisch", "rename")  # Replace with the path to the folder containing the files
prefix = "gr"
buchstaben = [chr(c) for c in range(ord('a'), ord('n')) if chr(c) != 'j']
Nummern = ["11", "12", "21", "22", "31", "32"]
nicht_vorhanden = ["f31", "i31", "k31", "k32"]

# Get a list of all files in the folder
file_list = os.listdir(folder_path)
if ".DS_Store" in file_list:
    file_list.remove(".DS_Store")
file_list.sort()
richtiger_name = []
# df = pd.DataFrame({'List of Files': file_list})
# # Export the DataFrame to an Excel file
# writer = pd.ExcelWriter('file_list.xlsx')
# df.to_excel(writer, sheet_name='File List', index=False)
# writer.save()
for nummer in Nummern:
    for buchstabe in buchstaben:
        neuer_name = buchstabe + nummer
        if neuer_name not in nicht_vorhanden:
            richtiger_name.append(neuer_name)
            nicht_vorhanden.append(neuer_name)

# Iterate over the list of files and rename each file
for i, filename in enumerate(file_list):
    # Check if the current path is a file (not a directory)
    if os.path.isfile(os.path.join(folder_path, filename)):
        # Split the file name and extension
        file_name, file_extension = os.path.splitext(filename)
        new_file_name = prefix + "_" + richtiger_name[i] + file_extension
        # Rename the file
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_file_name))

print(richtiger_name)