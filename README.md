# vastu-energie.be — Guide d'utilisation

Site vitrine de David Girol Garcia, consultant en Vastu Shastra en Wallonie.
Stack : HTML5 · CSS3 · JavaScript minimal · GitHub Pages · Formspree.

---

## Tester le site en local

Ouvrir un terminal dans ce dossier et lancer :

```bash
npx serve .
```

Ou, si Python est installé :

```bash
python3 -m http.server 8000
```

Puis ouvrir `http://localhost:8000` dans votre navigateur.

> Important : ne pas ouvrir directement `index.html` dans le navigateur
> (les chemins absolus `/assets/...` ne fonctionneraient pas sans serveur local).

---

## Structure des fichiers

```
vastu-energie.be/
│
├── index.html                    ← Page d'accueil
├── vastu-shastra/index.html      ← Page "Le Vastu Shastra"
├── harmonisation/index.html      ← Page "L'harmonisation en pratique"
├── pour-qui/index.html           ← Page "Pour qui / Dans quels cas"
├── a-propos/index.html           ← Page "À propos"
├── contact/index.html            ← Page "Contact & tarifs"
├── blog/
│   ├── index.html                ← Liste des articles
│   └── [slug-article]/
│       └── index.html            ← Page d'un article
├── mentions-legales/index.html
├── politique-confidentialite/index.html
│
├── assets/
│   ├── css/main.css              ← Feuille de style unique (toutes les pages)
│   ├── js/
│   │   ├── nav.js                ← Menu mobile
│   │   └── form.js               ← Validation formulaire contact
│   └── img/
│       ├── og/                   ← Images Open Graph (1200×630 px, WebP recommandé)
│       └── photos/               ← Vos photos (formats dans la section dédiée)
│
├── sitemap.xml                   ← Sitemap SEO
├── robots.txt
├── CNAME                         ← Nom de domaine GitHub Pages
└── README.md                     ← Ce fichier
```

---

## Modifier une page existante

Ouvrir le fichier HTML de la page concernée dans un éditeur de texte
(VS Code recommandé). Les contenus à compléter sont signalés par :

- Des commentaires HTML : `<!-- À RÉDIGER PAR DAVID : ... -->`
- Des encadrés orange visibles dans le navigateur

**Règle de base :** ne modifier que le contenu entre les balises.
Ne pas toucher aux balises `<head>`, aux classes CSS, ni aux scripts
sans être sûr de ce que vous faites.

---

## Configurer Formspree (formulaire de contact)

1. Créer un compte sur [formspree.io](https://formspree.io)
2. Créer un nouveau formulaire — noter l'ID (format `xabc1234`)
3. Dans `contact/index.html`, remplacer :
   ```html
   action="https://formspree.io/f/YOUR_FORMSPREE_ID"
   ```
   par :
   ```html
   action="https://formspree.io/f/xabc1234"
   ```
4. Tester avec une vraie soumission avant de mettre en ligne.

---

## Ajouter un article de blog

1. Créer un nouveau dossier dans `blog/` avec un slug explicite :
   ```
   blog/vastu-et-renovation/
   ```
2. Copier `blog/vastu-peb-deux-lectures/index.html` dans ce nouveau dossier
3. Dans le nouveau fichier, modifier :
   - `<title>` et `<meta name="description">`
   - `<link rel="canonical">`
   - Les balises Open Graph (`og:url`, `og:title`, `og:description`, `og:image`)
   - Le JSON-LD : `headline`, `url`, `datePublished`, `dateModified`
   - Le fil d'Ariane (breadcrumb)
   - Le `<h1>` et le chapeau `<p class="lead">`
   - Le corps de l'article (remplacer le placeholder orange)
4. Ajouter une carte `<article class="article-card">` dans `blog/index.html`
5. Ajouter l'URL dans `sitemap.xml`

---

## Ajouter une photo

Formats recommandés par emplacement :

| Emplacement         | Dimensions min. | Format  | Chemin suggéré                    |
|---------------------|-----------------|---------|-----------------------------------|
| Hero accueil        | 900 × 1 100 px  | WebP    | `assets/img/hero.webp`            |
| Portrait à propos   | 480 × 600 px    | WebP    | `assets/img/david-apropos.webp`   |
| Photo présentation  | 480 × 600 px    | WebP    | `assets/img/david-portrait.webp`  |
| Images blog         | 800 × 450 px    | WebP    | `assets/img/blog/nom-article.webp`|
| Open Graph          | 1 200 × 630 px  | JPG/WebP| `assets/img/og/og-home.jpg`       |

Pour chaque image, remplacer le `div` placeholder dans le HTML par :

```html
<picture>
  <source srcset="/assets/img/nom-image.webp" type="image/webp">
  <img src="/assets/img/nom-image.jpg" alt="Description de l'image" width="XXX" height="YYY" loading="lazy">
</picture>
```

---

## Publier les modifications sur GitHub Pages

```bash
git add .
git commit -m "Description du changement"
git push origin main
```

Le site est mis à jour automatiquement dans 1 à 2 minutes.

---

## Configurer le nom de domaine (une seule fois)

1. Le fichier `CNAME` contient déjà `vastu-energie.be`
2. Chez votre registrar (registraire du domaine), configurer les DNS :
   - Enregistrement `A` vers les IP GitHub Pages :
     ```
     185.199.108.153
     185.199.109.153
     185.199.110.153
     185.199.111.153
     ```
   - Enregistrement `CNAME` : `www` → `[votre-compte].github.io`
3. Dans les paramètres du dépôt GitHub → Pages → Custom domain : `vastu-energie.be`
4. Cocher "Enforce HTTPS"

---

## Décisions ouvertes (liste mise à jour)

| # | Décision                          | Statut        |
|---|-----------------------------------|---------------|
| 1 | Contenu page Vastu Shastra        | À rédiger     |
| 2 | Contenu page Harmonisation        | À rédiger     |
| 3 | Contenu page Pour qui             | À rédiger     |
| 4 | Contenu page À propos             | À fournir (a-propos-v1.md) |
| 5 | Contenu page d'accueil (textes)   | À rédiger     |
| 6 | Témoignages (textes réels)        | À fournir     |
| 7 | Toutes les photos                 | À fournir     |
| 8 | ID Formspree                      | À configurer  |
| 9 | Communes desservies (Hainaut/BW/Namur) | À préciser |
| 10| Baseline footer                   | À rédiger     |
| 11| Note tarifs + paiement échelonné  | À préciser    |
| 12| Date publication article-pivot    | À définir     |
