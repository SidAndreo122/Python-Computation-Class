# Anime DLC Store — Web + AI Chat Prototype


## Project Structure

```
web_st_ai_chat/
└── src/
    ├── web/                  # Flask storefront
    │   ├── app.py            # Flask application + product data
    │   ├── run.sh            # Start script
    │   ├── requirements.txt
    │   ├── templates/
    │   │   └── index.html    # Store page with iframe chat panel
    │   └── static/
    │       └── css/
    │           └── style.css
    │
    └── chat/                 # Streamlit chat assistant
        ├── app.py            # LangChain + Gemini chat interface
        ├── run.sh            # Start script
        └── requirements.txt
```

