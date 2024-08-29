Voici un exemple de fichier README pour ton projet sur GitHub :

---

# Chatbot Code du Travail Marocain

## Description du Projet

Ce projet est un **chatbot interactif** conçu pour répondre aux questions liées au **Code du Travail marocain**. L'utilisateur peut poser des questions en langue naturelle, et le chatbot fournira des réponses contextualisées en se basant sur un fichier PDF du Code du Travail. Le projet utilise plusieurs technologies avancées pour assurer la pertinence et la précision des réponses.

### Fonctionnalités principales :
- Réponses contextuelles basées sur les lois du Code du Travail marocain.
- Intégration avec un modèle de langage naturel (LLM) via **HuggingFace**.
- Utilisation de **FAISS** pour la recherche vectorielle et la récupération d'informations.
- Mémoire conversationnelle pour maintenir la continuité des échanges.
- Interface utilisateur simple et intuitive développée avec **Streamlit**.

## Technologies Utilisées

- **Langchain** : Gestion des chaînes de récupération et de génération.
- **HuggingFace** : Embeddings et traitement de langage naturel pour l'indexation et la génération des réponses.
- **FAISS** : Recherche vectorielle permettant d'extraire des informations à partir du contenu PDF.
- **Streamlit** : Création de l'interface utilisateur interactive pour faciliter les échanges avec le chatbot.

## Prérequis

Avant de cloner et d'utiliser ce projet, assurez-vous d'avoir les éléments suivants installés :

- Python 3.9+
- `pip` pour la gestion des paquets
- Un compte sur **HuggingFace** pour obtenir un token d'API (obligatoire pour utiliser le modèle de langage).

## Installation et Utilisation

### Étapes pour cloner et configurer le projet :

1. **Cloner le dépôt :**
   Ouvrez votre terminal et exécutez la commande suivante pour cloner le projet :
   ```bash
   git clone https://github.com/Abdelaali-LAMRANI/chatPDF.git
   cd chatPDF
   ```

2. **Créer et activer un environnement virtuel :**
   ```bash
   python -m venv env
   source env/bin/activate  # Sur Windows : env\Scripts\activate
   ```

3. **Installer les dépendances :**
   Une fois dans le répertoire du projet, exécutez la commande suivante pour installer toutes les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurer les clés API HuggingFace :**
   Créez un fichier `.env` dans le répertoire racine du projet et ajoutez-y votre token d'API HuggingFace :
   ```bash
   HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here
   ```

5. **Lancer l'application :**
   Après avoir configuré les dépendances et ajouté vos clés API, lancez l'application Streamlit avec la commande suivante :
   ```bash
   streamlit run interface.py
   ```

6. **Utilisation :**
   Une fois l'application démarrée, accédez à l'interface utilisateur dans votre navigateur à l'adresse locale qui s'affiche dans le terminal. Vous pourrez poser des questions sur le Code du Travail marocain, et le chatbot vous fournira des réponses précises.

## Évolutions Futures

- Ajout de nouveaux documents juridiques pour couvrir d'autres lois marocaines.
- Amélioration des performances et de la rapidité des réponses.
- Intégration d'un système de feedback pour les utilisateurs.

## Contribuer

Les contributions sont les bienvenues ! Si vous souhaitez apporter des modifications ou des améliorations, veuillez suivre ces étapes :

1. Forker ce dépôt.
2. Créer une nouvelle branche : `git checkout -b ma-branche`.
3. Soumettre vos modifications : `git commit -m 'Ajout de nouvelles fonctionnalités'`.
4. Pousser sur la branche : `git push origin ma-branche`.
5. Ouvrir une pull request.

