// ============================================
// Configuration de l'API
// ============================================

const API_BASE_URL = 'http://localhost:5000/api';

// ============================================
// ANIMATION AU SCROLL - Observer API
// ============================================

const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate');
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

// Observer les service cards, stat boxes, etc.
document.querySelectorAll('.service-card, .stat, .about-text').forEach(el => {
    observer.observe(el);
});

// ============================================
// SOUMISSION DU FORMULAIRE DE CONTACT
// ============================================

const contactForm = document.querySelector('.contact-form');
if (contactForm) {
    contactForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        // Récupérer les données du formulaire
        const formData = {
            nom: this.querySelector('input[type="text"]').value,
            email: this.querySelector('input[type="email"]').value,
            message: this.querySelector('textarea').value
        };

        // Valider les données côté client
        if (!formData.nom || !formData.email || !formData.message) {
            alert('Veuillez remplir tous les champs');
            return;
        }

        try {
            // Afficher un message de chargement
            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.textContent;
            submitBtn.textContent = 'Envoi en cours...';
            submitBtn.disabled = true;

            // Envoyer les données au serveur
            const response = await fetch(`${API_BASE_URL}/contact`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            });

            const result = await response.json();

            if (response.ok) {
                // Succès
                console.log('✓ Message envoyé avec succès:', result);
                
                // Afficher le message de succès
                const successDiv = document.createElement('div');
                successDiv.className = 'success-message';
                successDiv.textContent = '✓ Merci ! Votre message a été envoyé avec succès.';
                this.appendChild(successDiv);

                // Réinitialiser le formulaire
                this.reset();

                // Supprimer le message après 3 secondes
                setTimeout(() => {
                    successDiv.remove();
                }, 3000);
            } else {
                // Erreur
                console.error('✗ Erreur lors de l\'envoi:', result);
                alert(`Erreur: ${result.message}`);
            }
        } catch (error) {
            console.error('✗ Erreur réseau:', error);
            alert('Erreur de connexion au serveur. Assurez-vous que le serveur Python est en cours d\'exécution sur http://localhost:5000');
        } finally {
            // Réinitialiser le bouton
            submitBtn.textContent = originalText;
            submitBtn.disabled = false;
        }
    });
}

// ============================================
// SMOOTH SCROLL POUR LES LIENS DE NAVIGATION
// ============================================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href !== '#') {
            e.preventDefault();
            const target = document.querySelector(href);
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        }
    });
});

// ============================================
// EFFETS INTERACTIFS SUR LES CARTES
// ============================================

const serviceCards = document.querySelectorAll('.service-card');
serviceCards.forEach(card => {
    card.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-10px)';
    });
    
    card.addEventListener('mouseleave', function() {
        this.style.transform = 'translateY(0)';
    });
});

// ============================================
// COMPTEUR ANIMÉ POUR LES STATISTIQUES
// ============================================

function animateCountUp(element, target, duration = 2000) {
    let current = 0;
    const increment = target / (duration / 16);
    
    const counter = setInterval(() => {
        current += increment;
        if (current >= target) {
            element.textContent = target + '+';
            clearInterval(counter);
        } else {
            element.textContent = Math.floor(current) + '+';
        }
    }, 16);
}

// Observer pour déclencher le compteur
const statsObserver = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting && !entry.target.classList.contains('counted')) {
            entry.target.classList.add('counted');
            const number = parseInt(entry.target.textContent);
            animateCountUp(entry.target, number);
        }
    });
}, { threshold: 0.5 });

document.querySelectorAll('.stat h3').forEach(stat => {
    statsObserver.observe(stat);
});

// ============================================
// INDICATEUR DE SCROLL POUR LA NAVIGATION
// ============================================

window.addEventListener('scroll', function() {
    const navLinks = document.querySelectorAll('.nav-menu a');
    let current = '';

    const sections = document.querySelectorAll('section');
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        if (pageYOffset >= sectionTop - 200) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === '#' + current) {
            link.classList.add('active');
        }
    });
});

// ============================================
// ANIMATION CTA BUTTON
// ============================================

const ctaButtons = document.querySelectorAll('.cta-button');
ctaButtons.forEach(button => {
    button.addEventListener('click', function(e) {
        // Créer un ripple effect
        const ripple = document.createElement('span');
        const rect = this.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        const x = e.clientX - rect.left - size / 2;
        const y = e.clientY - rect.top - size / 2;

        ripple.style.width = ripple.style.height = size + 'px';
        ripple.style.left = x + 'px';
        ripple.style.top = y + 'px';
        ripple.classList.add('ripple');

        this.appendChild(ripple);

        // Supprimer le ripple après l'animation
        setTimeout(() => ripple.remove(), 600);
    });
});

// ============================================
// RESPONSIVE MENU (optionnel pour futur mobile)
// ============================================

function setupResponsiveMenu() {
    const navbar = document.querySelector('.navbar');
    const navMenu = document.querySelector('.nav-menu');
    
    if (window.innerWidth <= 768) {
        // Code pour menu mobile peut être ajouté ici
    }
}

window.addEventListener('resize', setupResponsiveMenu);
setupResponsiveMenu();

// ============================================
// LOGS DE DÉMARRAGE
// ============================================

console.log('✓ Site chargé avec succès');
console.log('✓ Animations au scroll actives');
console.log('✓ Formulaire de contact prêt');
