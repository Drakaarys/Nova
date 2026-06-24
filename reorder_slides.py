import re

with open('ppt-finale.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Extract Market section
# We must capture from <!-- 5 · MARKET --> to </section> before Demo
market_pattern = re.compile(r'(<!-- 5 · MARKET -->\s*<section class="slide" data-section="market">.*?</section>\n+)', re.DOTALL)
market_match = market_pattern.search(text)
if not market_match:
    print("Market section not found!")
    exit(1)

market_str = market_match.group(1)

# Remove market from its current position
text = text.replace(market_str, '')

# Update numbers in Market string
market_str = market_str.replace('<!-- 5 · MARKET -->', '<!-- 3 · MARKET (Moved) -->')
market_str = market_str.replace('<span class="num">04</span>', '<span class="num">02</span>')

# 2. Find Problem section and insert Market after it
problem_pattern = re.compile(r'(<!-- 2 · PROBLEM -->\s*<section class="slide" data-section="problem">.*?</section>\n+)', re.DOTALL)
problem_match = problem_pattern.search(text)
if not problem_match:
    print("Problem section not found!")
    exit(1)

problem_str = problem_match.group(1)
text = text.replace(problem_str, problem_str + market_str)

# 3. Update Solution and Features numbering
text = text.replace('<!-- 3 · SOLUTION -->', '<!-- 4 · SOLUTION (Moved) -->')
# We need to replace only in Solution block
solution_pattern = re.compile(r'(<!-- 4 · SOLUTION \(Moved\) -->\s*<section class="slide" data-section="solution">.*?</section>\n+)', re.DOTALL)
def fix_solution(m):
    return m.group(1).replace('<span class="num">02</span>', '<span class="num">03</span>')
text = solution_pattern.sub(fix_solution, text)

text = text.replace('<!-- 4 · FEATURES -->', '<!-- 5 · FEATURES (Moved) -->')
features_pattern = re.compile(r'(<!-- 5 · FEATURES \(Moved\) -->\s*<section class="slide" data-section="features">.*?</section>\n+)', re.DOTALL)
def fix_features(m):
    return m.group(1).replace('<span class="num">03</span>', '<span class="num">04</span>')
text = features_pattern.sub(fix_features, text)

# 4. Reorder NOTES array
# Extract the notes array block
notes_pattern = re.compile(r'const NOTES = \[\s*(.*?)\s*\];', re.DOTALL)
notes_match = notes_pattern.search(text)
if notes_match:
    notes_content = notes_match.group(1)
    # Split by lines or just by ",\n"
    # Actually, they are exactly one per line, and they end with ",\n" or ""
    # We can split by lines
    lines = notes_content.strip().split('\n')
    # Strip spaces
    lines = [l.strip() for l in lines]
    
    # We expect 12 lines
    if len(lines) == 12:
        # Move index 4 to index 2
        # Title(0), Problem(1), Solution(2), Features(3), Market(4)
        market_note = lines.pop(4)
        lines.insert(2, market_note)
        
        # Add a trailing comma except for the last
        for i in range(len(lines)):
            if lines[i].endswith(','):
                lines[i] = lines[i][:-1]
        
        for i in range(len(lines)-1):
            lines[i] = '    ' + lines[i] + ','
        lines[-1] = '    ' + lines[-1]
        
        new_notes_content = '\n'.join(lines)
        text = notes_pattern.sub(f'const NOTES = [\n{new_notes_content}\n  ];', text)
    else:
        print("Notes array lines count mismatch:", len(lines))

with open('ppt-finale.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Slides reordered.")
