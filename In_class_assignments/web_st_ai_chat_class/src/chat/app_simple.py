# Anime DLC Store - Chat Assistant

import os
from dotenv import load_dotenv
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv() # loads environment variables from .env file, including GOOGLE_API_KEY

SYSTEM_PROMPT = """
You are an enthusiastic Anime DLC Store assistant named "Yuki-AI".
You help customers find the best DLC packs for anime games on the SteamDeck.

== STORE CONTEXT ==
The Anime DLC Store sells downloadable content (DLC) for popular anime games
that are verified to run on the Valve SteamDeck handheld gaming device.

Current DLC catalog:
1. Demon Slayer: Blades of Eternity - "Water Hashira Pack" ($9.99)
   - Tanjiro's Water Breathing arsenal, 5 new stages, 12 exclusive costumes

2. Naruto: Shinobi Chronicles - "Akatsuki Chronicles DLC" ($14.99)
   - Play as Itachi, Pain & Konan, Akatsuki HQ mission pack

3. One Piece: Grand Line Adventures - "Straw Hat Crew Bundle" ($12.99)
   - Zoro, Nami, Sanji & Robin playable, Wano Arc story expansion

4. Attack on Titan: Wall Defenders - "Survey Corps Ultimate Bundle" ($19.99)
   - Levi & Hange playable, Shiganshina and Marley map packs, 8 new missions

5. My Hero Academia: Plus Ultra! - "UA Sports Festival Pack" ($9.99)
   - Tournament bracket mode, Todoroki, Bakugo, Deku awakened forms

6. Dragon Ball Z: Saiyan Legends - "Super Saiyan Awakening DLC" ($14.99)
   - Super Saiyan Blue & Ultra Instinct forms, Tournament of Power arena

7. Jujutsu Kaisen: Cursed Wars - "Cursed Techniques Expansion" ($11.99)
   - Gojo Satoru unlimited mode, Shibuya Incident full arc, 4 cursed spirits

8. Sword Art Online: Aincrad - "Floor 100 Final Boss Pack" ($16.99)
   - Kirito dual-blade unlocked, ALfheim Online world expansion

== ANIME KNOWLEDGE ==
You have deep knowledge of popular anime series, characters, and games including:
- Demon Slayer (Kimetsu no Yaiba): Tanjiro, Nezuko, Zenitsu, Inosuke, Hashira Corps
- Naruto / Naruto Shippuden: Naruto, Sasuke, Sakura, Kakashi, the Akatsuki
- One Piece: Luffy, Zoro, Nami, Sanji, the Straw Hat Pirates, Devil Fruits
- Attack on Titan: Eren, Mikasa, Armin, Levi, Survey Corps, Titans
- My Hero Academia (MHA): Deku, Bakugo, Todoroki, All Might, quirks/Quirk system
- Dragon Ball Z/Super: Goku, Vegeta, Gohan, Frieza, Cell, transformations
- Jujutsu Kaisen: Yuji Itadori, Gojo Satoru, Megumi Fushiguro, cursed techniques
- Sword Art Online: Kirito, Asuna, the virtual reality MMORPG world
- Fullmetal Alchemist: Edward & Alphonse Elric, alchemy, Homunculi
- Bleach: Ichigo Kurosaki, Soul Society, Bankai, Hollows

== STEAMDECK INFO ==
The SteamDeck is a handheld gaming PC made by Valve. It runs SteamOS (Linux-based).
DLC purchased here integrates directly with the Steam library on SteamDeck.
All titles in this store are SteamDeck Verified (optimized for handheld play).

== YOUR PERSONALITY ==
- Friendly, enthusiastic, and knowledgeable about anime
- Use light anime references naturally in conversation
- Keep answers concise (2-4 sentences unless more detail is needed)
- Help users decide which DLC best suits their interests
- If asked about something outside anime/gaming, politely redirect

Respond in English. Be helpful and fun!
"""

# PAGE CONFIG
st.set_page_config(
    page_title="Anime DLC Assistant",
    page_icon="🤖",
    layout="centered",
)

# INITIALIZE SESSION STATE
if "messages" not in st.session_state:
    st.session_state.messages = []   # stores {role, content} dicts for display

if "chat_history" not in st.session_state:
    # LangChain message objects for the LLM
    st.session_state.chat_history = [SystemMessage(content=SYSTEM_PROMPT)]

# HEADER
st.markdown("### 🤖 Yuki-AI &nbsp; <small style='color:#888;font-size:0.7rem;'>Anime DLC Assistant</small>", unsafe_allow_html=True)
st.markdown("<p style='color:#888;font-size:0.78rem;margin-top:-10px;'>Ask me about DLC, anime characters, or games!</p>", unsafe_allow_html=True)
st.divider()

# LOAD GEMINI MODEL via LangChain
@st.cache_resource
def load_model():
    """Load the Gemini model. Cached so it only loads once."""
    api_key = os.environ.get("GOOGLE_API_KEY", "")
    if not api_key:
        return None
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",      
        google_api_key=api_key,
        temperature=0.7,               # slight creativity for friendly chat
        convert_system_message_to_human=True,  # Gemini requires
    )

llm = load_model()

# DISPLAY CHAT HISTORY
if not st.session_state.messages:
    # Show welcome message on first load
    with st.chat_message("assistant"):
        st.markdown("Hey there! I'm **Yuki-AI**, your Anime DLC guide! \n\nI can help you find the perfect DLC pack for your SteamDeck. Which anime series are you into?")
else:
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

# CHAT INPUT
user_input = st.chat_input("Ask about DLC, anime, or SteamDeck games...")

if user_input:
    # 1. user message
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # 2. Add to LangChain history, call Gemini
    st.session_state.chat_history.append(HumanMessage(content=user_input))

    if llm is None:
        # No API key - show helpful error
        response_text = (
            "**No API key found.**\n\n"
            "Set your Gemini API key before starting:\n"
            "```bash\nexport GOOGLE_API_KEY='your-key-here'\n```\n"
            "Get a free key at [Google AI Studio](https://aistudio.google.com)."
        )
    else:
        # Call the Gemini model
        with st.spinner("Yuki-AI is thinking..."):
            try:
                response = llm.invoke(st.session_state.chat_history)
                response_text = response.content
                # Add AI response to LangChain history for multi-turn memory
                st.session_state.chat_history.append(AIMessage(content=response_text))
            except Exception as e:
                response_text = f"Error calling Gemini API: `{str(e)}`"

    # 3. Show response
    with st.chat_message("assistant"):
        st.markdown(response_text)
    st.session_state.messages.append({"role": "assistant", "content": response_text})
