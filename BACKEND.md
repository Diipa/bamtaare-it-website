# 🚀 Bamtaare IT - Backend Flask

Un serveur backend Python Flask pour gérer les formulaires de contact et les données de votre site web.

## 📋 Fonctionnalités

- ✅ API REST pour gérer les contacts
- ✅ Stockage des données en JSON (facile à utiliser, pas de base de données complexe)
- ✅ CORS activé pour permettre les requêtes du frontend
- ✅ Validation des données côté serveur
- ✅ Gestion des erreurs robuste
- ✅ Statistiques sur les contacts

## 🛠️ Installation

### 1. **Prérequis**
- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### 2. **Installer les dépendances**

```bash
# Naviguer dans le dossier du projet
cd "c:\Users\dipad\OneDrive\Bureau\Cv_lettre_de_presentation\Vibe code"

# Créer un environnement virtuel (recommandé)
python -m venv venv

# Activer l'environnement virtuel
# Sur Windows:
venv\Scripts\activate

# Installer les packages
pip install -r requirements.txt
```

### 3. **Démarrer le serveur**

```bash
python app.py
```

Vous devriez voir :
```
==================================================
🚀 Démarrage du serveur Bamtaare IT
==================================================
📍 Local: http://localhost:5000
==================================================
```

## 📡 API Endpoints

### 1. **Vérifier le serveur**
```
GET http://localhost:5000/
```

### 2. **Soumettre un contact**
```
POST http://localhost:5000/api/contact
Content-Type: application/json

{
    "nom": "Jean Dupont",
    "email": "jean@example.com",
    "message": "Votre message ici"
}
```

**Réponse succès (201):**
```json
{
    "status": "success",
    "message": "Votre message a été envoyé avec succès!",
    "data": {
        "id": 1,
        "nom": "Jean Dupont",
        "email": "jean@example.com",
        "message": "Votre message ici",
        "date": "2026-05-04 14:30:00",
        "lu": false
    }
}
```

### 3. **Récupérer tous les contacts**
```
GET http://localhost:5000/api/contacts
```

### 4. **Récupérer un contact spécifique**
```
GET http://localhost:5000/api/contacts/1
```

### 5. **Marquer un contact comme lu**
```
PUT http://localhost:5000/api/contacts/1/mark-read
```

### 6. **Supprimer un contact**
```
DELETE http://localhost:5000/api/contacts/1
```

### 7. **Obtenir les statistiques**
```
GET http://localhost:5000/api/stats
```

**Réponse:**
```json
{
    "status": "success",
    "data": {
        "total": 5,
        "non_lus": 2,
        "lus": 3
    }
}
```

## 📁 Structure des données

Les contacts sont stockés dans `data/contacts.json` :

```json
[
    {
        "id": 1,
        "nom": "Jean Dupont",
        "email": "jean@example.com",
        "message": "Un message...",
        "date": "2026-05-04 14:30:00",
        "lu": false
    }
]
```

## 🔗 Connexion avec le Frontend

Le frontend envoie automatiquement les données du formulaire au backend :

1. **Formulaire rempli** → Frontend JavaScript
2. **Validation** → Script JavaScript
3. **Envoi** → POST vers `http://localhost:5000/api/contact`
4. **Réponse** → Message de succès/erreur

## 🛡️ Sécurité

⚠️ **Pour la production :**
- Ajouter une authentification
- Valider et nettoyer les entrées utilisateur
- Utiliser une vraie base de données (PostgreSQL, MongoDB)
- Ajouter HTTPS
- Implémenter un rate limiting
- Ajouter des logs de sécurité

## 📦 Dépendances

```
Flask==2.3.3           - Framework web
Flask-CORS==4.0.0      - Gérer les requêtes cross-origin
python-dotenv==1.0.0   - Variables d'environnement
```

## 🐛 Dépannage

### Erreur : "ModuleNotFoundError: No module named 'flask'"
```bash
# Assurez-vous que l'environnement virtuel est activé et installez les dépendances
pip install -r requirements.txt
```

### Erreur : "Address already in use"
```bash
# Le port 5000 est déjà utilisé. Changez le port dans app.py:
app.run(debug=True, host='localhost', port=5001)
```

### Le frontend ne peut pas se connecter au backend
```bash
# Vérifiez que :
# 1. Le serveur Python est en cours d'exécution
# 2. L'URL API est correcte (http://localhost:5000)
# 3. CORS est activé (Flask-CORS)
# 4. Pas de firewall bloquant le port 5000
```

## 🚀 Améliorations futures

- [ ] Ajouter une base de données (PostgreSQL, MongoDB)
- [ ] Implémenter une authentification (JWT)
- [ ] Ajouter un système d'email pour notifier les contacts
- [ ] Créer un admin panel
- [ ] Ajouter des logs avancés
- [ ] Implémenter un système de pagination
- [ ] Ajouter des tests unitaires
- [ ] Déployer sur Heroku/AWS/Azure

## 📝 Notes

- Les données sont stockées localement en JSON
- Pas de base de données complexe requise pour démarrer
- Facile à migrer vers une base de données plus tard
- Perfect pour un MVP ou prototype

---

**Créé avec ❤️ pour Bamtaare IT**
