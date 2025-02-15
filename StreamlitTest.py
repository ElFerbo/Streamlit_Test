import streamlit as st
import pandas as pd

st.title('Uber pickups in NYC')

# Initialisierung des Zählers im session_state
if 'count' not in st.session_state:
    st.session_state.count = 0

st.title('Counter Example')

# Button zum Inkrementieren des Zählers
if st.button('Increment'):
    st.session_state.count += 1

st.write('Count = ', st.session_state.count)

st.balloons()
