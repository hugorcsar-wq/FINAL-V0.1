streamlit
pandas
numpy
matplotlib
seaborn
folium
scipy
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import folium
import streamlit.components.v1 as components

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(layout="wide", page_title="Dicrotec Intelligence", page_icon="⚡")

# --- ESTILOS CSS (MODO OSCURO PRO) ---
st.markdown("""
<style>
    .stApp {
        background-color: #0f172a;
        color: #f8fafc;
    }
    h1, h2, h3 {
        color: #f8fafc !important;
    }
    p, li, label {
        color: #cbd5e1 !important;
    }
    .metric-card {
        background-color: #1e293b;
        border: 1px solid #334155;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 10px;
    }
    .highlight {
        color: #10b981;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER PRINCIPAL ---
st.markdown("""
<div style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); padding: 30px; border-radius: 20px; border: 1px solid #334155; margin-bottom: 20px; text-align: center;">
    <h1 style="color: #f8fafc; margin: 0; font-size: 3em; font-weight: 900;">DICROTEC <span style="color: #10b981;">INTELLIGENCE</span></h1>
    <p style="color: #10b981; font-weight: bold; margin: 10px 0; letter-spacing: 2px;">QUANTUM SEMICONDUCTOR AUDIT | PATENT Tit. 383389</p>
    <p style="color: #64748b; margin: 0; font-size: 0.9em;">V5.0 MASTER FRAMEWORK | HIGH-FIDELITY ANALYTICS</p>
</div>
""", unsafe_allow_html=True)

# --- SECCIÓN 1: MAPA GEO-INTEL ---
st.markdown("## 🛰️ SECCIÓN 1: MAPA TÁCTICO DE DESPLIEGUE")

col1, col2 = st.columns([2, 1])

with col1:
    # Crear Mapa
    m = folium.Map(location=[23.6345, -102.5528], zoom_start=5, tiles='CartoDB dark_matter')
    
    escuelas = {
        'Primaria Chapultepec (CDMX)': [19.4268, -99.2088],
        'C.E. Tomas Moro (CDMX)': [19.3622, -99.2628],
        'Chihuahua Education Cluster': [28.6330, -106.0691]
    }
    
    for name, coords in escuelas.items():
        folium.CircleMarker(
            location=coords, radius=8, popup=name,
            color='#10b981' if 'CDMX' in name else '#3b82f6',
            fill=True, fill_color='#10b981' if 'CDMX' in name else '#3b82f6', fill_opacity=0.7
        ).add_to(m)
    
    # Renderizar mapa en Streamlit
    map_html = m._repr_html_()
    components.html(map_html, height=500)

with col2:
    st.markdown("""
    <div class="metric-card" style="border-left: 5px solid #10b981;">
        <h4 style="color:#94a3b8; margin:0;">CDMX PILOT</h4>
        <h2 style="color:#10b981; font-size: 2.5em; margin:0;">+400%</h2>
        <p style="margin:0;">LUX LEVEL INCREASE</p>
    </div>
    <div class="metric-card" style="border-left: 5px solid #3b82f6;">
        <h4 style="color:#94a3b8; margin:0;">CHIHUAHUA HUB</h4>
        <h2 style="color:#3b82f6; font-size: 2.5em; margin:0;">-38%</h2>
        <p style="margin:0;">OPEX REDUCTION</p>
    </div>
    <div class="metric-card" style="border-left: 5px solid #8b5cf6;">
        <h4 style="color:#94a3b8; margin:0;">NOM 025 STPS</h4>
        <h2 style="color:#8b5cf6; font-size: 2.5em; margin:0;">100%</h2>
        <p style="margin:0;">LEGAL COMPLIANCE</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- SECCIÓN 2: BENCHMARK EFICACIA ---
st.markdown("## ⚡ SECCIÓN 2: BENCHMARK DE EFICACIA (lm/W)")

years = np.array([2015, 2018, 2021, 2024, 2027, 2030, 2035])
doe_real = np.array([140, 150, 160, 170, 175, 180, 190]) 
dicrotec = np.array([145, 180, 250, 285, 330, 420, 550]) 

fig_eff, ax = plt.subplots(figsize=(12, 6))
fig_eff.patch.set_facecolor('#0f172a')
ax.set_facecolor('#0f172a')
ax.grid(color='#1e293b', linestyle='--', alpha=0.5)

ax.plot(years, doe_real, color='#ef4444', marker='s', ls='--', label='Industry Standard (LED)')
ax.plot(years, dicrotec, color='#10b981', marker='o', lw=4, label='DICROTEC Quantum Path')
ax.fill_between(years, doe_real, dicrotec, color='#10b981', alpha=0.1)

ax.set_title("EVOLUCIÓN DE EFICIENCIA LUMÍNICA", color='white', loc='left')
ax.set_ylabel("Lúmenes por Watt (lm/W)", color='#94a3b8')
ax.tick_params(colors='#94a3b8')
for spine in ax.spines.values():
    spine.set_color('#1e293b')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(facecolor='#0f172a', labelcolor='white')

st.pyplot(fig_eff)

st.info("💡 **Análisis:** Dicrotec supera el límite teórico del fósforo (LED tradicional) eliminando el efecto 'Stokes Shift', permitiendo proyecciones superiores a 500 lm/W para 2035.")

st.divider()

# --- SECCIÓN 3: ESPECTRO Y BIOSEGURIDAD ---
st.markdown("## 🔬 SECCIÓN 3: BIOSEGURIDAD & ESPECTRO")

c1, c2 = st.columns(2)

with c1:
    st.markdown("### 🌊 Gestión de Fotones (Espectro)")
    wavelength = np.linspace(380, 780, 1000)
    std_white = stats.norm.pdf(wavelength, 560, 60) * 0.42
    dicro_white = std_white * 1.85 
    
    fig_spec, ax = plt.subplots(figsize=(8, 5))
    fig_spec.patch.set_facecolor('#0f172a')
    ax.set_facecolor('#0f172a')
    
    ax.plot(wavelength, dicro_white, color='#10b981', lw=3, label='Dicrotec (High Fidelity)')
    ax.fill_between(wavelength, dicro_white, color='#10b981', alpha=0.2)
    ax.set_xlabel("Longitud de Onda (nm)", color='#94a3b8')
    ax.tick_params(colors='#94a3b8')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color('#1e293b')
    ax.spines['left'].set_color('#1e293b')
    
    st.pyplot(fig_spec)

with c2:
    st.markdown("### 🧠 Impacto Cognitivo (Auditado)")
    metrics = ['Lectura', 'Atención', 'Matemáticas', 'Memoria']
    values = [133, 115, 120, 126] # Porcentajes base 100
    
    fig_bar, ax = plt.subplots(figsize=(8, 5))
    fig_bar.patch.set_facecolor('#0f172a')
    ax.set_facecolor('#0f172a')
    
    bars = ax.bar(metrics, values, color=['#10b981', '#3b82f6', '#8b5cf6', '#f59e0b'])
    ax.set_ylim(100, 150)
    ax.axhline(y=100, color='white', linestyle='--', linewidth=1, label="Base LED Estándar")
    
    ax.tick_params(colors='#94a3b8')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color('#1e293b')
    ax.spines['left'].set_visible(False)
    
    # Etiquetas
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'+{height-100}%',
                ha='center', va='bottom', color='white', fontweight='bold')
                
    st.pyplot(fig_bar)

st.divider()

# --- SECCIÓN 4: SOBERANÍA ENERGÉTICA ---
st.markdown("## 💰 SECCIÓN 4: MACRO-ECONOMÍA Y AHORRO")

col_fin1, col_fin2 = st.columns([1, 2])

with col_fin1:
    st.markdown("""
    <div style="background: #064e3b; padding: 25px; border-radius: 15px; border: 1px solid #10b981;">
        <h3 style="color: #fff; margin:0;">AHORRO NACIONAL</h3>
        <p style="color: #6ee7b7; font-size: 0.9em;">Proyección Fiscal 2025</p>
        <hr style="border-color: #10b981;">
        <h1 style="color: #fff; font-size: 3.5em; margin: 10px 0;">60%</h1>
        <p style="color: #fff;">De la factura eléctrica de iluminación nacional liberada.</p>
    </div>
    """, unsafe_allow_html=True)

with col_fin2:
    # Datos simulados para gráfico
    labels = ['Consumo Nacional (GWh)', 'Iluminación Actual', 'Con DICROTEC']
    values = [345439, 69087, 27635] # Valores ejemplo
    
    fig_macro, ax = plt.subplots(figsize=(10, 4))
    fig_macro.patch.set_facecolor('#0f172a')
    ax.set_facecolor('#0f172a')
    
    ax.barh(labels, values, color=['#1e293b', '#ef4444', '#10b981'])
    ax.tick_params(colors='#94a3b8')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color('#1e293b')
    ax.spines['left'].set_visible(False)
    
    st.pyplot(fig_macro)

st.success("✅ Sistema Dicrotec V5.0 cargado exitosamente. Todos los módulos operativos.")
