import streamlit as st
import requests
import pandas as pd

# Configuração da Página
st.set_page_config(page_title="Método Babi - Automação Inteligente", layout="wide")

# Título do Dashboard
st.title("🤖 Método Babi - Automação Inteligente")

# Seção 1: Boas-Vindas e Configuração
st.header("📌 Configuração Inicial")
frequencia = st.selectbox("Frequência de Análise:", ["Tempo Real", "Diária", "Semanal"])
palavras_chave = st.text_input("Palavras-chave para monitoramento:")
if st.button("Salvar Configuração"):
    st.success("✅ Configuração salva!")

# Seção 2: Monitoramento e Coleta de Dados
st.header("📡 Coleta de Dados")
st.write("Últimos dados coletados de fontes monitoradas:")
data = {"Fonte": ["Google Alerts", "RSS Feeds", "LinkedIn", "Instagram", "TikTok"], "Status": ["Ativo", "Ativo", "Ativo", "Ativo", "Ativo"]}
df = pd.DataFrame(data)
st.dataframe(df)
if st.button("🔄 Atualizar Dados"):
    st.success("Dados atualizados com sucesso!")

# Seção 3: Categorização Automática das Notícias
st.header("📊 Categorização das Notícias")
st.write("Classificação automática das coletas")
categorias = ["BAU (Business as Usual)", "Bomba (Impacto Alto)", "Ação Ninja (Movimento Estratégico)"]
categoria_escolhida = st.radio("Escolha a categoria:", categorias)
if st.button("Classificar Notícias"):
    st.success(f"✅ Notícias categorizadas como: {categoria_escolhida}")

# Seção 4: Análise Semântica com InfraNodus
st.header("📈 Análise Semântica (InfraNodus)")
if st.button("🔍 Analisar com InfraNodus"):
    response = requests.get("https://api.infranodus.com/analysis", params={"query": palavras_chave})
    if response.status_code == 200:
        st.success("✅ Análise semântica concluída!")
        st.json(response.json())
    else:
        st.error("❌ Erro ao conectar com InfraNodus")

# Seção 5: Tomada de Decisão Interativa
st.header("🧠 Tomada de Decisão")
opcoes = ["Gerar insights estratégicos", "Priorizar categorização automática", "Ambos"]
decisao = st.radio("Qual abordagem deseja seguir?", opcoes)
if st.button("🚀 Enviar Decisão"):
    st.success(f"✅ Decisão enviada: {decisao}")

# Seção 6: Geração de Relatórios e Ações
st.header("📑 Geração de Relatórios e Ações")
if st.button("📤 Enviar relatório por e-mail"):
    st.success("✅ Relatório enviado para metodobabi@gmail.com")

# Seção 7: Chatbot com Zaia
st.header("🤖 Chatbot Zaia")
pergunta = st.text_input("Pergunte algo para Zaia:")
if st.button("Enviar Pergunta"):
    response = "Zaia ainda está aprendendo! Em breve, terá respostas mais inteligentes."
    st.write(response)

# Seção 8: Chat com API da Perplexity
st.header("🗣️ Chat com Perplexity API")
consulta = st.text_input("Faça uma consulta à Perplexity AI:")
if st.button("Consultar Perplexity"):
    response = requests.get("https://api.perplexity.ai/query", params={"query": consulta})
    if response.status_code == 200:
        st.write(response.json())
    else:
        st.error("❌ Erro ao conectar com Perplexity API")
