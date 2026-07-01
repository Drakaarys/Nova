import re

with open('ppt-finale.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Remove sparse class from market and scale
text = text.replace('<section class="slide sparse" data-section="market">', '<section class="slide" data-section="market">')
text = text.replace('<section class="slide sparse" data-section="scale">', '<section class="slide" data-section="scale">')

# Modify the sparse CSS block so if any slide still uses it, it doesn't break
# Let's just drastically reduce the padding and sizes in sparse CSS
new_sparse_css = """
  /* Sparse Slide Strategy: Typography & White Space */
  .sparse .card { padding: clamp(16px, 2vw, 24px); justify-content: center; align-items: center; text-align: center; font-size: 1.05em; box-shadow: var(--shadow); }
  .sparse .card .ttl { font-size: 1.1em; justify-content: center; margin-bottom: 0.8rem; text-align: center; }
  .sparse ul.clean { font-size: 1.05em; gap: 0.8rem; display: flex; flex-direction: column; align-items: center; list-style: none; padding: 0; }
  .sparse .card:hover { transform: translateY(-2px); box-shadow: var(--shadow-lg); }
  .sparse .stat { padding: clamp(16px, 2vw, 24px); justify-content: center; align-items: center; text-align: center; }
  .sparse .stat .n { font-size: clamp(32px, 3.5vw, 48px); margin-bottom: 0.2em; }
  .sparse .stat .l { font-size: 1em; max-width: 300px; line-height: 1.4; }
  .sparse p.mut { text-align: center; font-size: 1em; }
"""

sparse_regex = re.compile(r'/\* Sparse Slide Strategy: Typography & White Space \*/.*?\.sparse p\.mut \{ text-align: center; font-size: 1\.05em; \}', re.DOTALL)
text = sparse_regex.sub(new_sparse_css.strip(), text)

# Just to be sure, let's bump the default font size in the market and scale cards slightly to not look empty, 
# but keep the original grid layout which works well.
# For market:
market_pattern = re.compile(r'<section class="slide" data-section="market">.*?</section>', re.DOTALL)
def fix_market(m):
    s = m.group(0)
    s = s.replace('font-size:1.1em;', 'font-size:1.15em;')
    s = s.replace('gap:24px', 'gap:16px')
    return s
text = market_pattern.sub(fix_market, text)

scale_pattern = re.compile(r'<section class="slide" data-section="scale">.*?</section>', re.DOTALL)
def fix_scale(m):
    s = m.group(0)
    s = s.replace('gap:24px;', 'gap:12px;')
    s = s.replace('gap:16px', 'gap:12px')
    return s
text = scale_pattern.sub(fix_scale, text)


with open('ppt-finale.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Slide 4 and 9 fixed.")
