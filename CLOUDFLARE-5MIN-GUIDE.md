# ⚡ CLOUDFLARE PAGES - 5 MINUTES SETUP

**Temps total**: 5 minutes
**Difficulté**: Très facile (juste des clics)
**Bénéfice**: Site LIVE sur https://compararcripto.com

---

## 🎯 OBJECTIF

Connecter votre repo GitHub (`compararcripto`) à Cloudflare Pages et router le domaine.

---

## 📋 PRÉREQUIS ✅

- ✅ Compte Cloudflare (vous en avez un - domaine enregistré)
- ✅ Compte GitHub (vous en avez un - repo créé avec 10 articles)
- ✅ Domaine `compararcripto.com` (chez Cloudflare)

---

## ⏱️ ÉTAPE 1 (30 sec): Aller à Cloudflare Pages

1. Ouvrez: **https://dash.cloudflare.com/**
2. Connectez-vous (si nécessaire)
3. Cherchez **"Pages"** dans le menu de gauche
4. Cliquez dessus

✅ Vous êtes sur la page Pages

---

## ⏱️ ÉTAPE 2 (1 min): Créer un nouveau projet

1. Cliquez sur le bouton bleu: **"Create a project"**

   ![](image: bouton bleu 'Create a project')

2. Ou si vous ne le voyez pas, cliquez sur **"+ Create application"**

✅ Une popup ou nouvelle page s'ouvre

---

## ⏱️ ÉTAPE 3 (1 min 30 sec): Connecter GitHub

1. Vous verrez 2 options :
   - **"Create using Wrangler"**
   - **"Connect to Git"** ← CELUI-CI

2. Cliquez sur **"Connect to Git"**

   ![](image: bouton 'Connect to Git')

3. Une page GitHub s'ouvre pour autoriser Cloudflare

4. Autorisez (cliquez sur le bouton vert)

✅ Vous êtes redirigé vers Cloudflare

---

## ⏱️ ÉTAPE 4 (1 min): Sélectionner votre repo

1. Cherchez **"compararcripto"** dans la liste des repos
2. Cliquez dessus

   ![](image: liste 'compararcripto' repo)

3. Si vous avez plusieurs repos, tapez "compararcripto" dans le filtre

✅ Repo sélectionné

---

## ⏱️ ÉTAPE 5 (1 min): Configuration du build

Vous verrez un formulaire avec :

- **Project name**: `compararcripto` (OK)
- **Production branch**: `main` (OK)
- **Framework preset**: **Sélectionnez "None"** ← Important!
- **Build command**: (vide - OK)
- **Build output directory**: (vide - OK)
- **Root directory**: (vide - OK)

**Assurez-vous Framework = "None"** (pas Next.js, pas React, pas Hugo... juste HTML statique)

✅ Configuration OK

---

## ⏱️ ÉTAPE 6 (30 sec): Lancer le déploiement

1. Cliquez sur le bouton bleu : **"Save and Deploy"**

   ![](image: 'Save and Deploy')

2. Cloudflare affichera un message : "Your site is being deployed..."

3. **Attendez 1-2 minutes** (le message disparaîtra quand c'est prêt)

✅ Déploiement lancé!

---

## ⏱️ ÉTAPE 7 (1 min): Ajouter le domaine

Une fois le déploiement terminé:

1. Allez à **Settings** (en haut)
2. Cliquez sur **Domains**
3. Cliquez sur le bouton : **"Add domain"**

   ![](image: 'Add domain')

4. Vous verrez une liste de domaines disponibles
5. Cherchez et sélectionnez : **"compararcripto.com"**

   ![](image: compararcripto.com domaine)

6. Cliquez sur **"Continue"** ou **"Confirm"**

✅ Domaine routé!

---

## 🎉 C'EST FAIT!

Votre site est maintenant **LIVE** sur:

```
https://compararcripto.com ✅
```

### Vérifier que ça marche:

Attendez 1-2 minutes, puis:

```bash
curl -sI https://compararcripto.com | head -1
# Doit afficher: HTTP/1.1 200 OK
```

Ou ouvrez juste votre navigateur et allez à **https://compararcripto.com**

Vous devriez voir votre homepage (index.html) avec les 10 articles listés!

---

## 📊 RÉSUMÉ

| Étape | Temps | ✅ |
|-------|-------|-----|
| 1. Aller à Pages | 30 sec | ✅ |
| 2. Create project | 1 min | ✅ |
| 3. Connect GitHub | 1 min 30 | ✅ |
| 4. Sélectionner repo | 1 min | ✅ |
| 5. Config build | 1 min | ✅ |
| 6. Save and Deploy | 30 sec | ✅ |
| 7. Add domain | 1 min | ✅ |
| **TOTAL** | **~7 min** | ✅ |

*+ Attente de déploiement (1-2 min) en parallèle*

---

## ❓ PROBLÈMES COURANTS

### "Je ne vois pas mon repo GitHub"

**Solution**: Vous devez autoriser Cloudflare à accéder à vos repos GitHub. Cherchez "Install" ou "Authorize" à côté de votre username GitHub.

### "Framework preset ne montre pas 'None'"

**Solution**: Cherchez "Static site" ou "No framework" à la place. Cloudflare le propose souvent ainsi.

### "Le déploiement prend trop long"

**Solution**: C'est normal. Cloudflare peut prendre 2-5 minutes la première fois. Pas besoin de cliquer sur rien - attendre.

### "Le domaine compararcripto.com n'apparaît pas"

**Solution**:
- Vérifiez que le domaine est dans Cloudflare (il l'est - vous l'avez enregistré)
- Si toujours pas visible, cliquez sur "Add domain" et tapez "compararcripto.com" manuellement

---

## 📈 APRÈS CLOUDFLARE

Une fois LIVE, les prochaines étapes seront:

1. ✅ GA4 verification (G-LQVYBFTPH8 déjà en place)
2. ⏳ GSC submission + verification
3. ⏳ Affiliate accounts (MEXC, KuCoin, Binance, Coinbase)

---

**Bonne chance! 🚀**

*Questions? Regardez simplement le statut sur: https://dash.cloudflare.com/pages*

