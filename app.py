import streamlit as st
from datetime import datetime
import random

# --- 1. CONFIGURATION DE LA PAGE ---
st.set_page_config(
    page_title="Naouss ❤️", 
    page_icon="🌿", 
    layout="centered"
)

# --- 2. VARIABLES PERSONNALISÉES ---
PRENOM = "Nanou"
TEAM_NAME = "Naouss"
# Date de mise en couple : 22 Mars 2019 à 20h00
DATE_DEBUT = datetime(2019, 3, 22, 20, 0) 

# --- 3. DESIGN MODERN (CSS - STYLE 2026) ---
# Thème : Vert Olive, Glassmorphism (Effet verre dépoli), Minimaliste
st.markdown("""
<style>
    /* Import de la police moderne 'Poppins' */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap');

    /* Fond d'écran : Dégradé Vert Olive Profond */
    .stApp {
        background: linear-gradient(135deg, #2E3B28 0%, #556B2F 100%);
        font-family: 'Poppins', sans-serif;
        color: white;
    }

    /* Supprimer les marges inutiles en haut */
    .block-container {
        padding-top: 3rem;
        padding-bottom: 5rem;
    }

    /* Carte effet verre (Le conteneur du compteur) */
    .glass-card {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 30px;
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.15);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
        text-align: center;
        margin-top: 20px;
        margin-bottom: 30px;
    }

    /* Style du bouton interactif */
    div.stButton > button {
        background: rgba(255, 255, 255, 0.9);
        color: #2E3B28;
        border: none;
        border-radius: 12px;
        padding: 15px 25px;
        font-size: 16px;
        font-weight: 600;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    div.stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
        background: #ffffff;
        color: #556B2F;
    }
    
    /* Typographie */
    h1 { font-weight: 700; letter-spacing: -1px; text-shadow: 0 2px 10px rgba(0,0,0,0.2); }
    h3 { font-weight: 500; }
    p { font-weight: 300; opacity: 0.9; }
    
    /* Cacher le menu hamburger Streamlit et le footer "Made with Streamlit" */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
</style>
""", unsafe_allow_html=True)

# --- 4. CALCUL DU TEMPS ---
def get_detailed_time_diff():
    now = datetime.now()
    diff = now - DATE_DEBUT
    
    # Calcul précis
    years = diff.days // 365
    remaining_days = diff.days % 365
    
    return years, remaining_days

ans, jours_restants = get_detailed_time_diff()

# --- 5. INTERFACE UTILISATEUR ---

# A. La Photo (Centrée)
col_left, col_center, col_right = st.columns([1, 2, 1])
with col_center:
    # On affiche la photo si elle existe, sinon un message d'erreur discret
    try:
        # Border radius via CSS appliqué à l'image n'est pas natif simple en Streamlit, 
        # donc on affiche l'image brute, elle sera carrée/rectangle selon ton fichier.
        st.image("nous.jpg", use_column_width=True) 
    except:
        st.warning("⚠️ Ajoute une photo nommée 'nous.jpg' dans le dossier.")

# B. Titres
st.markdown(f"<h1 style='text-align: center; margin-top: 10px;'>Coucou {PRENOM} ❤️</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; font-size: 1.1em; margin-bottom: 20px;'>Bienvenue chez <b>{TEAM_NAME}</b></p>", unsafe_allow_html=True)

# C. Le Compteur Principal (Carte Glass)
st.markdown(f"""
<div class="glass-card">
    <p style="margin:0; font-size: 0.85em; text-transform: uppercase; letter-spacing: 2px; opacity: 0.8;">Depuis le 22 Mars 2019</p>
    <div style="font-size: 3.5em; font-weight: 700; line-height: 1.2; margin: 15px 0;">
        {ans} Ans<br>
        <span style="font-size: 0.5em; vertical-align: middle;">et {jours_restants} jours</span>
    </div>
    <p style="font-size: 0.9em; margin-top: 10px;">C'est pas mal, non ? 😉</p>
</div>
""", unsafe_allow_html=True)

# D. Zone Interactive (Bouton Love)
col_spacer, col_btn, col_spacer2 = st.columns([0.2, 3, 0.2])

with col_btn:
    if st.button("✨ Pourquoi je t'aime ? (Clique)"):
        reasons = [
            "Parce que tu es ma Nanou préférée.",
            "Pour ta patience légendaire avec moi.",
            "Parce que le vert olive, c'est la vie (et toi aussi).",
            "Parce qu'on est Naouss, et c'est pour toujours.",
            "Pour ton sourire quand tu me regardes.",
            "Parce que tu rends chaque jour meilleur."
        ]
        message_du_jour = random.choice(reasons)
        
        # Affichage du message style "Notification iOS"
        st.markdown(f"""
        <div style="
            background: rgba(255,255,255,0.95); 
            color: #2E3B28; 
            padding: 20px; 
            border-radius: 15px; 
            text-align: center; 
            margin-top: 20px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            font-weight: 600;
            animation: fadeIn 0.5s;
        ">
            {message_du_jour}
        </div>
        """, unsafe_allow_html=True)
        
        st.balloons()