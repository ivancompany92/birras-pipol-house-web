from apps import BPH1
import streamlit as st

# main function for the Dashboard of the project:
# we have 2 pages, with different information about our beers:

BPH1.app()
st.markdown("""
<style>
body {
color: #000000;
background-image: url("https://cervecear.com/wp-content/uploads/2012/05/espumabj1.jpg");
background-size: cover;
}
</style>
    """, unsafe_allow_html=True)
