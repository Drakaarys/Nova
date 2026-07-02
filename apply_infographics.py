import re

with open('ppt-finale.html', 'r', encoding='utf-8') as f:
    text = f.read()

market_html = """  <!-- 5 · MARKET -->
  <section class="slide" data-section="market">
    <div class="slide-head">
      <span class="kicker"><span class="num">04</span> Market & Opportunity</span>
      <h2>Amazon Now has the infrastructure. <span class="accent">Nobody has the conversation.</span></h2>
    </div>
    <div class="grow col" style="gap:1.5rem">
      <div class="three stagger">
        <div class="stat" style="position:relative; overflow:hidden;">
          <svg style="position:absolute; bottom:0; left:0; width:100%; height:60%; opacity:0.1; z-index:0;" viewBox="0 0 100 40" preserveAspectRatio="none"><path d="M0 40 L0 30 L20 25 L40 32 L60 15 L80 18 L100 5 L100 40 Z" fill="var(--orange-d)"/></svg>
          <div class="n" style="position:relative; z-index:1;">25% MoM</div><div class="l" style="position:relative; z-index:1;">Amazon Now order growth in India<sup>2</sup></div>
        </div>
        <div class="stat" style="position:relative; overflow:hidden;">
          <svg style="position:absolute; bottom:0; left:0; width:100%; height:60%; opacity:0.1; z-index:0;" viewBox="0 0 100 40" preserveAspectRatio="none"><path d="M0 40 L0 25 L30 20 L50 10 L80 15 L100 0 L100 40 Z" fill="var(--teal-d)"/></svg>
          <div class="n teal" style="position:relative; z-index:1;">3×</div><div class="l" style="position:relative; z-index:1;">Prime members' shopping frequency<sup>2</sup></div>
        </div>
        <div class="stat" style="position:relative; overflow:hidden;">
          <svg style="position:absolute; bottom:0; left:0; width:100%; height:60%; opacity:0.1; z-index:0;" viewBox="0 0 100 40" preserveAspectRatio="none"><path d="M0 40 L0 20 L25 28 L50 12 L75 18 L100 2 L100 40 Z" fill="var(--ink)"/></svg>
          <div class="n" style="position:relative; z-index:1;">$5–6B</div><div class="l" style="position:relative; z-index:1;">India quick-commerce GMV</div>
        </div>
      </div>
      <div class="two stagger" style="gap:16px">
        <div class="card glow" style="border-width:2px; padding:20px;">
          <div class="ttl" style="font-size:1.15em; margin-bottom:1rem;"><span class="glyph">👤</span> Customer Impact</div>
          <div style="display:flex; flex-wrap:wrap; gap:10px;">
            <span class="chip on" style="font-size:1em;">Time given back</span>
            <span class="chip on" style="font-size:1em;">Accessibility by design</span>
            <span class="chip on" style="font-size:1em;">Trust on every line</span>
            <span class="chip on" style="font-size:1em;">No checkout anxiety</span>
            <span class="chip on" style="font-size:1em;">Always deliverable</span>
          </div>
        </div>
        <div class="card soft" style="padding:20px;">
          <div class="ttl t-teal" style="font-size:1.15em; margin-bottom:1rem;"><span class="glyph teal">📈</span> Business Impact</div>
          <div style="display:flex; flex-wrap:wrap; gap:10px;">
            <span class="chip teal" style="font-size:1em;">↑ Frequency</span>
            <span class="chip teal" style="font-size:1em;">↑ Conversion</span>
            <span class="chip teal" style="font-size:1em;">↓ Returns</span>
            <span class="chip teal" style="font-size:1em;">↑ Basket size</span>
            <span class="chip teal" style="font-size:1em;">New proactive revenue</span>
          </div>
        </div>
      </div>
    </div>
    <p class="tiny mut" style="position:absolute;bottom:40px"><sup>2</sup> Amazon Now stats from Andy Jassy's 2025 Letter to Shareholders. Market figures sourced from RedSeer Q-Commerce estimates.</p>
  </section>"""

lp_html = """  <!-- 9 · LEADERSHIP PRINCIPLES -->
  <section class="slide" data-section="lp">
    <div class="slide-head">
      <span class="kicker teal"><span class="num">08</span> Amazon Leadership Principles</span>
      <h2>Built the Amazon way</h2>
    </div>
    <div class="grow col" style="justify-content:center;gap:1.5rem; position:relative; z-index:1;">
      
      <!-- The spokes -->
      <div style="display:grid; grid-template-columns: repeat(3, 1fr); gap:16px; position:relative; z-index:2;">
        <div class="card soft" style="padding:12px; text-align:center;"><div class="ttl" style="font-size:0.95em; justify-content:center;">★ Customer Obsession</div><p class="mut tiny" style="margin:0;">Removed decision tax.</p></div>
        <div class="card soft" style="padding:12px; text-align:center;"><div class="ttl t-teal" style="font-size:0.95em; justify-content:center;">★ Invent & Simplify</div><p class="mut tiny" style="margin:0;">12 steps collapsed to 1.</p></div>
        <div class="card soft" style="padding:12px; text-align:center;"><div class="ttl" style="font-size:0.95em; justify-content:center;">★ Frugality</div><p class="mut tiny" style="margin:0;">2–3 LLM calls.</p></div>
        
        <div class="card soft" style="padding:12px; text-align:center;"><div class="ttl t-teal" style="font-size:0.95em; justify-content:center;">★ Deliver Results</div><p class="mut tiny" style="margin:0;">Working prototype today.</p></div>
        <div class="card soft" style="padding:12px; text-align:center;"><div class="ttl" style="font-size:0.95em; justify-content:center;">★ Dive Deep</div><p class="mut tiny" style="margin:0;">Measured 2.4s SLA.</p></div>
        <div class="card soft" style="padding:12px; text-align:center;"><div class="ttl t-teal" style="font-size:0.95em; justify-content:center;">★ Earn Trust</div><p class="mut tiny" style="margin:0;">Deterministic guardrails.</p></div>
      </div>
      
      <!-- Connecting lines (svg) -->
      <svg style="position:absolute; top:45%; left:0; width:100%; height:25%; z-index:0; pointer-events:none;" preserveAspectRatio="none">
         <path d="M 16% 0 C 16% 100, 50% 50, 50% 100" stroke="rgba(0,0,0,0.15)" stroke-width="2" fill="none" stroke-dasharray="4" />
         <path d="M 50% 0 L 50% 100" stroke="rgba(0,0,0,0.15)" stroke-width="2" fill="none" stroke-dasharray="4" />
         <path d="M 83% 0 C 83% 100, 50% 50, 50% 100" stroke="rgba(0,0,0,0.15)" stroke-width="2" fill="none" stroke-dasharray="4" />
      </svg>

      <!-- The hub -->
      <div class="card glow stagger" style="text-align:center; padding:16px; margin:0 auto; width:60%; z-index:2; position:relative; background:#fff; border-width:2px;">
        <div class="ttl" style="justify-content:center; font-size:1.2em; color:var(--orange-d);">★ Think Big</div>
        <p class="mut" style="margin:0;">The conversational layer for Amazon's entire delivery network.</p>
      </div>
      
    </div>
  </section>"""

scale_html = """  <!-- 10 · SCALABILITY -->
  <section class="slide" data-section="scale">
    <div class="slide-head">
      <span class="kicker"><span class="num">09</span> Scalability</span>
      <h2>A real production path — <span class="accent">built to scale</span></h2>
    </div>
    <div class="grow col" style="gap:1.5rem">
      <div class="three stagger">
        <div class="stat"><div class="n">0 → ∞</div><div class="l">Serverless auto-scaling</div></div>
        <div class="stat"><div class="n teal">2–3</div><div class="l">Bounded LLM calls</div></div>
        <div class="stat"><div class="n">→ ₹0</div><div class="l">Zero Idle cost</div></div>
      </div>
      <div class="two stagger" style="gap:12px; margin-top: 1rem">
        <div class="col" style="gap:12px">
          <!-- Flowchart Infographic -->
          <div class="card soft" style="display:flex; flex-direction:column; justify-content:space-between; flex:1;">
            <div class="ttl" style="font-size:1.1em;"><span class="glyph">∞</span> Scales with load</div>
            <div style="display:flex; align-items:center; justify-content:space-around; background:#f9f9f9; padding:12px; border-radius:8px; border:1px dashed #ccc; font-family:var(--mono); font-size:0.7em; font-weight:700; color:var(--mut); margin:8px 0;">
              <span style="background:#fff; padding:4px 8px; border-radius:4px; box-shadow:var(--shadow-sm);">API Gateway</span>
              <span style="color:var(--orange-d);">→</span>
              <span style="background:#fff; padding:4px 8px; border-radius:4px; box-shadow:var(--shadow-sm);">Lambda</span>
              <span style="color:var(--orange-d);">→</span>
              <span style="background:#fff; padding:4px 8px; border-radius:4px; box-shadow:var(--shadow-sm);">DynamoDB</span>
            </div>
            <p class="mut tiny" style="margin:0;">Serverless architecture handles traffic spikes perfectly.</p>
          </div>
          
          <div class="card soft" style="flex:0 0 auto;">
             <div class="ttl" style="font-size:1.1em;"><span class="glyph teal">▦</span> Search that grows</div>
             <p class="mut small" style="margin:0;">Ready for OpenSearch Serverless as catalog expands seamlessly.</p>
          </div>
        </div>
        <div class="col" style="gap:12px">
          
          <!-- Cost Graph Infographic -->
          <div class="card soft" style="position:relative; overflow:hidden; flex:1;">
            <div class="ttl" style="font-size:1.1em; position:relative; z-index:2;"><span class="glyph teal">₹</span> Predictable cost</div>
            <p class="mut small" style="position:relative; z-index:2; margin:0;">Fixed LLM usage + cached routes = fully forecastable margins.</p>
            <svg style="position:absolute; bottom:-10px; right:0; width:60%; height:80px; z-index:1; opacity:0.15;" viewBox="0 0 100 40" preserveAspectRatio="none">
              <path d="M0 35 L20 35 L30 10 L40 35 L60 35 L70 5 L80 35 L100 35" stroke="var(--ink)" stroke-width="2" fill="none" stroke-dasharray="2" />
              <path d="M0 35 L100 35" stroke="var(--teal-d)" stroke-width="4" fill="none" />
              <text x="5" y="10" font-size="6" fill="var(--ink)" font-family="sans-serif">Traffic Spikes</text>
              <text x="5" y="32" font-size="6" fill="var(--teal-d)" font-weight="bold" font-family="sans-serif">Flat Cost</text>
            </svg>
          </div>
          
          <div class="card soft" style="flex:0 0 auto;">
             <div class="ttl" style="font-size:1.1em;"><span class="glyph">🔌</span> Catalog-agnostic</div>
             <p class="mut small" style="margin:0;">Portable across Fresh, Pharmacy, and Grocery catalogs.</p>
          </div>
        </div>
      </div>
    </div>
  </section>"""

text = re.sub(r'<!-- 5 · MARKET -->\s*<section class="slide".*?data-section="market">.*?</section>', market_html, text, flags=re.DOTALL)
text = re.sub(r'<!-- 9 · LEADERSHIP PRINCIPLES -->\s*<section class="slide".*?data-section="lp">.*?</section>', lp_html, text, flags=re.DOTALL)
text = re.sub(r'<!-- 10 · SCALABILITY -->\s*<section class="slide".*?data-section="scale">.*?</section>', scale_html, text, flags=re.DOTALL)

with open('ppt-finale.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Infographics successfully generated and injected.")
