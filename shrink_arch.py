import re

v5_arch_html = """  <!-- 7 · HOW IT WORKS / ARCHITECTURE COMBINED -->
  <section class="slide" data-section="pipeline">
    <style>
      .arch-grid-v5 { 
         display: grid; 
         grid-template-columns: auto 30px auto 30px 240px 40px 260px; 
         gap: 6px; 
         align-items: start; 
         justify-content: center;
         font-family: var(--ff); 
         font-size: 0.7em; 
         width: 100%; 
         max-width: 1050px; 
         margin: 0 auto; 
         transform: scale(0.9); 
         transform-origin: top center; 
         margin-top: 0px; 
      }
      
      .box-v5 { background: #ffffff; border: 2px solid #e2e8f0; border-radius: 8px; padding: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); color:var(--ink); text-align:center; }
      
      .box-deploy { background: #fff7ed; border-color: #fdba74; }
      .box-front { border-color: #3b82f6; border-top-width: 4px; }
      .box-back { border-color: #ea580c; border-top-width: 4px; }
      
      .box-title { font-weight: 800; margin-bottom:4px; font-size:1.1em; }
      .box-sub { color: #64748b; font-weight: 500; font-size: 0.85em; margin-bottom:8px; }
      
      .inner-list { font-family:var(--mono); font-size:0.85em; line-height:1.5; color:#475569; margin:0; padding:0; list-style:none; }
      .inner-list li { margin-bottom:4px; }
      
      .h-arrow-v5 { display:flex; flex-direction:column; align-items:center; justify-content:center; color:#64748b; font-weight:600; font-size:0.85em; height:100%; }
      .h-arrow-v5 .arr { font-size: 2em; color:#94a3b8; margin:0; line-height:1; }
      
      .v-arrow-v5 { display:flex; flex-direction:column; align-items:center; justify-content:center; color:#64748b; font-weight:600; font-size:0.85em; padding: 0; margin:-2px 0; }
      .v-arrow-v5 .arr { font-size: 2em; line-height:0.8; color:#94a3b8; margin:0; }
      
      .step-list { text-align:left; list-style:none; padding:0; margin:0; font-size:0.9em; line-height:1.3; }
      .step-list li { margin-bottom:2px; }
      .step-list li span { color:#ea580c; font-weight:bold; width:14px; display:inline-block; }
      
      .db-box { border:2px solid #e2e8f0; border-radius:6px; padding:8px; font-size:0.85em; background:#f8fafc; font-weight:600; color:#334155; line-height:1.3; text-align:center; }
      .db-box ul { list-style:none; padding:0; margin:0; margin-top:6px; font-weight:500; font-size:0.85em; text-align:center; }
      .db-box ul li { margin-bottom:2px; }
    </style>
    
    <div class="slide-head" style="margin-bottom:0">
      <span class="kicker teal"><span class="num">06</span> How It Works & Architecture</span>
      <h2 style="font-size:1.5em; margin:0;">Amazon Nova Architecture: <span class="accent">The 10-Second Funnel</span></h2>
    </div>
    
    <div class="grow col" style="justify-content:center; align-items:center;">
      <div class="arch-grid-v5">
        
        <!-- ================= ROW 1: TOP HORIZONTAL INGRESS PIPELINE ================= -->
        
        <!-- 1: Customer -->
        <div class="box-v5" style="grid-column: 1; grid-row: 1; border-radius:30px; padding:8px 16px; background:#f8fafc; border-color:#94a3b8; align-self:center;">
           <div style="font-size:1.1em; font-weight:800; color:#334155;"><span class="glyph">👤</span> CUSTOMER</div>
        </div>
        
        <!-- 2: Arrow -->
        <div class="h-arrow-v5" style="grid-column: 2; grid-row: 1;"><div class="arr">➔</div></div>
        
        <!-- 3: CDN -->
        <div class="box-v5 box-deploy" style="grid-column: 3; grid-row: 1; align-self:center; padding:8px;">
           <div style="color:#ea580c; font-weight:800; font-size:0.95em;">DEPLOYMENT: AWS<br>CloudFront + S3</div>
           <div style="color:#c2410c; font-size:0.75em;">(Edge CDN)</div>
        </div>
        
        <!-- 4: Arrow -->
        <div class="h-arrow-v5" style="grid-column: 4; grid-row: 1;"><div class="arr">➔</div></div>
        
        <!-- 5: React SPA -->
        <div class="box-v5 box-front" style="grid-column: 5; grid-row: 1;">
           <div class="box-title" style="color:#2563eb;">React SPA</div>
           <div class="box-sub">(Vite + TypeScript)</div>
           <div style="background:#f0f9ff; border:1px solid #bae6fd; border-radius:6px; padding:8px; margin-top:4px;">
              <ul class="inner-list">
                 <li>IntentBar</li>
                 <li>CartProposalCard</li>
                 <li>EmergencyChips</li>
                 <li>SwipeCheckoutButton</li>
                 <li style="font-weight:bold; color:#0369a1; margin-top:6px;">Tailwind - Mobile-First</li>
              </ul>
           </div>
        </div>
        
        <!-- 6: REST API Arrow -->
        <div class="h-arrow-v5" style="grid-column: 6; grid-row: 1;">
           <div style="font-size:0.75em; text-align:center; line-height:1.1;">REST API<br>Requests</div>
           <div class="arr">➔</div>
        </div>
        
        <!-- 7: API Gateway -->
        <div class="box-v5 box-deploy" style="grid-column: 7; grid-row: 1; display:flex; flex-direction:column; justify-content:center; align-self:stretch;">
           <div style="color:#ea580c; font-weight:800; font-size:1.05em;">DEPLOYMENT: AWS<br>API Gateway + Lambda</div>
           <div style="color:#c2410c; font-size:0.85em; margin-top:4px;">(Serverless Compute)</div>
        </div>
        
        <!-- ================= ROW 2: ARROW DOWN FROM API GATEWAY ================= -->
        <div class="v-arrow-v5" style="grid-column: 7; grid-row: 2;">
           <div class="arr">↓</div>
        </div>
        
        <!-- ================= ROW 3: EXPRESS BACKEND (Spans col 5 to 7) ================= -->
        <div class="box-v5 box-back" style="grid-column: 5 / span 3; grid-row: 3; display:flex; flex-direction:column; padding:0; overflow:hidden;">
           <div style="background:#fff7ed; padding:6px; border-bottom:1px solid #ffedd5;">
              <div class="box-title" style="color:#ea580c; margin:0;">EXPRESS BACKEND API</div>
              <div class="box-sub" style="margin:0;">(Node.js + TypeScript)</div>
           </div>
           
           <div style="display:flex; padding:10px; gap:12px;">
              <!-- Internal Services -->
              <div style="flex:1.2; background:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; padding:8px;">
                 <div style="font-size:0.9em; color:#ea580c; font-weight:800; margin-bottom:6px;">Internal Services</div>
                 <ul class="inner-list" style="font-weight:600; display:flex; flex-wrap:wrap; gap:6px; justify-content:center;">
                    <li style="background:#e2e8f0; padding:2px 6px; border-radius:4px;">catalog.ts</li>
                    <li style="background:#e2e8f0; padding:2px 6px; border-radius:4px;">dynamodb.ts</li>
                    <li style="background:#e2e8f0; padding:2px 6px; border-radius:4px;">bedrock.ts</li>
                    <li style="background:#e2e8f0; padding:2px 6px; border-radius:4px;">calendar.ts</li>
                    <li style="background:#e2e8f0; padding:2px 6px; border-radius:4px;">vectorSrch</li>
                 </ul>
              </div>
              
              <!-- Nova Agent Pipeline -->
              <div style="flex:1; background:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; padding:8px;">
                 <div style="font-size:0.9em; color:#ea580c; font-weight:800; margin-bottom:6px;">NOVA AGENT Pipeline</div>
                 <div style="display:flex; gap:10px;">
                    <ul class="step-list" style="flex:1;">
                       <li><span>1.</span> Parse Intent</li>
                       <li><span>2.</span> Context</li>
                       <li><span>3.</span> Decompose</li>
                       <li><span>4.</span> Search</li>
                    </ul>
                    <ul class="step-list" style="flex:1;">
                       <li><span style="color:#ea580c">5.</span> <strong style="color:#ea580c">Assemble</strong></li>
                       <li><span>6.</span> Availability</li>
                       <li><span>7.</span> Budget Limit</li>
                       <li><span>8.</span> Explain</li>
                    </ul>
                 </div>
              </div>
           </div>
        </div>
        
        <!-- ================= ROW 4: BRANCHING ARROWS ================= -->
        <div style="grid-column: 5 / span 3; grid-row: 4; display:flex; width:100%; margin-top:2px;">
           <div style="flex:1.2; display:flex; justify-content:center;">
              <div class="v-arrow-v5"><div class="arr">↓</div></div>
           </div>
           <div style="flex:1; display:flex; justify-content:center;">
              <div class="v-arrow-v5"><div class="arr">↓</div></div>
           </div>
        </div>
        
        <!-- ================= ROW 5: DATABASES ================= -->
        <div style="grid-column: 1 / span 7; grid-row: 5; display:flex; width:100%; gap:8px;">
           
           <div class="db-box" style="border-color:#10b981; flex:1;">
              <div style="color:#047857; font-weight:800;">DynamoDB</div>
              <ul>
                 <li>- Catalog (400+ SKUs)</li>
                 <li>- Users (Learned Prefs)</li>
                 <li>- Order History</li>
              </ul>
           </div>
           
           <div class="db-box" style="border-color:#a855f7; flex:1;">
              <div style="color:#7e22ce; font-weight:800;">Google Calendar API</div>
              <ul>
                 <li>- OAuth 2.0 (HTTP-Only)</li>
                 <li>- Events for Proactive Carts</li>
              </ul>
           </div>
           
           <div class="db-box" style="border-color:#64748b; flex:1; display:flex; flex-direction:column; justify-content:center;">
              <div style="color:#334155; font-weight:800;">In-Memory Vector Store</div>
              <div style="font-weight:500; margin-top:6px;">(Cosine Similarity)</div>
           </div>
           
           <div class="db-box" style="border-color:#3b82f6; flex:1.2; display:flex; flex-direction:column; justify-content:center;">
              <div style="color:#1d4ed8; font-weight:800; font-size:1.05em;">AWS Bedrock</div>
              <ul style="margin-top:8px;">
                 <li>- Nova Lite (Reasoning & Vision)</li>
                 <li>- Titan Embed V2 (256-dim Vectors)</li>
              </ul>
           </div>
           
        </div>
        
      </div>
    </div>
  </section>"""

with open('ppt-finale.html', 'r', encoding='utf-8') as f:
    text = f.read()

pattern = re.compile(r'<!-- 7 · HOW IT WORKS / ARCHITECTURE COMBINED -->\s*<section class="slide" data-section="pipeline">.*?</section>', re.DOTALL)
text = pattern.sub(v5_arch_html, text)

with open('ppt-finale.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Architecture diagram v5 (L-Shape horizontal layout) injected.")
