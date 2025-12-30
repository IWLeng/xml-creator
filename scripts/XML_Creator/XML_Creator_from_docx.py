#!/usr/bin/env python3
"""
DOCX to XML Converter - User Friendly Version
Converts DOCX files to XML using Azure or Amazon TTS templates
"""

import os
import sys
from pathlib import Path
from docx import Document
from xml.dom import minidom

def extract_text_from_docx(docx_path):
    """Extract plain text from DOCX file"""
    try:
        doc = Document(docx_path)
        full_text = []
        
        for paragraph in doc.paragraphs:
            text = paragraph.text.strip()
            if text:  # Only add non-empty paragraphs
                full_text.append(text)
        
        # Join paragraphs with newlines
        return "\n\n".join(full_text)
    
    except Exception as e:
        print(f"Error reading {docx_path}: {e}")
        return ""

def create_azure_xml(content, voice):
    """Create XML using Azure template"""
    azure_template = """<speak xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="http://www.w3.org/2001/mstts" xmlns:emo="http://www.w3.org/2009/10/emotionml" version="1.0" xml:lang="en-US"><voice name="Microsoft Server Speech Text to Speech Voice ({voice})"><prosody rate="-5%" pitch="0%"><mstts:silence type="Sentenceboundary" value="200ms"/>\n\n{content}\n<mstts:silence type="Tailing" value="200ms"/></prosody></voice></speak>"""
    
    # Clean and prepare content
    cleaned_content = content.strip()
    
    # Apply template
    xml_content = azure_template.format(voice=voice, content=cleaned_content)
    
    # Pretty print the XML
    return pretty_print_xml(xml_content)

def create_amazon_xml(content):
    """Create XML using Amazon template"""
    amazon_template = """<speak><prosody rate="95%">\n\n{content}\n</prosody></speak>"""
    
    # Clean and prepare content
    cleaned_content = content.strip()
    
    # Apply template
    xml_content = amazon_template.format(content=cleaned_content)
    
    # Pretty print the XML
    return pretty_print_xml(xml_content)

def pretty_print_xml(xml_string):
    """Format XML string to be human-readable"""
    try:
        # Parse the XML string
        parsed = minidom.parseString(xml_string)
        
        # Pretty print with indentation
        pretty_xml = parsed.toprettyxml(indent="  ")
        
        # Remove excessive newlines from minidom's output
        lines = pretty_xml.split('\n')
        non_empty_lines = [line for line in lines if line.strip()]
        
        # Join with single newline
        return '\n'.join(non_empty_lines)
    
    except Exception as e:
        print(f"Warning: Could not pretty print XML: {e}")
        return xml_string

def process_docx_file(docx_path, engine_select, azure_voice=None):
    """Process a single DOCX file and save XML"""
    try:
        # Extract text from DOCX
        print(f"  Processing: {os.path.basename(docx_path)}")
        content = extract_text_from_docx(docx_path)
        
        if not content:
            print(f"    Warning: No text content found")
            return False
        
        # Create XML based on engine
        if engine_select == 1:  # Azure
            xml_content = create_azure_xml(content, azure_voice)
        else:  # Amazon/Google
            xml_content = create_amazon_xml(content)
        
        # Create output filename (same name, .xml extension)
        output_filename = os.path.splitext(docx_path)[0] + '.xml'
        
        # Save XML file
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(xml_content)
        
        print(f"    Created: {os.path.basename(output_filename)}")
        return True
        
    except Exception as e:
        print(f"    Error: {e}")
        return False

def main():
    """Main interactive function"""
    print("=" * 50)
    print("Welcome to DOCX to XML Creator")
    print("=" * 50)
    
    # Check if python-docx is installed
    try:
        from docx import Document
    except ImportError:
        print("\nError: Required library 'python-docx' not found!")
        print("Please install it by running: pip install python-docx")
        input("\nPress Enter to exit...")
        sys.exit(1)
    
    while True:
        print("\n" + "=" * 50)
        
        # Get directory path
        directory_path = input("\nPlease enter the directory containing the DOCX files: ").strip()
        
        # Validate directory
        if not os.path.exists(directory_path):
            print(f"Error: Directory '{directory_path}' does not exist!")
            continue
        
        if not os.path.isdir(directory_path):
            print(f"Error: '{directory_path}' is not a directory!")
            continue
        
        # Engine selection
        print("\nSelect TTS engine:")
        print("  1. Azure")
        print("  2. Amazon/Google")
        
        while True:
            try:
                engine_select = int(input("\nYour choice (1 or 2): "))
                if engine_select in [1, 2]:
                    break
                else:
                    print("Please enter 1 or 2")
            except ValueError:
                print("Please enter a number (1 or 2)")
        
        # Azure voice input if needed
        azure_voice = None
        if engine_select == 1:
            print("\nAzure Voice Format: 'xx-XX, NameNeural'")
            print("Examples: 'en-US, AriaNeural', 'de-DE, KatjaNeural'")
            azure_voice = input("Please input voice: ").strip()
            
            if not azure_voice:
                print("Warning: No voice specified, using default format")
                azure_voice = "en-US, AriaNeural"
        
        print("\n" + "-" * 50)
        print(f"Processing files in: {directory_path}")
        print(f"Engine: {'Azure' if engine_select == 1 else 'Amazon/Google'}")
        if engine_select == 1:
            print(f"Voice: {azure_voice}")
        print("-" * 50)
        
        # Find all DOCX files
        docx_files = []
        for file_name in os.listdir(directory_path):
            if file_name.lower().endswith('.docx'):
                file_path = os.path.join(directory_path, file_name)
                docx_files.append(file_path)
        
        if not docx_files:
            print(f"No DOCX files found in '{directory_path}'")
            continue
        
        print(f"Found {len(docx_files)} DOCX file(s):")
        for file_path in docx_files:
            print(f"  • {os.path.basename(file_path)}")
        
        # Process files
        success_count = 0
        for file_path in docx_files:
            if process_docx_file(file_path, engine_select, azure_voice):
                success_count += 1
        
        print(f"\n✓ Successfully processed {success_count}/{len(docx_files)} files")
        print(f"  XML files saved in: {directory_path}")
        
        # Ask to process another folder
        print("\n" + "-" * 50)
        another = input("\nProcess another folder? (y/n): ").strip().lower()
        if another not in ['y', 'yes']:
            break
    
    print("\n" + "=" * 50)
    print("Thank you for using DOCX to XML Creator!")
    print("=" * 50)
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()