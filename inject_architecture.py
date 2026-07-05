import re

arch_html = """  <!-- 7 · HOW IT WORKS / ARCHITECTURE COMBINED -->
  <section class="slide" data-section="pipeline">
    <style>
      .arch-wrap {
        display: grid;
        grid-template-columns: 1.2fr 2fr;
        grid-template-rows: auto auto auto;
        gap: 20px;
        font-size: 0.75em;
        position: relative;
        font-family: var(--ff);
        margin-top: 1rem;
        width: 100%;
        max-width: 900px;
      }
      .arch-box {
        background: #18181b;
        color: #fff;
        border: 2px solid #FF9900;
        border-radius: 8px;
        padding: 16px;
        position: relative;
        box-shadow: var(--shadow-md);
      }
      .arch-box-title {
        font-weight: 800;
        text-transform: uppercase;
        border-bottom: 1px solid rgba(255,255,255,0.2);
        padding-bottom: 8px;
        margin-bottom: 8px;
        font-size: 1.1em;
        text-align: center;
      }
      .arch-box-sub { color: #a1a1aa; font-weight: 500; font-size: 0.85em; text-align:center; margin-top:-4px; margin-bottom:8px; }
      .customer-box {
        grid-column: 1 / -1;
        background: #18181b; border: 2px solid #fff; border-radius: 30px;
        text-align: center; color: #fff; padding: 10px 30px; justify-self: center;
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        z-index: 10; width: 340px;
      }
      
      .bottom-row {
        grid-column: 1 / -1;
        display: grid;
        grid-template-columns: 1fr 1.1fr 1fr;
        gap: 16px;
        margin-top: 10px;
      }
      .nested-box {
        border: 1px solid rgba(255,255,255,0.2);
        border-radius: 6px;
        padding: 8px;
        background: rgba(255,255,255,0.03);
      }
      
      .tag { background: rgba(255,255,255,0.1); padding: 4px 8px; border-radius: 4px; display:inline-block; margin: 3px; font-size: 0.9em; font-family: var(--mono); }
      .step-list { list-style: none; padding: 0; margin: 0; line-height: 1.4; font-size: 0.95em; }
      .step-list li { margin-bottom: 4px; }
      .step-list li span { color: #FF9900; font-weight:bold; margin-right:4px; }
      
      .lbl { font-size:0.75em; color:var(--ink); position:absolute; font-weight:700; text-align:center; line-height:1.2; z-index:5; background:var(--bg); }
    </style>
    
    <div class="slide-head" style="margin-bottom:0">
      <span class="kicker teal"><span class="num">06</span> How It Works & Architecture</span>
      <h2 style="font-size:1.6em">Amazon Nova Architecture: <span class="accent">The 10-Second Funnel</span></h2>
    </div>
    
    <div class="grow col" style="justify-content:center; align-items:center; position:relative;">
      
      <!-- SVG Lines in background -->
      <svg style="position:absolute; inset:0; pointer-events:none; z-index:0; width:100%; height:100%;">
         <defs>
           <marker id="arrowhead" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
             <polygon points="0 0, 6 3, 0 6" fill="#333" />
           </marker>
           <marker id="arrowhead-thick" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
             <polygon points="0 0, 6 3, 0 6" fill="#333" />
           </marker>
         </defs>
         
         <!-- Customer to React -->
         <path d="M 450, 45 L 200, 45 L 200, 60" stroke="#333" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
         
         <!-- React to Express -->
         <path d="M 370, 180 L 415, 180" stroke="#333" stroke-width="4" fill="none" marker-end="url(#arrowhead-thick)"/>
         
         <!-- React to Bedrock (down) -->
         <path d="M 120, 310 L 120, 340" stroke="#333" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
         <!-- Bedrock to React (up) -->
         <path d="M 220, 340 L 220, 310" stroke="#333" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
         
         <!-- Backend to DynamoDB -->
         <path d="M 580, 310 L 580, 340" stroke="#333" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
         <path d="M 520, 340 L 520, 310" stroke="#333" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>

         <!-- Backend to Calendar -->
         <path d="M 800, 310 L 800, 340" stroke="#333" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
         <path d="M 840, 340 L 840, 310" stroke="#333" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
      </svg>

      <div class="arch-wrap">
        
        <!-- Customer -->
        <div class="customer-box" style="grid-column: 1 / -1;">
          <div style="font-size:1.2em; font-weight:bold;"><span class="glyph">👤</span> CUSTOMER</div>
          <div style="color:#a1a1aa; font-size:0.85em; margin-top:4px;">Action: State your need (Text/Voice/Photo)</div>
        </div>

        <!-- Left Box: Frontend -->
        <div class="arch-box" style="grid-column: 1;">
          <div class="arch-box-title">REACT SPA WEB APPLICATION</div>
          <div class="arch-box-sub">(Vite + TypeScript)</div>
          
          <div style="display:flex; gap:12px;">
            <div style="flex:1;">
               <div class="nested-box" style="text-align:center; margin-bottom:8px;">React 19, Tailwind 4, Lucide Icons</div>
               <div class="nested-box" style="font-family:var(--mono); font-size:0.75em; text-align:center; padding:12px 8px; line-height:1.4;">
                 IntentBar, CartProposalCard, EmergencyChips, ReorderStrip, SwipeCheckoutButton, ProductOverlay, LiveDeliveryRadar
               </div>
            </div>
            <div class="nested-box" style="width:70px; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center;">
              <span class="glyph" style="font-size:2em; margin-bottom:4px;">📱</span><br><span style="font-size:0.8em">Mobile-First</span>
            </div>
          </div>
          <div class="nested-box" style="text-align:center; margin-top:8px; border-color:#FF9900; color:#FF9900; font-weight:bold;">Browser Cookie Storage</div>
        </div>

        <!-- Right Box: Backend -->
        <div class="arch-box" style="grid-column: 2; display:flex; gap:16px;">
          <div style="writing-mode: vertical-rl; transform: rotate(180deg); text-align:center; font-weight:bold; letter-spacing:1px; border-left:1px solid rgba(255,255,255,0.2); padding-left:8px; display:flex; align-items:center; justify-content:center;">
            API GATEWAY / ROUTING
          </div>
          
          <div style="flex:1;">
            <div class="arch-box-title" style="color:#FF9900">EXPRESS BACKEND API</div>
            <div class="arch-box-sub">(Node.js + TypeScript)</div>
            
            <div style="display:flex; gap:12px; margin-top:12px;">
              <div class="nested-box" style="flex:1; text-align:center;">
                <div style="font-size:0.85em; color:#FF9900; font-weight:bold; margin-bottom:6px;">Internal Services</div>
                <div class="tag">catalog.ts</div><br>
                <div class="tag">dynamodb.ts</div><br>
                <div class="tag">bedrock.ts</div><br>
                <div class="tag">calendar.ts</div><br>
                <div class="tag">vectorSrch</div><br>
                <div class="tag">userCtx.ts</div>
              </div>
              <div class="nested-box" style="flex:1.4;">
                <div style="text-align:center; font-size:0.85em; color:#FF9900; font-weight:bold; margin-bottom:6px;">NOVA AGENT<br><span style="font-size:0.8em;font-weight:normal;color:#aaa">(8-Step Pipeline)</span></div>
                <ul class="step-list">
                  <li><span>1.</span> Parse Intent</li>
                  <li><span>2.</span> Get User Context</li>
                  <li><span>3.</span> Decompose Recipe</li>
                  <li><span>4.</span> Search Candidates</li>
                  <li><span style="color:#FF9900">5.</span> <strong style="color:#FF9900">Assemble Cart (LLM)</strong></li>
                  <li><span>6.</span> Enforce Availability</li>
                  <li><span>7.</span> Enforce Budget</li>
                  <li><span>8.</span> Explain & Return</li>
                </ul>
              </div>
            </div>
          </div>
        </div>

        <!-- Bottom Row (3 items) -->
        <div class="bottom-row">
          <div class="arch-box" style="border-color:#3b82f6;">
            <div class="arch-box-title" style="border-bottom-color:rgba(59,130,246,0.5)">AWS BEDROCK</div>
            <div class="arch-box-sub">(External LLM)</div>
            <ul style="padding-left:16px; margin-top:8px; font-size:0.9em; color:#ddd; line-height:1.4">
              <li>Reasoning & Vision (Nova Lite)</li>
              <li>Titan Embed V2 (256-dim Vectors)</li>
            </ul>
          </div>
          
          <div class="arch-box" style="border-color:#10b981;">
            <div class="arch-box-title" style="border-bottom-color:rgba(16,185,129,0.5)">DYNAMODB</div>
            <div class="arch-box-sub">(External Database)</div>
            <ul style="padding-left:16px; margin-top:8px; font-size:0.9em; color:#ddd; line-height:1.4">
              <li>Catalog (329 SKUs)</li>
              <li>Users (profiles + prefs)</li>
              <li>Orders (history)</li>
            </ul>
          </div>
          
          <div class="arch-box" style="border-color:#a855f7;">
            <div class="arch-box-title" style="border-bottom-color:rgba(168,85,247,0.5)">GOOGLE CALENDAR API</div>
            <div class="arch-box-sub">(External API)</div>
            <ul style="padding-left:16px; margin-top:8px; font-size:0.9em; color:#ddd; line-height:1.4">
              <li>Read upcoming events</li>
              <li>Build proactive carts</li>
            </ul>
          </div>
        </div>

        <!-- Floating Labels -->
        <div class="lbl" style="top:25px; left:230px;">HTTPS/User Interaction</div>
        
        <div class="lbl" style="top:150px; left:375px; text-align:center;">HTTPS /<br>REST API<br>REQUESTS</div>
        <div class="lbl" style="top:205px; left:375px; text-align:center; font-weight:500;">/intent, /proactive,<br>/auth, etc.</div>
        
        <div class="lbl" style="top:320px; left:0px;">LLM Request<br>(Intent, Context) →</div>
        <div class="lbl" style="top:320px; left:160px; text-align:left;">← Response<br>(Cart Proposal with reasons)</div>
        
        <div class="lbl" style="top:320px; left:390px; text-align:left;">Semantic Vector Search (Step 4)<br>Catalog lookup (Step 6)<br>Budget lookup (Step 7)<br>Data R/W (Catalog, Users, Orders)</div>
        
        <div class="lbl" style="top:320px; left:670px; text-align:left;">Read Events →<br>← Events for Proactive Carts</div>
        
        <div class="lbl" style="top:315px; right:0px; text-align:right;">Conceptual OAuth<br>Token/Cookie Flow<br>(HTTP-Only 24hr persist)</div>
        
      </div>
    </div>
  </section>"""

with open('ppt-finale.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the pipeline block entirely
pattern = re.compile(r'<!-- 7 · HOW IT WORKS / ARCHITECTURE COMBINED -->\s*<section class="slide" data-section="pipeline">.*?</section>', re.DOTALL)
text = pattern.sub(arch_html, text)

with open('ppt-finale.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Architecture diagram injected.")
