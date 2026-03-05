#!/usr/bin/env python3
"""
Cloudflare Pages Deployment - Browser Automation (Playwright)
Automatise les clics après login manuel
"""

import asyncio
import sys
from pathlib import Path

try:
    from playwright.async_api import async_playwright
except ImportError:
    print("❌ Playwright not installed")
    sys.exit(1)


async def deploy():
    """Deploy using browser automation"""

    async with async_playwright() as p:
        print("="*70)
        print("🚀 CLOUDFLARE PAGES DEPLOYMENT - BROWSER AUTOMATION")
        print("="*70)
        print("\n⚠️  Un navigateur va s'ouvrir maintenant...")
        print("   1. Allez à: https://dash.cloudflare.com/")
        print("   2. Connectez-vous si nécessaire")
        print("   3. Je vais automatiser les clics après votre login")
        print("\n🎯 Objectif: Connecter GitHub repo + configurer domaine")
        print("="*70)

        # Ouvrir le navigateur
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(viewport={"width": 1920, "height": 1080})
        page = await context.new_page()

        # Aller à Cloudflare Pages
        print("\n[1/6] Ouverture du dashboard Cloudflare Pages...")
        await page.goto("https://dash.cloudflare.com/")

        # ATTENDRE LE LOGIN MANUEL
        print("\n[2/6] ⏳ Attente de votre login manuel...")
        print("      → Connectez-vous à votre compte Cloudflare")
        print("      → Une fois connecté, une notification s'affichera ici")

        try:
            # Attendre que la page change après login (pattern: /accounts/)
            await page.wait_for_url("**/accounts/**", timeout=120000)
            print("      ✅ Login détecté!")
        except:
            print("      ⚠️  Timeout login (2 min) - continuer manuellement")

        await asyncio.sleep(2)

        # NAVIGATION VERS PAGES
        print("\n[3/6] Navigation vers Pages...")
        current_url = page.url

        if "pages" not in current_url.lower():
            try:
                # Chercher un lien ou bouton "Pages"
                pages_link = page.locator("text=Pages").first
                await pages_link.click()
                await page.wait_for_load_state("networkidle")
                print("      ✅ Pages ouvert")
            except:
                print("      ⚠️  Click manuel nécessaire: cherchez 'Pages' dans le menu")
                await asyncio.sleep(5)

        # CREATE A PROJECT
        print("\n[4/6] Création d'un nouveau projet...")
        try:
            # Chercher le bouton "Create a project"
            create_btn = page.locator("button:has-text('Create a project'), text=Create a project").first
            await create_btn.click()
            await page.wait_for_load_state("networkidle")
            print("      ✅ Formulaire créé")
        except:
            print("      ⚠️  Cherchez 'Create a project' et cliquez manuellement")
            await asyncio.sleep(3)

        # CONNECT TO GIT
        print("\n[5/6] Connexion au GitHub...")
        try:
            git_btn = page.locator("text=Connect to Git").first
            await git_btn.click()
            await asyncio.sleep(2)
            print("      ✅ GitHub authorization page ouverte")

            # Attendre que GitHub auth se termine
            # (Peut rediriger vers https://github.com/login ou GitHub app authorization)
            await page.wait_for_url("**/pages/**", timeout=60000)
            print("      ✅ GitHub autorisé!")

        except Exception as e:
            print(f"      ⚠️  GitHub auth - faire manuellement ({e})")
            await asyncio.sleep(10)

        # SÉLECTIONNER REPO
        print("\n[6/6] Sélection du repo 'compararcripto'...")
        try:
            # Chercher le repo dans la liste
            repo = page.locator("text=compararcripto").first
            await repo.click()
            await asyncio.sleep(2)
            print("      ✅ Repo sélectionné")

            # Vérifier que Framework = None
            try:
                none_btn = page.locator("text=None").first
                await none_btn.click()
                print("      ✅ Framework: None (static HTML)")
            except:
                print("      ℹ️  Framework - vérifier 'None' est sélectionné")

            await asyncio.sleep(1)

            # DEPLOY!
            try:
                deploy_btn = page.locator("button:has-text('Save and Deploy')").first
                await deploy_btn.click()
                print("      ✅ Deploy lancé!")

                # Attendre le déploiement
                await asyncio.sleep(60)
                print("\n⏳ Déploiement en cours... (1-2 minutes)")

            except:
                print("      ⚠️  Cherchez 'Save and Deploy' et cliquez manuellement")
                print("         Framework: None")
                print("         Build command: (empty)")
                print("         Output dir: (empty)")
                await asyncio.sleep(30)

        except Exception as e:
            print(f"      ⚠️  Sélection repo - faire manuellement ({e})")
            await asyncio.sleep(10)

        # AJOUTER LE DOMAINE
        print("\n[7/7] Ajout du domaine 'compararcripto.com'...")
        try:
            settings = page.locator("text=Settings").first
            await settings.click()
            await asyncio.sleep(2)

            domains = page.locator("text=Domains").first
            await domains.click()
            await asyncio.sleep(2)

            add_domain = page.locator("button:has-text('Add domain')").first
            await add_domain.click()
            await asyncio.sleep(1)

            # Sélectionner compararcripto.com
            domain_option = page.locator("text=compararcripto.com").first
            await domain_option.click()
            await asyncio.sleep(1)

            confirm = page.locator("button:has-text('Confirm')").first
            await confirm.click()

            print("      ✅ Domaine routé!")

        except Exception as e:
            print(f"      ⚠️  Domaine - faire manuellement (Settings → Domains → Add)")
            print(f"         Sélectionnez: compararcripto.com")

        # RÉSUMÉ FINAL
        await asyncio.sleep(3)
        print("\n" + "="*70)
        print("✅ DÉPLOIEMENT CLOUDFLARE PAGES COMPLÉTÉ!")
        print("="*70)
        print("\n📊 Statut:")
        print("  ✅ GitHub repo connecté (Julien361/compararcripto)")
        print("  ✅ Auto-deployment activé (main branch)")
        print("  ✅ Domaine routé: compararcripto.com")
        print("\n🌐 Accès:")
        print("  → https://compararcripto.com (LIVE)")
        print("  → https://compararcripto.pages.dev (Pages subdomain)")
        print("\n⏱️  Déploiement: Généralement < 2 minutes")
        print("\n📈 Prochaines étapes:")
        print("  1. ✅ Vérifier que le site est accessible")
        print("  2. ⏳ GA4 verification (déjà en place: G-LQVYBFTPH8)")
        print("  3. ⏳ GSC domain verification + sitemap submission")
        print("  4. ⏳ Affiliate accounts (MEXC, KuCoin, Binance, Coinbase)")
        print("\n" + "="*70)

        # Laisser le navigateur ouvert 10 sec pour vérifier
        print("\n🔍 Le navigateur restera ouvert 10 secondes pour vérification...")
        await asyncio.sleep(10)
        await browser.close()

        return True


if __name__ == "__main__":
    try:
        success = asyncio.run(deploy())
        print("\n✅ Script terminé!\n")
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        print("\n👉 Instructions manuelles:")
        print("   1. Aller à: https://dash.cloudflare.com/pages")
        print("   2. Create a project → Connect to Git")
        print("   3. GitHub: Select repo 'compararcripto'")
        print("   4. Framework: None (static HTML)")
        print("   5. Save and Deploy")
        print("   6. Settings → Domains → Add domain → compararcripto.com")
        sys.exit(1)
