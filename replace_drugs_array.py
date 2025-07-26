import csv
import re

def generate_id(name):
    """Generate a valid ID from drug name"""
    # Remove Persian text and special characters
    id_name = re.sub(r'[^a-zA-Z0-9\s]', '', name)
    # Convert to lowercase and replace spaces with underscores
    id_name = id_name.lower().replace(' ', '_')
    # Remove extra underscores
    id_name = re.sub(r'_+', '_', id_name).strip('_')
    return id_name if id_name else 'drug_' + str(hash(name) % 10000)

def escape_quotes(text):
    """Escape single quotes in text"""
    if text is None:
        return ''
    return str(text).replace("'", "\\'")

def convert_csv_to_js_array(csv_file_path):
    """Convert CSV to JavaScript array format"""
    drugs_array = []
    
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            # Generate ID if missing or empty
            drug_id = row.get('id', '').strip()
            if not drug_id:
                drug_id = generate_id(row.get('name', ''))
            
            drug_entry = f"""    {{
      id: '{escape_quotes(drug_id)}',
      name: '{escape_quotes(row.get('name', ''))}',
      form: '{escape_quotes(row.get('form', ''))}',
      commonDose: '{escape_quotes(row.get('commonDose', ''))}',
      usage: '{escape_quotes(row.get('usage', ''))}',
      indications: '{escape_quotes(row.get('indications', ''))}',
      contraindications: '{escape_quotes(row.get('contraindications', ''))}',
      interactions: '{escape_quotes(row.get('interactions', ''))}',
      sideEffects: '{escape_quotes(row.get('sideEffects', ''))}',
      pregnancy: '{escape_quotes(row.get('pregnancy', ''))}',
      formula: '{escape_quotes(row.get('formula', ''))}',
      maxDose: '{escape_quotes(row.get('maxDose', ''))}',
      frequency: '{escape_quotes(row.get('frequency', ''))}',
      source: '{escape_quotes(row.get('source', ''))}',
      maxDaily: '{escape_quotes(row.get('maxDaily', ''))}',
      category: '{escape_quotes(row.get('category', ''))}',
      dividedDose: '{escape_quotes(row.get('dividedDose', ''))}',
    }}"""
            
            drugs_array.append(drug_entry)
    
    return drugs_array

def create_complete_drugs_array(csv_file_path, output_file):
    """Create complete drugs array for App.jsx"""
    drugs_entries = convert_csv_to_js_array(csv_file_path)
    
    complete_array = "const drugs = [\n" + ",\n".join(drugs_entries) + "\n  ];"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(complete_array)
    
    return len(drugs_entries)

if __name__ == "__main__":
    csv_file = 'final_farsi_100drugs_app_cleaned.csv'
    output_file = 'complete_drugs_array.js'
    
    count = create_complete_drugs_array(csv_file, output_file)
    print(f'تبدیل {count} دارو به فرمت JavaScript انجام شد.')
    print(f'فایل {output_file} ایجاد شد.')