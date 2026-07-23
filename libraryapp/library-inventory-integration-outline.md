# Project Outline: library-app + python-inventory-api Integration

## Goal
Connect the existing `library-app` frontend to the existing `python-inventory-api` backend so the two disconnected repos become one working full-stack app. No new frontend framework, no new backend framework — the point is wiring, not rebuilding.

## Skill Gap This Targets
Full-stack integration: real HTTP requests between a live frontend and a live backend, including error/loading states, CORS, and request/response shape handling. Neither existing repo currently demonstrates this on its own.

## Backend Prep — Daily Blocks (python-inventory-api)
30–60 minutes each. Do these before starting Phase 1 below — they get the API into a known-good, frontend-ready state so the integration work isn't interrupted by backend surprises.

### Day 1 — Run it and map the responses
**What:** Start `python-inventory-api` locally, open the FastAPI auto-docs at `/docs`, and manually call every endpoint from there. Write down the exact JSON shape (field names, types) each one returns. No code changes today.
**Why:** You can't build a frontend against an API you don't have documented in your own head. This is also your first checkpoint that the backend still runs cleanly after having sat untouched — catching bit-rot now is cheaper than catching it mid-integration.

### Day 2 — Add CORS
**What:** Add `fastapi.middleware.cors.CORSMiddleware` to the app, configured to allow requests from wherever `library-app` will run locally (e.g. `http://localhost:5500`). Verify it by running a one-line `fetch()` from the browser console against a live endpoint.
**Why:** CORS is a browser-enforced security rule that blocks a page on one origin from calling an API on another origin unless the server explicitly allows it. This is the single most common blocker the first time someone connects a static frontend to a separate API — better to hit it in isolation today than debug it later while also debugging your own fetch code.

### Day 3 — Validate the read path
**What:** Look closely at `GET /inventory` and `GET /inventory/{id}`. Confirm the response has everything the UI will need (id, name, price/value, category, etc.) and that field names are consistent. Adjust the Pydantic response model now if anything's missing or awkwardly named.
**Why:** The frontend will be written against whatever shape the API returns today. Changing a field name later means changing it in two places instead of one — fixing the contract now, before frontend code depends on it, avoids rework.

### Day 4 — Validate the write path and error shape
**What:** Test `POST /inventory` and `PUT /inventory/{id}` with both a valid payload and a deliberately bad one (missing field, wrong type). Inspect exactly what a 422 validation error looks like in the response body.
**Why:** Client-side error handling can only be as good as your understanding of what errors actually look like. Seeing the real error shape now means Phase 2's "surface API errors in the UI" step is translation, not guesswork.

### Day 5 — Validate DELETE and edge cases
**What:** Test `DELETE /inventory/{id}` on both a real and a non-existent id (should 404 cleanly, not crash). Also check what `GET /inventory` returns when the table is empty.
**Why:** Edge cases are where "it works on my machine" demos fall apart in front of someone else. An empty-state and a not-found-state are both things the frontend will need to handle gracefully, so the backend needs to behave predictably in both first.

### Day 6 — Polish the analytics endpoints
**What:** Re-test `category_totals`, `highest_value_item`, and `total_inventory_value`. Check number formatting (e.g. currency rounding) and confirm each handles an empty inventory without erroring.
**Why:** These three endpoints feed the Phase 3 summary panel directly — any roughness here (a `None`, an unrounded float, an unhandled empty case) becomes a visible bug on the frontend later. Fixing it at the source is simpler than patching around it in JS.

### Day 7 — Seed data and buffer
**What:** Make sure there's a fast way to reset/seed the database with a handful of realistic sample items. Use this day to catch up on anything from Days 1–6 that ran long.
**Why:** You'll want to reset to a known state repeatedly while building and testing the frontend — doing this by hand every time wastes your limited daily window. A buffer day also keeps the schedule realistic; multi-day plans that assume every block goes perfectly rarely survive contact with real debugging.

## Phase 1 — Read Integration (Display Live Data)
- Replace whatever hardcoded/static data `library.js` currently uses with a `fetch('GET /inventory')` call.
- Render the returned items into the existing HTML/CSS structure.
- Add basic loading and error states (e.g., "Loading inventory…", "Couldn't reach the server").
- **Checkpoint:** page loads and shows real data pulled from the running API, not local/static data.

## Phase 2 — Write Integration (Add / Edit / Delete)
- Wire an "add item" form to `POST /inventory`.
- Wire edit controls to `PUT /inventory/{id}`.
- Wire delete controls to `DELETE /inventory/{id}`.
- Add client-side validation before submitting (required fields, numeric checks).
- Handle and surface API error responses (e.g., 422 validation errors) in the UI instead of failing silently.
- **Checkpoint:** full CRUD loop works end-to-end from the browser, no server restarts or manual DB edits needed to see changes reflected.

## Phase 3 — Surface Analytics
- Add a small summary panel to the UI that calls the existing analytics endpoints (`category_totals`, `highest_value_item`, `total_inventory_value`).
- Refresh this panel automatically after any add/edit/delete action.
- **Checkpoint:** UI reflects both the raw inventory list and the aggregate analytics, staying in sync after changes.

## Stretch Goals (Optional, Later)
- Basic styling pass so it reads as a finished product, not a CRUD demo.
- Deploy both pieces (e.g., API on Render, frontend on GitHub Pages or Netlify) and link them in each repo's README.
- Add simple auth if you want to practice that pattern here before tackling it in a larger project.

## What This Does *Not* Cover (Deliberately Out of Scope for Now)
- No new frontend framework (React, etc.) — vanilla JS is fine for this exercise.
- No data warehousing / dbt work — that's a separate track (see transaction-analytics).
- No ML/regression work — deferred to future coursework per current plan.

## Definition of Done
- `library-app` has zero hardcoded inventory data; everything comes from `python-inventory-api`.
- All four CRUD operations work from the UI.
- Analytics panel displays live, correct aggregates.
- Both repos' READMEs updated to reference each other and explain the combined app.
