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
    fig = px.bar(artilheiros, x = 'Jogador', y = 'Gols', text_auto=True, color='Gols', color_continuous_scale='Blues')
    st.plotly_chart(fig, use_container_width = True)

if opcao == "Top Assistencias":
    st.subheader('Top Assistencias')
    assistencias = dados.groupby('Jogador')[['Assis.', 'Gols']].sum().sort_values(by='Assis.', ascending=False).head(10).reset_index()
    fig = px.bar(assistencias, x='Jogador', y='Assis.', text_auto=True, color='Assis.', color_continuous_scale='Reds')
    st.plotly_chart(fig, use_container_width=True)

if opcao == "Mais Participações em Gols":
    st.subheader('Mais Participações em Gols')
    dados["Participacoes"] = dados["Gols"].fillna(0) + dados["Assis."].fillna(0)
    ga = dados.groupby('Jogador')['Participacoes'].sum().sort_values(ascending= False).head(10).reset_index()
    fig = px.bar(ga, x = 'Jogador', y = 'Participacoes', text_auto = True, color = 'Participacoes', color_continuous_scale = 'Greens')
    st.plotly_chart(fig, use_container_width = True)