import os
import re
import requests
from lxml import etree
import importlib.util
import tempfile

def fetch_and_load_python_module(url):
    """Fetch a .py file from GitHub and load it as a Python module."""
    temp_file_path = None
    try:
        response = requests.get(url)
        response.raise_for_status()

        with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as temp_file:
            temp_file.write(response.content)
            temp_file_path = temp_file.name

        spec = importlib.util.spec_from_file_location("ruleset", temp_file_path)
        ruleset_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(ruleset_module)

        return ruleset_module
    except Exception as e:
        print(f"Error loading ruleset: {e}")
        return None
    finally:
        if temp_file_path:
            try:
                os.remove(temp_file_path)
            except Exception as e:
                print(f"Error deleting temporary file: {e}")

def apply_replacements(xml_content, rules):
    """Apply regex-based replacements to the XML content."""
    for pattern, replacement, *optional in rules:
        flags = optional[0] if optional else re.IGNORECASE
        xml_content = re.sub(pattern, replacement, xml_content, flags=flags)
    return xml_content

def process_xml_file(file_path, rules):
    """Process a single XML file: apply replacements and save the changes."""
    with open(file_path, 'r', encoding='utf-8') as f:
        xml_content = f.read()

    updated_xml_content = apply_replacements(xml_content, rules)
    parser = etree.XMLParser(remove_blank_text=True)
    root = etree.XML(updated_xml_content, parser)

    with open(file_path, 'wb') as f:
        root_bytes = etree.tostring(root, encoding='utf-8', xml_declaration=False, pretty_print=False)
        f.write(root_bytes)

def process_directory(directory_path, rules):
    """Process all XML files in the given directory."""
    for filename in os.listdir(directory_path):
        if filename.endswith('.xml'):
            file_path = os.path.join(directory_path, filename)
            print(f'Processing: {file_path}')
            process_xml_file(file_path, rules)

def main():
    while True:
        directory_path = input("Enter the directory path containing XML files: ").strip()
        if not os.path.isdir(directory_path):
            print("Invalid directory. Please try again.")
            continue
        
        clients = {
            "1": {
                "name": "Icario",
                "url": "https://raw.githubusercontent.com/IWLeng/xml-creator/main/libraries/Icario/rules_library_icario.py"
            },
            "2": {
                "name": "Proofpoint",
                "url": "https://raw.githubusercontent.com/IWLeng/xml-creator/main/libraries/Proofpoint/rules_library_proofpoint.py"
            },
            "3": {
                "name": "Briljent",
                "url": "https://raw.githubusercontent.com/IWLeng/xml-creator/main/libraries/Briljent/rules_library_briljent.py"
            },
            "4": {
                "name": "Alliance Safety Council",
                "url": "https://raw.githubusercontent.com/IWLeng/xml-creator/main/libraries/Alliance_Safety_Council/rules_library_alliance_safety_council.py"
            }
        }
        
        print("Select the client you are working on:")
        for key, client in clients.items():
            print(f"{key}: {client['name']}")

        selected_client_key = input("Enter the number corresponding to the client: ").strip()
        if selected_client_key not in clients:
            print("Invalid choice. Try again.")
            continue

        selected_client = clients[selected_client_key]
        print(f"Selected client: {selected_client['name']}")

        ruleset_module = fetch_and_load_python_module(selected_client["url"])
        if not ruleset_module:
            print("Failed to load ruleset. Exiting.")
            return
        
        rule_sets = ruleset_module.rule_sets

        print("Select a rule set to apply:")
        for key, value in rule_sets.items():
            print(f"{key}: {value['name']}")

        selected_rule_set_key = input("Enter the number corresponding to your choice: ").strip()
        if selected_rule_set_key not in rule_sets:
            print("Invalid choice. Try again.")
            continue

        selected_rules = rule_sets[selected_rule_set_key]["rules"]
        process_directory(directory_path, selected_rules)
        print(f"Processing completed using the {rule_sets[selected_rule_set_key]['name']} rules for {selected_client['name']}.")
        
        repeat = input("Would you like to process another folder? (y/n): ").strip().lower()
        if repeat not in ('yes', 'y', '1'):
            break

if __name__ == '__main__':
    main()
