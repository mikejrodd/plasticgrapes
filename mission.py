import streamlit as st

# Set page config for wide layout
st.set_page_config(layout="wide")

# Set custom CSS for Poppins font and expanding content width
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

        .post-title {
            font-family: 'Poppins', sans-serif;
            font-size: 2rem;
            color: black;
            margin-top: 2rem;
            margin-bottom: 0.5rem;
        }

        .post-content {
            font-family: 'Poppins', sans-serif;
            font-size: 1.1rem;
            color: black;
            line-height: 1.6;
        }

        /* Expand content width */
        .main {
            max-width: 1200px;
            margin: 0 auto;
        }

        /* Limit page height to content */
        .main {
            max-height: 100vh;
            overflow-y: hidden;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Mission Section with correct title color
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

# Add the post section
st.markdown('<h2 class="post-title">The Limit Does Not Exist: Plastic Vineyards</h2>', unsafe_allow_html=True)
st.markdown(
    """
    <p class="post-content">
        Plasticity refers to an ecosystem's ability to adapt and reorganize the interactions among plants, animals, 
        and microorganisms in response to shifts in community dynamics or environmental conditions. In a vineyard, this 
        adaptability presents as resilience against challenges such as pests, diseases, or climatic variations while maintaining 
        ecological balance and productivity.
    </p>
    <p class="post-content">
        Organic, Regenerative, Sustainable, sometimes even Synthetics... whatever the buzzword, whatever you are trying in the 
        vineyard is likely a great step in the right direction if you are focused on responsible viticulture. But our ultimate 
        goal is to curiously and flexibly adapt portions of all of these practices, with the aspirational goal of creating plasticity.  
    </p>
    """,
    unsafe_allow_html=True,
)
