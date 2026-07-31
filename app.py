import streamlit as st

st.title("Bem-vindo")

nome = st.text_input("Digite seu nome")
idade = st.text_input("Digite sua idade")
tipo_usuario = st.selectbox("selecione o tipo de usuario", ["nenhum", "um", "dois"])

cadastrar = st.button("cadastrar")

if cadastrar:
    with open("cadastro.txt","a") as arquivo:
        arquivo.write(f"Nome: {nome}, Idade: {idade}, Tipo de Usuário: {tipo_usuario}\n")
        st.success( "parabens, você e linda!")
       

