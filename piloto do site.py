import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="SPEEDMAIS - Central Inteligente",
    page_icon="🚗",
    layout="wide"
)

# Estilo visual personalizado (inspirado em painéis modernos)
st.markdown("""
    <style>
    .main-header {
        font-size: 24px;
        font-weight: bold;
        color: #1E3A8A;
    }
    .badge-urgente {
        background-color: #FEE2E2;
        color: #DC2626;
        padding: 4px 8px;
        border-radius: 4px;
        font-weight: bold;
        font-size: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# Topo da Aplicação
st.markdown('<p class="main-header">SPEEDMAIS • DETRAN-MG (Central Inteligente)</p>', unsafe_allow_html=True)
st.caption("Central Inteligente de Consulta e Procedimentos de Atendimento com Assistência de IA")

# Barra Lateral de Navegação / Filtros
st.sidebar.header("Filtros e Módulos")
categoria = st.sidebar.selectbox("Selecione a Categoria:", ["Todos", "Habilitação (CNH)", "Infrações", "Veículos / CRLV", "Prazos e Alertas"])

# Simulação de base de conhecimento da Central
base_conhecimento = [
    {
        "titulo": "Impactos da Greve dos Correios no Envio de CNH",
        "categoria": "Habilitação (CNH)",
        "resumo": "Obtenção do código de segurança da CNH Digital pelo Fala.BR caso a CNH física sofra atrasos de entrega.",
        "procedimento": "Acessar o Fala.BR (gov.br), selecionar 'Acesso à Informação (LAI)' e solicitar o código de segurança do documento."
    },
    {
        "titulo": "Calendário do CRLV 2026",
        "categoria": "Veículos / CRLV",
        "resumo": "Prazos obrigatórios para licenciamento: Placas 1-3 (Set), 4-6 (Out), 7-0 (Nov).",
        "procedimento": "Quitar IPVA, taxa de licenciamento e multas pendentes antes da data limite para emissão do CRLV 2026."
    },
    {
        "titulo": "Exame Toxicológico na Primeira Habilitação",
        "categoria": "Habilitação (CNH)",
        "resumo": "Exigência de resultado negativo registrado no Renach para PPD nas categorias A, B e AB (processos a partir de 20/06/2026).",
        "procedimento": "Realizar o exame em laboratório credenciado pela Senatran após a aprovação no exame prático."
    }
]

# Campo de Pesquisa Principal com IA
st.subheader("🔍 Consulta Inteligente")
termo_busca = st.text_input("Digite sua dúvida ou procedimento (Ex: 'atraso correios cnh', 'prazo crlv'):")

if termo_busca:
    st.info(f"🤖 **Assistente IA:** Analisando a base para o termo: *'{termo_busca}'*...")
    
    # Aqui você conectaria com a API da IA (ex: google-generativeai) para buscar na base ou gerar a resposta.
    # Exemplo de resposta simulada inteligente:
    st.success("Resposta encontrada com base nos protocolos vigentes:")
    
    # Filtrando resultados locais simples baseados no termo digitado
    resultados_filtrados = [item for item in base_conhecimento if termo_busca.lower() in item['titulo'].lower() or termo_busca.lower() in item['resumo'].lower()]
    
    if resultados_filtrados:
        for res in resultados_filtrados:
            st.markdown(f"### {res['titulo']}")
            st.write(f"**Resumo:** {res['resumo']}")
            st.markdown(f"**Procedimento Operacional:** {res['procedimento']}")
            st.markdown("---")
    else:
        st.warning("Nenhum procedimento exato encontrado na busca rápida. A IA gerou a diretriz padrão: verifique se há erros de digitação ou abra um chamado interno no canal de suporte.")

else:
    st.markdown("### 📌 Alertas e Prazos em Destaque")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<span class="badge-urgente">URGENTE</span>', unsafe_allow_html=True)
        st.markdown("**Validade de CNHs Vencidas**")
        st.write("Fim da prorrogação excepcional. Condutores têm o prazo regular de 30 dias para iniciar o processo de renovação tradicional.")
        
    with col2:
        st.markdown('<span class="badge-urgente">PRAZO</span>', unsafe_allow_html=True)
        st.markdown("**Exame Toxicológico (1ª Habilitação)**")
        st.write("Obrigatório para processos abertos a partir de 20/06/2026 nas categorias A, B e AB com registro prévio no Renach.")

        import streamlit as st

st.subheader("🤖 Assistente")

pergunta = st.text_input("Digite sua dúvida:")

if st.button("Perguntar"):
    if "correios" in pergunta.lower():
        st.write("Pra Correios: 1. Vai em rastreio, 2. Pega o código, 3. Abre reclamação no site.")
    elif "cnh" in pergunta.lower():
        st.write("Pra CNH: 1. Entra no Detran, 2. Vê os pontos, 3. Agenda atendimento.")
    elif "atraso" in pergunta.lower():
        st.write("Se for atraso: anota o protocolo, tira print e abre chamado.")
    else:
        st.write("Ainda não sei responder isso, mas anotei sua dúvida!")
