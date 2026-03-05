# GA4 + GSC Setup Guide — MANUAL (nécessite Google Account)

## 🎯 Étapes à faire MANUELLEMENT

Malheureusement, Google bloque l'automatisation bot pour GA4 et GSC. Vous devez faire ceci manuellement dans votre navigateur.

---

## STEP 1: Créer GA4 Property

1. **Accédez Google Analytics**: https://analytics.google.com/
2. **Connectez-vous** avec votre compte Google
3. **Créez une nouvelle propriété**:
   - Cliquez sur **"Administration"** (engrenage, bas gauche)
   - Cliquez **"Créer une propriété"**
   - Nom: `Compararcripto.com`
   - Fuseau horaire: `(UTC+01:00) Amsterdam, Berlin...` ou votre fuseau
   - Devise: `EUR` (ou votre devise)
   - Créez
4. **Obtenez l'ID GA4**:
   - Allez dans **"Admin" → "Propriétés"**
   - Cherchez **"Informations sur la propriété"**
   - Copiez l'ID (format: `G-XXXXXXXXXX`)
5. **Créez le flux de données web**:
   - Allez dans **"Admin" → "Flux de données"**
   - Cliquez **"Créer un flux"**
   - Sélectionnez **"Web"**
   - URL: `https://compararcripto.com`
   - Nom du flux: `Compararcripto Main`
   - Créez le flux
6. **Obtenez le code de suivi**:
   - Dans le flux créé, allez dans **"Paramètres du flux de données"**
   - Copiez le code Google Tag Manager (ou le code GA4 direct)

### Exemple de code GA4 à ajouter dans `index.html` (ligne 17):
```html
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXX"></script>
<script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-XXXXX');
</script>
```

Remplacez `G-XXXXX` par votre ID réel.

---

## STEP 2: Ajouter le Code GA4 au Site

1. **Éditez `index.html`**:
   ```bash
   nano ~/Library/CloudStorage/Dropbox/METIS/compararcripto/index.html
   ```

2. **Trouvez la ligne 17** (dans la section `<head>`):
   ```html
   <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXX"></script>
   ```

3. **Remplacez `G-XXXXX`** par votre vrai GA4 ID (ex: `G-ABCD1234EF`)

4. **Sauvegardez et committez**:
   ```bash
   cd ~/Library/CloudStorage/Dropbox/METIS/compararcripto
   git add index.html
   git commit -m "Add GA4 tracking code"
   git push
   ```

5. **Cloudflare Pages redéploiera automatiquement** → ~2 minutes

---

## STEP 3: Créer Propriété Google Search Console (GSC)

1. **Accédez Google Search Console**: https://search.google.com/search-console
2. **Cliquez "Ajouter une propriété"**
3. **Sélectionnez "Domaine"** (pas "URL prefix")
4. **Entrez**: `compararcripto.com`
5. **Vérifiez la propriété**:
   - Google vous demandera de vérifier ownership
   - Méthode recommandée: **Enregistrement DNS**
   - Copiez la valeur TXT que Google fournit
   - Allez à votre **registrar (Cloudflare)** → DNS
   - Ajoutez un enregistrement TXT avec la valeur
   - Attendez 5-10 min pour que le DNS se propage
   - Retournez à GSC et cliquez "Vérifier"

### Vérification via Cloudflare DNS:
1. Ouvrez https://dash.cloudflare.com
2. Sélectionnez `compararcripto.com`
3. Allez dans **DNS**
4. Cliquez **"Ajouter un enregistrement"**
5. Type: **TXT**
6. Nom: `@` (ou ce que Google dit)
7. Contenu: (la valeur TXT que Google fournit)
8. Cliquez **"Sauvegarder"**
9. Retournez à GSC et cliquez "Vérifier"

---

## STEP 4: Tester Que Tout Fonctionne

### Tester GA4:
1. Ouvrez votre site: https://compararcripto.com
2. Ouvrez DevTools (F12)
3. Allez dans **"Network"**
4. Cherchez des requêtes à `googletagmanager.com` ou `google-analytics`
5. Retournez à Google Analytics
6. Allez dans **"Rapports" → "En temps réel"**
7. Vous devriez voir **1 utilisateur actif**

### Tester GSC:
1. Dans GSC, allez dans **"Aperçu"**
2. Cliquez **"Demander une indexation"**
3. Entrez: `https://compararcripto.com`
4. Attendez quelques minutes
5. Vous devriez voir le site en attente d'indexation

---

## STEP 5: Soumettre Sitemap à GSC

1. Dans GSC, allez dans **"Sitemaps"**
2. Cliquez **"Ajouter/Tester un sitemap"**
3. Entrez: `https://compararcripto.com/sitemap.xml`
4. Cliquez **"Soumettre"**
5. Attendez quelques heures pour l'indexation

---

## ⏱️ Timeline

- GA4 setup: 10 minutes
- GSC setup: 15 minutes (+ 5-10 min pour DNS propagation)
- **Total: 30-40 minutes** (dont la plupart c'est attendre)

---

## 📋 Checklist

- [ ] GA4 property créée
- [ ] GA4 ID copié (G-XXXXX)
- [ ] Code GA4 ajouté à `index.html`
- [ ] Code pushé à GitHub
- [ ] Cloudflare Pages redéployé
- [ ] GA4 vérifiée (utilisateurs actifs visibles)
- [ ] GSC propriété créée
- [ ] Vérification DNS terminée
- [ ] Sitemap soumis à GSC
- [ ] Indexation en cours

---

## ❓ Problèmes Courants

**Q: GA4 n'affiche pas les utilisateurs actifs**
A: Attendez 24-48h après le premier déploiement. Vérifiez que le code est correctement injecté dans le HTML.

**Q: GSC dit "Propriété non vérifiée"**
A: Vérifiez que l'enregistrement TXT a été créé correctement dans Cloudflare DNS. Attendez 10 min pour la propagation.

**Q: Je ne vois pas mon site dans GSC rapports**
A: Attendez 48-72h. Google indexe progressivement. Vous pouvez "Demander l'indexation" pour accélérer.

---

## 🚀 Prochaines Étapes

Une fois GA4 + GSC live:
1. Attendez 1-2 semaines pour voir du trafic
2. Analysez les keywords en GSC
3. Identifiez les "quick wins" (position 11-20, volume > 100)
4. Enrichissez ces articles pour les passer à position 1-10

