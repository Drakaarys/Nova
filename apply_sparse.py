import re

with open('ppt-finale.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Inject the CSS block
sparse_css = """
  /* Sparse Slide Strategy: Typography & White Space */
  .sparse .card { padding: clamp(32px, 4vw, 56px); justify-content: center; align-items: center; text-align: center; font-size: 1.15em; box-shadow: var(--shadow); }
  .sparse .card .ttl { font-size: 1.25em; justify-content: center; margin-bottom: 1rem; text-align: center; }
  .sparse ul.clean { font-size: 1.15em; gap: 1rem; display: flex; flex-direction: column; align-items: center; list-style: none; padding: 0; }
  .sparse .card:hover { transform: translateY(-4px); box-shadow: var(--shadow-lg); }
  .sparse .stat { padding: clamp(24px, 3vw, 40px); justify-content: center; align-items: center; text-align: center; }
  .sparse .stat .n { font-size: clamp(38px, 4.5vw, 64px); margin-bottom: 0.2em; }
  .sparse .stat .l { font-size: 1.1em; max-width: 300px; line-height: 1.4; }
  .sparse p.mut { text-align: center; font-size: 1.05em; }
"""

# Find a good place to inject the CSS, e.g., right before </style> which is in <head> but there is no </style> tag in the file exactly, wait, let me check where to inject.
# We can inject it right before `</style>` if it exists, or just after `.card.glow:hover{...}`
# The file has `</style>` around line 240. Let's just find `</style>` and replace it with sparse_css + `\n</style>`.
content = content.replace('</style>', sparse_css + '\n</style>')

# 2. Add `sparse` class to specific slides
slides_to_update = ['features', 'market', 'lp', 'scale']
for section in slides_to_update:
    old_tag = f'<section class="slide" data-section="{section}">'
    new_tag = f'<section class="slide sparse" data-section="{section}">'
    content = content.replace(old_tag, new_tag)

with open('ppt-finale.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Sparse layout applied.")
