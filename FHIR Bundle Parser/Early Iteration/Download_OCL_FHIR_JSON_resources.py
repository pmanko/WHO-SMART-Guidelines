import requests
import pandas as pd
import os

# Load the Excel file containing URLs and filenames
df = pd.read_excel('Resources_to_download_save.xlsx')

# Create the target folder if it doesn't exist
target_folder = 'Measles_Terminology_OCL_download'
os.makedirs(target_folder, exist_ok=True)

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    url = row['URL']
    filename = row['Filename']

    # Fetch the content from the URL
    response = requests.get(url)

    # Save the content as JSON
    json_path = os.path.join(target_folder, f"{filename}.json")
    with open(json_path, 'w', encoding='utf-8') as json_file:
        json_file.write(response.text)

    print(f"Saved {filename}.json")