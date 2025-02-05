import streamlit as st
import requests

# URL do webhook do Make
MAKE_WEBHOOK_URL = "https://hook.make.com/SEU-WEBHOOK-AQUI"

st.title("Demo de Automação com AI no Make")

# Input do usuário
user_input = st.text_area("Digite sua pergunta:")

if st.button("Enviar para Make"):
    if user_input:
        response = requests.post(MAKE_WEBHOOK_URL, json={"input": user_input})
        if response.status_code == 200:
            st.success("Processando... Aguarde a resposta no destino configurado no Make.")
        else:
            st.error(f"Erro: {response.text}")
    else:
        st.warning("Digite algo antes de enviar.")

