# Assistant IA local

Un petit assistant conversationnel qui utilise un modèle d'intelligence artificielle exécuté sur votre ordinateur avec [Ollama](https://ollama.com/).

L'objectif du projet est de découvrir les modèles de langage, de comprendre comment une application communique avec une IA et de proposer une base simple, modifiable et accessible aux débutants.

## Fonctionnalités

- Conversation dans le terminal.
- Connexion à une instance Ollama locale.
- Modèle configurable (par défaut : `qwen2.5:3b`).
- Historique de conversation conservé pendant la session.
- Code Python simple, sans dépendance externe.

## Prérequis

- Python 3.10 ou plus récent.
- Ollama installé et démarré : https://ollama.com/
- Un modèle téléchargé dans Ollama.

## Installation

1. Téléchargez ou clonez ce dépôt.
2. Dans un terminal, téléchargez le modèle :

   ```bash
   ollama pull qwen2.5:3b
   ```

3. Lancez l'assistant :

   ```bash
   python main.py
   ```

Pour utiliser un autre modèle, définissez la variable d'environnement `OLLAMA_MODEL`.

Sous Windows PowerShell :

```powershell
$env:OLLAMA_MODEL="qwen2.5:3b"
python main.py
```

## Utilisation

Écrivez votre message puis appuyez sur Entrée. Pour quitter, tapez `/quit`.

L'application contacte uniquement le serveur Ollama configuré sur votre ordinateur (`http://localhost:11434` par défaut). Vos messages ne sont pas envoyés à une API Claude ou à un service distant par ce programme.

## Configuration

Vous pouvez modifier ces variables d'environnement :

- `OLLAMA_HOST` : adresse du serveur Ollama (par défaut `http://localhost:11434`).
- `OLLAMA_MODEL` : nom du modèle (par défaut `qwen2.5:3b`).

## Limites

La qualité et la vitesse des réponses dépendent du modèle choisi et du matériel disponible. Un modèle local peut produire des erreurs : vérifiez les informations importantes.

## Pistes d'amélioration

- Ajouter une interface graphique.
- Permettre d'exporter les conversations.
- Ajouter une gestion de plusieurs conversations.
- Comparer les performances de différents modèles locaux.
- Ajouter des tests automatisés.

## État du projet

Projet personnel en développement. Les fonctionnalités et améliorations seront ajoutées progressivement. Les statistiques d'utilisation ne sont pas publiées tant qu'elles ne sont pas mesurées.

## Licence

Ce projet est distribué sous licence MIT. Voir le fichier `LICENSE`.
