import re

with open('ppt-finale.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix Slide 3 (Solution)
# Change gap:2rem to gap:1rem
text = text.replace('<div class="grow col center" style="gap:2rem">', '<div class="grow col center" style="gap:1rem">')
# Change padding 24px and font size 2.8em in center card
text = text.replace('style="flex:0 0 auto;text-align:center; padding:24px;"', 'style="flex:0 0 auto;text-align:center; padding:16px;"')
text = text.replace('<div style="font-size:2.8em">✦</div>', '<div style="font-size:2em">✦</div>')
text = text.replace('style="font-weight:800;font-size:1.4em; margin-bottom:8px;"', 'style="font-weight:800;font-size:1.2em; margin-bottom:4px;"')
text = text.replace('style="width:100%; margin-top:1rem;"', 'style="width:100%; margin-top:0.5rem;"')
# Reduce padding in the small soft cards
text = text.replace('style="padding:14px 18px; font-weight:600;"', 'style="padding:10px 14px; font-weight:600;"')

# Fix Slide 4 (Features)
# Remove sparse class
text = text.replace('<section class="slide sparse" data-section="features">', '<section class="slide" data-section="features">')

# Fix Slide 8 (Tech Stack)
# Reduce gaps and font sizes
text = text.replace('<div class="grow two stagger" style="gap:24px;">', '<div class="grow two stagger" style="gap:12px;">')
# There are two <div class="col" style="gap:16px;"> inside this section, we can replace them using regex to be safe
text = re.sub(r'<section class="slide" data-section="stack">.*?</section>', 
              lambda m: m.group(0).replace('gap:16px;', 'gap:10px;').replace('font-size:1.15em;', 'font-size:1.05em;').replace('class="card soft"', 'class="card soft" style="padding:14px;"'), 
              text, flags=re.DOTALL)

# Fix Slide 9 (Leadership Principles)
# Remove sparse class
text = text.replace('<section class="slide sparse" data-section="lp">', '<section class="slide" data-section="lp">')
# Reduce gaps and font sizes within this section
text = re.sub(r'<section class="slide" data-section="lp">.*?</section>', 
              lambda m: m.group(0).replace('gap:1.5rem', 'gap:0.8rem').replace('gap:24px;', 'gap:12px;').replace('font-size:1.15em;', 'font-size:1.05em;').replace('class="card soft"', 'class="card soft" style="padding:12px;"').replace('padding:18px;', 'padding:14px;'), 
              text, flags=re.DOTALL)

with open('ppt-finale.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Overflow issues fixed.")
