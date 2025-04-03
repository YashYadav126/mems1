import streamlit as st
import requests
import random

# Apply custom CSS to limit image height
st.markdown(
    """
    <style>
    img {
        max-height: 300px; /* Limits height while keeping width flexible */
        object-fit: contain; /* Ensures the image isn't stretched */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Function to get a comic meme from XKCD
def get_comic_meme():
    comic_id = random.randint(1, 2800)  # XKCD has thousands of comics
    url = f"https://xkcd.com/{comic_id}/info.0.json"  
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data["title"], data["img"]

    return "Failed to fetch comic meme!", "https://via.placeholder.com/400"

# Streamlit UI
st.title("🤣 Funny Comic Memes")

if st.button("Get Comic Meme 📖"):
    title, image_url = get_comic_meme()
    st.subheader(title)
    st.image(image_url, use_container_width=True)  # FIXED: New method

st.sidebar.write("Made with ❤️ using Streamlit & XKCD API")
