# Amazon Now - Project Details

> **Delivery is fast. Now shopping is too.**
> *An AI-powered conversational commerce layer built for HackOn with Amazon — Season 6.0*

## 1. Overview
**Amazon Now** completely reimagines urgent shopping. Instead of the traditional "search → compare → build cart" flow, customers simply state their *outcome* (via text, voice, or photo). The **Now Agent** figures out the rest, building a complete, budget-checked cart in seconds and showing exactly *why* it chose each item.

## 2. Key Features

### Tier 1 (Core F1-F4)
- **F1: Intent-to-Cart (Hero):** Converts a stated need into one ready-to-buy cart. Every item has a plain-text reason, confidence score, and nudge.
- **F2: Multimodal Intent:** Upload a photo of an empty fridge, a handwritten list, or a recipe, and the vision model extracts the required products.
- **F3: Budget Rebalancing:** If the cart exceeds the user's budget, the agent deterministically swaps the most expensive items for cheaper same-subcategory equivalents and shows exactly how much was saved.
- **F4: Recipe / Occasion-to-Cart:** Converts "Paneer butter masala for 4" or "Diwali for 10" into scaled ingredients, excluding likely-owned staples (salt, water, common spices).

### Tier 2 (Predictive F5, F6, F12)
- **F5: Context-aware Proactivity:** Uses a static Indian festival calendar, weather season detection, and Google Calendar integration to predict needs before the customer asks.
- **F6: Consumption-rate Prediction:** Shows a "Running low?" strip based on past order history. Combines a deterministic "frequently bought" lane with an LLM-estimated consumption lane for single-purchase items.
- **F12: Emergency Mode:** One-tap SOS chips for scenarios like "Cut Finger", "Burned Cooking", or "Severe Cramps", bypassing the search funnel entirely.

### Tier 3 (Enhancers F7-F11)
- **F7: Substitution Resilience:** If the LLM picks an out-of-stock item, the vector search automatically finds the closest in-stock substitute.
- **F8: One-pick decision:** Surfaces a confidence score. If low, provides alternative options.
- **F9: Learns from edits:** When a user adds or removes items, their preferences are saved and applied to future carts.
- **F10: Health/diet-aware swaps:** Respects dietary constraints like vegan or vegetarian, automatically down-ranking incompatible items.
- **F11: Unit-economics nudges:** Provides tips when larger pack sizes offer better value.

---

## 3. Architecture & Tech Stack

### Tech Stack
- **Frontend:** React + TypeScript + Vite + Tailwind CSS (`lucide-react` for icons). Dark mode (`#131A22`) + Amazon Orange (`#FF9900`) aesthetics.
- **Backend:** Node.js + Express + TypeScript, structured to be deployed as an AWS Lambda function using `serverless-http`.
- **Database:** AWS DynamoDB (Mock catalog, users, orders).
- **AI Models (AWS Bedrock):**
  - **Reasoning/Vision:** `amazon.nova-lite-v1:0` (Nova Lite).
  - **Embeddings:** `amazon.titan-embed-text-v2:0` (Titan Text Embeddings V2).
- **Vector Search:** In-memory cosine similarity over precomputed embeddings from Bedrock.
- **Deployment (AWS):** S3 + CloudFront (Frontend), API Gateway + Lambda (Backend), Route 53 (DNS).

### The Now Agent Pipeline
Instead of a slow, free-running loop, the agent uses an orchestrated deterministic pipeline:
1. **Parse Intent:** LLM extracts sub-needs, quantities, budget, and dietary constraints from text or image. 
2. **Clarification (Chat Mode):** If essential info (budget, preferences) is missing in Chat Mode, the LLM sets a `clarifyingQuestion` and the pipeline returns early to ask the user.
3. **Decompose Recipe / Occasion:** If a complex occasion is detected (e.g., "dinner for 9"), a dedicated prompt breaks it down into precise ingredients, intelligently estimating realistic quantities instead of blindly multiplying by servings.
4. **Context Gathering:** Fetch user household size, default budget, past orders, and learned preferences.
5. **Candidate Search:** Vector search fetches top 8 candidates for *each* sub-need, passing along the precisely parsed quantities and units.
6. **Assemble Cart:** LLM picks the *single best* item per sub-need from the candidates using the requested quantities, providing a reason and confidence score.
7. **Availability & Substitution:** Deterministically swap out-of-stock items for nearest matches.
8. **Enforce Budget:** Deterministically swap items for cheaper alternatives if the total exceeds the budget.

---

## 4. API Contract

The Express backend exposes the following REST routes (`/api/*`):

| Method | Route | Description |
|---|---|---|
| `POST` | `/intent` | Main cart generation. Body: `{ userId, text, imageBase64 }`. Returns `CartProposal`. |
| `POST` | `/emergency` | One-tap SOS bundles. Body: `{ userId, scenario }`. Returns `CartProposal`. |
| `GET` | `/reorder/:userId` | Get consumption-rate predictions. Returns `{ candidates: CartItem[] }`. |
| `GET` | `/proactive/:userId` | Get event/weather/calendar suggestions. Returns `{ suggestions: ProactiveSuggestion[] }`. |
| `POST` | `/proactive/:userId/update`| Caches proactive suggestions when answered. |
| `POST` | `/feedback` | Update user prefs. Body: `{ userId, removed: string[], added: string[] }`. |
| `POST` | `/checkout` | Mock checkout. Body: `{ userId, items }`. Returns `{ orderId, status }`. |
| `GET` | `/history/:userId` | Enriched past orders for the UI. |
| `GET` | `/auth/google` | OAuth redirect for Google Calendar sync. |

---

## 5. Data Models

### Product
```typescript
interface Product {
  id: string; name: string; category: string; subcategory: string; brand?: string;
  price: number; unit: string; packSize?: string; tags: string[]; dietary: string[];
  inStock: boolean; popularity: number; imageUrl: string;
  rating?: number; reviewCount?: number; deliveryTime?: string; isPrime?: boolean;
  embedding?: number[];
}
```

### Cart Proposal (Output of `/intent`)
```typescript
interface CartProposal {
  intentSummary: string;
  assumptions: string[];
  items: CartItem[];
  total: number;
  budget: number | null;
  withinBudget: boolean;
  rebalance?: Swap[]; // Items swapped to stay under budget
  occasion?: Occasion;
  clarifyingQuestion: string | null;
}
```

### User Profile
```typescript
interface User {
  id: string; name: string; city?: string;
  household: { size: number; dietary: string[]; budgetSensitivity: string; };
  defaultBudget?: number;
  learnedPrefs?: { avoid: string[]; prefer: string[] };
}
```

---

## 6. Codebase Structure

```
amazon-now/
├── backend/
│   ├── src/
│   │   ├── agent/            # nowAgent.ts (pipeline), prompts.ts
│   │   ├── services/         # bedrock.ts, vectorSearch.ts, dynamodb.ts, catalog.ts, calendar.ts
│   │   ├── routes/           # intent.ts, proactive.ts, reorder.ts, emergency.ts, checkout.ts, history.ts, auth.ts
│   │   ├── types/            # index.ts (Zod schemas and TS interfaces)
│   │   ├── data/             # seed-catalog.json, seed-user.json, seed-orders.json
│   │   ├── index.ts          # Express setup
│   │   └── lambda.ts         # Serverless wrapper
│   ├── scripts/              # Migration and seeding scripts
│   ├── serverless.yml        # AWS Lambda deployment config
│   └── package.json
├── frontend/
│   ├── src/
│   │   ├── components/       # IntentBar.tsx, CartProposalCard.tsx, ReorderStrip.tsx, ProactiveBanner.tsx, EmergencyChips.tsx...
│   │   ├── pages/            # Home.tsx, PurchaseHistory.tsx
│   │   ├── lib/              # api.ts (fetch wrapper), types.ts
│   │   ├── App.tsx           # Layout and routing
│   │   └── index.css         # Tailwind directives and custom CSS
│   ├── vite.config.ts        # Vite config with proxy to backend
│   └── package.json
├── setup-dns.js              # AWS Route53 script
├── IMPLEMENTATION_PLAN.md    # Step-by-step build guide
├── agent.md                  # PRD and AI agent rules
└── README.md                 # Project introduction
```

## 7. Setup & Run Instructions

### Prerequisites
- Node.js 18+
- AWS Account with DynamoDB and Amazon Bedrock (`amazon.nova-lite-v1:0`, `amazon.titan-embed-text-v2:0`) enabled in `us-east-1` (or your configured region).
- `.env` configured in `backend/` with AWS credentials and Google OAuth keys.

### Local Development
1. Start the backend:
   ```bash
   cd backend
   npm run dev  # Starts tsx watch on port 4000/4001
   ```
2. Start the frontend:
   ```bash
   cd frontend
   npm run dev  # Starts Vite on port 5173
   ```
3. Load the frontend at `http://localhost:5173`. The backend seeds its memory state from DynamoDB on startup.

### Deployment
- **Frontend**: Run `npm run build` inside `frontend/` and upload `dist/` to an S3 bucket configured for static website hosting, fronted by CloudFront.
- **Backend**: Uses Serverless Framework. Run `npx serverless deploy` in the `backend/` directory to deploy to AWS Lambda + API Gateway. Update the frontend's `VITE_API_BASE_URL` to point to the API Gateway URL.
