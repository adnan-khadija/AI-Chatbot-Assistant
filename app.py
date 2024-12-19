from flask import Flask, render_template, request, jsonify
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Initialisation du modèle Llama 2
model = OllamaLLM(model="llama2")

# Création du modèle de prompt avec template
template = """
Answer the question below.
Here is the conversation history:{context}
Question:{question}
"""
prompt = ChatPromptTemplate.from_template(template)

# Chaîne qui relie le modèle au prompt
chain = prompt | model

# Initialisation de Flask
app = Flask(__name__)

# Variable pour garder l'historique de la conversation
context = ""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    global context

    # Récupérer la question de l'utilisateur depuis le formulaire
    user_input = request.form['user_input']

    # Construire un contexte pour le modèle
    conversation_history = context + f"User: {user_input}\n"

    # Générer une réponse via Llama 2 en utilisant le modèle
    response = chain.invoke({"context": conversation_history, "question": user_input})

    # Mettre à jour le contexte pour la prochaine itération
    context += f"User: {user_input}\nBot: {response}\n"

    # Retourner la réponse sous forme de JSON
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)
