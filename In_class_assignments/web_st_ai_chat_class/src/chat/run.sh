#!/usr/bin/env bash

# Start the Anime DLC Chat Assistant (Streamlit)


# Set Gemini API key before running
# Get a free key at https://aistudio.google.com
if [ -z "$GOOGLE_API_KEY" ]; then
    echo ""
    echo "  WARNING: GOOGLE_API_KEY is not set."
    echo "  Export it before running:"
    echo "    export GOOGLE_API_KEY='your-key-here'"
    echo ""
fi

# Install dependencies before starting the app
# uv install -r requirements.txt or uv sync

echo ""
if [ -n "$CODESPACE_NAME" ] && [ -n "$GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN" ]; then
    echo "  Starting Anime DLC Chat Assistant on:"
    echo "    https://${CODESPACE_NAME}-8501.${GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN}"
    echo "  (Container-local address: http://localhost:8501)"
else
    echo "  Starting Anime DLC Chat Assistant on http://localhost:8501"
fi
echo "  The Flask store should embed this in its iframe."
echo ""

# Start Streamlit (disable CORS so iframe embedding works)
streamlit run app_simple.py \
    --server.port 8501 \
    --server.address 0.0.0.0 \
    --server.enableCORS false \
    --server.enableXsrfProtection false
