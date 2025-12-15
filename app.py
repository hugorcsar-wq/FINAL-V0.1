import streamlit as st
import pandas as pd
import numpy as np

st.title('Mi Primera App Gratis desde Colab')

st.write("¡Esto funciona!")
x = st.slider('Selecciona un valor')
st.write(f'El cuadrado es: {x * x}')

# Aquí puedes pegar tus gráficos y lógica
