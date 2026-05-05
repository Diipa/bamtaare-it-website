"""
Bamtaare IT - Backend Flask
Application serveur pour gérer les formulaires de contact et les données
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from datetime import datetime
import os
from pathlib import Path

# Initialiser l'application Flask
app = Flask(__name__)

# Activer CORS pour permettre les requêtes depuis le frontend
CORS(app)

# Configuration
app.config['JSON_SORT_KEYS'] = False

# Créer un dossier pour stocker les données
DATA_FOLDER = Path(__file__).parent / 'data'
DATA_FOLDER.mkdir(exist_ok=True)

CONTACTS_FILE = DATA_FOLDER / 'contacts.json'


# ============================================
# HELPER FUNCTIONS
# ============================================

def load_contacts():
    """Charger tous les contacts depuis le fichier JSON"""
    if CONTACTS_FILE.exists():
        with open(CONTACTS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []


def save_contacts(contacts):
    """Sauvegarder les contacts dans le fichier JSON"""
    with open(CONTACTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(contacts, f, indent=2, ensure_ascii=False)


# ============================================
# ROUTES - API ENDPOINTS
# ============================================

@app.route('/', methods=['GET'])
def home():
    """Route d'accueil - vérifier que le serveur fonctionne"""
    return jsonify({
        'status': 'success',
        'message': 'Bienvenue sur le backend Bamtaare IT',
        'version': '1.0.0'
    }), 200


@app.route('/api/contact', methods=['POST'])
def submit_contact():
    """
    Endpoint pour soumettre un formulaire de contact
    Accepte: POST request avec JSON data
    """
    try:
        # Récupérer les données du formulaire
        data = request.get_json()
        
        # Valider les données
        nom = data.get('nom', '').strip()
        email = data.get('email', '').strip()
        message = data.get('message', '').strip()
        
        # Vérifier que les champs obligatoires sont remplis
        if not nom or not email or not message:
            return jsonify({
                'status': 'error',
                'message': 'Tous les champs sont obligatoires'
            }), 400
        
        # Valider l'email basique
        if '@' not in email:
            return jsonify({
                'status': 'error',
                'message': 'Email invalide'
            }), 400
        
        # Créer le nouvel enregistrement de contact
        nouveau_contact = {
            'id': len(load_contacts()) + 1,
            'nom': nom,
            'email': email,
            'message': message,
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'lu': False
        }
        
        # Charger les contacts existants et ajouter le nouveau
        contacts = load_contacts()
        contacts.append(nouveau_contact)
        save_contacts(contacts)
        
        print(f"✓ Nouveau contact reçu de {nom} ({email})")
        
        return jsonify({
            'status': 'success',
            'message': 'Votre message a été envoyé avec succès!',
            'data': nouveau_contact
        }), 201
    
    except Exception as e:
        print(f"✗ Erreur lors du traitement du contact: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': f'Erreur serveur: {str(e)}'
        }), 500


@app.route('/api/contacts', methods=['GET'])
def get_contacts():
    """
    Endpoint pour récupérer tous les contacts
    (À protéger avec authentification en production)
    """
    try:
        contacts = load_contacts()
        return jsonify({
            'status': 'success',
            'data': contacts,
            'total': len(contacts)
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Erreur serveur: {str(e)}'
        }), 500


@app.route('/api/contacts/<int:contact_id>', methods=['GET'])
def get_contact(contact_id):
    """Récupérer un contact spécifique"""
    try:
        contacts = load_contacts()
        contact = next((c for c in contacts if c['id'] == contact_id), None)
        
        if not contact:
            return jsonify({
                'status': 'error',
                'message': f'Contact avec l\'ID {contact_id} non trouvé'
            }), 404
        
        return jsonify({
            'status': 'success',
            'data': contact
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Erreur serveur: {str(e)}'
        }), 500


@app.route('/api/contacts/<int:contact_id>/mark-read', methods=['PUT'])
def mark_contact_read(contact_id):
    """Marquer un contact comme lu"""
    try:
        contacts = load_contacts()
        contact = next((c for c in contacts if c['id'] == contact_id), None)
        
        if not contact:
            return jsonify({
                'status': 'error',
                'message': f'Contact avec l\'ID {contact_id} non trouvé'
            }), 404
        
        contact['lu'] = True
        save_contacts(contacts)
        
        return jsonify({
            'status': 'success',
            'message': 'Contact marqué comme lu',
            'data': contact
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Erreur serveur: {str(e)}'
        }), 500


@app.route('/api/contacts/<int:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    """Supprimer un contact"""
    try:
        contacts = load_contacts()
        contact = next((c for c in contacts if c['id'] == contact_id), None)
        
        if not contact:
            return jsonify({
                'status': 'error',
                'message': f'Contact avec l\'ID {contact_id} non trouvé'
            }), 404
        
        contacts = [c for c in contacts if c['id'] != contact_id]
        save_contacts(contacts)
        
        return jsonify({
            'status': 'success',
            'message': 'Contact supprimé'
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Erreur serveur: {str(e)}'
        }), 500


@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Obtenir des statistiques sur les contacts"""
    try:
        contacts = load_contacts()
        stats = {
            'total': len(contacts),
            'non_lus': len([c for c in contacts if not c['lu']]),
            'lus': len([c for c in contacts if c['lu']])
        }
        
        return jsonify({
            'status': 'success',
            'data': stats
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Erreur serveur: {str(e)}'
        }), 500


# ============================================
# ERROR HANDLERS
# ============================================

@app.errorhandler(404)
def not_found(error):
    """Gérer les erreurs 404"""
    return jsonify({
        'status': 'error',
        'message': 'Endpoint non trouvé'
    }), 404


@app.errorhandler(500)
def server_error(error):
    """Gérer les erreurs 500"""
    return jsonify({
        'status': 'error',
        'message': 'Erreur serveur interne'
    }), 500


# ============================================
# MAIN
# ============================================

if __name__ == '__main__':
    print("=" * 50)
    print("🚀 Démarrage du serveur Bamtaare IT")
    print("=" * 50)
    print("📍 Local: http://localhost:5000")
    print("=" * 50)
    app.run(debug=True, host='localhost', port=5000)
