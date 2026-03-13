# Anime DLC Store - Flask Web Application
# Prototype for CS students learning web development with AI integration

import os
from flask import Flask, render_template

app = Flask(__name__)

# Fictitious DLC products for popular anime games on SteamDeck
PRODUCTS = [
    {
        "id": 1,
        "game": "Demon Slayer: Blades of Eternity",
        "dlc": "Water Hashira Pack",
        "description": "Unlock Tanjiro's full Water Breathing arsenal. 5 new stages, 12 exclusive costumes.",
        "price": 9.99,
        "color": "#1a6bb5",
        "accent": "#5ec8f0",
        "badge": "HOT",
    },
    {
        "id": 2,
        "game": "Naruto: Shinobi Chronicles",
        "dlc": "Akatsuki Chronicles DLC",
        "description": "Play as Itachi, Pain & Konan. Includes Akatsuki HQ mission pack.",
        "price": 14.99,
        "color": "#8b1a1a",
        "accent": "#e05555",
        "badge": "NEW",
    },
    {
        "id": 3,
        "game": "One Piece: Grand Line Adventures",
        "dlc": "Straw Hat Crew Bundle",
        "description": "Zoro, Nami, Sanji & Robin playable. Wano Arc story expansion included.",
        "price": 12.99,
        "color": "#b56a00",
        "accent": "#f5c842",
        "badge": "SALE",
    },
    {
        "id": 4,
        "game": "Attack on Titan: Wall Defenders",
        "dlc": "Survey Corps Ultimate Bundle",
        "description": "Levi & Hange playable. Shiganshina and Marley map packs. 8 new missions.",
        "price": 19.99,
        "color": "#2a5c2a",
        "accent": "#5ab85a",
        "badge": "TOP",
    },
    {
        "id": 5,
        "game": "My Hero Academia: Plus Ultra!",
        "dlc": "UA Sports Festival Pack",
        "description": "Tournament bracket mode. 6 new heroes: Todoroki, Bakugo, Deku awakened.",
        "price": 9.99,
        "color": "#4a1a8b",
        "accent": "#a855f7",
        "badge": "NEW",
    },
    {
        "id": 6,
        "game": "Dragon Ball Z: Saiyan Legends",
        "dlc": "Super Saiyan Awakening DLC",
        "description": "Super Saiyan Blue & Ultra Instinct forms. Tournament of Power arena.",
        "price": 14.99,
        "color": "#8b6a00",
        "accent": "#fbbf24",
        "badge": "HOT",
    },
    {
        "id": 7,
        "game": "Jujutsu Kaisen: Cursed Wars",
        "dlc": "Cursed Techniques Expansion",
        "description": "Gojo Satoru unlimited mode. Shibuya Incident full arc. 4 cursed spirits.",
        "price": 11.99,
        "color": "#1a1a4a",
        "accent": "#6366f1",
        "badge": "NEW",
    },
    {
        "id": 8,
        "game": "Sword Art Online: Aincrad",
        "dlc": "Floor 100 Final Boss Pack",
        "description": "Kirito dual-blade unlocked. ALfheim Online world expansion. Asuna support mode.",
        "price": 16.99,
        "color": "#1a4a4a",
        "accent": "#22d3ee",
        "badge": "SALE",
    },
]


@app.route("/")
def index():
    chat_iframe_url = os.getenv("CHAT_IFRAME_URL", "").strip()

    # Auto-build a public Streamlit URL when running in GitHub Codespaces.
    if not chat_iframe_url:
        codespace_name = os.getenv("CODESPACE_NAME", "").strip()
        forwarding_domain = os.getenv(
            "GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN", ""
        ).strip()
        if codespace_name and forwarding_domain:
            chat_iframe_url = (
                f"https://{codespace_name}-8501.{forwarding_domain}"
            )
        else:
            chat_iframe_url = "http://localhost:8501"

    return render_template(
        "index.html", products=PRODUCTS, chat_iframe_url=chat_iframe_url
    )


if __name__ == "__main__":
    # Run with Flask dev server (prototype mode)
    # For uvicorn: pip install uvicorn asgiref, then use asgiref.wsgi.WsgiToAsgi wrapper
    app.run(debug=True, host="0.0.0.0", port=5000)
