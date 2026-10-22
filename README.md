# Prompt Engineering DSL

Ce dépôt est le squelette d’un projet de DSL pour décrire des demandes de génération
de prompts. Le flux visé est : concevoir une instance dans AToMPM, la convertir en
méta-prompt, puis utiliser un LLM pour produire le prompt final.

## Prérequis

- Python 3.10 ou une version ultérieure pour les outils du dossier `generator/`.
- Eclipse avec Xtext pour éditer et générer l’éditeur du DSL.
- AToMPM pour créer et exporter le métamodèle et ses instances.
- Une clé API LLM pour la génération, à configurer localement (voir `.env.example`).

## Dossiers

- `metamodel/` : export JSON du métamodèle AToMPM et instances de prompts.
- `grammar/` : grammaire Xtext et, à terme, les sources du projet Eclipse.
- `generator/metaprompt/` : gabarits de méta-prompts.
- `generator/generate.py` et `generator/llm_client.py` : points d’entrée prévus pour
  le pipeline et l’appel au LLM. Ils sont actuellement des squelettes : le format
  d’export AToMPM et le fournisseur LLM doivent être définis avant leur implémentation.
- `templates/` : extension Mustache prévue pour la phase 2.
- `examples/` : exemples d’entrée du DSL.
- `evaluation/` : tâches, évaluations déterministes, évaluations par LLM et résultats.
- `docs/` : notes de réunion, rapport et diapositives.

## Préparation locale

1. Copier `.env.example` vers `.env` et renseigner les variables nécessaires sans
   ajouter `.env` au dépôt.
2. Créer un environnement Python :

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Créer le métamodèle et les instances dans AToMPM, puis placer les exports dans
   `metamodel/` et `metamodel/instances/`.
4. Ouvrir/importer le projet Xtext dans Eclipse et faire évoluer
   `grammar/PromptDsl.xtext` selon le métamodèle retenu.
5. Compléter le pipeline et son client LLM avant de lancer une génération. À ce stade,
   `python generator/generate.py` affiche l’état du squelette et retourne un code
   d’erreur, plutôt que de produire un résultat incomplet.

## Évaluation

Ajouter les tâches d’évaluation dans `evaluation/tasks/`, les tests déterministes
dans `evaluation/deterministic/` et les évaluations par juge LLM dans
`evaluation/llm_judge/`. Les résultats reproductibles peuvent être conservés dans
`evaluation/results/`.

Les conventions de parsing, le fournisseur LLM, les commandes d’évaluation et la
correspondance entre l’export AToMPM et le DSL restent à préciser.
