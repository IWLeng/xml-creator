import os
import re
import pandas as pd
from docx import Document
from openpyxl import load_workbook

def clean_text(text):
    """Apply regex replacements to clean the extracted text."""
    text = re.sub(r"\.wav", "", text)  # Remove ".wav"
    text = re.sub(r"content key.*", "", text, flags=re.IGNORECASE)  # Remove "content key:" and everything after
    text = re.sub(r"\<.*?\>", "", text)
    return text.strip()

def extract_highlighted_text(cell):
    """Extract highlighted text from a DOCX table cell."""
    highlighted_text = []
    non_highlighted_text = []
    
    for para in cell.paragraphs:
        for run in para.runs:
            if run.font.highlight_color:  # Check if the text is highlighted
                highlighted_text.append(run.text)
            else:
                non_highlighted_text.append(run.text)
    
    highlighted = clean_text(''.join(highlighted_text))
    non_highlighted = clean_text(''.join(non_highlighted_text))
    
    return highlighted, non_highlighted

def autofit_columns(xlsx_path):
    """Auto-fit the columns in the Excel file."""
    wb = load_workbook(xlsx_path)
    ws = wb.active

    for col in ws.columns:
        max_length = 0
        col_letter = col[0].column_letter  # Get the column letter

        for cell in col:
            if cell.value:
                max_length = max(max_length, len(str(cell.value)))

        ws.column_dimensions[col_letter].width = max_length + 2  # Add some padding

    wb.save(xlsx_path)

def process_docx_to_xlsx(docx_path):
    """Extract highlighted and non-highlighted text from DOCX and save to XLSX."""
    doc = Document(docx_path)
    extracted_data = []

    for table in doc.tables:
        for row in table.rows:
            if len(row.cells) > 0:  # Ensure at least one column exists
                cell = row.cells[min(1, len(row.cells) - 1)]  # Use column 2 if available, otherwise column 1
                highlighted, non_highlighted = extract_highlighted_text(cell)
                
                if highlighted:  # Process only if there is highlighted text
                    extracted_data.append([highlighted, non_highlighted])

    if extracted_data:
        df = pd.DataFrame(extracted_data)
        xlsx_path = os.path.splitext(docx_path)[0] + ".xlsx"
        df.to_excel(xlsx_path, index=False, header=False)

        autofit_columns(xlsx_path)  # Auto-fit columns
        print(f"Saved: {xlsx_path}")
    else:
        print(f"No highlighted text found in: {docx_path}")

# Prompt user for folder path input
print("DOCX Preprocess for Icario")

folder_path = input("Enter the folder path containing DOCX files: ").strip()

if not os.path.isdir(folder_path):
    print("Invalid folder path. Exiting.")
else:
    docx_files = [f for f in os.listdir(folder_path) if f.endswith(".docx")]

    if not docx_files:
        print("No DOCX files found in the specified folder.")
    else:
        for docx_file in docx_files:
            docx_path = os.path.join(folder_path, docx_file)
            process_docx_to_xlsx(docx_path)
