# 🚀 Site Web Professionnel Dynamique

Un site web moderne et interactif inspiré de [GOX.ca](https://www.gox.ca/fr/accueil), créé avec HTML5, CSS3 et JavaScript vanille.

## 📋 Fonctionnalités

### ✨ Caractéristiques Principales
- **Navigation responsive** avec smooth scroll
- **Hero section** avec gradient dynamique
- **Grille de services** avec effets au survol
- **Section À propos** avec statistiques animées
- **Formulaire de contact** fonctionnel
- **Footer informatif** avec liens utiles
- **Animations au scroll** avec Intersection Observer API
- **Design épuré et professionnel**
- **Entièrement responsive** (mobile, tablette, desktop)

### 🎨 Effets Interactifs
- Animations des cartes de services au survol
- Compteur animé pour les statistiques
- Ripple effect sur les boutons
- Transition smooth au scroll
- Indicateur de section active dans la navigation
- Feedback visuel sur le formulaire

## 🛠️ Technologies Utilisées

- **HTML5** - Structure sémantique
- **CSS3** - Design moderne avec variables CSS et grid/flexbox
- **JavaScript (Vanilla)** - Interactivité sans dépendances externes
  - Intersection Observer API
  - Event Listeners
  - DOM Manipulation

## 📁 Structure du Projet

```
projet/
├── index.html        # Page HTML principale
├── styles.css        # Feuille de styles CSS
├── script.js         # Logique JavaScript
└── README.md         # Ce fichier
```

## 🚀 Comment Utiliser

### 1. **Ouvrir le projet**
```bash
# Cloner ou télécharger les fichiers
# Ouvrir index.html dans un navigateur
```

### 2. **Démarrer un serveur local** (optionnel mais recommandé)

**Avec Python 3:**
```bash
python -m http.server 8000
```

**Avec Python 2:**
```bash
python -m SimpleHTTPServer 8000
```

**Avec Node.js (si http-server est installé):**
```bash
npx http-server
```

Puis accédez à `http://localhost:8000` dans votre navigateur.

## 📱 Sections du Site

### 1. **Navigation (Navbar)**
- Logo/Titre de l'entreprise
- Liens vers les sections principales
- Sticky navigation

### 2. **Hero Section**
- Titre accrocheur
- Sous-titre descriptif
- Bouton CTA (Call-to-Action)

### 3. **Services**
- 4 cartes de services
- Icônes emoji
- Description et lien "EN SAVOIR PLUS"
- Effets au survol

### 4. **À Propos**
- Texte descriptif
- Statistiques animées (clients, années, experts)

### 5. **Contact**
- Formulaire interactif
- Informations de contact
- Validation de formulaire

### 6. **Footer**
- Navigation secondaire
- Liens services
- Liens légaux
- Copyright

## 🎯 Effets JavaScript Principaux

### Intersection Observer (Animations au scroll)
Détecte quand les éléments deviennent visibles et déclenche les animations.

```javascript
const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate');
        }
    });
});
```

### Compteur Animé
Anime les statistiques quand elles deviennent visibles.

### Smooth Scroll
Les liens internes font défiler vers la section sans saut.

### Gestion du Formulaire
Soumet et affiche un message de succès sans rechargement de page.

## 🎨 Personnalisation

### Changer les Couleurs

Modifiez les variables CSS dans `styles.css`:

```css
:root {
    --primary-color: #1e3a5f;      /* Bleu foncé */
    --secondary-color: #ff6b35;    /* Orange */
    --light-bg: #f8f9fa;           /* Gris très clair */
    /* ... autres couleurs ... */
}
```

### Ajouter des Services

Ajoutez une nouvelle carte dans la section services:

```html
<div class="service-card">
    <div class="service-icon">🔒</div>
    <h3>Sécurité</h3>
    <p>Protégez vos données avec nos solutions de sécurité avancées.</p>
    <a href="#" class="service-link">EN SAVOIR PLUS →</a>
</div>
```

### Modifier le Texte

Tous les textes sont directement dans `index.html` et faciles à modifier.

## 📊 Responsive Design

Le site s'adapte automatiquement à:
- **Desktop** (1200px+)
- **Tablette** (768px - 1199px)
- **Mobile** (-767px)

Les breakpoints peuvent être ajustés dans `styles.css`.

## 🔧 Améliorations Futures Possibles

- [ ] Ajouter une base de données
- [ ] Implémenter un vrai système de contact (envoi d'email)
- [ ] Ajouter des images/photos
- [ ] Créer des pages de détail pour chaque service
- [ ] Implémenter un système de pagination
- [ ] Ajouter un blog
- [ ] Intégrer des cartes Google Maps
- [ ] Ajouter des témoignages clients
- [ ] Créer un portfolio/galerie

## 📝 Notes

- Le formulaire affiche actuellement un message de succès simulé
- Pour envoyer des emails réels, vous devrez implémenter un backend
- Les styles utilisent CSS Grid et Flexbox pour la flexibilité
- Le code JavaScript est commenté pour faciliter la compréhension

## 📄 Licence

Libre d'utilisation pour vos projets personnels et commerciaux.

---

**Créé avec ❤️ pour démontrer les capacités du web moderne**
