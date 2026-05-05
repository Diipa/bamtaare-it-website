# 🚀 Guide Complet de Déploiement sur RENDER

Render est la plateforme **la plus simple et la plus moderne** pour déployer votre site Bamtaare IT.

## ✅ Prérequis

- [ ] Un compte GitHub
- [ ] Votre code pushé sur GitHub
- [ ] Un email valide
- [ ] Optionnel : Un domaine personnalisé

## 📋 Étape 1 : Préparer votre code

### 1.1 Installer gunicorn
```bash
pip install gunicorn
```

### 1.2 Mettre à jour requirements.txt
```bash
pip freeze > requirements.txt
```

### 1.3 Vérifier que vous avez ces fichiers
```
✅ app.py                    # Serveur Flask
✅ requirements.txt          # Dépendances Python
✅ Procfile                  # Instructions de déploiement
✅ index.html, styles.css    # Frontend
✅ .gitignore               # Fichiers à ignorer
```

## 📤 Étape 2 : Pousser le code sur GitHub

### 2.1 Créer un repository GitHub
1. Allez sur https://github.com/new
2. Nommez-le `bamtaare-it-website`
3. Cochez "Initialize with README"
4. Créez le repository

### 2.2 Cloner et pousser votre code
```bash
# Cloner le repository
git clone https://github.com/votre-username/bamtaare-it-website.git

# Copier vos fichiers dans ce dossier
# (index.html, app.py, styles.css, etc.)

# Ajouter et commiter
git add .
git commit -m "Initial commit - Bamtaare IT Website"
git push origin main
```

## 🌐 Étape 3 : Créer un compte Render

1. Allez sur https://render.com/
2. Cliquez sur "Sign Up"
3. Inscrivez-vous avec GitHub
4. Autorisez Render à accéder à GitHub
5. Complétez votre profil

## 🚀 Étape 4 : Déployer sur Render

### 4.1 Créer un nouveau Web Service
1. Cliquez sur le bouton "New +" en haut à droite
2. Sélectionnez "Web Service"
3. Cliquez sur "Connect Repository" à côté de votre repository GitHub
4. Sélectionnez `bamtaare-it-website`
5. Cliquez "Connect"

### 4.2 Configurer le service
Remplissez les champs :

| Champ | Valeur |
|-------|--------|
| **Name** | `bamtaare-it` |
| **Environment** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn app:app` |

### 4.3 Variables d'environnement
Cliquez sur "Advanced" et ajoutez ces variables :

```
FLASK_ENV=production
DEBUG=False
```

### 4.4 Déployer
Cliquez sur "Create Web Service" et attendez quelques minutes.

Vous verrez :
```
✅ Build successful
✅ Service is live at: https://bamtaare-it.onrender.com
```

## ✨ Étape 5 : Tester votre site

1. Visitez votre URL : `https://bamtaare-it.onrender.com`
2. Testez le formulaire de contact
3. Vérifiez que tout fonctionne

## 🎯 Étape 6 : Ajouter un domaine personnalisé (Optionnel)

### 6.1 Acheter un domaine
- GoDaddy : https://www.godaddy.com/
- Namecheap : https://www.namecheap.com/
- Google Domains : https://domains.google/

Exemple : `bamtaare-it.com`

### 6.2 Configurer sur Render
1. Allez dans les paramètres de votre service
2. Cliquez sur "Custom Domain"
3. Entrez votre domaine : `bamtaare-it.com`
4. Suivez les instructions de configuration DNS

## 🔄 Étape 7 : Mettre à jour le site

Chaque fois que vous poussez sur GitHub, Render redéploie automatiquement :

```bash
# Faire vos modifications
git add .
git commit -m "Update: Ajout de nouvelles sections"
git push origin main
```

Render redéploiera automatiquement !

## 📊 Supervision

### Voir les logs
1. Dans le dashboard Render
2. Cliquez sur votre service
3. Allez dans "Logs"

### Redémarrer le service
1. Cliquez sur les 3 points "..."
2. Sélectionnez "Restart"

## 🛠️ Dépannage

### Le service est "Suspended"
- [ ] Mettez à jour vers un plan payant
- [ ] Assurez-vous d'avoir au moins 1 déploiement par 24h

### Erreur "ModuleNotFoundError"
```bash
# Assurez-vous que requirements.txt est à jour
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Update requirements"
git push origin main
```

### Le formulaire ne fonctionne pas
1. Ouvrez la console du navigateur (F12)
2. Regardez les erreurs
3. Vérifiez l'URL de l'API dans `script.js`

## 💰 Coût

- **Plan gratuit** : Démarrage illimité, ressources limitées
- **Plan payant** : À partir de 7$ USD/mois

## 🎉 Félicitations !

Votre site Bamtaare IT est maintenant accessible au monde entier ! 🌍

---

## 📞 Support

- Render Support : https://render.com/docs/
- Forum : https://render.com/community
- Email : support@render.com
