import re

v3_arch_html = """  <!-- 7 · HOW IT WORKS / ARCHITECTURE COMBINED -->
  <section class="slide" data-section="pipeline">
    <style>
      .arch-v3 { font-family: var(--ff); font-size: 0.75em; display:flex; justify-content:center; align-items:flex-start; width:100%; max-width:1050px; margin:0 auto; gap: 16px; transform: scale(0.9); transform-origin: top center; margin-top:-10px; }
      
      .col-left { display:flex; flex-direction:column; align-items:center; width: 320px; flex-shrink:0; }
      .col-mid { display:flex; flex-direction:column; justify-content:center; margin-top: 280px; width:120px; flex-shrink:0; }
      .col-right { display:flex; flex-direction:column; align-items:center; width: 560px; flex-shrink:0; }
      
      .box-v3 { background: #ffffff; border: 2px solid #e2e8f0; border-radius: 8px; padding: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); color:var(--ink); width:100%; text-align:center; }
      
      .box-deploy { background: #fff7ed; border-color: #fdba74; }
      .box-front { border-color: #3b82f6; border-top-width: 4px; }
      .box-back { border-color: #ea580c; border-top-width: 4px; }
      
      .box-title { font-weight: 800; margin-bottom:4px; font-size:1.1em; }
      .box-sub { color: #64748b; font-weight: 500; font-size: 0.85em; margin-bottom:8px; }
      
      .inner-list { font-family:var(--mono); font-size:0.85em; line-height:1.6; color:#475569; margin:0; padding:0; list-style:none; }
      .inner-list li { margin-bottom:4px; }
      
      .v-arrow-v3 { display:flex; flex-direction:column; align-items:center; color:#64748b; font-weight:600; font-size:0.8em; line-height:1.2; padding: 4px 0; }
      .v-arrow-v3 .arr { font-size: 1.8em; line-height:0.6; color:#94a3b8; margin:4px 0; }
      
      .h-arrow-v3 { display:flex; flex-direction:column; align-items:center; color:#64748b; font-weight:600; font-size:0.8em; line-height:1.2; }
      .h-arrow-v3 .arr { font-size: 2.5em; line-height:0.6; color:#94a3b8; margin:4px 0; }
      
      .step-list { text-align:left; list-style:none; padding:0; margin:0; font-size:0.9em; line-height:1.4; }
      .step-list li { margin-bottom:3px; }
      .step-list li span { color:#ea580c; font-weight:bold; width:14px; display:inline-block; }
      
      .db-box { border:2px solid #e2e8f0; border-radius:6px; padding:8px; font-size:0.8em; background:#f8fafc; font-weight:600; color:#334155; }
    </style>
    
    <div class="slide-head" style="margin-bottom:0">
      <span class="kicker teal"><span class="num">06</span> How It Works & Architecture</span>
      <h2 style="font-size:1.5em; margin:0;">Amazon Nova Architecture: <span class="accent">The 10-Second Funnel</span></h2>
    </div>
    
    <div class="grow col" style="justify-content:center; align-items:center;">
      <div class="arch-v3">
        
        <!-- LEFT COLUMN -->
        <div class="col-left">
           <!-- Customer -->
           <div class="box-v3" style="border-radius:30px; padding:8px 24px; background:#f8fafc; border-color:#94a3b8; width:auto;">
              <div style="font-size:1.15em; font-weight:800; color:#334155;"><span class="glyph">👤</span> CUSTOMER</div>
           </div>
           
           <div class="v-arrow-v3">
              <div class="arr">↓</div>
           </div>
           
           <!-- Deployment CDN -->
           <div class="box-v3 box-deploy">
              <div style="color:#ea580c; font-weight:800; font-size:1.05em;">DEPLOYMENT: AWS CloudFront + S3</div>
              <div style="color:#c2410c; font-size:0.85em;">(Global Edge CDN Distribution)</div>
           </div>
           
           <div class="v-arrow-v3">
              <div class="arr">↓</div>
           </div>
           
           <!-- React SPA -->
           <div class="box-v3 box-front">
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
        </div>
        
        <!-- MIDDLE COLUMN (Arrow) -->
        <div class="col-mid">
           <div class="h-arrow-v3">
              <div style="background:#f1f5f9; padding:4px 8px; border-radius:4px; border:1px solid #cbd5e1;">REST API Requests</div>
              <div class="arr">➔</div>
           </div>
        </div>
        
        <!-- RIGHT COLUMN -->
        <div class="col-right">
           <!-- API Gateway -->
           <div class="box-v3 box-deploy" style="width:320px;">
              <div style="color:#ea580c; font-weight:800; font-size:1.05em;">DEPLOYMENT: AWS<br>API Gateway + Lambda</div>
              <div style="color:#c2410c; font-size:0.85em;">(Serverless Compute)</div>
           </div>
           
           <div class="v-arrow-v3">
              <div class="arr">↓</div>
           </div>
           
           <!-- Express Backend -->
           <div class="box-v3 box-back" style="display:flex; flex-direction:column; padding:0; overflow:hidden;">
              <div style="background:#fff7ed; padding:8px; border-bottom:1px solid #ffedd5;">
                 <div class="box-title" style="color:#ea580c; margin:0;">EXPRESS BACKEND API</div>
                 <div class="box-sub" style="margin:0;">(Node.js + TypeScript)</div>
              </div>
              
              <div style="display:flex; padding:12px; gap:12px;">
                 <!-- Internal Services -->
                 <div style="flex:1; background:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; padding:10px;">
                    <div style="font-size:0.9em; color:#ea580c; font-weight:800; margin-bottom:8px;">Internal Services</div>
                    <ul class="inner-list" style="font-weight:600;">
                       <li>catalog.ts</li>
                       <li>dynamodb.ts</li>
                       <li>bedrock.ts</li>
                       <li>calendar.ts</li>
                       <li>vectorSrch</li>
                    </ul>
                 </div>
                 
                 <!-- Nova Agent Pipeline -->
                 <div style="flex:1.2; background:#f8fafc; border:1px solid #e2e8f0; border-radius:6px; padding:10px;">
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
           
           <!-- Branching Arrows to DBs -->
           <div style="display:flex; width:100%; margin-top:4px;">
              <!-- Left branch from Internal Services -->
              <div style="flex:1; display:flex; flex-direction:column; align-items:center; padding-right:12px;">
                 <div class="v-arrow-v3"><div class="arr">↓</div></div>
                 <div style="display:flex; gap:6px; width:100%; justify-content:center;">
                    <div class="db-box" style="border-color:#10b981; color:#047857;">DynamoDB</div>
                    <div class="db-box" style="border-color:#a855f7; color:#7e22ce;">Google Calendar</div>
                    <div class="db-box" style="border-color:#64748b; color:#334155;">In-Memory Vector Search</div>
                 </div>
              </div>
              
              <!-- Right branch from Nova Agent -->
              <div style="flex:1.2; display:flex; flex-direction:column; align-items:center; padding-left:12px;">
                 <div class="v-arrow-v3"><div class="arr">↓</div></div>
                 <div class="db-box" style="border-color:#3b82f6; color:#1d4ed8; font-size:1em; padding:10px 20px;">AWS Bedrock</div>
              </div>
           </div>
           
        </div>
      </div>
    </div>
  </section>"""

with open('ppt-finale.html', 'r', encoding='utf-8') as f:
    text = f.read()

pattern = re.compile(r'<!-- 7 · HOW IT WORKS / ARCHITECTURE COMBINED -->\s*<section class="slide" data-section="pipeline">.*?</section>', re.DOTALL)
text = pattern.sub(v3_arch_html, text)

with open('ppt-finale.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Architecture diagram v3 injected.")
