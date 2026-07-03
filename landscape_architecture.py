import re

landscape_arch_html = """  <!-- 7 · HOW IT WORKS / ARCHITECTURE COMBINED -->
  <section class="slide" data-section="pipeline">
    <style>
      .arch-ls { font-family: var(--ff); font-size: 0.72em; display:flex; flex-direction:column; align-items:center; width:100%; max-width:960px; margin:0 auto; gap: 8px; }
      
      .box-ls { background: #ffffff; border: 2px solid #e2e8f0; border-radius: 8px; padding: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); color:var(--ink); width:100%; position:relative; }
      .box-ls.front { border-color: #3b82f6; border-top-width: 4px; }
      .box-ls.back { border-color: #ea580c; border-top-width: 4px; }
      .box-ls.data-bed { border-color: #3b82f6; }
      .box-ls.data-dyn { border-color: #10b981; }
      .box-ls.data-cal { border-color: #a855f7; }
      
      .box-title-ls { font-weight: 800; text-align: center; margin-bottom:2px; font-size:1.15em; }
      .box-title-ls.blue { color: #2563eb; }
      .box-title-ls.orange { color: #ea580c; }
      .box-sub-ls { color: #64748b; font-weight: 500; font-size: 0.8em; text-align:center; margin-bottom:8px; }
      
      .inner-box-ls { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 8px; }
      .tag-ls { background: #e2e8f0; color: #334155; padding: 2px 6px; border-radius: 4px; display:inline-block; margin: 2px; font-family: var(--mono); font-size:0.8em; font-weight:600; }
      
      .step-list-ls { list-style: none; padding: 0; margin: 0; font-size: 0.9em; line-height: 1.3; }
      .step-list-ls li { margin-bottom: 2px; }
      .step-list-ls li span { color: #ea580c; font-weight:bold; margin-right:4px; display:inline-block; width:12px; }
      
      .h-arrow-ls { display:flex; flex-direction:column; align-items:center; justify-content:center; color:#64748b; font-weight:bold; font-size:0.8em; text-align:center; padding: 0 8px; }
      .h-arrow-ls .arr { font-size: 2.5em; line-height:0.5; color:#94a3b8; margin:6px 0; }
      
      .v-arrow-ls { display:flex; flex-direction:column; align-items:center; justify-content:center; color:#64748b; font-weight:bold; font-size:0.75em; text-align:center; padding: 2px 0; }
      .v-arrow-ls .arr { font-size: 1.8em; line-height:0.5; color:#94a3b8; margin:4px 0; }
    </style>
    
    <div class="slide-head" style="margin-bottom:0">
      <span class="kicker teal"><span class="num">06</span> How It Works & Architecture</span>
      <h2 style="font-size:1.5em; margin:0;">Amazon Nova Architecture: <span class="accent">The 10-Second Funnel</span></h2>
    </div>
    
    <div class="grow col" style="justify-content:center; align-items:center;">
      <div class="arch-ls">
        
        <!-- Top: Customer -->
        <div class="box-ls" style="border-radius:30px; padding:6px 24px; text-align:center; width:auto; background:#f8fafc; border-color:#94a3b8; margin-top:-10px;">
           <div style="font-size:1.15em; font-weight:800; color:#334155;"><span class="glyph">👤</span> CUSTOMER &nbsp; <span style="color:#64748b; font-size:0.75em; font-weight:500;">Text / Voice / Photo</span></div>
        </div>
        
        <div class="v-arrow-ls" style="margin-top:-6px; margin-bottom:-6px;">
           <div>HTTPS / User Interaction</div><div class="arr">↓</div>
        </div>

        <!-- Middle: Front & Back -->
        <div style="display:flex; width:100%; align-items:stretch; gap:4px;">
           <!-- Frontend -->
           <div class="box-ls front" style="flex:1;">
              <div class="box-title-ls blue">REACT SPA</div>
              <div class="box-sub-ls">(Vite + TypeScript)</div>
              <div style="display:flex; gap:6px;">
                 <div class="inner-box-ls" style="flex:1; text-align:center;">
                    <div style="font-weight:700; color:#334155; font-size:0.9em; margin-bottom:4px;">React 19, Tailwind</div>
                    <div style="font-family:var(--mono); font-size:0.8em; line-height:1.4; color:#475569;">IntentBar, ProposalCard...</div>
                 </div>
                 <div class="inner-box-ls" style="display:flex; flex-direction:column; align-items:center; justify-content:center;">
                    <span class="glyph" style="font-size:1.6em;">📱</span><strong style="font-size:0.85em;">Mobile-First</strong>
                 </div>
              </div>
           </div>

           <!-- Arrow -->
           <div class="h-arrow-ls" style="width:85px; flex:0 0 auto;">
             <div>REST API</div><div class="arr">➔</div><div style="font-size:0.8em;font-weight:normal;">/intent</div>
           </div>

           <!-- Backend -->
           <div class="box-ls back" style="flex:1.6;">
              <div class="box-title-ls orange">EXPRESS BACKEND API</div>
              <div class="box-sub-ls">(Node.js + TypeScript)</div>
              <div style="display:flex; gap:6px;">
                 <div class="inner-box-ls" style="flex:1; text-align:center;">
                    <div style="font-size:0.85em; color:#ea580c; font-weight:800; margin-bottom:6px;">Internal Services</div>
                    <div class="tag-ls">catalog.ts</div> <div class="tag-ls">dynamodb.ts</div>
                    <div class="tag-ls">bedrock.ts</div> <div class="tag-ls">calendar.ts</div>
                 </div>
                 <div class="inner-box-ls" style="flex:1.2;">
                    <div style="text-align:center; font-size:0.85em; color:#ea580c; font-weight:800; margin-bottom:6px;">NOVA AGENT Pipeline</div>
                    <div style="display:grid; grid-template-columns: 1fr 1fr; gap:4px;">
                       <ul class="step-list-ls">
                          <li><span>1.</span> Parse Intent</li>
                          <li><span>2.</span> Context</li>
                          <li><span>3.</span> Decompose</li>
                          <li><span>4.</span> Search</li>
                       </ul>
                       <ul class="step-list-ls">
                          <li><span style="color:#ea580c">5.</span> <strong style="color:#ea580c">Assemble</strong></li>
                          <li><span>6.</span> Availability</li>
                          <li><span>7.</span> Budget</li>
                          <li><span>8.</span> Explain</li>
                       </ul>
                    </div>
                 </div>
              </div>
           </div>
        </div>

        <!-- DB arrows -->
        <div style="display:flex; width:100%; align-items:center; padding: 0 40px; margin-top:-4px; margin-bottom:-4px;">
           <div class="v-arrow-ls" style="flex:1;"><div>LLM Request</div><div class="arr">↓</div></div>
           <div class="v-arrow-ls" style="flex:1;"><div>Data R/W</div><div class="arr">↓</div></div>
           <div class="v-arrow-ls" style="flex:1;"><div>Read Events</div><div class="arr">↓</div></div>
        </div>

        <!-- Databases -->
        <div style="display:grid; grid-template-columns: 1fr 1fr 1fr; gap:12px; width:100%;">
           <div class="box-ls data-bed" style="padding:10px; text-align:center;">
              <div class="box-title-ls" style="color:#3b82f6; font-size:0.95em;">AWS BEDROCK</div>
              <div style="font-size:0.85em; color:#475569; font-weight:500;">Reasoning (Nova Lite)<br>Titan Embed V2</div>
           </div>
           <div class="box-ls data-dyn" style="padding:10px; text-align:center;">
              <div class="box-title-ls" style="color:#10b981; font-size:0.95em;">DYNAMODB</div>
              <div style="font-size:0.85em; color:#475569; font-weight:500;">Catalog (329 SKUs)<br>Users / Orders</div>
           </div>
           <div class="box-ls data-cal" style="padding:10px; text-align:center;">
              <div class="box-title-ls" style="color:#a855f7; font-size:0.95em;">GOOGLE CALENDAR</div>
              <div style="font-size:0.85em; color:#475569; font-weight:500;">Upcoming events<br>Proactive carts</div>
           </div>
        </div>
      </div>
    </div>
  </section>"""

with open('ppt-finale.html', 'r', encoding='utf-8') as f:
    text = f.read()

pattern = re.compile(r'<!-- 7 · HOW IT WORKS / ARCHITECTURE COMBINED -->\s*<section class="slide" data-section="pipeline">.*?</section>', re.DOTALL)
text = pattern.sub(landscape_arch_html, text)

with open('ppt-finale.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Landscape architecture diagram injected.")
