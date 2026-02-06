import streamlit as st
from datetime import datetime
import random

# --- 1. CONFIGURATION ---
st.set_page_config(
    page_title="Notre Amour ❤️", 
    page_icon="💖", 
    layout="centered"
)

# --- 2. VARIABLES ---
# Date : 22 Mars 2019 à 20h00
DATE_DEBUT = datetime(2019, 3, 22, 20, 0) 

# --- 3. DESIGN ROMANTIQUE (CSS) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap');

    /* Fond Rose Pastel Dégradé */
    .stApp {
        background: linear-gradient(180deg, #ff9a9e 0%, #fad0c4 99%, #fad0c4 100%);
        font-family: 'Poppins', sans-serif;
        color: #5e2a2a; /* Texte rouge sombre/marron pour le contraste */
    }

    /* Animation de cœurs en arrière-plan (Effet visuel) */
    .heart-bg {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background-image: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.2'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
        z-index: 0;
        pointer-events: none;
    }

    /* Carte effet verre teinté rose */
    .glass-card {
        background: rgba(255, 255, 255, 0.25);
        border-radius: 20px;
        padding: 30px;
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.4);
        box-shadow: 0 8px 32px 0 rgba(255, 105, 135, 0.2);
        text-align: center;
        margin-top: 20px;
        margin-bottom: 30px;
    }

    /* Bouton centré et stylé */
    div.stButton > button {
        background: #ff758c;
        color: white;
        border: none;
        border-radius: 25px;
        padding: 15px 30px;
        font-size: 16px;
        font-weight: 600;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(255, 117, 140, 0.4);
    }
    
    div.stButton > button:hover {
        transform: scale(1.05);
        background: #ff5e78;
        box-shadow: 0 6px 20px rgba(255, 117, 140, 0.6);
        color: white;
    }
    
    h1 { font-weight: 700; color: #880e4f; text-shadow: 0 2px 4px rgba(255,255,255,0.3); }
    p { font-weight: 400; font-size: 1.1em; }
    
    /* Cacher les menus */
    #MainMenu, footer, header {visibility: hidden;}
    
</style>
<div class="heart-bg"></div>
""", unsafe_allow_html=True)

# --- 4. CALCUL DU TEMPS ---
def get_detailed_time_diff():
    now = datetime.now()
    diff = now - DATE_DEBUT
    years = diff.days // 365
    remaining_days = diff.days % 365
    return years, remaining_days

ans, jours_restants = get_detailed_time_diff()

# --- 5. INTERFACE ---

# A. Photo (Toujours vérifier qu'elle est droite sur ton ordi avant upload !)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        st.image("nous.jpg", use_column_width=True) 
    except:
        st.warning("Ajoute la photo 'nous.jpg'")

# B. Textes
st.markdown(f"<h1 style='text-align: center; margin-top: 10px;'>Bonjour ma chérie ❤️</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; margin-bottom: 20px; color: #5e2a2a;'>Bienvenue sur notre site d'amour</p>", unsafe_allow_html=True)

# C. Compteur
st.markdown(f"""
<div class="glass-card">
    <p style="margin:0; font-size: 0.85em; text-transform: uppercase; letter-spacing: 2px; color: #880e4f;">Depuis le 22 Mars 2019</p>
    <div style="font-size: 3.5em; font-weight: 700; line-height: 1.2; margin: 15px 0; color: #d81b60;">
        {ans} ans<br>
        <span style="font-size: 0.5em; vertical-align: middle; color: #5e2a2a;">et {jours_restants} jours</span>
    </div>
    <p style="font-size: 1em; margin-top: 10px; font-style: italic;">d'amour... 🌹</p>
</div>
""", unsafe_allow_html=True)

# D. Bouton (Centré via colonnes équilibrées)
# Avant c'était [0.2, 3, 0.2] -> Trop large. Maintenant [1, 2, 1] -> Plus centré.
col_left, col_btn, col_right = st.columns([1, 2, 1])

with col_btn:
    if st.button("💌 Pourquoi je t'aime ?"):
        reasons = [
            "Pour ton sourire qui me fait fondre.",
            "Parce que tu es ma meilleure amie.",
            "Pour tous nos souvenirs depuis 2019.",
            "Parce que je ne peux pas imaginer ma vie sans toi.",
            "Tout simplement parce que je t'aime."
        ]
        msg = random.choice(reasons)
        
        st.markdown(f"""
        <div style="
            background: white; 
            color: #d81b60; 
            padding: 15px; 
            border-radius: 15px; 
            text-align: center; 
            margin-top: 20px;
            font-weight: bold;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            animation: fadeIn 0.5s;
        ">
            {msg}
        </div>
        """, unsafe_allow_html=True)
        
        st.balloons()