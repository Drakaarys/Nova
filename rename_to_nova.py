import re

def replace_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Custom tweaks for better flow
    text = text.replace("What Now Agent?", "What is Nova?")
    
    # Generic replacements
    text = re.sub(r'\bthe Now Agent\b', 'Nova', text, flags=re.IGNORECASE)
    text = re.sub(r'\bNow Agent\b', 'Nova', text, flags=re.IGNORECASE)
    
    # In slide 1, there's "Amazon Now conversational agent"
    text = text.replace("Amazon Now conversational agent", "Nova, our conversational AI")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

replace_in_file('ppt-finale.html')
replace_in_file(r'C:\Users\visha\.gemini\antigravity-ide\brain\16adb843-7698-43f6-a2d9-28e69297c87a\presentation_script.md')

print("Renamed 'Now Agent' to 'Nova' across files.")
