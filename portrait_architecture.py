import re

portrait_arch_html = """  <!-- 7 · HOW IT WORKS / ARCHITECTURE COMBINED -->
  <section class="slide" data-section="pipeline">
    <style>
      .arch { font-family: var(--ff); font-size: 0.85em; display:flex; flex-direction:column; align-items:center; width:100%; max-width:800px; margin:0 auto; margin-top:0.5rem; }
      
      .box { background: #ffffff; border: 2px solid #e2e8f0; border-radius: 12px; padding: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.06); color:var(--ink); width:100%; position:relative; }
      
      .box.front { border-color: #3b82f6; border-top-width: 4px; }
      .box.back { border-color: #FF9900; border-top-width: 4px; }
      .box.data-bed { border-color: #3b82f6; }
      .box.data-dyn { border-color: #10b981; }
      .box.data-cal { border-color: #a855f7; }
      
      .box-title { font-weight: 800; text-align: center; margin-bottom:4px; font-size:1.15em; color:var(--ink); }
      .box-title.blue { color: #2563eb; }
      .box-title.orange { color: #ea580c; }
      .box-sub { color: #64748b; font-weight: 500; font-size: 0.85em; text-align:center; margin-bottom:12px; }
      
      .inner-box { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 12px; }
      
      .tag { background: #e2e8f0; color: #334155; padding: 4px 8px; border-radius: 6px; display:inline-block; margin: 3px; font-family: var(--mono); font-size:0.85em; font-weight:600; }
      
      .step-list { list-style: none; padding: 0; margin: 0; font-size: 0.95em; line-height: 1.5; }
      .step-list li { margin-bottom: 4px; }
      .step-list li span { color: #ea580c; font-weight:bold; margin-right:6px; display:inline-block; width:16px; }
      
      .v-arrow { display:flex; flex-direction:column; align-items:center; justify-content:center; color:#64748b; font-weight:bold; font-size:0.8em; text-align:center; line-height:1.2; padding: 8px 0; }
      .v-arrow .arr { font-size: 2em; line-height:0.5; color:#94a3b8; margin:6px 0; }
      
      .db-row { display:grid; grid-template-columns: 1fr 1fr 1fr; gap:16px; width:100%; }
      .db-box { text-align:center; padding:12px; }
      .db-box ul { padding-left:0; list-style:none; margin:0; margin-top:8px; font-size:0.85em; color:#475569; }
      
    </style>
    
    <div class="slide-head" style="margin-bottom:0">
      <span class="kicker teal"><span class="num">06</span> How It Works & Architecture</span>
      <h2 style="font-size:1.5em; margin:0;">Amazon Nova Architecture: <span class="accent">The 10-Second Funnel</span></h2>
    </div>
    
    <div class="grow col" style="justify-content:center; align-items:center;">
      <div class="arch">
        
        <!-- 1. Customer -->
        <div class="box" style="border-radius:30px; padding:10px 32px; text-align:center; width:auto; border-color:#94a3b8; background:#f8fafc;">
          <div style="font-size:1.2em; font-weight:800; color:#334155;"><span class="glyph">👤</span> CUSTOMER</div>
          <div style="color:#64748b; font-size:0.85em; margin-top:2px; font-weight:500;">Text / Voice / Photo</div>
        </div>
        
        <div class="v-arrow">
          <div>HTTPS / User Interaction</div>
          <div class="arr">↓</div>
        </div>

        <!-- 2. Frontend -->
        <div class="box front">
          <div class="box-title blue">REACT SPA WEB APPLICATION</div>
          <div class="box-sub">(Vite + TypeScript)</div>
          
          <div style="display:flex; gap:12px;">
            <div class="inner-box" style="flex:1;">
              <div style="text-align:center; margin-bottom:8px; font-weight:700; color:#334155;">React 19, Tailwind 4, Lucide Icons</div>
              <div style="font-family:var(--mono); font-size:0.85em; text-align:center; line-height:1.5; color:#475569;">
                IntentBar, CartProposalCard, EmergencyChips, ReorderStrip, SwipeCheckoutButton
              </div>
            </div>
            <div class="inner-box" style="display:flex; flex-direction:column; justify-content:center; align-items:center; padding:0 24px; color:#334155;">
              <span class="glyph" style="font-size:2em; margin-bottom:4px;">📱</span>
              <strong style="font-size:0.9em;">Mobile-First</strong>
            </div>
          </div>
        </div>
        
        <div class="v-arrow">
          <div>REST API (/intent, /auth)</div>
          <div class="arr">↓</div>
        </div>

        <!-- 3. Backend -->
        <div class="box back">
          <div class="box-title orange">EXPRESS BACKEND API</div>
          <div class="box-sub">(Node.js + TypeScript)</div>
          
          <div style="display:flex; gap:12px;">
            <div class="inner-box" style="flex:1; text-align:center;">
              <div style="font-size:0.9em; color:#ea580c; font-weight:800; margin-bottom:10px;">Internal Services</div>
              <div class="tag">catalog.ts</div>
              <div class="tag">dynamodb.ts</div>
              <div class="tag">bedrock.ts</div>
              <div class="tag">calendar.ts</div>
              <div class="tag">vectorSrch</div>
            </div>
            
            <div class="inner-box" style="flex:1.5;">
              <div style="text-align:center; font-size:0.9em; color:#ea580c; font-weight:800; margin-bottom:10px;">NOVA AGENT Pipeline</div>
              <div style="display:grid; grid-template-columns: 1fr 1fr; gap:8px;">
                 <ul class="step-list">
                    <li><span>1.</span> Parse Intent</li>
                    <li><span>2.</span> Context</li>
                    <li><span>3.</span> Decompose</li>
                    <li><span>4.</span> Vector Search</li>
                 </ul>
                 <ul class="step-list">
                    <li><span style="color:#ea580c">5.</span> <strong style="color:#ea580c">Assemble (LLM)</strong></li>
                    <li><span>6.</span> Availability</li>
                    <li><span>7.</span> Budget Limit</li>
                    <li><span>8.</span> Explain</li>
                 </ul>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Multi-arrow to DBs -->
        <div style="display:grid; grid-template-columns: 1fr 1fr 1fr; width:100%; gap:16px;">
          <div class="v-arrow"><div>LLM Request</div><div class="arr">↓</div></div>
          <div class="v-arrow"><div>Data R/W</div><div class="arr">↓</div></div>
          <div class="v-arrow"><div>Read Events</div><div class="arr">↓</div></div>
        </div>

        <!-- 4. Databases -->
        <div class="db-row">
          <div class="box db-box data-bed">
            <div class="box-title" style="color:#3b82f6; font-size:1em;">AWS BEDROCK</div>
            <ul>
              <li>Reasoning (Nova Lite)</li>
              <li>Titan Embed V2</li>
            </ul>
          </div>
          
          <div class="box db-box data-dyn">
            <div class="box-title" style="color:#10b981; font-size:1em;">DYNAMODB</div>
            <ul>
              <li>Catalog (329 SKUs)</li>
              <li>Users / Orders</li>
            </ul>
          </div>
          
          <div class="box db-box data-cal">
            <div class="box-title" style="color:#a855f7; font-size:1em;">GOOGLE CALENDAR</div>
            <ul>
              <li>Upcoming events</li>
              <li>Proactive carts</li>
            </ul>
          </div>
        </div>

      </div>
    </div>
  </section>"""

with open('ppt-finale.html', 'r', encoding='utf-8') as f:
    text = f.read()

pattern = re.compile(r'<!-- 7 · HOW IT WORKS / ARCHITECTURE COMBINED -->\s*<section class="slide" data-section="pipeline">.*?</section>', re.DOTALL)
text = pattern.sub(portrait_arch_html, text)

with open('ppt-finale.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Portrait architecture diagram injected.")
