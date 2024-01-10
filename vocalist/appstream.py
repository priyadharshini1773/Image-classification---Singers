import streamlit as st

# Streamlit app title
st.title("Vocalist Image Classifier")
with open('app.css') as f:
    st.markdown(),f'<style>{f.read()}</style>,unsafe_allow_html=True>

# Define the images and corresponding labels
images = {
    "Alec Benjamin": "./images/alec.jpg",
    "AR Rahman": "./images/arrahman.jpg",
    "Illayaraja": "./images/illayaraja.jpg",
    "Shreya Ghoshal": "./images/shreya.jpg",
    "Taylor Swift": "./images/taylor.jpg"
}

# Display the cards using Streamlit columns
col1, col2, col3, col4, col5 = st.beta_columns(5)

# Iterate through images and display in columns
for artist, image_path in images.items():
    with eval(f"col{len(artist.split()[0]) + 1}"):
        st.image(image_path, caption=artist, use_column_width=True)
        st.write(f"**{artist}**")

# Upload file and classify
uploaded_file = st.file_uploader("Upload an image for classification", type=["jpg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    st.write("Classify Button Placeholder")  # Replace with your classification logic

# Display classification results table
st.write("## Classification Results")

# Create a table with artist names and corresponding probability scores
table_data = {
    "Vocalist": ["Alec Benjamin", "AR Rahman", "Illayaraja", "Shreya Ghoshal", "Taylor Swift"],
    "Probability Score": [0.0, 0.0, 0.0, 0.0, 0.0]  # Replace with actual probability scores
}

st.table(table_data)

# Display error message
st.error("Can't classify image. Classifier was not able to detect face and two eyes properly")
