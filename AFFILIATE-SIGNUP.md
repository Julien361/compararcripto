# Affiliate Signup — Compararcripto (PT-BR Crypto)

**Goal**: Get 4 affiliate codes + activate tracking
**Timeline**: 30 min per program = 2h total
**Revenue Impact**: €4,300-11,000/month once active

---

## 🔴 MEXC — 70% LIFETIME (Highest Commission!)

**Signup**: https://www.mexc.com/partner
**Commission**: 70% of trading fees (lifetime)

### Step 1: Create Account
1. Go to https://www.mexc.com/partner
2. Click **"Become a Partner"**
3. Fill form:
   - Email: contact@metis-digital.click
   - Password: [Use secure password]
   - Referral URL: https://compararcripto.com/exchanges/mexc
4. Submit + verify email
5. Complete KYC (ID verification)

### Step 2: Get Referral Code
1. Dashboard → **Invite Code**
2. Copy your referral code (format: `ABC123DEF`)
3. Save to file: `~/Desktop/affiliate-codes.txt`

### Step 3: Update index.html
```html
<!-- Find this section in index.html around line 150 -->
<a href="https://www.mexc.com/user/register?inviteCode=ABC123DEF" class="btn-primary">
  Abrir Conta MEXC
</a>
```

### Timeline: 15-20 min

---

## 🟠 KUCOIN — 60% LIFETIME (Second Highest)

**Signup**: https://www.kucoin.com/referral
**Commission**: 60% of trading fees (lifetime)

### Step 1: Create Account
1. Go to https://www.kucoin.com/referral
2. Click **"Become Referrer"**
3. Fill form (same email as above):
   - Email: contact@metis-digital.click
   - Account type: Website/Blog
   - Website: https://compararcripto.com
4. Submit + verify email
5. Complete identity verification

### Step 2: Get Referral Code
1. Dashboard → **Referral Program** → **My Code**
2. Copy referral link (format: `https://www.kucoin.com/r/ref/XXXXXX`)
3. Save to file

### Step 3: Update index.html
```html
<!-- Find this section in index.html around line 160 -->
<a href="https://www.kucoin.com/r/ref/XXXXXX" class="btn-primary">
  Abrir Conta KuCoin
</a>
```

### Timeline: 15-20 min

---

## 🟡 BINANCE — 50% LIFETIME

**Signup**: https://www.binance.com/en/activity/referral
**Commission**: 50% of commission (lifetime)

### Step 1: Create Account
1. Go to https://www.binance.com/en/activity/referral
2. Sign in with Binance account (or create new)
3. Click **"Invite Friend"** → **"Create Referral Link"**
4. Fill details:
   - Referral name: "Compararcripto"
   - Commission tier: 50% (if available) or standard
5. Click **"Create Link"**

### Step 2: Get Referral Link
1. Dashboard → **Referral Program**
2. Copy your referral link (format: `https://www.binance.com/ref/XXXXXX`)
3. Save to file

### Step 3: Update index.html
```html
<!-- Find this section in index.html around line 170 -->
<a href="https://www.binance.com/ref/XXXXXX" class="btn-primary">
  Abrir Conta Binance
</a>
```

### Timeline: 10-15 min

---

## 🟢 COINBASE — 30% RECURRING

**Signup**: https://www.coinbase.com/affiliates
**Commission**: 30% recurring (per transaction)

### Step 1: Create Account
1. Go to https://www.coinbase.com/affiliates
2. Click **"Sign Up"**
3. Fill form:
   - Email: contact@metis-digital.click
   - Publisher type: Website/Blog
   - Website: https://compararcripto.com
4. Submit + verify email
5. Complete KYC

### Step 2: Get Affiliate Link
1. Dashboard → **Creative Assets** → **Links**
2. Select link type: **Referral Link**
3. Copy your link (format: `https://www.coinbase.com/join/XXXXXX`)
4. Save to file

### Step 3: Update index.html
```html
<!-- Find this section in index.html around line 180 -->
<a href="https://www.coinbase.com/join/XXXXXX" class="btn-primary">
  Abrir Conta Coinbase
</a>
```

### Timeline: 10-15 min

---

## 📋 FINAL CHECKLIST

```
[ ] MEXC account created + code: _____________
[ ] KuCoin account created + link: _____________
[ ] Binance account created + link: _____________
[ ] Coinbase account created + link: _____________

[ ] All 4 links updated in index.html
[ ] index.html committed + pushed
[ ] Cloudflare auto-deployed new version
[ ] Test each affiliate link (should open signup page)
```

## 💰 TRACKING SETUP

Once live, track affiliate conversions in GA4:

```javascript
<!-- Add this to index.html AFTER GA4 initialization -->
<script>
document.querySelectorAll('a[data-affiliate]').forEach(link => {
  link.addEventListener('click', () => {
    gtag('event', 'affiliate_click', {
      'exchange': link.dataset.affiliate,
      'url': link.href
    });
  });
});
</script>

<!-- Update affiliate links with data attribute -->
<a href="..." class="btn-primary" data-affiliate="mexc">...</a>
<a href="..." class="btn-primary" data-affiliate="kucoin">...</a>
<a href="..." class="btn-primary" data-affiliate="binance">...</a>
<a href="..." class="btn-primary" data-affiliate="coinbase">...</a>
```

## 📊 Revenue Projection

| Exchange | Commission | Est. Monthly Users | Est. Revenue |
|----------|------------|-------------------|-------------|
| MEXC | 70% | 50 | €2,100 |
| KuCoin | 60% | 40 | €1,440 |
| Binance | 50% | 60 | €1,800 |
| Coinbase | 30% | 30 | €270 |
| **TOTAL** | - | **180** | **€5,610/month** |

*(Based on 180 monthly signups, €150 avg first transaction)*

---

**Status**: READY FOR EXECUTION
**Next**: GA4 setup on 18 sites (Blocker 3)
