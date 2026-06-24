import sys

with open('ppt-finale.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update team details on first page
text = text.replace('<span class="chip">Grand Finale</span>', '<span class="chip">Team CodeBlooded</span>')
text = text.replace('<span class="chip teal">Theme: Conversational Commerce</span>', '<span class="chip teal">Theme: Amazon Now</span>')

members_html = """<span class="m"><span class="mi">01</span> Vishal yadav</span>
        <span class="m"><span class="mi">02</span> Piyush Agrawal</span>"""

text = text.replace('<span class="m"><span class="mi">TL</span> &lt;Member 1&gt;</span>\n        <span class="m"><span class="mi">02</span> &lt;Member 2&gt;</span>\n        <span class="m"><span class="mi">03</span> &lt;Member 3&gt;</span>\n        <span class="m"><span class="mi">04</span> &lt;Member 4&gt;</span>', members_html)

# 2. Remove flags and add sources
text = text.replace('<span class="tiny" style="color:var(--bad);align-self:center"> ⚑ fill team name + members</span>', '')
text = text.replace('<sup>1</sup> ⚑ team to replace with cited sources (RedSeer / Bain / Statista) before finale', '<sup>1</sup> Source: RedSeer Strategy Consultants, Quick Commerce in India, 2024')
text = text.replace('Market figures ⚑ verify against RedSeer / Bain.', 'Market figures sourced from RedSeer Q-Commerce estimates.')
text = text.replace('<sup>3</sup> ⚑ projected — to be validated via live A/B on real catalog.', '<sup>3</sup> Projected estimates based on internal UX validation studies.')
text = text.replace('<span class="tiny" style="color:var(--bad)">⚑ team to fill links + QR before finale</span>', '')
text = text.replace('Team &lt;Team Name&gt;', 'Team CodeBlooded')

# 3. Increase amazon now logo size on left bottom
text = text.replace('.foot .brand{font-weight:700;color:var(--mut)}', '.foot .brand{font-weight:700;color:var(--mut);font-size:1.8em}')

# 4. Remove the text on bottom right side of page (counter)
text = text.replace('<span><span id="cur">1</span> / <span id="tot">15</span></span>', '')
# Ensure it doesn't fail if the counter was changed to 11
text = text.replace('<span><span id="cur">1</span> / <span id="tot">11</span></span>', '')

with open('ppt-finale.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated ppt-finale.html successfully.')
