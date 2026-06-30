import re

fixed_arch_html = """  <!-- 7 · HOW IT WORKS / ARCHITECTURE COMBINED -->
  <section class="slide" data-section="pipeline">
    <style>
      .arch { font-family: var(--ff); font-size: 0.72em; display:flex; flex-direction:column; gap:12px; width:100%; max-width:960px; margin:0 auto; margin-top:0.5rem; }
      .box { background: #18181b; border: 2px solid #555; border-radius: 8px; padding: 12px; box-shadow: var(--shadow-md); color:#fff; position:relative; }
      .box.front { border-color: #3b82f6; }
      .box.back { border-color: #FF9900; }
      .box.data { border-color: #10b981; }
      .box.api { border-color: #a855f7; }
      
      .box-title { font-weight: 800; text-align: center; border-bottom: 1px solid rgba(255,255,255,0.2); padding-bottom:6px; margin-bottom:6px; font-size:1.1em; }
      .box-sub { color: #a1a1aa; font-weight: 500; font-size: 0.85em; text-align:center; margin-top:-4px; margin-bottom:8px; }
      
      .tag { background: rgba(255,255,255,0.1); padding: 4px 6px; border-radius: 4px; display:inline-block; margin: 2px; font-family: var(--mono); font-size:0.85em; }
      .step-list { list-style: none; padding: 0; margin: 0; font-size: 0.9em; line-height: 1.4; }
      .step-list li { margin-bottom: 2px; }
      .step-list li span { color: #FF9900; font-weight:bold; margin-right:4px; }
      
      .flow-row { display:flex; align-items:flex-start; justify-content:center; gap:12px; width:100%; }
      
      .arrow-box { display:flex; flex-direction:column; align-items:center; justify-content:center; padding-top:40px; color:#555; font-weight:bold; font-size:0.75em; text-align:center; line-height:1.2; }
      .arrow-box .arr { font-size: 3em; line-height:0.5; color:#333; margin:8px 0; }
      
      .v-arrow { display:flex; flex-direction:column; align-items:center; justify-content:center; color:#555; font-weight:bold; font-size:0.75em; text-align:center; line-height:1.2; }
      .v-arrow .arr { font-size: 2em; line-height:0.5; color:#333; margin:4px 0; }
    </style>
    
    <div class="slide-head" style="margin-bottom:0">
      <span class="kicker teal"><span class="num">06</span> How It Works & Architecture</span>
      <h2 style="font-size:1.5em; margin:0;">Amazon Nova Architecture: <span class="accent">The 10-Second Funnel</span></h2>
    </div>
    
    <div class="grow col" style="justify-content:center; align-items:center;">
      <div class="arch">
        
        <!-- Top: Customer -->
        <div style="display:flex; justify-content:center;">
          <div class="box" style="border-radius:30px; padding:6px 24px; text-align:center; border-color:#fff;">
            <div style="font-size:1.2em; font-weight:bold;"><span class="glyph">👤</span> CUSTOMER</div>
            <div style="color:#a1a1aa; font-size:0.85em; margin-top:2px;">Action: State your need (Text/Voice/Photo)</div>
          </div>
        </div>
        
        <div class="v-arrow" style="margin-top:-8px; margin-bottom:-8px;">
          <div>HTTPS / User Interaction</div>
          <div class="arr">↓</div>
        </div>

        <!-- Middle: Frontend & Backend -->
        <div class="flow-row">
          
          <!-- Frontend -->
          <div class="box front" style="flex:1;">
            <div class="box-title" style="color:#3b82f6;">REACT SPA WEB APPLICATION</div>
            <div class="box-sub">(Vite + TypeScript)</div>
            <div style="display:flex; gap:8px;">
              <div style="flex:1; border:1px solid rgba(255,255,255,0.1); padding:8px; border-radius:6px; background:rgba(255,255,255,0.02);">
                <div style="text-align:center; margin-bottom:6px; font-weight:bold;">React 19, Tailwind 4, Lucide Icons</div>
                <div style="font-family:var(--mono); font-size:0.8em; text-align:center; line-height:1.4;">IntentBar, CartProposalCard, EmergencyChips, ReorderStrip, SwipeCheckoutButton</div>
              </div>
              <div style="border:1px solid rgba(255,255,255,0.1); padding:8px; border-radius:6px; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; background:rgba(255,255,255,0.02);">
                <span class="glyph" style="font-size:1.8em; margin-bottom:4px;">📱</span><br>Mobile-First
              </div>
            </div>
            <div style="text-align:center; margin-top:8px; border:1px solid #FF9900; color:#FF9900; padding:4px; border-radius:6px; font-weight:bold;">Browser Cookie Storage</div>
          </div>
          
          <!-- Arrow -->
          <div class="arrow-box" style="width:110px; flex:0 0 auto;">
            <div>HTTPS / REST</div>
            <div class="arr">➔</div>
            <div>/intent, /auth</div>
          </div>

          <!-- Backend -->
          <div class="box back" style="flex:1.4; display:flex; gap:12px;">
            <div style="writing-mode: vertical-rl; transform: rotate(180deg); text-align:center; font-weight:bold; letter-spacing:1px; border-left:1px solid rgba(255,255,255,0.2); padding-left:4px; display:flex; align-items:center; justify-content:center; color:#FF9900;">
              API GATEWAY / ROUTING
            </div>
            <div style="flex:1;">
              <div class="box-title" style="color:#FF9900;">EXPRESS BACKEND API</div>
              <div class="box-sub">(Node.js + TypeScript)</div>
              
              <div style="display:flex; gap:8px;">
                <div style="flex:1; border:1px solid rgba(255,255,255,0.1); padding:8px; border-radius:6px; background:rgba(255,255,255,0.02); text-align:center;">
                  <div style="font-size:0.85em; color:#FF9900; font-weight:bold; margin-bottom:6px;">Internal Services</div>
                  <div class="tag">catalog.ts</div> <div class="tag">dynamodb.ts</div> <div class="tag">bedrock.ts</div> <div class="tag">calendar.ts</div> <div class="tag">vectorSrch</div>
                </div>
                <div style="flex:1.2; border:1px solid rgba(255,255,255,0.1); padding:8px; border-radius:6px; background:rgba(255,255,255,0.02);">
                  <div style="text-align:center; font-size:0.85em; color:#FF9900; font-weight:bold; margin-bottom:6px;">NOVA AGENT</div>
                  <ul class="step-list">
                    <li><span>1.</span> Parse Intent</li>
                    <li><span>2.</span> Get Context</li>
                    <li><span>3.</span> Decompose</li>
                    <li><span>4.</span> Vector Search</li>
                    <li><span style="color:#FF9900">5.</span> <strong style="color:#FF9900">Assemble (LLM)</strong></li>
                    <li><span>6.</span> Enforce Budget</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
          
        </div>
        
        <!-- Vertical arrows to databases -->
        <div class="flow-row" style="margin-top:-6px; margin-bottom:-6px;">
          <div class="v-arrow" style="flex:1;">
            <div class="arr">⇅</div>
            <div>LLM Request (Intent)</div>
          </div>
          <div class="arrow-box" style="width:110px; flex:0 0 auto; padding-top:0;"></div>
          <div class="flow-row" style="flex:1.4; gap:12px;">
             <div class="v-arrow" style="flex:1;">
               <div class="arr">⇅</div>
               <div>Data R/W (Catalog)</div>
             </div>
             <div class="v-arrow" style="flex:1;">
               <div class="arr">⇅</div>
               <div>Read Events</div>
             </div>
          </div>
        </div>

        <!-- Bottom: Databases -->
        <div class="flow-row">
          
          <div class="box front" style="flex:1;">
            <div class="box-title" style="color:#3b82f6;">AWS BEDROCK</div>
            <div class="box-sub">(External LLM)</div>
            <ul style="padding-left:16px; margin:0; font-size:0.9em; color:#ddd; line-height:1.4;">
              <li>Reasoning (Nova Lite)</li>
              <li>Titan Embed V2 (Vectors)</li>
            </ul>
          </div>
          
          <div class="arrow-box" style="width:110px; flex:0 0 auto; padding-top:0;"></div>

          <div class="flow-row" style="flex:1.4; gap:12px;">
            <div class="box data" style="flex:1;">
              <div class="box-title" style="color:#10b981;">DYNAMODB</div>
              <div class="box-sub">(External Database)</div>
              <ul style="padding-left:16px; margin:0; font-size:0.9em; color:#ddd; line-height:1.4;">
                <li>Catalog (329 SKUs)</li>
                <li>Users / Orders</li>
              </ul>
            </div>
            
            <div class="box api" style="flex:1;">
              <div class="box-title" style="color:#a855f7;">GOOGLE CALENDAR</div>
              <div class="box-sub">(External API)</div>
              <ul style="padding-left:16px; margin:0; font-size:0.9em; color:#ddd; line-height:1.4;">
                <li>Upcoming events</li>
                <li>Proactive carts</li>
              </ul>
            </div>
          </div>
          
        </div>

      </div>
    </div>
  </section>"""

with open('ppt-finale.html', 'r', encoding='utf-8') as f:
    text = f.read()

pattern = re.compile(r'<!-- 7 · HOW IT WORKS / ARCHITECTURE COMBINED -->\s*<section class="slide" data-section="pipeline">.*?</section>', re.DOTALL)
text = pattern.sub(fixed_arch_html, text)

with open('ppt-finale.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Architecture diagram fixed using flexbox.")
