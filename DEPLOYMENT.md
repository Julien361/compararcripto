# Compararcripto.com — Deployment Guide

**Status**: Ready for Cloudflare Pages deployment ✅

## 📋 What's Ready

✅ Git repo initialized (local)
✅ index.html (PT-BR landing page)
✅ affiliates.json (4 programs)
✅ OpenGraph + GA4 placeholder
✅ First commit: `483ade1`

## 🚀 STEP 1: Push to GitHub

```bash
# Create new GitHub repo "compararcripto" (https://github.com/YOUR-USERNAME/compararcripto)

cd ~/Library/CloudStorage/Dropbox/METIS/compararcripto

# Add remote
git remote add origin https://github.com/YOUR-USERNAME/compararcripto.git
git branch -M main
git push -u origin main
```

## 🔗 STEP 2: Connect to Cloudflare Pages

1. Open https://dash.cloudflare.com/
2. Go to **Pages**
3. Click **Create a project** → **Connect to Git**
4. Select GitHub account
5. Find repository: **compararcripto**
6. Click **Connect**
7. Framework preset: **None** (static HTML)
8. Build settings: Leave empty (no build needed)
9. Click **Save and Deploy**

## ✨ STEP 3: Configure Domain

1. After deploy, go to **Settings** → **Domains**
2. Click **Add domain**
3. Select: `compararcripto.com` (already connected to Cloudflare)
4. Confirm routing

## 📊 STEP 4: Update GA4

```bash
# Once deployed:
1. Create GA4 property for compararcripto.com in Google Analytics
2. Get property ID: G-XXXXXX
3. Update index.html line 17:
   <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXX"></script>
4. Commit + push
5. Cloudflare Pages auto-deploys
```

## 💰 STEP 5: Activate Affiliates

```bash
# 1. Signup for 4 programs (see below)
# 2. Get referral codes
# 3. Update index.html affiliate buttons with real URLs
# 4. Commit + push

Affiliate signup links:
- MEXC: https://www.mexc.com/partner (70% lifetime)
- KuCoin: https://www.kucoin.com/referral (60% lifetime)
- Binance: https://www.binance.com/en/activity/referral (50% lifetime)
- Coinbase: https://www.coinbase.com/affiliates (30% recurring)
```

## 📈 STEP 6: Verify Live

```bash
curl -sI https://compararcripto.com | head -1
# Should return: HTTP/1.1 200 OK

# Check GA4 tracking:
1. Open https://compararcripto.com in browser
2. DevTools → Network → look for gtag requests
3. Google Analytics → Real-time → should show 1 user
```

## 🔍 Deployment Checklist

- [ ] GitHub repo created + code pushed
- [ ] Cloudflare Pages connected (auto-deploy enabled)
- [ ] Domain routed (compararcripto.com → Cloudflare Pages)
- [ ] GA4 property created + ID updated
- [ ] Affiliates signed up + codes in index.html
- [ ] Test: Visit https://compararcripto.com (should load)
- [ ] Test: Click affiliate button (should track in GA4)

## ⏱️ Timeline

- GitHub push: 2 min
- Cloudflare setup: 5 min
- Deploy: Automatic (< 1 min)
- GA4 setup: 5 min
- **Total: 15 minutes** (+ affiliate signup time)

---

**Next**: Blockers 3 & 4 (GA4 setup + affiliate signup instructions)
