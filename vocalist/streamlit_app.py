import streamlit as st

# Streamlit app title
st.title("Vocalist Image Classifier")

# Read and render the external CSS file
with open('app.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Rest of your Streamlit app code
# ...

# Example: Display an image
st.image("path/to/your/image.jpg", caption="Uploaded Image", use_column_width=True)

# Example: Display a table
table_data = {
    "Vocalist": ["Alec Benjamin", "AR Rahman", "Illayaraja", "Shreya Ghoshal", "Taylor Swift"],
    "Probability Score": [0.0, 0.0, 0.0, 0.0, 0.0]  # Replace with actual probability scores
}

st.table(table_data)

# Example: Display error message
st.error("Can't classify image. Classifier was not able to detect face and two eyes properly")
