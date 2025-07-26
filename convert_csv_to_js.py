import csv
import json
import re

def generate_id(name):
    """Generate a valid ID from drug name"""
    # Remove special characters and convert to lowercase
    id_name = re.sub(r'[^a-zA-Z0-9\s]', '', name.lower())
    # Replace spaces with underscores
    id_name = re.sub(r'\s+', '_', id_name.strip())
    # Remove non-ASCII characters
    id_name = ''.join(char for char in id_name if ord(char) < 128)
    return id_name if id_name else 'unknown_drug'

def convert_csv_to_js_array():
    drugs = []
    
    with open('final_farsi_100drugs_app_cleaned.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            # Skip empty rows
            if not row['name']:
                continue
            
            # Generate ID if missing
            drug_id = row['id'] if row['id'] else generate_id(row['name'])
                
            drug = {
                'id': drug_id,
                'name': row['name'],
                'form': row['form'],
                'commonDose': row['commonDose'],
                'usage': row['usage'],
                'indications': row['indications'],
                'contraindications': row['contraindications'],
                'interactions': row['interactions'],
                'sideEffects': row['sideEffects'],
                'pregnancy': row['pregnancy'],
                'formula': row['formula'],
                'maxDose': row['maxDose'],
                'frequency': row['frequency'],
                'source': row['source'],
                'maxDaily': row['maxDaily'],
                'category': row['category'],
                'dividedDose': row['dividedDose']
            }
            drugs.append(drug)
    
    # Generate JavaScript array format
    js_content = "const drugs = [\n"
    
    for i, drug in enumerate(drugs):
        js_content += "    {\n"
        for key, value in drug.items():
            # Escape single quotes in values
            escaped_value = str(value).replace("'", "\\'")
            js_content += f"      {key}: '{escaped_value}',\n"
        js_content += "    }"
        if i < len(drugs) - 1:
            js_content += ","
        js_content += "\n"
    
    js_content += "  ];\n"
    
    # Write to file
    with open('drugs_array_fixed.js', 'w', encoding='utf-8') as f:
        f.write(js_content)
    
    print(f"تبدیل {len(drugs)} دارو به فرمت JavaScript انجام شد.")
    print("فایل drugs_array_fixed.js ایجاد شد.")
    
    # Also create a list of drug IDs for calculateDosage function
    drug_ids = [drug['id'] for drug in drugs]
    with open('drug_ids.txt', 'w', encoding='utf-8') as f:
        for drug_id in drug_ids:
            f.write(f"'{drug_id}',\n")
    
    print("فایل drug_ids.txt نیز ایجاد شد.")

if __name__ == "__main__":
    convert_csv_to_js_array()