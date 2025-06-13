#creates one xml per xlsx, adding 2s break between each row

import openpyxl as op
import os

print("Welcome to XML Creator")

folder_path = input("Please enter the folder path containing the .xlsx files: ")

# Validate folder path
if not os.path.exists(folder_path):
    print("Error: The specified folder path does not exist.")
    exit(1)

# List all Excel files in the folder
excel_files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]

if not excel_files:
    print("No .xlsx files found in the specified folder.")
    exit(1)

# Engine selection
engine_select = input("Select engine. Press '1' for Azure; press '2' for Amazon/Google: ")
if engine_select not in ['1', '2']:
    print("Invalid engine selection. Please choose either '1' or '2'.")
    exit(1)

azure_voice = ""
if engine_select == '1':
    azure_voice = input("Please input voice in format 'xx-XX, nameNeural' [for example: en-US, AriaNeural]: ")

azure_header1 = """<speak xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="http://www.w3.org/2001/mstts" xmlns:emo="http://www.w3.org/2009/10/emotionml" version="1.0" xml:lang="en-US"><voice name="Microsoft Server Speech Text to Speech Voice ("""
azure_header2 = """)"><prosody rate="0%" pitch="0%">"""
azure_footer = """</prosody></voice></speak>"""

amazon_header = """<speak>"""
amazon_footer = """</speak>"""

column_index = 4  # Column E in 0-based indexing

for excel_file_name in excel_files:
    excel_file_path = os.path.join(folder_path, excel_file_name)
    try:
        wb = op.load_workbook(excel_file_path)
    except Exception as e:
        print(f"Error loading file {excel_file_name}: {e}")
        continue

    base_dir = os.path.dirname(excel_file_path)
    output_dir = base_dir  # Use the same folder as the .xlsx file

    content_lines = []
    for sheet_name in wb.sheetnames:
        sheet = wb[sheet_name]
        print(f"Processing sheet: {sheet_name} in file: {excel_file_name}")

        for row in range(2, sheet.max_row + 1):
            cell_value = str(sheet.cell(row=row, column=column_index + 1).value or "").strip()
            if cell_value:
                # Add <break time="2000ms" /> after each line
                content_lines.append(f'{cell_value} <break time="2000ms" />')

    if not content_lines:
        print(f"No content found in column E of file {excel_file_name}. Skipping...")
        continue

    content = "\n".join(content_lines)
    filename = f"{os.path.splitext(excel_file_name)[0]}.xml"
    filepath = os.path.join(output_dir, filename)

    if engine_select == '1':
        combined = f"{azure_header1}{azure_voice}{azure_header2}\n\n{content}\n{azure_footer}"
    else:
        combined = f"{amazon_header}\n\n{content}\n{amazon_footer}"

    with open(filepath, 'w', encoding="utf-8") as file:
        file.write(combined)

    print(f"Created file: {filepath}")

print("All files have been processed.")
input("Press Enter to exit.")
