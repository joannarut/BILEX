#!/usr/bin/env python3
import pandas as pd
import os
import glob
import openpyxl

folder_path = os.path.join("Mandarin", "cut")  # Replace with the path to the folder containing the files
prefix = "ma"
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

richtiger_name.extend(["w_i_apfel", "apfel", "w_i_hund", "hund"])
print(richtiger_name)
i = 10
for name in richtiger_name:
    dateiname = prefix + "_" + name + ".wav"
    new_file_name = dateiname
    for dateiname in file_list:
        print(dateiname)
        if name in dateiname:
            os.rename(os.path.join(folder_path, dateiname), os.path.join(folder_path, new_file_name))
            #print(new_file_name)
            i = i + 1




#print(file_list)