import streamlit as st
import pandas as pd
import numpy as np
from streamlit_authenticator import Authenticate
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import nltk
from nltk.corpus import stopwords


# Configuration de la page
st.set_page_config(
    page_title="Cinéma EDEN",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Style CSS pour améliorer le design
st.markdown(
    """
    <style>
    /* Fond général de l'application */
    .stApp {
        background-color: #1E1E1E !important;
        color: white !important;
    }

    /* Style de la sidebar */
    [data-testid="stSidebar"] {
        background-color: #2C2F33 !important;
        color: black !important;
    }
    
    /* Modifier la couleur des labels */
        [data-testid="stSidebar"] label {
        color: white !important; /* Texte des labels en blanc */
    }

    /* Style des titres */
    .title {
    text-align: center;
    font-size: 36px;
    font-weight: bold;
    margin-bottom: 20px;
    color: #FFD700;
    font-family: "Georgia", serif; /* Police élégante et disponible par défaut */
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); /* Ombre pour du relief */
    letter-spacing: 2px; /* Espacement des lettres pour un effet premium */
    text-transform: uppercase; /* Mise en majuscules pour plus d'impact */
    -webkit-text-stroke: 1px black; /* Contour fin pour améliorer la lisibilité */
}

    /* Style des cartes */
    .film-card {
        background-color: #2C2F33 ;
        border-radius: 10px;
        padding: 15px;
        margin: 10px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
        text-align: center;
    }

    /* Style des affiches */
    .film-card img {
        border-radius: 10px;
        margin-bottom: 10px;
    }

    /* Style du texte des cartes */
    .film-card h3 {
        text-align: center;
        color: #FFD700;
        font-family: "Georgia", serif; /* Police élégante et disponible par défaut */
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); /* Ombre pour du relief */
        letter-spacing: 2px; /* Espacement des lettres pour un effet premium */       
        -webkit-text-stroke: 1px black; /* Contour fin pour améliorer la lisibilité */

    }

    .film-card p {
        text-align: center;
        font-size: 17px;
        color: #CCCCCC;
        font-family: "Georgia", serif; /* Police élégante et disponible par défaut */
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); /* Ombre pour du relief */
    }

    </style>
    """,
    unsafe_allow_html=True
)

# Logo dans la sidebar
logo_url = "https://i.postimg.cc/kXQh8mwP/7-Lcp-Gic-Ou-DIIL9-C8-generated-image.png"
st.sidebar.image(logo_url, use_container_width=True)



df = pd.read_csv('https://drive.google.com/uc?id=16jDWelG0YHTFIrFbGucCJtjUCh_L_gSz')
dfml=pd.read_csv('https://drive.google.com/uc?id=1WJIfk0EwlhTn4Qk66qFzA7HTmV3j8iBO')
dfml=dfml.fillna('')
nltk.download('stopwords')
french_stopwords=stopwords.words('french')
tfidf=TfidfVectorizer(stop_words=french_stopwords)
tfidf_matrix=tfidf.fit_transform(dfml['features'])
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)


menu_options = ["Accueil","Catalogue Films","Assistant de recommandations","Nos Partenaires"]
selection = st.sidebar.selectbox("Choisissez une section", menu_options)

    # 🌟 **Accueil**
    
if selection == "Accueil":
        st.markdown('<div class="title"> Bienvenue au Cinéma Eden </div>', unsafe_allow_html=True)
        eden_url = "https://www.ville-lasouterraine.fr/app/uploads/2022/04/eden.jpg"
        eden_url2='https://api.cloudly.space/resize/clip/1900/1080/75/aHR0cHM6Ly9jZHQ2NC5tZWRpYS50b3VyaW5zb2Z0LmV1L3VwbG9hZC8xNzYwMDAxNjgtNC5qcGc=/image.jpg'
        st.markdown(
                f"""
                <div class="film-card">
                    <img src="{eden_url2}" width="850">
                    <p>Le Cinéma Eden est situé à La Souterraine, dans le département de la Creuse.</p>
                    <p>Ce cinéma historique est un lieu incontournable pour les passionnés de films et de culture.</p>
                    <p>Il propose une programmation variée allant des films récents aux classiques, et est un lieu de rencontre pour tous les amoureux du 7ème art.</p> 
                    <p>Venez découvrir une expérience cinématographique dans un cadre chaleureux et convivial ! </p> 
                    
                </div>
                """,
                unsafe_allow_html=True
            )
        
        st.markdown(
                f"""                
                <div class="film-card">                    
                    <img src="{eden_url}" width="850">
                    <p>Il propose une programmation variée allant des films récents aux classiques, et est un lieu de rencontre pour tous les amoureux du 7ème art.</p> 
                    <p>Venez découvrir une expérience cinématographique dans un cadre chaleureux et convivial ! </p> 
                    <a href="{imdb_lien}" target="_blank">
                    <p>RESERVEZ VOS PLACES ICI !!</p> </a>
                    
                </div>
                """,
                unsafe_allow_html=True
            )
    # 🎞 **Catalogue Films**
    
# 🎞 **Catalogue Films**

elif selection == "Catalogue Films":
    st.markdown('<div class="title"> Catalogue des films </div>', unsafe_allow_html=True)

    film_choice= st.sidebar.selectbox("🎬 Choisissez un film", [""] + list(df['titre_fr'].unique()), index=0)
    
    # Si un film est sélectionné dans le catalogue, affiche sa fiche détaillée
    selected_film = df[df['titre_fr'] == film_choice]
    if selected_film.empty:
        st.markdown(
            f"""
            <div class="film-card">                                
                <h3>Veuillez sélectionner un film  dans la barre latérale</h3>
                <img src="{logo_url}" width="1000">                  
            </div>
            """,
            unsafe_allow_html=True
        )
        
    if not selected_film.empty:
        poster_path = selected_film['poster'].values[0]
        poster_url = 'https://image.tmdb.org/t/p/original' + poster_path
        imdb_id=selected_film['tconst'].values[0]
        imdb_lien = f"https://www.imdb.com/title/{imdb_id}/"

        # Carte film avec affiche
        st.markdown(
            f"""
            <div class="film-card">
                <h3>{film_choice}</h3>
                <a href="{imdb_lien}" target="_blank">
                <img src="{poster_url}" width="350"></a>                
                <p><b>Genres :</b> {selected_film["genres"].values[0]}</p>
                <p><b>Popularité :</b> {round(selected_film["popularite"].values[0], 2)}</p>
                <p><b>Date de sortie :</b> {selected_film["date_de_sortie"].values[0]}</p>
                <p>{selected_film["synopsis"].values[0]}</p>
                <p><b>Durée (minutes) :</b> {selected_film["duree"].values[0]}</p>
                <p><b>Réalisateur(s) :</b> {selected_film["realisateurs"].values[0]}</p>
                <p><b>Acteurs principaux :</b> {selected_film["acteurs_actrices"].values[0]}</p>
                <p><b>Pays de production :</b> {selected_film["pays_production"].values[0]}</p>    
            </div>
            """,
            unsafe_allow_html=True
        )

# 🤖 **Assistant de recommandation**

elif selection == "Assistant de recommandations":
    st.markdown('<div class="title"> Assistant de recommandations </div>', unsafe_allow_html=True)
    

    def recommend_movies(title1, title2, actor, df, cosine_sim, weight_sim=0.85, weight_pop=0.15):
        dfml['titre_fr_lower'] = dfml['titre_fr'].str.lower()

        # Vérification des films existants
        idx1 = dfml[dfml['titre_fr_lower'] == title1.lower()].index[0] if title1 else None
        idx2 = dfml[dfml['titre_fr_lower'] == title2.lower()].index[0] if title2 else None

        # Calcul des similarités cosinus
        sim_scores_1 = np.array(cosine_sim[idx1]) if idx1 is not None else np.zeros(len(dfml))
        sim_scores_2 = np.array(cosine_sim[idx2]) if idx2 is not None else np.zeros(len(dfml))

        # Pondération des similarités
        weight1 = 55 if title1 and title2 else 100
        weight2 = 45 if title1 and title2 else 0
        combined_similarity = (sim_scores_1 * weight1 + sim_scores_2 * weight2) / 100

        # Normalisation de la popularité
        dfml['pop_normalized'] = (dfml['popularite'] - dfml['popularite'].min()) / (dfml['popularite'].max() - dfml['popularite'].min())

        # Score final (similarité + popularité)
        final_scores = (weight_sim * combined_similarity) + (weight_pop * dfml['pop_normalized'].values)

        def get_top_movies(sim_scores, count, exclude=[]):
            movies = sorted(list(enumerate(sim_scores)), key=lambda x: x[1], reverse=True)
            movies = [i for i in movies if i[0] not in exclude][:count]
            return [(dfml['titre_fr'].iloc[i[0]], round(i[1] * 100, 2)) for i in movies]

        # Sélection des recommandations
        recommendations = {}

        if title1:
            top_5_from_1 = get_top_movies(sim_scores_1, 5, exclude=[idx1] if idx1 is not None else [])
            recommendations[f"Top 5 basés sur {title1}"] = top_5_from_1

        if title2:
            top_5_from_2 = get_top_movies(sim_scores_2, 5, exclude=[idx2] if idx2 is not None else [])
            recommendations[f"Top 5 basés sur {title2}"] = top_5_from_2

        if title1 and title2:
            already_recommended = [idx1, idx2] + [dfml[dfml['titre_fr'] == title].index[0] for title, _ in top_5_from_1] + [dfml[dfml['titre_fr'] == title].index[0] for title, _ in top_5_from_2]
            top_5_combined = get_top_movies(combined_similarity, 5, exclude=already_recommended)
            recommendations["Top 5 basés sur la moyenne des 2 films"] = top_5_combined

        # Recherche des films avec l'acteur
        if actor:
            dfml['has_actor'] = dfml['acteur_actrice'].apply(lambda x: 1 if actor.lower() in str(x).lower() else 0)
            actor_movies = dfml[dfml['has_actor'] == 1].copy()

            if not actor_movies.empty:
                actor_movies['actor_similarity'] = actor_movies.index.map(lambda i: combined_similarity[i])
                best_actor_movies = actor_movies.sort_values(by='actor_similarity', ascending=False).iloc[:3]
                best_actor_movies_results = [(row['titre_fr'], round(row['actor_similarity'] * 100, 2)) for _, row in best_actor_movies.iterrows()]
            else:
                best_actor_movies_results = [('Aucun film trouvé avec cet acteur', 0)]

            recommendations[f"Top 3 films avec {actor}"] = best_actor_movies_results

        return recommendations

    # Sélection des films et acteurs
    selected_movie = st.sidebar.selectbox("🎬 Choisissez un film", [""] + list(dfml['titre_fr'].unique()), index=0)
    selected_movie2 = st.sidebar.selectbox("🎬 Choisissez un 2ème film (optionnel)", [""] + list(dfml['titre_fr'].unique()), index=0)
    selected_actor = st.sidebar.selectbox("🎭 Choisissez un Acteur(rice) (optionnel)", (set(",".join(dfml['acteur_actrice'].dropna().to_list()).split(","))))
    
    if not selected_movie and not selected_movie2 and not selected_actor:
        st.markdown(
            f"""
            <div class="film-card">                                
                <h3>Veuillez sélectionner un film ou un(e) acteur(ice) dans la barre latérale</h3>
                <img src="{logo_url}" width="1000">                  
            </div>
            """,
            unsafe_allow_html=True
        )
        
    # Bouton pour lancer la recherche
    if st.sidebar.button("🔍 Rechercher"):
        if not selected_movie and not selected_movie2 and not selected_actor:
            st.write("❌ Veuillez sélectionner au moins un film ou un acteur.")
        else:
            recommendations = recommend_movies(selected_movie, selected_movie2, selected_actor, df, cosine_sim)

            if recommendations:
                st.markdown(
                                f"""
                                <div class="film-card">
                                <h3>Films recommandés :</h3>                                                                                           
                                </div>
                                """,
                                unsafe_allow_html=True
                            )
                for category, movies in recommendations.items():
                    st.markdown(f"""
                                <div class="film-card">
                                <h3>{category}</h3> 
                                </div>
                                """,
                                unsafe_allow_html=True
                                )
                    for movie_title, similarity in movies:
                        movie_info = dfml[dfml['titre_fr'] == movie_title]

                        if not movie_info.empty:
                            poster = movie_info["poster"].values[0] if "poster" in movie_info else ""
                            poster_url2 = 'https://image.tmdb.org/t/p/original' + poster
                            imdb=movie_info['tconst'].values[0]
                            imdb_url = f"https://www.imdb.com/title/{imdb}/"
                            
                            st.markdown(
                                f"""
                                <div class="film-card">
                                <h3>{movie_title}</h3>  
                                <a href="{imdb_url}" target="_blank">
                                <img src="https://image.tmdb.org/t/p/original{poster_url2}" width="300"></a>                                                             
                                </div>
                                """,
                                unsafe_allow_html=True
                            )
            else:
                st.write("❌ Aucune recommandation trouvée.")

elif selection == "Nos Partenaires":
    st.markdown('<div class="title"> Nos Partenaires </div>', unsafe_allow_html=True)
    part_url = "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2e/22/87/3e/caption.jpg"
    part_url2='https://www.hautsdefrance-id.fr/wp-content/uploads/2022/04/wild-code-school-logo-1024x614-1.jpg'
    part_url3='https://www.francebleu.fr/s3/cruiser-production/2021/09/b63b6dd7-90eb-4bff-84fe-e141528a30a5/600_240952903_135288148794417_3383181307061931271_n.webp'
    
    st.markdown(
                f"""
                <div class="film-card">
                    <h3> Restaurant la Terre du Milieu à La Souterraine </h3>
                    <a href="{'https://www.tripadvisor.fr/Restaurant_Review-g616100-d26350634-Reviews-La_Terre_du_Milieu-La_Souterraine_Creuse_Nouvelle_Aquitaine.html'}" target="_blank">
                    <img src="{part_url}" width="550"></a>
                    <p>Situé tout près de notre cinéma ,</p>  
                    <p>il saura porter haut et fort la culture limousine mais aussi et surtout</p> 
                    <p>faire découvrir des recettes qui viennent d'ailleurs et qui invitent au voyage. </p> 
                    <p>Les plats du jours originaux sont servis chaque midi pour un prix tout à fait raisonnable! </p> 
                    <img src="{part_url3}" width="700">
                    <p>A la carte on retrouve de la charcuterie fine et cosmopolite,</p> 
                    <p> des burgers maison, des pokes bowls,</p> 
                    <p>  bar à viande avec des viandes limousines </p>
                    <p>Et comme dirait ce bon vieux Gandalf:</p> 
                    <p> VENEZ !! Pauvres Fous !! </p>
                </div>
                """,
                unsafe_allow_html=True
            )
        
    st.markdown(
                f"""                
                <div class="film-card">   
                    <h3> Wild Code School </h3> 
                    <a href="{'https://www.wildcodeschool.com/'}" target="_blank">                
                    <img src="{part_url2}" width="850"></a>
                    <p>Depuis plus de 10 ans, la Wild Code School forme des talents aux métiers de la tech et de l'IA.</p>
                    <p>Avec plus de 8 000 alumni, des formations adaptées au marché, et une pédagogie innovante,</p>
                    <p>nous préparons les professionnels de demain.</p>
                    <p>Découvrez nos spécialités pour réussir : développement web, data et IA,</p>
                    <p>IT et cybersécurité, design et gestion de projet.</p>
                    <p>Vous aurez les codes ! </p>                   
                    </div>
                """,
        unsafe_allow_html=True
            )
