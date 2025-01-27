import streamlit as st

# Set custom CSS for Poppins font
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;700&display=swap');

        .mission-text {
            font-family: 'Poppins', sans-serif;
            font-size: 1.2rem;
            color: black;
            line-height: 1.6;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Mission Section with inline style for color
st.markdown('<h1 style="font-family: Poppins, sans-serif; font-size: 3rem; color: #D4B9DB; margin-bottom: 0.5rem;">mission</h1>', unsafe_allow_html=True)
st.markdown(
    """
    <p class="mission-text">
        Our mission is to connect vineyard professionals and winemakers from all stages of responsible viticulture, 
        fostering collaboration and knowledge-sharing to advance sustainable practices. Through this community, we aim to 
        deepen understanding of the methods, financial and physical impacts, and their influence on wine quality, empowering 
        members to achieve truly resilient winemaking.
    </p>
    """,
    unsafe_allow_html=True,
)
