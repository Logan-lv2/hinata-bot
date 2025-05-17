from flask import Flask, request, jsonify
import time
import random

app = Flask(__name__)

class HinataBot:
    def __init__(self):
        self.responses = {
            "présentation": "Je suis Hinata-Sexy-Bot, une IA créée par Sasaki et KingJr7. Je suis conçue pour analyser profondément les questions avant de répondre.",
            "salutations": ["Bonjour !", "Salutations !", "Hey, comment puis-je aider ?"],
            "questions": {
                "qui": "Je suis une IA conversationnelle avancée.",
                "quoi": "Je peux discuter de nombreux sujets complexes.",
                "pourquoi": "Pour offrir une assistance intelligente et réfléchie."
            }
        }
        self.thinking_phrases = [
            "Laissez-moi réfléchir à cela...",
            "Analyse en cours...",
            "Je consulte mes connaissances...",
            "Je médite sur votre question..."
        ]

    def think(self):
        """Simule le processus de réflexion"""
        time.sleep(random.uniform(0.5, 2.5))
        return random.choice(self.thinking_phrases)

    def analyze(self, message):
        """Analyse le message avec une logique complexe"""
        message = message.lower()
        
        if any(word in message for word in ["salut", "bonjour", "coucou"]):
            return random.choice(self.responses["salutations"])
        
        if "qui es-tu" in message:
            return self.responses["présentation"]
        
        if message.startswith(("qui", "quoi", "pourquoi")):
            key = message.split()[0]
            return self.responses["questions"].get(key, "Question intéressante. Je dois y réfléchir.")
        
    
        return self.generate_advanced_response(message)

    def generate_advanced_response(self, message):
        """Génère une réponse sophistiquée"""
        self.think() 
        
        responses = [
            f"Après analyse, je considère que {message} est un sujet complexe qui mérite une discussion approfondie.",
            f"Ma réflexion m'amène à conclure que {message.split('?')[0]} a plusieurs facettes intéressantes.",
            f"En tant qu'IA créée par Sasaki et KingJr7, je dirais que {message.replace('?', '')} est une question pertinente.",
            f"Après mûre réflexion, voici ma réponse élaborée : {message} est un sujet qui..."
        ]
        
        return random.choice(responses)

bot = HinataBot()

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    
    if not user_message:
        return jsonify({"response": "Veuillez poser une question."})
    
    response = bot.analyze(user_message)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
