import re

with open('ppt-finale.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_deck = """<div id="deck">

  <!-- 1 · TITLE -->
  <section class="slide active" data-section="hook">
    <div class="title-bg" style="background-image:url('assets/shot-home.png')"></div>
    <div class="title-wrap">
      <div class="logo-mark mut" style="margin-bottom:1.4rem"><span class="spark">✦</span> Amazon <span class="accent">Now</span></div>
      <h1>Delivery got instant.<br><span class="grad-text">Shopping didn't.</span><br>We fixed that.</h1>
      
      <div class="two" style="margin-top:2rem; max-width: 600px;">
        <div class="stat"><div class="n" style="font-size:1.8em;">20 min</div><div class="l">Current cart building time</div></div>
        <div class="stat glow"><div class="n accent" style="font-size:1.8em;">2.4s</div><div class="l">Amazon Now conversational agent</div></div>
      </div>

      <div class="team" style="margin-top:2.5rem">
        <span class="chip on">HackOn with Amazon · Season 6.0</span>
        <span class="chip">Team CodeBlooded</span>
        <span class="chip teal">Theme: Amazon Now</span>
      </div>
      <div class="members" style="margin-top:1rem">
        <span class="m"><span class="mi">01</span> Vishal yadav</span>
        <span class="m"><span class="mi">02</span> Piyush Agrawal</span>
      </div>
    </div>
  </section>

  <!-- 2 · PROBLEM -->
  <section class="slide" data-section="problem">
    <div class="slide-head">
      <span class="kicker"><span class="num">01</span> The Problem · Work Backwards from the Customer</span>
      <h2>The <span class="accent">30-minute morning</span> nobody talks about</h2>
    </div>
    <div class="grow col" style="gap:1.5rem; justify-content:center;">
      <div class="three stagger">
        <div class="card glow"><div class="ttl" style="font-size:1.2em"><span class="glyph">⌖</span> Decision fatigue</div><p class="mut small">40 variants per query.</p></div>
        <div class="card glow"><div class="ttl" style="font-size:1.2em"><span class="glyph">↻</span> Repetitive loop</div><p class="mut small">Search → filter → compare → add.</p></div>
        <div class="card glow"><div class="ttl" style="font-size:1.2em"><span class="glyph">₹</span> Invisible budget</div><p class="mut small">Overshoots discovered at checkout.</p></div>
      </div>
      <div class="row stagger wrap" style="gap:16px; margin-top:1rem;">
        <div class="stat todo" style="flex:1;"><div class="n">~70%</div><div class="l">of carts abandoned — friction & decision fatigue are top drivers<sup>1</sup></div></div>
        <div class="stat todo" style="flex:1;"><div class="n">8–12</div><div class="l">searches to assemble one urgent multi-item trip<sup>1</sup></div></div>
        <div class="stat todo" style="flex:1;"><div class="n">&gt;5 min</div><div class="l">time-to-cart for a 10-item basket on quick-commerce<sup>1</sup></div></div>
      </div>
    </div>
    <p class="tiny mut" style="position:absolute;bottom:40px"><sup>1</sup> Source: RedSeer Strategy Consultants, Quick Commerce in India, 2024</p>
  </section>

  <!-- 3 · SOLUTION -->
  <section class="slide" data-section="solution">
    <div class="slide-head">
      <span class="kicker teal"><span class="num">02</span> The Solution · Invent & Simplify</span>
      <h2>Meet <span class="accent">the Now Agent</span></h2>
    </div>
    <div class="grow col center" style="gap:2rem">
      <div class="row center wrap" style="width:100%;gap:6px">
        <div class="col" style="gap:10px;flex:0 0 auto">
          <div class="card soft" style="padding:14px 18px; font-weight:600;"><span class="glyph">⌨</span> "Breakfast for 4, ₹500"</div>
          <div class="card soft" style="padding:14px 18px; font-weight:600;"><span class="glyph">🎙</span> Voice intent</div>
          <div class="card soft" style="padding:14px 18px; font-weight:600;"><span class="glyph">📷</span> Photo of empty fridge</div>
        </div>
        <div class="arrow">➜</div>
        <div class="card glow" style="flex:0 0 auto;text-align:center; padding:24px;">
          <div style="font-size:2.8em">✦</div>
          <div style="font-weight:800;font-size:1.4em; margin-bottom:8px;">The Now Agent</div>
          <div class="mut small">8-step deterministic<br>orchestration on AWS</div>
        </div>
        <div class="arrow">➜</div>
        <div class="col" style="gap:10px;flex:0 0 auto">
          <div class="card soft" style="padding:14px 18px; font-weight:600;"><b class="teal">✓ Ready cart</b></div>
          <div class="card soft" style="padding:14px 18px; font-weight:600;"><b class="teal">✓ Budget-checked</b></div>
          <div class="card soft" style="padding:14px 18px; font-weight:600;"><b class="teal">✓ Explained</b></div>
        </div>
      </div>
      <div class="three stagger" style="width:100%; margin-top:1rem;">
        <div class="card soft"><div class="ttl"><div class="glyph accent">①</div> Parse Intent</div></div>
        <div class="card soft"><div class="ttl"><div class="glyph teal">②</div> Decide & Explain</div></div>
        <div class="card soft"><div class="ttl"><div class="glyph vio">③</div> Guard the Outcome</div></div>
      </div>
    </div>
  </section>

  <!-- 4 · FEATURES -->
  <section class="slide" data-section="features">
    <div class="slide-head">
      <span class="kicker"><span class="num">03</span> What It Does · 13 features, 3 tiers</span>
      <h2>From a sentence to a <span class="accent">smart</span> cart</h2>
    </div>
    <div class="grow col" style="gap:1rem">
      <div class="three stagger">
        <div class="card"><div class="ttl" style="font-size:1.1em"><span class="glyph">①</span> Core</div><ul class="clean" style="font-size:1.1em"><li><b>Intent-to-Cart</b></li><li><b>Multimodal</b> (text/voice/photo)</li><li><b>Budget rebalancing</b></li><li><b>Recipe Scaling</b></li></ul></div>
        <div class="card"><div class="ttl" style="font-size:1.1em"><span class="glyph teal">②</span> Predictive</div><ul class="clean" style="font-size:1.1em"><li><b>Proactivity</b> (weather)</li><li><b>Consumption refills</b></li><li><b>Emergency Mode</b></li></ul></div>
        <div class="card"><div class="ttl" style="font-size:1.1em"><span class="glyph vio">③</span> Enhancers</div><ul class="clean" style="font-size:1.1em"><li><b>Out-of-stock swaps</b></li><li><b>Confidence scores</b></li><li><b>Learns from edits</b></li><li><b>Diet-aware swaps</b></li></ul></div>
      </div>
      <div class="card soft" style="display:flex;align-items:center;gap:14px;flex-wrap:wrap; margin-top:1rem;">
        <span class="chip teal" style="font-size:1em;">♿ Accessibility win</span>
        <p class="mut" style="margin:0;flex:1;min-width:240px; font-weight:500;">Voice + photo input means elderly & low-literacy shoppers get the same 2.4s outcome natively.</p>
      </div>
    </div>
  </section>

  <!-- 5 · MARKET -->
  <section class="slide" data-section="market">
    <div class="slide-head">
      <span class="kicker"><span class="num">04</span> Market & Opportunity</span>
      <h2>Amazon Now has the infrastructure. <span class="accent">Nobody has the conversation.</span></h2>
    </div>
    <div class="grow col" style="gap:1.5rem">
      <div class="three stagger">
        <div class="stat"><div class="n">25% MoM</div><div class="l">Amazon Now order growth in India<sup>2</sup></div></div>
        <div class="stat"><div class="n teal">3×</div><div class="l">Prime members' shopping frequency<sup>2</sup></div></div>
        <div class="stat"><div class="n">$5–6B</div><div class="l">India quick-commerce GMV</div></div>
      </div>
      <div class="two stagger" style="gap:24px">
        <div class="card glow" style="border-width:2px; padding:24px;">
          <div class="ttl" style="font-size:1.3em; margin-bottom:1rem;"><span class="glyph">👤</span> Customer Impact</div>
          <ul class="clean" style="font-size:1.1em; gap:0.8em;">
            <li><b>Time given back</b></li>
            <li><b>Accessibility by design</b></li>
            <li><b>Trust on every line</b></li>
            <li><b>No checkout anxiety</b></li>
            <li><b>Always deliverable</b></li>
          </ul>
        </div>
        <div class="card soft" style="padding:24px;">
          <div class="ttl t-teal" style="font-size:1.3em; margin-bottom:1rem;"><span class="glyph teal">📈</span> Business Impact</div>
          <ul class="clean" style="font-size:1.1em; gap:0.8em;">
            <li><b>↑ Frequency</b></li>
            <li><b>↑ Conversion</b></li>
            <li><b>↓ Returns</b></li>
            <li><b>↑ Basket size</b></li>
            <li><b>New proactive revenue</b></li>
          </ul>
        </div>
      </div>
    </div>
    <p class="tiny mut" style="position:absolute;bottom:40px"><sup>2</sup> Amazon Now stats from Andy Jassy's 2025 Letter to Shareholders. Market figures sourced from RedSeer Q-Commerce estimates.</p>
  </section>

  <!-- 6 · LIVE DEMO -->
  <section class="slide" data-section="demo">
    <div class="slide-head" style="margin-bottom:.7rem">
      <span class="kicker"><span class="num">05</span> Live Demo · this is the real, working product</span>
      <h2>Watch the <span class="accent">demo video</span> — cart built in ~2.4s</h2>
    </div>
    <div class="grow" style="justify-content:center">
      <div class="video-ph" style="min-height: 400px;">
        <div class="play-btn" style="transform: scale(1.2);">▶</div>
        <div class="ph-label" style="font-size: 1.5em; margin-top:1rem;">Demo video placeholder</div>
        <div class="mut">embed your demo video here</div>
      </div>
    </div>
    <div class="card soft" style="margin-top:.7rem;display:flex;gap:14px;align-items:center;flex-wrap:wrap">
      <span class="chip on">▶ Run-of-show</span>
      <p class="mut small" style="margin:0;flex:1;min-width:300px">Live order: <b>photo→cart</b> · <b>"Diwali for 10"→scaled</b> · <b>over-budget→auto-rebalance (₹ saved)</b> · <b>"Cut Finger"→SOS bundle</b>. <span class="tiny">(video fallback cued — network permitting)</span></p>
    </div>
  </section>

  <!-- 7 · HOW IT WORKS / ARCHITECTURE COMBINED -->
  <section class="slide" data-section="pipeline">
    <div class="slide-head">
      <span class="kicker teal"><span class="num">06</span> How It Works & Architecture</span>
      <h2>Serverless Orchestration — <span class="accent">2.4s end to end</span></h2>
    </div>
    <div class="grow col center" style="gap:1.5rem">
      <!-- Pipeline visually enhanced -->
      <div class="pipe stagger" style="width:100%;">
        <div class="step llm"><span class="sn">1</span><div class="si">LLM</div><div class="st">Parse Intent</div></div>
        <div class="step det"><span class="sn">2</span><div class="si">DET</div><div class="st">Clarify</div></div>
        <div class="step llm"><span class="sn">3</span><div class="si">LLM</div><div class="st">Decompose</div></div>
        <div class="step det"><span class="sn">4</span><div class="si">DET</div><div class="st">Context</div></div>
        <div class="step det"><span class="sn">5</span><div class="si">DET</div><div class="st">Candidate Search</div></div>
        <div class="step llm"><span class="sn">6</span><div class="si">LLM</div><div class="st">Assemble</div></div>
        <div class="step det"><span class="sn">7</span><div class="si">DET</div><div class="st">Availability</div></div>
        <div class="step det"><span class="sn">8</span><div class="si">DET</div><div class="st">Enforce Budget</div></div>
      </div>
      
      <!-- Arch diagram visually enhanced -->
      <div class="layer stagger" style="margin-top:1rem; border-color: rgba(10,147,150, 0.4); background: rgba(10,147,150, 0.02); padding: 24px;">
        <span class="band-tag" style="color: var(--teal-d); background: #fff;">Application Layer</span>
        <div class="arch" style="gap:16px">
          <div class="node"><div class="nt">React + TS</div><div class="ns">Frontend UI</div></div>
          <div class="arrow">→</div>
          <div class="node aws"><div class="nt">CloudFront & S3</div><div class="ns">Static Hosting</div></div>
          <div class="arrow">→</div>
          <div class="node aws"><div class="nt">API Gateway</div><div class="ns">REST APIs</div></div>
          <div class="arrow">→</div>
          <div class="node aws"><div class="nt">Lambda</div><div class="ns">Serverless Backend</div></div>
        </div>
      </div>
      
      <div class="layer stagger" style="border-color: rgba(255,153,0, 0.4); background: rgba(255,153,0, 0.02); padding: 24px;">
        <span class="band-tag">Amazon Bedrock & Data</span>
        <div class="arch" style="gap:16px">
          <div class="node aws" style="border-width:2px;"><div class="nt">Amazon Nova Lite</div><div class="ns">LLM Reasoning</div></div>
          <div class="node aws" style="border-width:2px;"><div class="nt">Titan Embeddings v2</div><div class="ns">Vector Generation</div></div>
          <div class="node"><div class="nt">In-memory Search</div><div class="ns">Cosine Similarity</div></div>
          <div class="node aws"><div class="nt">DynamoDB</div><div class="ns">Catalog Data</div></div>
        </div>
      </div>

      <div class="legend" style="justify-content:center; font-size:0.9em; margin-top:0.5rem;">
        <span><i style="background:var(--orange)"></i>LLM reasoning (only 2–3 calls)</span>
        <span><i style="background:var(--teal)"></i>Deterministic code — fast, cheap, predictable</span>
      </div>
    </div>
  </section>

  <!-- 8 · TECH STACK & TRUST COMBINED -->
  <section class="slide" data-section="stack">
    <div class="slide-head">
      <span class="kicker"><span class="num">07</span> Tech Stack & Trust</span>
      <h2>AWS-native & <span class="accent">Secure by Design</span></h2>
    </div>
    <div class="grow two stagger" style="gap:24px;">
      <div class="col" style="gap:16px;">
        <div class="card soft"><div class="ttl" style="font-size:1.15em;"><span class="glyph">⚛</span> React + Node (Lambda)</div><p class="mut">Type-safe UI, zero idle cost, auto-scale.</p></div>
        <div class="card soft"><div class="ttl" style="font-size:1.15em;"><span class="glyph">✦</span> Amazon Nova Lite & Titan</div><p class="mut">Amazon's frontier models. Fast, low cost, multimodal.</p></div>
        <div class="card soft"><div class="ttl" style="font-size:1.15em;"><span class="glyph">🗄</span> DynamoDB & Vector Search</div><p class="mut">Single-digit-ms reads. Precomputed embeddings.</p></div>
      </div>
      <div class="col" style="gap:16px;">
        <div class="card soft"><div class="ttl t-vio" style="font-size:1.15em;"><span class="glyph vio">🛡</span> Deterministic Guardrails</div><p class="mut">Money, stock & diet enforced strictly by code — never the model.</p></div>
        <div class="card soft"><div class="ttl t-teal" style="font-size:1.15em;"><span class="glyph teal">💡</span> Explainable Picks</div><p class="mut">Every single item ships with a plain-text reason & confidence score.</p></div>
        <div class="card soft"><div class="ttl t-vio" style="font-size:1.15em;"><span class="glyph vio">🔒</span> Privacy & Safety</div><p class="mut">Images not stored. PII protected. Temp 0.2 for stable outputs.</p></div>
      </div>
    </div>
  </section>

  <!-- 9 · LEADERSHIP PRINCIPLES -->
  <section class="slide" data-section="lp">
    <div class="slide-head">
      <span class="kicker teal"><span class="num">08</span> Amazon Leadership Principles</span>
      <h2>Built the Amazon way</h2>
    </div>
    <div class="grow col" style="justify-content:center;gap:1.5rem">
      <div class="two stagger" style="gap:24px;">
        <div class="card soft"><div class="ttl" style="font-size:1.15em;">★ Customer Obsession</div><p class="mut">Removed the decision tax. Kept the shopper in focus.</p></div>
        <div class="card soft"><div class="ttl t-teal" style="font-size:1.15em;">★ Invent & Simplify</div><p class="mut">12-step search funnel collapsed into one simple sentence.</p></div>
        <div class="card soft"><div class="ttl" style="font-size:1.15em;">★ Frugality</div><p class="mut">Only 2–3 LLM calls per cart, precomputed vectors.</p></div>
        <div class="card soft"><div class="ttl t-teal" style="font-size:1.15em;">★ Deliver Results</div><p class="mut">Working prototype, 9 live routes, demo-ready today.</p></div>
        <div class="card soft"><div class="ttl" style="font-size:1.15em;">★ Dive Deep</div><p class="mut">Measured latency step-by-step for a real 2.4s SLA.</p></div>
        <div class="card soft"><div class="ttl t-teal" style="font-size:1.15em;">★ Earn Trust</div><p class="mut">Deterministic guardrails and explainable AI picks.</p></div>
      </div>
      <div class="card glow stagger" style="text-align:center; padding:18px;">
        <div class="ttl" style="justify-content:center; font-size:1.2em;">★ Think Big</div>
        <p class="mut">The conversational layer for Amazon's entire delivery network.</p>
      </div>
    </div>
  </section>

  <!-- 10 · SCALABILITY -->
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
      <div class="two stagger" style="gap:24px; margin-top: 1rem">
        <div class="col" style="gap:16px">
          <div class="card soft"><div class="ttl" style="font-size:1.1em;"><span class="glyph">∞</span> Scales with load</div><p class="mut">API Gateway → Lambda → DynamoDB handle traffic spikes perfectly.</p></div>
          <div class="card soft"><div class="ttl" style="font-size:1.1em;"><span class="glyph teal">▦</span> Search that grows</div><p class="mut">Ready for OpenSearch Serverless as catalog expands seamlessly.</p></div>
        </div>
        <div class="col" style="gap:16px">
          <div class="card soft"><div class="ttl" style="font-size:1.1em;"><span class="glyph teal">₹</span> Predictable cost</div><p class="mut">Fixed LLM usage + cached routes = fully forecastable margins.</p></div>
          <div class="card soft"><div class="ttl" style="font-size:1.1em;"><span class="glyph">🔌</span> Catalog-agnostic</div><p class="mut">Portable across Fresh, Pharmacy, and Grocery catalogs.</p></div>
        </div>
      </div>
    </div>
  </section>

  <!-- 11 · FUTURE VISIONS -->
  <section class="slide" data-section="future">
    <div class="slide-head">
      <span class="kicker teal"><span class="num">10</span> Future Roadmap</span>
      <h2>Where Now goes <span class="accent">next</span></h2>
    </div>
    <div class="grow center">
      <div class="road stagger" style="width:100%">
        <div class="mile now"><div class="dotm"></div><div class="when">NOW · SHIPPED</div><h3 style="font-size:1.2em;">Working prototype</h3><p style="font-size:0.9em;">Multimodal agent · Live Bedrock pipeline</p></div>
        <div class="mile"><div class="dotm"></div><div class="when">+90 DAYS</div><h3 style="font-size:1.2em;">Real catalog + A/B</h3><p style="font-size:0.9em;">Amazon Now integration · OpenSearch</p></div>
        <div class="mile"><div class="dotm"></div><div class="when">Q1 2027</div><h3 style="font-size:1.2em;">Urgent Booking</h3><p style="font-size:0.9em; font-weight:600; color:var(--ink);">Ticket booking for Buses & Flights in urgency</p></div>
        <div class="mile"><div class="dotm"></div><div class="when">2027+</div><h3 style="font-size:1.2em;">Autonomous Refills</h3><p style="font-size:0.9em;">Predictive subscriptions · Amazon Now expansion</p></div>
      </div>
    </div>
  </section>

  <!-- 12 · CLOSING -->
  <section class="slide" data-section="close">
    <div class="title-bg" style="background-image:url('assets/shot-home.png');opacity:.1"></div>
    <div class="title-wrap" style="position:relative;z-index:2">
      <span class="kicker"><span class="num">11</span> Thank You</span>
      <h1 style="margin:.3em 0">Delivery is fast.<br><span class="grad-text">Now shopping is too.</span></h1>
      
      <div class="row stagger" style="margin-top:2rem;align-items:flex-start;gap:24px;flex-wrap:wrap">
        <div class="col" style="gap:.55em;flex:1;min-width:300px">
          <div class="mut small" style="font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--orange-d);font-size:.8em">Our ask — 90-day pilot</div>
          <div class="chip on" style="align-self:flex-start; font-size:1em; padding:8px 16px;">① Pilot on Amazon Now's India catalog</div>
          <div class="chip teal" style="align-self:flex-start; font-size:1em; padding:8px 16px;">② Sandboxed catalog access</div>
          <div class="chip vio" style="align-self:flex-start; font-size:1em; padding:8px 16px;">③ Bedrock credits + mentorship</div>
        </div>
        <div class="col" style="gap:.8em">
          <div class="qr" style="width:140px; height:140px; font-size:12px;">QR →<br>live demo</div>
          <div class="chip" style="font-size:0.9em;">💻 GitHub — &lt;repo URL&gt;</div>
          <div class="chip" style="font-size:0.9em;">▶ Demo video — &lt;video URL&gt;</div>
        </div>
      </div>
      <div class="row" style="margin-top:2rem;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px">
        <div class="logo-mark"><span class="spark">✦</span> Amazon <span class="accent">Now</span></div>
        <span class="mut small">HackOn with Amazon · S6.0 Grand Finale · Team CodeBlooded</span>
      </div>
    </div>
  </section>

</div>"""

new_notes = """  const NOTES = [
    "Open with the hook. 'Amazon Now delivers in 20 minutes — but building the cart takes 20. We close that gap.' Pause 2 seconds. Let the screenshot do the talking.",
    "Tell the 8:30 AM story visually. Make them feel the clock. This is the 'Why' Jassy asks. Point to the abandonment stats.",
    "Frame the shift: outcome-first, not search-first. The agent builds AND explains. Point at the visual flow.",
    "13 features, all in the demo. Point at the tiers. Mention the accessibility win.",
    "Lead with the hero stats. Business FOLLOWS from the customer. Cite the 3x frequency stat from Jassy's letter.",
    "THIS is the finale-winning slide. Spend the most time here. Rehearse the live run. Video as fallback. Judges reward working demos above all else.",
    "PROOF. Walk the pipeline and architecture. Show the new Application vs Bedrock layout. The LLM only parses & chooses — money/stock/diet are code.",
    "Responsible AI & Tech Stack. This is Earn Trust. Deterministic guardrails mean the model can't spend money. AWS-native throughout.",
    "HackOn rewards LP alignment. Show how each point directly aligns with the Amazon way. Point at the Think Big anchor.",
    "Most important feasibility slide. Land: scales to zero, bounded LLM cost, OpenSearch path, multi-region. Feasible at Amazon scale.",
    "Four milestones. Emphasize urgent ticket booking for buses & flights to show versatility beyond groceries.",
    "Restate vision. Make the ASK specific. Point at the QR + links. Hold during Q&A."
  ];"""

# Replace deck
deck_pattern = re.compile(r'<div id="deck">.*?</div>\s*<div class="rail" id="rail"></div>', re.DOTALL)
content = deck_pattern.sub(new_deck + '\n\n<div class="rail" id="rail"></div>', content)

# Replace NOTES
notes_pattern = re.compile(r'const NOTES = \[.*?\];', re.DOTALL)
content = notes_pattern.sub(new_notes, content)

with open('ppt-finale.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML re-write complete.")
