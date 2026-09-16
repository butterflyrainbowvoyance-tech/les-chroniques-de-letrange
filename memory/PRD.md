# Les Chroniques de l'Étrange — PRD

## Concept
Application immersive documentant l'histoire de la spiritualité, du mysticisme, de l'occultisme, des arts divinatoires et des grandes légendes. Chaque récit indique clairement son statut (attesté / tradition / légende / hypothèse) avec sources vérifiables.

## Architecture
- Backend FastAPI (in-memory seed) + Claude Sonnet 5 SSE pour l'IA
- Frontend React + Tailwind + shadcn/ui
- Favoris localStorage

## Livré (Feb 2026)
### Iteration 1
- 22 récits sur 7 univers, endpoints, pages Home/Univers/Récit/Frise/Carte/Etrange/Quiz/Favoris/Recherche
- Design "Bibliothèque nocturne"
- Renommage : Les Chroniques de l'Étrange

### Iteration 2 (grande expansion)
- **45 récits sur 10 univers** (ajout : Histoire secrète + 10 dossiers, Ils y croyaient vraiment, La légende contre les archives)
- **Voyage dans le temps** : 5 panoramas d'époque (Antiquité → XIXe) avec 5 panneaux (croyances / pratiques / consultants / objets / peurs) + récits liés
- Formats signature avec sections + verdict point par point (attesté/probable/contesté/légende tardive)
- Recherche full-text (titre, sous-titre, excerpt, tags, contenu)
- Navigation croisée : /api/stories/{id}/related, tags cliquables
- Filtre région/pays sur la carte, filtre dossier sur univers
- Ruban catégories défilant, hero rewritten
- Tests : 17/17 backend + 11/11 frontend ✅

## Prochaine phase (backlog)
- P1: Section "À l'origine de..." (racines historiques d'un symbole donné)
- P1: Audio narrateur ElevenLabs pour lire un récit
- P2: Enrichir 2-3 dossiers restants encore vides
- P2: Frise chronologique avec scroll horizontal + repères visuels d'époques
- P2: Partage social récit-par-récit
