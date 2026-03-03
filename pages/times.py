import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Times - Brasileirão", layout="wide")

@st.cache_data
def carregar_dados():
    return pd.read_csv("data/brasileirao.csv", encoding="latin-1")

dados = carregar_dados()

st.title("⚽ Times — Brasileirão (2003–2024)")
st.divider()

opcao = st.sidebar.selectbox(
    "📊 Escolha qual estatística analisar:",
    ("Maiores Campeões", "Times com Mais Gols", "Times com Mais Vitórias",
     "Times com Mais Gols Sofridos", "Média de Gols por Temporada")
)

if opcao == "Maiores Campeões":
    df_campeoes = dados[dados['place'] == 1]
    contagem = df_campeoes['team'].value_counts().reset_index()
    contagem.columns = ['Time', 'Títulos']
    fig = px.bar(contagem, x='Time', y='Títulos', text_auto=True, color='Títulos', color_continuous_scale='Blues')
    st.plotly_chart(fig, use_container_width=True)

elif opcao == "Times com Mais Gols":
    gols_time = dados.groupby('team')['goals'].sum().sort_values(ascending=False).head(10).reset_index()
    fig = px.bar(gols_time, x='team', y='goals', text_auto=True, color='goals', color_continuous_scale='Greens')
    st.plotly_chart(fig, use_container_width=True)

elif opcao == "Times com Mais Vitórias":
    maisvit = dados.groupby('team')['won'].sum().sort_values(ascending=False).head(10).reset_index()
    fig = px.bar(maisvit, x='team', y='won', text_auto=True, color='won', color_continuous_scale='Oranges')
    st.plotly_chart(fig, use_container_width=True)

elif opcao == "Times com Mais Gols Sofridos":
    sofridos = dados.groupby('team')['goals_taken'].sum().sort_values(ascending=False).head(10).reset_index()
    fig = px.bar(sofridos, x='team', y='goals_taken', text_auto=True, color='goals_taken', color_continuous_scale='Reds')
    st.plotly_chart(fig, use_container_width=True)

elif opcao == "Média de Gols por Temporada":
    media = dados.groupby('season')['goals'].mean().reset_index()
    fig = px.line(media, x='season', y='goals', markers=True)
    st.plotly_chart(fig, use_container_width=True)