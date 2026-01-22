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

def select_rule_set_for_folder(folder_name, rule_sets):
    """Allow user to select a rule set for a specific folder."""
    print(f"\nSelect rules for folder: {folder_name}")
    print("Available rule sets:")
    for key, value in rule_sets.items():
        print(f"{key}: {value['name']}")
    print("0: Skip this folder")
    
    while True:
        choice = input(f"Enter your choice for '{folder_name}' (0-{max(rule_sets.keys())}): ").strip()
        if choice == "0":
            return None
        elif choice in rule_sets:
            return rule_sets[choice]["rules"]
        else:
            print("Invalid choice. Please try again.")

def process_directory_with_rules(directory_path, folder_rules_mapping):
    """Process all XML files in the directory and subdirectories using folder-specific rules."""
    for root_dir, dirs, files in os.walk(directory_path):
        # Get the relative path from the main directory
        rel_path = os.path.relpath(root_dir, directory_path)
        
        # If this folder has rules assigned, process it
        if rel_path in folder_rules_mapping:
            rules = folder_rules_mapping[rel_path]
            if rules:  # Skip if rules is None (folder was skipped)
                print(f"\nProcessing folder: {rel_path} (or root)")
                for filename in files:
                    if filename.endswith('.xml'):
                        file_path = os.path.join(root_dir, filename)
                        print(f'  Processing: {file_path}')
                        process_xml_file(file_path, rules)

def get_all_subfolders(directory_path):
    """Get all subfolders (including root) recursively."""
    folders = ["."]  # Root folder represented as "."
    
    for root_dir, dirs, files in os.walk(directory_path):
        rel_path = os.path.relpath(root_dir, directory_path)
        if rel_path != ".":  # Don't add root again
            folders.append(rel_path)
    
    return sorted(folders)

def select_client():
    """Prompt user to select a client and load their ruleset."""
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
        },
        "5": {
            "name": "Insight",
            "url": "https://raw.githubusercontent.com/IWLeng/xml-creator/main/libraries/Insight/rules_library_insight.py"
        },
        "6": {
            "name": "Ohio State University",
            "url": "https://raw.githubusercontent.com/IWLeng/xml-creator/main/libraries/Ohio_State_University/rules_library_OSU.py"
        },
        "7": {
            "name": "PPG",
            "url": "https://raw.githubusercontent.com/IWLeng/xml-creator/main/libraries/PPG/rules_library_ppg.py"
        },
        "8": {
            "name": "Private Health Management",
            "url": "https://raw.githubusercontent.com/IWLeng/xml-creator/main/libraries/Private_Health_Management/rules_library_private_health_management.py"
        },
        "9": {
            "name": "Alcoa",
            "url": "https://raw.githubusercontent.com/IWLeng/xml-creator/main/libraries/Alcoa/rules_library_alcoa.py"
        },
        "10": {
            "name": "Fanatics",
            "url": "https://raw.githubusercontent.com/IWLeng/xml-creator/main/libraries/Fanatics/rules_library_fanatics.py"
        },
        "11": {
            "name": "Shipco",
            "url": "https://raw.githubusercontent.com/IWLeng/xml-creator/main/libraries/Shipco/rules_library_shipco.py"
        },
        "12": {
            "name": "Burkle",
            "url": "https://raw.githubusercontent.com/IWLeng/xml-creator/main/libraries/Burkle/rules_library_burkle.py"
        },
        "13": {
            "name": "Hyatt",
            "url": "https://raw.githubusercontent.com/IWLeng/xml-creator/main/libraries/Hyatt/rules_library_hyatt.py"
        },
        "14": {
            "name": "Caterpillar",
            "url": "https://raw.githubusercontent.com/IWLeng/xml-creator/main/libraries/Caterpillar/rules_library_caterpillar.py"
        }
    }
    
    print("Select the client you are working on:")
    for key, client in clients.items():
        print(f"{key}: {client['name']}")

    while True:
        selected_client_key = input("Enter the number corresponding to the client: ").strip()
        if selected_client_key in clients:
            selected_client = clients[selected_client_key]
            print(f"Selected client: {selected_client['name']}")
            return selected_client
        else:
            print("Invalid choice. Try again.")

def main():
    # Step 1: Select client (once for the entire run)
    selected_client = select_client()
    
    # Load the client's ruleset
    ruleset_module = fetch_and_load_python_module(selected_client["url"])
    if not ruleset_module:
        print("Failed to load ruleset. Exiting.")
        return
    
    rule_sets = ruleset_module.rule_sets
    
    while True:
        # Step 2: Get the main folder path
        while True:
            directory_path = input("\nEnter the main directory path containing XML files: ").strip()
            if os.path.isdir(directory_path):
                break
            else:
                print("Invalid directory. Please try again.")
        
        # Step 3: Get all subfolders (including root)
        folders = get_all_subfolders(directory_path)
        print(f"\nFound {len(folders)} folders (including root):")
        for i, folder in enumerate(folders, 1):
            print(f"{i}. {folder if folder != '.' else 'Root folder'}")
        
        # Step 4: Select rules for each folder
        folder_rules_mapping = {}
        print("\n" + "="*50)
        print("Configure rules for each folder:")
        print("="*50)
        
        for folder in folders:
            rules = select_rule_set_for_folder(folder if folder != '.' else 'Root folder', rule_sets)
            folder_rules_mapping[folder] = rules
        
        # Step 5: Show configuration summary
        print("\n" + "="*50)
        print("Configuration Summary:")
        print("="*50)
        print(f"Client: {selected_client['name']}")
        print("Folder rules assignment:")
        
        folders_to_process = 0
        for folder, rules in folder_rules_mapping.items():
            if rules:
                rule_name = "Unknown"
                for key, rule_set in rule_sets.items():
                    if rule_set["rules"] == rules:
                        rule_name = rule_set["name"]
                        break
                print(f"  {folder if folder != '.' else 'Root folder'}: {rule_name}")
                folders_to_process += 1
        
        if folders_to_process == 0:
            print("No folders selected for processing. Skipping...")
            continue
        
        # Step 6: Confirm and process
        confirm = input(f"\nProcess {folders_to_process} folder(s) with the above configuration? (y/n): ").strip().lower()
        if confirm in ('y', 'yes'):
            process_directory_with_rules(directory_path, folder_rules_mapping)
            print(f"\nProcessing completed for {selected_client['name']}!")
        
        # Step 7: Ask if user wants to process another folder with the same client
        repeat = input("\nWould you like to process another folder with the same client? (y/n): ").strip().lower()
        if repeat not in ('y', 'yes'):
            print(f"Thank you for using the XML processor with {selected_client['name']}!")
            break

if __name__ == '__main__':
    main()