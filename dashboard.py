import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="SSC 2026 Hub", 
    page_icon="",
    layout="centered"
)

# 2. Main Header and Styling
st.image("Main Banner.png", use_container_width=True)
st.title(" Switch Staff Challenge 2026")
st.markdown("### Dashboard Access Portal")
st.write("Please select a performance level below to view the detailed analytics.")

st.markdown("---")

# 3. Navigation Links
# We use columns to make the buttons look organized in the center
col1, col2, col3 = st.columns(3)

with col1:
    st.header("🥉")
    st.subheader("Explorer")
    st.write("Discovery and First Steps")
    st.write("Go to Level 1")
    st.link_button("iPhone and Apple Watch", "https://levelssc2026januaryquest-chdvfgsnwh3vfajfeaj9pe.streamlit.app", use_container_width=True)
    st.link_button("iPad", "https://ssc2026februaryquest-hjxkt9mlcfccphmmuxetgw.streamlit.app", use_container_width=True)

with col2:
    with col1:
    st.markdown("<h2 style='text-align: center;'>🥈</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Adventurer</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Bravery and Skill</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Go to Level 2</p>", unsafe_allow_html=True)
    
    st.link_button("iPhone and Apple Watch", "https://levelssc2026januaryquest-chdvfgsnwh3vfajfeaj9pe.streamlit.app", use_container_width=True)
    st.link_button("iPad", "https://ssc2026februaryquest-hjxkt9mlcfccphmmuxetgw.streamlit.app", use_container_width=True)

with col3:
    st.header("🥇")
    st.subheader("Master")
    st.write("Legacy and Ultimate Challenge")
    st.link_button("Go to Level 3", "", use_container_width=True)

st.markdown("---")
st.caption("© 2026 Switch Staff Challenge | Insight Team")
