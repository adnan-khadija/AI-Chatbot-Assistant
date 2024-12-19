# Chatbot AI avec Flask et Llama 2

Ce projet implémente un chatbot alimenté par le modèle Llama 2 de LangChain, accessible via une interface web construite avec Flask. Le chatbot peut répondre à des questions basées sur l'historique de la conversation, offrant ainsi une expérience interactive avec un modèle de langage avancé.

## Fonctionnalités

- Interaction en temps réel avec un modèle de langage (Llama 2).
- Historique des conversations sauvegardé pour chaque utilisateur.
- Interface web simple avec Flask.
- Génération de réponses contextuelles basées sur l'historique de la conversation.

## Prérequis

Avant de commencer, assurez-vous d'avoir Python 3.x installé sur votre machine. Vous devrez également installer les bibliothèques suivantes :

- **Flask** : Pour le développement de l'application web.
- **langchain_ollama** : Pour intégrer et interagir avec le modèle Llama 2.
- **langchain_core** : Pour la création et l'exécution de prompts.
- **requests** : Pour effectuer des requêtes HTTP.
- **python-dotenv** : Pour charger les variables d'environnement.

## Installation

Clonez ce repository et installez les dépendances requises :

```bash
git clone https://github.com/adnan-khadija/AI-Chatbot-Assistant.git
cd AI-Chatbot-Assistant
pip install -r requirements.txt

```

## Utilisation

Lancez l'application Flask en utilisant la commande suivante :

```bash
python app.py
```

L'application sera disponible sur `http://127.0.0.1:5000/` dans votre navigateur.

Vous pouvez maintenant poser des questions à votre chatbot via l'interface web et voir les réponses générées en fonction de l'historique des conversations.

## Structure du projet
```bash
/chatbot
├── app.py               # Script principal de l'application Flask
├── requirements.txt      # Liste des dépendances du projet
├── templates/
│   └── index.html        # Page HTML pour l'interface utilisateur
├── static/
│   └── style.css         # Fichier CSS pour styliser l'interface
└── .env                  # Fichier de configuration des variables d'environnement
```

## Auteurs

- **[Khadija ADNAN](https://github.com/adnan-khadija)**


