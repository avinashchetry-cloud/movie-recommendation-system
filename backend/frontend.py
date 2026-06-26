import streamlit as st
import requests
import pickle

st.set_page_config(page_title="Movie Recommender", layout="wide")

st.title("🎬 Movie Recommender System")

# Load movie list
movies = pickle.load(open('models/movie_df.pkl', 'rb'))
movie_list = sorted(movies['title'].unique())

# dropdown
movie = st.selectbox("Select a movie", movie_list)

if st.button("Get Recommendations"):

    if not movie:
        st.warning("Please select a movie")
    else:
        try:
            with st.spinner("Fetching recommendations..."):

                response = requests.post(
                    "http://127.0.0.1:5000/recommend",
                    json={"movie": movie},
                    timeout=10
                )

                if response.status_code != 200:
                    st.error("Backend error")
                    st.write(response.text)
                    st.stop()

                data = response.json()
                recommendations = data.get("recommendations", [])

                if not recommendations:
                    st.error("No recommendations found")
                else:
                    st.subheader(f"Recommendations for '{movie}'")

                    cols = st.columns(4)

                    for idx, rec in enumerate(recommendations):

                        with cols[idx % 4]:

                            st.markdown(f"### {rec.get('title', 'No Title')}")

                            # Poster
                            if rec.get("poster"):
                                st.image(rec["poster"], use_container_width=True)
                            else:
                                st.write("🚫 No Image")

                            # Release date
                            st.caption(f"📅 {rec.get('release_date', 'N/A')}")

                            # Overview
                            with st.expander("Overview"):
                                st.write(rec.get("overview", "No overview available"))

        except Exception as e:
            st.error("Backend not running or network issue")
            st.write(str(e))