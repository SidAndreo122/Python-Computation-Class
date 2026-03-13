#!/usr/bin/env bash
# ─────────────────────────────────────────────────────
# Start the Anime DLC Store Flask web server
# Run from the web_st_ai_chat/src/web/ directory
# ─────────────────────────────────────────────────────

# Install dependencies if needed
# pip install -r requirements.txt

echo ""
echo "  Starting Anime DLC Store on http://localhost:5000"
if [ -n "$CHAT_IFRAME_URL" ]; then
    echo "  Using chat iframe URL from CHAT_IFRAME_URL: $CHAT_IFRAME_URL"
else
    echo "  CHAT_IFRAME_URL is not set. Flask will auto-detect Codespaces or use localhost:8501."
fi
echo ""

# Option A: Flask built-in dev server (simplest for learning)
python app.py

# Option B: Uvicorn via ASGI wrapper (uncomment to use)
# pip install uvicorn asgiref
# uvicorn app:app --host 0.0.0.0 --port 5000 --reload
# Note: Flask is WSGI; for uvicorn wrap with: asgiref.wsgi.WsgiToAsgi(app)
