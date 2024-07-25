#!/usr/bin/env python3
import pandas as pd
import os
import glob
import openpyxl

nummern = [range(1,55)]
stored = pd.DataFrame(nummern)
#print(stored)
language_list = os.listdir("sound_files")
exclude = [".DS_Store"] #exclude certain languages from being used (if for example not all sound files are present)
language_list = [x for x in language_list if x not in exclude]
language_list = sorted(language_list) #sort list alphabatically

age = ["2","3","4"]
standard = ["std", "other"]
for language in language_list:
    for thisstandard in standard:
        for thisage in age:
            not_found = []
            liste = "age" + thisage + "_" + thisstandard + ".xlsx"
            filename = str(os.path.join("trial_lists", liste))

            # Specify folder path and xlsx file name
            folder_path = os.path.join("sound_files", language)
            xlsx_file = filename

            # Read xlsx file and extract names from specified column
            df = pd.read_excel(xlsx_file)
            df= df.sort_values("sound_file")
            names = df.iloc[:, 0].apply(lambda x: str(x) + ".wav").tolist()


            # Check if folder contains files with specified names
            for name in names:
                if not glob.glob(os.path.join(folder_path, "??_" + name)):
                    # print(f"{name} not found in folder.")
                    if not_found.count(name) == 0:
                        not_found.append(f"{name}")
    #check for familiarization
    familiarization_files = ["hund", "apfel", "w_i_hund", "w_i_apfel"]
    for fam in familiarization_files:
        if not glob.glob(os.path.join(folder_path, "??_" + fam + ".wav")):
            not_found.append(f"{fam}")

    vector_length = len(not_found)
    zeros_to_add = 54 - vector_length
    not_found += [0] * zeros_to_add
    #print(vector_length)


    stored.loc[language] = not_found
stored = stored.iloc[1:]
excel_name = "Missing_sounds.xlsx"
stored.to_excel(excel_name)


#check pictures
nummern = [range(1,51)]
stored = pd.DataFrame(nummern)
for thisage in age:
    for thisstandard in standard:      
        not_found = []
        liste = "age" + thisage + "_" + thisstandard + ".xlsx"
        filename = str(os.path.join("trial_lists", liste))

        # Specify folder path and xlsx file name
        folder_path = os.path.join("pictures")
        xlsx_file = filename

        # Read xlsx file and extract names from specified column
        df = pd.read_excel(xlsx_file)
        df= df.sort_values("sound_file")
        names = df.iloc[:, 1].apply(lambda x: str(x) + ".jpg").tolist()
 
    # Check if folder contains files with specified names
        for name in names:
            if not glob.glob(os.path.join(folder_path, name)):
                # print(f"{name} not found in folder.")
                if not_found.count(name) == 0:
                    not_found.append(f"{name}")

        vector_length = len(not_found)
        zeros_to_add = 50 - vector_length
        not_found += [0] * zeros_to_add
        stored.loc[thisage + "_" +thisstandard] = not_found

stored = stored.iloc[1:]
excel_name = "Missing_picture.xlsx"
stored.to_excel(excel_name)