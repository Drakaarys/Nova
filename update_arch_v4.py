import re

v4_arch_html = """  <!-- 7 · HOW IT WORKS / ARCHITECTURE COMBINED -->
  <section class="slide" data-section="pipeline">
    <style>
      .arch-grid { 
         display: grid; 
         grid-template-columns: 300px 120px 620px; 
         gap: 12px; 
         align-items: start; 
         justify-content: center;
         font-family: var(--ff); 
         font-size: 0.72em; 
         width: 100%; 
         max-width: 1100px; 
         margin: 0 auto; 
         transform: scale(0.85); 
         transform-origin: top center; 
         margin-top: -15px; 
      }
      
      .box-v4 { background: #ffffff; border: 2px solid #e2e8f0; border-radius: 8px; padding: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); color:var(--ink); width:100%; text-align:center; }
      
      .box-deploy { background: #fff7ed; border-color: #fdba74; }
      .box-front { border-color: #3b82f6; border-top-width: 4px; }
      .box-back { border-color: #ea580c; border-top-width: 4px; }
      
      .box-title { font-weight: 800; margin-bottom:4px; font-size:1.1em; }
      .box-sub { color: #64748b; font-weight: 500; font-size: 0.85em; margin-bottom:8px; }
      
      .inner-list { font-family:var(--mono); font-size:0.85em; line-height:1.6; color:#475569; margin:0; padding:0; list-style:none; }
      .inner-list li { margin-bottom:4px; }
      
      .v-arrow-v4 { display:flex; flex-direction:column; align-items:center; justify-content:center; color:#64748b; font-weight:600; font-size:0.85em; line-height:1.2; padding: 0; margin:-4px 0; }
      .v-arrow-v4 .arr { font-size: 2em; line-height:0.5; color:#94a3b8; margin:6px 0; }
      
      .h-arrow-v4 { display:flex; flex-direction:column; align-items:center; justify-content:center; color:#64748b; font-weight:600; font-size:0.85em; line-height:1.2; height:100%; }
      .h-arrow-v4 .arr { font-size: 3em; line-height:0.5; color:#94a3b8; margin:8px 0; }
      
      .step-list { text-align:left; list-style:none; padding:0; margin:0; font-size:0.9em; line-height:1.4; }
      .step-list li { margin-bottom:3px; }
      .step-list li span { color:#ea580c; font-weight:bold; width:14px; display:inline-block; }
      
      .db-box { border:2px solid #e2e8f0; border-radius:6px; padding:10px; font-size:0.85em; background:#f8fafc; font-weight:600; color:#334155; line-height:1.4; text-align:center; }
      .db-box ul { list-style:none; padding:0; margin:0; margin-top:6px; font-weight:500; font-size:0.9em; text-align:center; }
      .db-box ul li { margin-bottom:4px; }
    </style>
    
    <div class="slide-head" style="margin-bottom:0">
      <span class="kicker teal"><span class="num">06</span> How It Works & Architecture</span>
      <h2 style="font-size:1.5em; margin:0;">Amazon Nova Architecture: <span class="accent">The 10-Second Funnel</span></h2>
    </div>
    
    <div class="grow col" style="justify-content:center; align-items:center;">
      <div class="arch-grid">
        
        <!-- Row 1: Customer -->
        <div style="grid-column: 1; grid-row: 1; display:flex; justify-content:center;">
           <div class="box-v4" style="border-radius:30px; padding:8px 24px; background:#f8fafc; border-color:#94a3b8; width:auto;">
              <div style="font-size:1.15em; font-weight:800; color:#334155;"><span class="glyph">👤</span> CUSTOMER</div>
           </div>
        </div>
        
        <!-- Row 2: Arrow -->
        <div class="v-arrow-v4" style="grid-column: 1; grid-row: 2;">
           <div class="arr">↓</div>
        </div>
        
        <!-- Row 3: Deployment CDN -->
        <div class="box-v4 box-deploy" style="grid-column: 1; grid-row: 3;">
           <div style="color:#ea580c; font-weight:800; font-size:1.05em;">DEPLOYMENT: AWS CloudFront + S3</div>
           <div style="color:#c2410c; font-size:0.85em;">(Global Edge CDN Distribution)</div>
        </div>
        
        <!-- Row 4: Arrow -->
        <div class="v-arrow-v4" style="grid-column: 1; grid-row: 4;">
           <div class="arr">↓</div>
        </div>
        
        <!-- Row 5: React SPA & Arrow & API Gateway -->
        <div class="box-v4 box-front" style="grid-column: 1; grid-row: 5;">
           <div class="box-title" style="color:#2563eb;">React SPA (Vite + TypeScript)</div>
           <div style="background:#f0f9ff; border:1px solid #bae6fd; border-radius:6px; padding:12px; margin-top:8px;">
              <ul class="inner-list">
                 <li>IntentBar</li>
                 <li>CartProposalCard</li>
                 <li>EmergencyChips</li>
                 <li>SwipeCheckoutButton</li>
                 <li style="font-weight:bold; color:#0369a1; margin-top:8px;">Tailwind CSS - Mobile-First</li>
              </ul>
           </div>
        </div>
        
        <!-- Arrow pointing from React to API Gateway -->
        <div class="h-arrow-v4" style="grid-column: 2; grid-row: 5;">
           <div style="background:#f1f5f9; padding:4px 8px; border-radius:4px; border:1px solid #cbd5e1;">REST API Requests</div>
           <div class="arr">➔</div>
        </div>
        
        <!-- API Gateway (Aligned with React SPA) -->
        <div class="box-v4 box-deploy" style="grid-column: 3; grid-row: 5; display:flex; flex-direction:column; justify-content:center;">
           <div style="color:#ea580c; font-weight:800; font-size:1.05em;">DEPLOYMENT: AWS API Gateway + Lambda</div>
           <div style="color:#c2410c; font-size:0.85em;">(Serverless Compute)</div>
        </div>
        
        <!-- Row 6: Arrow Down to Express Backend -->
        <div class="v-arrow-v4" style="grid-column: 3; grid-row: 6;">
           <div class="arr">↓</div>
        </div>
        
        <!-- Row 7: Express Backend API -->
        <div class="box-v4 box-back" style="grid-column: 3; grid-row: 7; display:flex; flex-direction:column; padding:0; overflow:hidden;">
           <div style="background:#fff7ed; padding:8px; border-bottom:1px solid #ffedd5;">
              <div class="box-title" style="color:#ea580c; margin:0;">EXPRESS BACKEND API</div>
              <div class="box-sub" style="margin:0;">(Node.js + TypeScript)</div>
           </div>
           
           <div style="display:flex; padding:12px; gap:12px;">
              <!-- Internal Services -->
              <div style="flex:1.5; background:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; padding:10px;">
                 <div style="font-size:0.9em; color:#ea580c; font-weight:800; margin-bottom:8px;">Internal Services</div>
                 <ul class="inner-list" style="font-weight:600; display:flex; flex-wrap:wrap; gap:8px; justify-content:center;">
                    <li style="background:#e2e8f0; padding:4px 8px; border-radius:4px;">catalog.ts</li>
                    <li style="background:#e2e8f0; padding:4px 8px; border-radius:4px;">dynamodb.ts</li>
                    <li style="background:#e2e8f0; padding:4px 8px; border-radius:4px;">bedrock.ts</li>
                    <li style="background:#e2e8f0; padding:4px 8px; border-radius:4px;">calendar.ts</li>
                    <li style="background:#e2e8f0; padding:4px 8px; border-radius:4px;">vectorSrch</li>
                 </ul>
              </div>
              
              <!-- Nova Agent Pipeline -->
              <div style="flex:1; background:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; padding:10px;">
                 <div style="font-size:0.9em; color:#ea580c; font-weight:800; margin-bottom:8px;">NOVA AGENT Pipeline</div>
                 <ul class="step-list">
                    <li><span>1.</span> Parse Intent</li>
                    <li><span>2.</span> Get User Context</li>
                    <li><span>3.</span> Decompose Recipe</li>
                    <li><span>4.</span> Search Candidates</li>
                    <li><span style="color:#ea580c">5.</span> <strong style="color:#ea580c">Assemble Cart (LLM)</strong></li>
                    <li><span>6.</span> Enforce Availability</li>
                    <li><span>7.</span> Enforce Budget</li>
                    <li><span>8.</span> Explain & Return</li>
                 </ul>
              </div>
           </div>
        </div>
        
        <!-- Row 8: Branching Arrows to DBs -->
        <div style="grid-column: 3; grid-row: 8; display:flex; width:100%; margin-top:2px;">
           <!-- Left branch from Internal Services -->
           <div style="flex:1.5; display:flex; flex-direction:column; align-items:center; padding-right:12px;">
              <div class="v-arrow-v4"><div class="arr">↓</div></div>
           </div>
           <!-- Right branch from Nova Agent -->
           <div style="flex:1; display:flex; flex-direction:column; align-items:center; padding-left:12px;">
              <div class="v-arrow-v4"><div class="arr">↓</div></div>
           </div>
        </div>
        
        <!-- Row 9: Databases -->
        <div style="grid-column: 3; grid-row: 9; display:flex; width:100%;">
           <!-- 3 DBs from Internal Services -->
           <div style="flex:1.5; display:flex; gap:8px; padding-right:8px;">
              <div class="db-box" style="border-color:#10b981; flex:1;">
                 <div style="color:#047857; font-weight:800;">DynamoDB</div>
                 <ul>
                    <li>- Catalog (400+ SKUs)</li>
                    <li>- Users (Learned Prefs from Edits)</li>
                    <li>- Order History</li>
                 </ul>
              </div>
              
              <div class="db-box" style="border-color:#a855f7; flex:1;">
                 <div style="color:#7e22ce; font-weight:800;">Google Calendar API</div>
                 <ul>
                    <li>- OAuth 2.0 (HTTP-Only Cookies)</li>
                    <li>- Reads events for Proactive Carts</li>
                 </ul>
              </div>
              
              <div class="db-box" style="border-color:#64748b; flex:1; display:flex; flex-direction:column; justify-content:center;">
                 <div style="color:#334155; font-weight:800;">In-Memory Vector Store</div>
                 <div style="font-weight:500; margin-top:8px;">(Cosine Similarity matching)</div>
              </div>
           </div>
           
           <!-- Bedrock from Nova Agent -->
           <div style="flex:1; padding-left:8px;">
              <div class="db-box" style="border-color:#3b82f6; height:100%; display:flex; flex-direction:column; justify-content:center;">
                 <div style="color:#1d4ed8; font-weight:800; font-size:1.1em;">AWS Bedrock</div>
                 <ul style="margin-top:12px; font-size:0.95em;">
                    <li>- Nova Lite (Reasoning & Vision)</li>
                    <li>- Titan Embed V2 (256-dim Vectors)</li>
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
text = pattern.sub(v4_arch_html, text)

with open('ppt-finale.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Architecture diagram v4 injected.")
