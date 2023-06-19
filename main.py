import pandas as pd
import os
import shutil

# read the csv file
data = pd.read_csv("names.csv")

# directory path
path = "C:\\autoo-ForDataBlogposts\\images"

for index, row in data.iterrows():
    current_name = row[0]
    new_name = row[1]

    # construct the full file path
    current_file_path = os.path.join(path, current_name)
    new_file_path = os.path.join(path, new_name)

    # rename the file
    if os.path.exists(current_file_path):
        shutil.move(current_file_path, new_file_path)
    else:
        print(f"The file {current_file_path} does not exist.")
