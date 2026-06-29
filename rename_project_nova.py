import os

def replace_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    new_text = text.replace('Amazon Now', 'Amazon NOVA')
    new_text = new_text.replace('Now Agent', 'NOVA Agent')
    new_text = new_text.replace('Now Assistant', 'NOVA Assistant')
    new_text = new_text.replace('Now backend', 'NOVA backend')
    
    if new_text != text:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_text)
        print(f"Updated {filepath}")

for root, dirs, files in os.walk('frontend/src'):
    for file in files:
        if file.endswith('.ts') or file.endswith('.tsx') or file.endswith('.css'):
            replace_in_file(os.path.join(root, file))

for root, dirs, files in os.walk('backend/src'):
    for file in files:
        if file.endswith('.ts') or file.endswith('.json'):
            replace_in_file(os.path.join(root, file))
