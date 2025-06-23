#creates one xml per xlsx, adding 2s break between each row

import openpyxl as op
import os
import re

def process_folder(folder_path):
    # List all Excel files in the folder
    excel_files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]

    if not excel_files:
        print(f"No .xlsx files found in the folder: {folder_path}")
        return False

    # Get column selection
    while True:
        column_input = input("Enter column letter (A-Z) or number (1-based) to extract text from: ").strip().upper()
        try:
            if column_input.isalpha():
                # Convert letter to column index (0-based)
                column_index = ord(column_input) - ord('A')
            else:
                # Convert number to column index (0-based)
                column_index = int(column_input) - 1
            
            if column_index < 0:
                raise ValueError("Column must be positive")
            break
        except (ValueError, TypeError) as e:
            print(f"Invalid column input: {e}. Please try again.")

    # Get start row
    while True:
        start_row_input = input("Enter starting row number (1-based, default is 2): ").strip()
        if not start_row_input:
            start_row = 2
            break
        try:
            start_row = int(start_row_input)
            if start_row < 1:
                raise ValueError("Row must be at least 1")
            break
        except ValueError as e:
            print(f"Invalid row input: {e}. Please try again.")

    # Engine selection
    while True:
        engine_select = input("Select engine. Press '1' for Azure; press '2' for Amazon/Google: ").strip()
        if engine_select in ['1', '2']:
            break
        print("Invalid engine selection. Please choose either '1' or '2'.")

    azure_voice = ""
    if engine_select == '1':
        while True:
            azure_voice = input("Please input voice in format 'xx-XX, nameNeural' [for example: en-US, AriaNeural]: ").strip()
            if azure_voice:
                break
            print("Voice input cannot be empty.")

    azure_header1 = """<speak xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="http://www.w3.org/2001/mstts" xmlns:emo="http://www.w3.org/2009/10/emotionml" version="1.0" xml:lang="en-US"><voice name="Microsoft Server Speech Text to Speech Voice ("""
    azure_header2 = """)"><prosody rate="0%" pitch="0%">"""
    azure_footer = """</prosody></voice></speak>"""

    amazon_header = """<speak>"""
    amazon_footer = """</speak>"""

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

            for row in range(start_row, sheet.max_row + 1):
                cell_value = str(sheet.cell(row=row, column=column_index + 1).value or "").strip()
                if cell_value:
                    # Add <break time="2000ms" /> after each line
                    content_lines.append(f'{cell_value} <break time="2000ms" />')

        if not content_lines:
            print(f"No content found in column {column_input} of file {excel_file_name}. Skipping...")
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
    
    return True

def main():
    print("Welcome to XML Creator")
    print("This script creates XML files from Excel files with 2-second breaks between each row.")

    while True:
        print("\n" + "="*50)
        folder_path = input("Please enter the folder path containing the .xlsx files: ").strip()
            
        # Validate folder path
        if not os.path.exists(folder_path):
            print("Error: The specified folder path does not exist.")
            continue
            
        process_folder(folder_path)
        
        another = input("\nProcess another folder? (y/n): ").strip().lower()
        if another not in ['y', '1']:
            break

    print("\nThank you for using XML Creator!")
    input("Press Enter to exit.")

if __name__ == "__main__":
    main()