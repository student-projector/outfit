import streamlit as st

st.markdown("""
    <style>
        body {
            background-color: #ece9f7;
        }
        .main {
            background-color: #fff7e6;
            border-radius: 12px;
            padding: 2em;
        }
        h1, h2, h3 {
            color: #7d3c98;
        }
    </style>
""", unsafe_allow_html=True)

#st.title("Fantasy Book Recommender")
#st.header("Which world is right for you?")
#st.image("https://github.com/nzhiv-eurogym/fantasy-recommender/blob/main/recomender.png", use_container_width=True)
st.image("https://raw.githubusercontent.com/nzhiv-eurogym/fantasy-recommender/main/recomender.png", use_container_width=True)



st.title("Which Fantasy World is Right for You?")

st.write("Answer a few questions and get your fantasy book recommendation!")

# Questions
weather = st.selectbox("Is the weather ousidde cold 0-10?", ["Yes", "No"])
rain = st.selectbox("Is it rainy outside?", ["Yes", "No"])
size = st.selectbox("Which clothes out of the following do you like more?", ["Oversized", "Tight", "Something in between"])
shade = st.selectbox("Do you prefer dark or bright colors when choosing clothes?", ["Dark", "Bright"])
color = st.selectbox("What color out of the following do you like the most?", ["Shades of green", "YELLLOW and orange" "shades of blue and purple" "shades of red" "black & white"])
style = st.selectbox("What do you usually wear?", ["Something like an oversized sweater, tousers or a skirt", "Something smart casual, like a shirt, dark skirt or trousers" "Something girly and soft" "Something like sun, yellow and orange, maybe a dress" "something sporty"])

# Recomendation
recommendation = ""

if magic_world == "Yes" and epic_scale == "No":
    recommendation = "Harry Potter (J.K. Rowling) – magic, wizarding school, modern world"
elif epic_scale == "Yes" and politics == "No" and portal_world == "No":
    recommendation = "The Lord of the Rings (J.R.R. Tolkien) – classic fantasy, epic battle between good and evil"
elif politics == "Yes":
    recommendation = "A Song of Ice and Fire / Game of Thrones (George R.R. Martin) – intrigues, dynasties, a harsh world"
elif monsters == "Yes":
    recommendation = "The Witcher (Andrzej Sapkowski) – monsters, monster hunters, Eastern European flavor"
elif myths == "Yes" and portal_world == "No":
    recommendation = "Percy Jackson (Rick Riordan) – teenage adventures, Greek mythology"
elif portal_world == "Yes":
    recommendation = "The Chronicles of Narnia (C.S. Lewis) – magical world, portals, allegories, fairytale adventures"
else:
    recommendation = "Try the classics — The Lord of the Rings (Tolkien) — or explore new fantasy worlds!"

if st.button("Get My Recommendation!"):
    st.markdown(f"### Your recommended fantasy world:\n**{recommendation}**")
