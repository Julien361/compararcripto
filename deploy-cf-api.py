#!/usr/bin/env python3
"""
Cloudflare Pages Deployment via API
Automated: GitHub connection + domain routing
"""

import requests
import json
import sys
from pathlib import Path

class CloudflareDeployer:
    def __init__(self, api_token: str, account_id: str, github_token: str = None):
        self.api_token = api_token
        self.account_id = account_id
        self.github_token = github_token
        self.base_url = "https://api.cloudflare.com/client/v4"
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json"
        }

    def create_pages_project(self) -> dict:
        """Créer un Pages project et connecter GitHub"""
        print("\n[1/3] Création du Pages project...")

        payload = {
            "name": "compararcripto",
            "production_branch": "main",
            "source": {
                "type": "github",
                "config": {
                    "owner": "Julien361",
                    "repo_name": "compararcripto",
                    "production_branch": "main"
                }
            },
            "build_config": {
                "build_command": "",  # No build needed for static HTML
                "destination_dir": "",
                "root_dir": ""
            }
        }

        response = requests.post(
            f"{self.base_url}/accounts/{self.account_id}/pages/projects",
            headers=self.headers,
            json=payload
        )

        if response.status_code in [200, 201]:
            data = response.json()["result"]
            print(f"✅ Project créé: {data['name']}")
            print(f"   URL: https://{data['subdomain']}.pages.dev")
            return data
        else:
            print(f"❌ Erreur: {response.status_code}")
            print(response.json())
            return None

    def get_zones(self) -> dict:
        """Récupérer les zones DNS (domaines)"""
        print("\n[2/3] Récupération des zones...")

        response = requests.get(
            f"{self.base_url}/zones",
            headers=self.headers
        )

        if response.status_code == 200:
            zones = response.json()["result"]
            for zone in zones:
                if zone["name"] == "compararcripto.com":
                    print(f"✅ Zone trouvée: {zone['name']} (ID: {zone['id']})")
                    return zone
            print("❌ Zone compararcripto.com non trouvée")
            return None
        else:
            print(f"❌ Erreur: {response.status_code}")
            return None

    def add_domain_to_pages(self, project_name: str, domain: str, zone_id: str) -> bool:
        """Ajouter le domaine au Pages project"""
        print(f"\n[3/3] Routage du domaine {domain}...")

        payload = {
            "domain": domain
        }

        response = requests.post(
            f"{self.base_url}/accounts/{self.account_id}/pages/projects/{project_name}/domains",
            headers=self.headers,
            json=payload
        )

        if response.status_code in [200, 201]:
            print(f"✅ Domaine {domain} routé vers Pages!")
            return True
        else:
            print(f"❌ Erreur: {response.status_code}")
            print(response.json())
            return False

    def deploy(self) -> bool:
        """Orchestrer tout le déploiement"""
        print("="*60)
        print("🚀 CLOUDFLARE PAGES DEPLOYMENT VIA API")
        print("="*60)

        # Étape 1: Créer le project et connecter GitHub
        project = self.create_pages_project()
        if not project:
            return False

        # Étape 2: Récupérer la zone
        zone = self.get_zones()
        if not zone:
            return False

        # Étape 3: Ajouter le domaine
        success = self.add_domain_to_pages(project["name"], "compararcripto.com", zone["id"])

        if success:
            print("\n" + "="*60)
            print("✅ DÉPLOIEMENT RÉUSSI!")
            print("="*60)
            print(f"\n📊 Résumé:")
            print(f"  ✅ Project: {project['name']}")
            print(f"  ✅ Domaine: compararcripto.com")
            print(f"  ✅ Repo: GitHub (Julien361/compararcripto)")
            print(f"  ✅ Branch: main")
            print(f"\n🌐 Accessible à: https://compararcripto.com")
            print(f"📱 Pages Dev: https://{project['subdomain']}.pages.dev")
            print(f"\n⏱️  Déploiement: Automatique à chaque push (main)")
            print(f"\n📈 Prochaine étape:")
            print(f"  1. GA4 verification")
            print(f"  2. GSC domain verification")
            print(f"  3. Affiliate accounts setup")

        return success


def get_credentials():
    """Demander les credentials à l'utilisateur"""
    print("\n" + "="*60)
    print("🔐 CREDENTIALS CLOUDFLARE NÉCESSAIRES")
    print("="*60)
    print("\nPour obtenir vos credentials:")
    print("1. Aller à: https://dash.cloudflare.com/profile/api-tokens")
    print("2. Créer un token avec permissions:")
    print("   - Zone.DNS (read)")
    print("   - Account.Cloudflare Pages (write)")
    print("   - Zone.Zone (read)")
    print("3. Copier le token")
    print("\n4. Aller à: https://dash.cloudflare.com/?account=ACCOUNT_ID")
    print("   (L'account ID est dans l'URL)")

    api_token = input("\n👉 Coller votre Cloudflare API Token: ").strip()
    account_id = input("👉 Coller votre Account ID: ").strip()

    if not api_token or not account_id:
        print("❌ Credentials manquants!")
        sys.exit(1)

    return api_token, account_id


if __name__ == "__main__":
    # Récupérer les credentials
    api_token, account_id = get_credentials()

    # Déployer
    deployer = CloudflareDeployer(api_token, account_id)
    success = deployer.deploy()

    sys.exit(0 if success else 1)
