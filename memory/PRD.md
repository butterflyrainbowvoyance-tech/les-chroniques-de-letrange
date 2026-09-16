# Les Chroniques de l'Étrange — PRD

## Original problem statement
Application immersive consacrée à l'histoire de la spiritualité, du mysticisme, de l'occultisme, de l'ésotérisme, des arts divinatoires, des croyances populaires, des phénomènes étranges, des symboles et des grandes légendes. Ton oral, passionné, vulgarisateur. Chaque récit doit indiquer clairement son statut : fait attesté / tradition / légende / hypothèse.

## Architecture
- Backend: FastAPI + MongoDB (seeded content, no persistent DB yet), Claude Sonnet 5 via emergentintegrations for AI-streamed strange anecdotes.
- Frontend: React + Tailwind + shadcn/ui, react-router, favorites via localStorage.

## Implemented (Feb 2026)
- 22 seeded stories across 7 univers (ésotérisme, arts divinatoires, mystères, légendes, regalia, pierres, personnages) with sources + status labeling.
- Endpoints: /api/universes, /api/eras, /api/stories (+filters+search), /random, /timeline, /map, /quiz, /{id}, AI SSE /ai/tell-strange.
- Pages: Home (hero + bento univers), Universe, Story detail (badge+narratif+sources), Timeline, Map (SVG grid), Random, Quiz "Vrai/croyance/légende", Favorites, Search.
- Design: "Chroniques de l'Étrange" — bleu-nuit, dorures cuivrées, Cormorant Garamond + EB Garamond + Manrope.
- Renommage app: "Les Chroniques de l'Étrange".

## Backlog
- P1: Section "Avant de pratiquer" (dossier méthode pour chaque art divinatoire).
- P1: Section "À l'origine de…" (racines historiques d'un symbole).
- P2: Compte utilisateur pour synchroniser les favoris entre appareils.
- P2: Enrichir chaque univers à 8-10 récits.
- P2: Audio "narrateur" via ElevenLabs pour lire un récit.
