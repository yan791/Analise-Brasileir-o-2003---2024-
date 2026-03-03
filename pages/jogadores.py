import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title= 'Jogadores - Brasileirão', layout = 'wide')

dados = pd.read_csv('data/database.csv', encoding = 'latin-1')
st.title('🧑‍💼 Jogadores — Brasileirão (2024)')
st.divider()

opcao = st.sidebar.selectbox(
    "📊 Escolha qual estatística analisar:",
    ("Top Artilheiros", "Top Assistencias", "Mais Participações em Gols")
)

if opcao == "Top Artilheiros":
    st.subheader('Top Artilheiros 2024')
    artilheiros = dados.groupby('Jogador')['Gols'].sum().sort_values(ascending = False).head(10).reset_index()
    fig = px.bar(artilheiros, x = 'Jogador', y = 'Gols', text_auto=True, color='Gols', color_continuous_scale='Purples')
    st.plotly_chart(fig, use_container_width = True)