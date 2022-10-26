import streamlit as st
import pandas as pd

st.title('Uber pickups in NYC')


st.title('Counter Example')
count = 0

increment = st.button('Increment')
if increment:
    count += 1

st.write('Count = ', count)

st.balloons()
#st.success