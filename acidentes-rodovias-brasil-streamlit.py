# =======================================================
# Imports
# =======================================================
import pandas as pd
import streamlit as st
import altair as alt
import numpy as np

from vega_datasets import data

from tcc_painel_graficos import *

# =======================================================
# Datasets
# =======================================================
df_acidentes_geral_por_uf    = pd.read_csv('datasets/acidentes_geral_por_uf.csv', sep=',', encoding="UTF-8") 
df_acidentes_geral_por_tipo  = pd.read_csv('datasets/acidentes_geral_por_tipo.csv', sep=',', encoding="UTF-8") 
df_acidentes_geral_por_br    = pd.read_csv('datasets/acidentes_geral_por_br.csv', sep=',', encoding="UTF-8") 
df_acidentes_geral_por_causa = pd.read_csv('datasets/acidentes_geral_por_causa.csv', sep=',', encoding="UTF-8") 
df_acidentes_geral_por_classificacao = pd.read_csv('datasets/acidentes_geral_por_classificacao.csv', sep=',', encoding="UTF-8") 
df_acidentes_geral_por_fasedia = pd.read_csv('datasets/acidentes_geral_por_fase_dia.csv', sep=',', encoding="UTF-8") 
df_acidentes_geral_por_condicaometereologica = pd.read_csv('datasets/acidentes_geral_por_condicao_metereologica.csv', sep=',', encoding="UTF-8") 
df_acidentes_geral_por_dia_semana = pd.read_csv('datasets/acidentes_geral_por_dia_semana.csv', sep=',', encoding="UTF-8") 
df_acidentes_geral_por_tipo_veiculo = pd.read_csv('datasets/acidentes_geral_por_tipo_veiculo.csv', sep=',', encoding="UTF-8") 

# =======================================================
# Datasets de geolocalização
# =======================================================

df_acid_local_2017 = pd.read_csv('geo/acidentes_localizacao_processado_2017.csv', sep=';', encoding="ISO-8859-1")
df_acid_local_2018 = pd.read_csv('geo/acidentes_localizacao_processado_2018.csv', sep=';', encoding="ISO-8859-1")
df_acid_local_2019 = pd.read_csv('geo/acidentes_localizacao_processado_2019.csv', sep=';', encoding="ISO-8859-1")
df_acid_local_2020 = pd.read_csv('geo/acidentes_localizacao_processado_2020.csv', sep=';', encoding="ISO-8859-1")
df_acid_local_2021 = pd.read_csv('geo/acidentes_localizacao_processado_2021.csv', sep=';', encoding="ISO-8859-1")
df_acid_local_2022 = pd.read_csv('geo/acidentes_localizacao_processado_2022.csv', sep=';', encoding="ISO-8859-1")
df_acid_local_2023 = pd.read_csv('geo/acidentes_localizacao_processado_2023.csv', sep=';', encoding="ISO-8859-1")
df_acid_local_2024 = pd.read_csv('geo/acidentes_localizacao_processado_2024.csv', sep=';', encoding="ISO-8859-1")

# =======================================================
# Constantes do dashboard
# =======================================================
OPCAO_TODOS = 'Todos'
COLUNA_ANO = 'ano'

st.set_page_config(layout="wide")

# Definir o título fixo para o painel
st.title("Acidentes nas Rodovias Federais do Brasil (2007 a 2024)")

st.sidebar.markdown("# Filtros:")

# Adiciona uma caixa de seleção no sidebar
ano_selecionado = st.sidebar.selectbox(
    'Qual o ano deseja visualizar?',
    (OPCAO_TODOS, '2024', '2023', '2022', '2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011', '2010', '2009', '2008', '2007')
)

print(f'Ano Selecionado = {ano_selecionado}')

# Definição de abas
tab01, tab02, tab05, tab06, tab07, tab09, tab03 = st.tabs(
  [
    "Acidentes por Critérios",
    "Rankings Diversos",   
    "Gráficos Fluxo",
    "Gráficos Barras Empilhadas",
    "Gráficos de Distribuição",    
    "Mapa das BRs",
    "Mapa de Calor",  
  ]
)

lista_cores_graficos = [
    '#007bff', '#28a745', '#ffc107', '#dc3545', '#6c757d', '#d95b43', '#5bc0de', '#4caf50', '#ffeb3b', '#c497d9',
    '#00BFFF', '#32CD32', '#FF00FF', '#FFA500', '#5A87E8', '#00CED1', '#FF7F50', '#228B22', '#FFD700', '#000080',
    '#FF1493', '#4B0082', '#8A2BE2', '#7FFF00', '#00FFFF', '#008000'
]

# ==============================================================================
with tab01:

    # =======================================================
    # aba 01
    # =======================================================
    titulo = f'<h3> Acidentes por UF / Tipo / BR / Causa / Classificação / Fase do Dia / Condição Metereológica / Dia da Semana / Tipo de Veículo'
    st.markdown(titulo, unsafe_allow_html=True)  

    tab1_sub1, tab1_sub2, tab1_sub3, tab1_sub4, tab1_sub5, tab1_sub6, tab1_sub7, tab1_sub8, tab1_sub9  = st.tabs(
        [
            "Acidentes por UF", "Acidentes por Tipo", "Acidentes por BR", 
            "Acidentes por Causa", "Acidentes por Classificação", "Acidentes por Fase do Dia", 
            "Acidentes por Condição Metereológica", "Acidentes por Dia da Semana",
            "Acidentes por Tipo de Veículo"
        ])
        
    if ano_selecionado != OPCAO_TODOS:
        
      df_filtrado_uf = df_acidentes_geral_por_uf[(df_acidentes_geral_por_uf[COLUNA_ANO] == int(ano_selecionado))]
      titulo = f'Acidentes por UF em {ano_selecionado}'
      grafico_aba_01 = gera_grafico_barras_horizontal_por_uf(titulo, df_filtrado_uf)

      df_filtrado_tipo = df_acidentes_geral_por_tipo[(df_acidentes_geral_por_tipo[COLUNA_ANO] == int(ano_selecionado))]
      titulo = f'Acidentes por Tipo em {ano_selecionado}'  
      grafico_aba_02 = gera_grafico_barras_horizontal_por_tipo(titulo, df_filtrado_tipo)

      df_filtrado_br = df_acidentes_geral_por_br[(df_acidentes_geral_por_br[COLUNA_ANO] == int(ano_selecionado))]
      titulo = f'Acidentes por BR em {ano_selecionado}'  
      grafico_aba_03 = gera_grafico_barras_horizontal_por_br(titulo, df_filtrado_br)

      df_filtrado_causa = df_acidentes_geral_por_causa[(df_acidentes_geral_por_causa[COLUNA_ANO] == int(ano_selecionado))]
      titulo = f'Acidentes por Causa em {ano_selecionado}'  
      grafico_aba_04 = gera_grafico_barras_horizontal_por_causa(titulo, df_filtrado_causa)

      df_filtrado_classificacao = df_acidentes_geral_por_classificacao[(df_acidentes_geral_por_classificacao[COLUNA_ANO] == int(ano_selecionado))]
      titulo = f'Acidentes por Classificacao em {ano_selecionado}'  
      grafico_aba_05 = gera_grafico_por_classificacao(titulo, df_filtrado_classificacao)

      df_filtrado_fasedia = df_acidentes_geral_por_fasedia[(df_acidentes_geral_por_fasedia[COLUNA_ANO] == int(ano_selecionado))]
      titulo = f'Acidentes por Fase do Dia em {ano_selecionado}'  
      grafico_aba_06 = gera_grafico_por_fase_dia(titulo, df_filtrado_fasedia)

      df_filtrado_condicaometereologica = df_acidentes_geral_por_condicaometereologica[(df_acidentes_geral_por_condicaometereologica[COLUNA_ANO] == int(ano_selecionado))]
      titulo = f'Acidentes por Condição Metereológica em {ano_selecionado}'  
      grafico_aba_07 = gera_grafico_por_condicao_metereologica(titulo, df_filtrado_condicaometereologica)

      df_filtrado_dia_semana = df_acidentes_geral_por_dia_semana[(df_acidentes_geral_por_dia_semana[COLUNA_ANO] == int(ano_selecionado))]
      titulo = f'Acidentes por Dia da Semana em {ano_selecionado}'  
      grafico_aba_08 = gera_grafico_por_dia_semana(titulo, df_filtrado_dia_semana)

      df_filtrado_tipo_veiculo = df_acidentes_geral_por_tipo_veiculo[(df_acidentes_geral_por_tipo_veiculo[COLUNA_ANO] == int(ano_selecionado))]
      titulo = f'Acidentes por Tipo de Veículo em {ano_selecionado}'  
      grafico_aba_09 = gera_grafico_por_tipo_veiculo(titulo, df_filtrado_tipo_veiculo)
    
    else:
      titulo = f'Acidentes por UF (Geral)'    
      grafico_aba_01 = gera_grafico_barras_horizontal_por_uf(titulo, df_acidentes_geral_por_uf)

      titulo = f'Acidentes por Tipo (Geral)'    
      grafico_aba_02 = gera_grafico_barras_horizontal_por_tipo(titulo, df_acidentes_geral_por_tipo)

      titulo = f'Acidentes por BR (Geral)'    
      grafico_aba_03 = gera_grafico_barras_horizontal_por_br(titulo, df_acidentes_geral_por_br)

      titulo = f'Acidentes por Causa (Geral)'    
      grafico_aba_04 = gera_grafico_barras_horizontal_por_causa(titulo, df_acidentes_geral_por_causa)

      titulo = f'Acidentes por Classificacao (Geral)'    
      grafico_aba_05 = gera_grafico_por_classificacao(titulo, df_acidentes_geral_por_classificacao)

      titulo = f'Acidentes por Fase do Dia (Geral)'    
      grafico_aba_06 = gera_grafico_por_fase_dia(titulo, df_acidentes_geral_por_fasedia)

      titulo = f'Acidentes por Condição Metereológica (Geral)'    
      grafico_aba_07 = gera_grafico_por_condicao_metereologica(titulo, df_acidentes_geral_por_condicaometereologica)

      titulo = f'Acidentes por Dia da Semana (Geral)'  
      grafico_aba_08 = gera_grafico_por_dia_semana(titulo, df_acidentes_geral_por_dia_semana)

      titulo = f'Acidentes por Tipo de Veículo (Geral)'  
      grafico_aba_09 = gera_grafico_por_tipo_veiculo(titulo, df_acidentes_geral_por_tipo_veiculo)
    
    # Exibir o gráfico de barras empilhadas
    with tab1_sub1:
        st.altair_chart(grafico_aba_01)
    with tab1_sub2:    
        st.altair_chart(grafico_aba_02)
    with tab1_sub3:            
        st.altair_chart(grafico_aba_03)
    with tab1_sub4:    
        st.altair_chart(grafico_aba_04)
    with tab1_sub5:        
        st.altair_chart(grafico_aba_05)
    with tab1_sub6:        
        st.altair_chart(grafico_aba_06)
    with tab1_sub7:        
        st.altair_chart(grafico_aba_07)
    with tab1_sub8:        
        st.altair_chart(grafico_aba_08)
    with tab1_sub9:        
        st.altair_chart(grafico_aba_09)

# ==============================================================================
with tab02:    

    tab2_sub1, tab2_sub2, tab2_sub3, tab2_sub4, tab2_sub5, tab2_sub6, tab2_sub7  = st.tabs(
        ["Ranking por UF", "Ranking por Tipo", 
         "Ranking por BR", "Ranking por Classificação", 
         "Ranking por Fase do Dia", "Ranking por Dia da Semana",
         "Ranking por Tipo de Veículo"
        ]
    )
    
    with tab2_sub1:

        # ========================================================
        # Aba 02 - Acidentes por UF
        # ========================================================        
        titulo = f'<h2> Ranking dos Acidentes por UF (2007 a 2024)'
        st.markdown(titulo, unsafe_allow_html=True)  
       
           
        st.altair_chart(gera_grafico_ranking_uf_01(df_acidentes_geral_por_uf))   
        st.altair_chart(gera_grafico_ranking_uf_02(df_acidentes_geral_por_uf))
    
    with tab2_sub2:

        # ========================================================
        # Aba 02 - Acidentes por Tipo
        # ========================================================               
        titulo = f'<h2> Ranking dos Acidentes por Tipo (2007 e 2024)'
        st.markdown(titulo, unsafe_allow_html=True)   
       
        st.altair_chart(gera_grafico_ranking_tipo_01(df_acidentes_geral_por_tipo))   
        st.altair_chart(gera_grafico_ranking_tipo_02(df_acidentes_geral_por_tipo))
    
    with tab2_sub3:

        # ========================================================
        # Aba 02 - Acidentes por BR
        # ========================================================               
        titulo = f'<h2> Ranking dos Acidentes por BR (2007 e 2024)'
        st.markdown(titulo, unsafe_allow_html=True)
      
        st.altair_chart(gera_grafico_ranking_br_01(df_acidentes_geral_por_br))   
        st.altair_chart(gera_grafico_ranking_br_02(df_acidentes_geral_por_br))
    
    with tab2_sub4:

        # ========================================================
        # Aba 02 - Acidentes por Classificação
        # ========================================================        
        titulo = f'<H2> Ranking por Classificação'
        st.markdown(titulo, unsafe_allow_html=True)
    
        st.altair_chart(gera_grafico_ranking_classificacao_01(df_acidentes_geral_por_classificacao))
        st.altair_chart(gera_grafico_ranking_classificacao_02(df_acidentes_geral_por_classificacao))
    
    with tab2_sub5:

        # ========================================================
        # Aba 02 - Acidentes por Fase do Dia
        # ========================================================               
        titulo = f'<H2> Ranking por Fase do Dia'
        st.markdown(titulo, unsafe_allow_html=True)
    
        st.altair_chart(gera_grafico_ranking_fasedia_01(df_acidentes_geral_por_fasedia))   
        st.altair_chart(gera_grafico_ranking_fasedia_02(df_acidentes_geral_por_fasedia))

    with tab2_sub6:

        # ========================================================
        # Aba 02 - Acidentes por Dia da Semana
        # ========================================================               
        titulo = f'<H2> Ranking por Dia da Semana'
        st.markdown(titulo, unsafe_allow_html=True)
    
        st.altair_chart(gera_grafico_ranking_diasemana_01(df_acidentes_geral_por_dia_semana))   
        st.altair_chart(gera_grafico_ranking_diasemana_02(df_acidentes_geral_por_dia_semana))

    with tab2_sub7:

        # ========================================================
        # Aba 02 - Acidentes por Dia da Semana
        # ========================================================               
        titulo = f'<H2> Ranking por Tipo de Veículo'
        st.markdown(titulo, unsafe_allow_html=True)
    
        st.altair_chart(gera_grafico_ranking_tipoveiculo_01(df_acidentes_geral_por_tipo_veiculo))   
        st.altair_chart(gera_grafico_ranking_tipoveiculo_02(df_acidentes_geral_por_tipo_veiculo))

# ==============================================================================
with tab03:

    # aba 03
    titulo = f'<H2> Mapa de Calor por Classificação'
    st.markdown(titulo, unsafe_allow_html=True)  

    if ano_selecionado == OPCAO_TODOS:
        df_envolvidos = pd.read_csv(f'mapa_calor/mapa_calor_classificacao_geral.csv')
    else:
        df_envolvidos = pd.read_csv(f'mapa_calor/mapa_calor_classificacao_{ano_selecionado}.csv')
        
    # Define os dados
    dados = df_envolvidos.set_index('classificacao').T.reset_index().melt(id_vars='index', var_name='classificacao', value_name='value')

    # Cria o gráfico de calor
    heatmap = alt.Chart(dados).mark_rect().encode(
        x=alt.X('index:O', title=None, axis=alt.Axis(orient='top')),  # Define a orientação do eixo x como 'top'
        y=alt.Y('classificacao:O', title=None),
        color=alt.Color('value:Q', scale=alt.Scale(scheme='yellowgreenblue')),    
    )

    # Adiciona o texto dentro de cada célula com o valor real e ajusta a cor do texto
    text = alt.Chart(dados).mark_text(baseline='middle', fontSize=10).encode(
        x='index:O',
        y='classificacao:O',
        text=alt.Text('value:Q', format='.0f'),
        color=alt.condition(
            alt.datum['value'] > (dados['value'].max() - dados['value'].min()) / 2,
            alt.value('white'),
            alt.value('black')
        )
    )

    # Combina o gráfico de calor com o texto
    heatmap_with_text = (heatmap + text).properties(
        width=800,
        height=600,
        title=f'Mapa de Calor por Classificação x Envolvidos ({ano_selecionado})'
    )

    # Exibe o gráfico    
    st.altair_chart(heatmap_with_text)
  
# ==============================================================================
with tab05:

    titulo = f'<H2> Gráficos de Fluxo por UF / Tipo / BR / Causa / Classificação / Fase do Dia / Condição Metereológica / Dia da Semana / Tipo de Veículo'
    st.markdown(titulo, unsafe_allow_html=True)
    
    tab5_sub1, tab5_sub2, tab5_sub3, tab5_sub4, tab5_sub5, tab5_sub6, tab5_sub7, tab5_sub8, tab5_sub9 = st.tabs(
        [
            "Fluxo por UF", "Fluxo por Tipo",
            "Fluxo por BR", "Fluxo por Causa",
            "Fluxo por Classificação", "Fluxo por Fase do Dia",
            "Fluxo por Condição Metereológica",
            "Fluxo por Dia da Semana",
            "Fluxo por Tipo de Veículo",
        ])   

    grafico1 = alt.Chart(df_acidentes_geral_por_uf).mark_area().encode(
        alt.X('ano:Q').axis(domain=False, tickSize=0),
        alt.Y('sum(Qtd):Q').stack('center').axis(None),
        alt.Color('UF:N').scale(scheme='category20b')
    ).properties(
      title='Fluxo de Acidentes por UF (2007 a 2024)',
      width=800, height=600            
    ).interactive()

    grafico2 = alt.Chart(df_acidentes_geral_por_tipo).mark_area().encode(
        alt.X('ano:Q').axis(domain=False, tickSize=0),
        alt.Y('sum(qtd):Q').stack('center').axis(None),
        alt.Color('tipo_acidente:N').scale(scheme='category20b')
    ).properties(
      title='Fluxo de Acidentes por Tipo (2007 a 2024)',
      width=800, height=600            
    ).interactive()

    grafico3 = alt.Chart(df_acidentes_geral_por_br).mark_area().encode(
        alt.X('ano:Q').axis(domain=False, tickSize=0),
        alt.Y('sum(qtd):Q').stack('center').axis(None),
        alt.Color('br:N').scale(scheme='category20b')
    ).properties(
      title='Fluxo Acidentes por BR (2007 a 2024)',
      width=800, height=600            
    ).interactive()

    grafico4 = alt.Chart(df_acidentes_geral_por_causa).mark_area().encode(
        alt.X('ano:Q').axis(domain=False, tickSize=0),
        alt.Y('sum(qtd):Q').stack('center').axis(None),
        alt.Color('causa_acidente:N').scale(scheme='category20b')
    ).properties(
      title='Fluxo Acidentes por Causa (2007 a 2024)',
      width=800, height=600            
    ).interactive()

    grafico5 = alt.Chart(df_acidentes_geral_por_classificacao).mark_area().encode(
        alt.X('ano:Q').axis(domain=False, tickSize=0),
        alt.Y('sum(qtd):Q').stack('center').axis(None),
        alt.Color('classificacao_acidente:N').scale(scheme='category20b')
    ).properties(
      title='Fluxo Acidentes por Classificação (2007 a 2024)',
      width=800, height=600            
    ).interactive()

    grafico6 = alt.Chart(df_acidentes_geral_por_fasedia).mark_area().encode(
        alt.X('ano:Q').axis(domain=False, tickSize=0),
        alt.Y('sum(qtd):Q').stack('center').axis(None),
        alt.Color('fase_dia:N').scale(scheme='category20b')
    ).properties(
      title='Fluxo Acidentes por Fase do Dia (2007 a 2024)',
      width=800, height=600            
    ).interactive()

    grafico7 = alt.Chart(df_acidentes_geral_por_condicaometereologica).mark_area().encode(
        alt.X('ano:Q').axis(domain=False, tickSize=0),
        alt.Y('sum(qtd):Q').stack('center').axis(None),
        alt.Color('condicao_metereologica:N').scale(scheme='category20b')
    ).properties(
      title='Fluxo Acidentes por Condição Metereológica (2007 a 2024)',
      width=800, height=600            
    ).interactive()

    grafico8 = alt.Chart(df_acidentes_geral_por_dia_semana).mark_area().encode(
        alt.X('ano:Q').axis(domain=False, tickSize=0),
        alt.Y('sum(qtd):Q').stack('center').axis(None),
        alt.Color('dia_semana:N').scale(scheme='category20b')
    ).properties(
      title='Fluxo Acidentes por Dia da Semana (2007 a 2024)',
      width=800, height=600            
    ).interactive()

    grafico9 = alt.Chart(df_acidentes_geral_por_tipo_veiculo).mark_area().encode(
        alt.X('ano:Q').axis(domain=False, tickSize=0),
        alt.Y('sum(qtd):Q').stack('center').axis(None),
        alt.Color('tipo_veiculo:N').scale(scheme='category20b')
    ).properties(
      title='Fluxo Acidentes por Tipo de Veículo (2007 a 2024)',
      width=800, height=600            
    ).interactive()
    
    # Exibir o gráfico de barras empilhadas
    with tab5_sub1:
        st.altair_chart(grafico1)
    with tab5_sub2:    
        st.altair_chart(grafico2)
    with tab5_sub3:            
        st.altair_chart(grafico3)
    with tab5_sub4:    
        st.altair_chart(grafico4)
    with tab5_sub5:        
        st.altair_chart(grafico5)
    with tab5_sub6:        
        st.altair_chart(grafico6)
    with tab5_sub7:        
        st.altair_chart(grafico7)
    with tab5_sub8:        
        st.altair_chart(grafico8)
    with tab5_sub9:        
        st.altair_chart(grafico9)
    
# ==============================================================================  
with tab06:
    
    titulo = f'<H2> Gráficos de Barras Empilhadas'
    st.markdown(titulo, unsafe_allow_html=True)    

    if ano_selecionado != OPCAO_TODOS:

      # por UF      
      df_filtrado_uf = df_acidentes_geral_por_uf[(df_acidentes_geral_por_uf[COLUNA_ANO] == int(ano_selecionado))]
      titulo = f'Barras Empilhadas por UF em {ano_selecionado}'
      grafico1 = grafico_barras_empilhadas_por_uf(titulo, df_filtrado_uf)        

      # por BR    
      df_filtrado_br = df_acidentes_geral_por_br[(df_acidentes_geral_por_br[COLUNA_ANO] == int(ano_selecionado))]
      titulo = f'Barras Empilhadas por BR em {ano_selecionado}'
      grafico2 = grafico_barras_empilhadas_por_br(titulo, df_filtrado_br)  

      # por Tipo 
      df_filtrado_tipo = df_acidentes_geral_por_tipo[(df_acidentes_geral_por_tipo[COLUNA_ANO] == int(ano_selecionado))]
      titulo = f'Barras Empilhadas por Tipo em {ano_selecionado}'
      grafico3 = grafico_barras_empilhadas_por_tipo(titulo, df_filtrado_tipo)  

      # por Causa 
      df_filtrado_causa = df_acidentes_geral_por_causa[(df_acidentes_geral_por_causa[COLUNA_ANO] == int(ano_selecionado))]
      titulo = f'Barras Empilhadas por Causa de Acidente em {ano_selecionado}'
      grafico4 = grafico_barras_empilhadas_por_causa(titulo, df_filtrado_causa)  

      # por Classificacao
      df_filtrado_classificacao = df_acidentes_geral_por_classificacao[(df_acidentes_geral_por_classificacao[COLUNA_ANO] == int(ano_selecionado))]
      titulo = f'Barras Empilhadas por Classificação de Acidente em {ano_selecionado}'
      grafico5 = grafico_barras_empilhadas_por_classificacao(titulo, df_filtrado_causa)  

      # por Fase do Dia
      df_filtrado_fase_dia = df_acidentes_geral_por_fasedia[(df_acidentes_geral_por_fasedia[COLUNA_ANO] == int(ano_selecionado))]
      titulo = f'Barras Empilhadas por Fase do Dia de Acidente em {ano_selecionado}'
      grafico6 = grafico_barras_empilhadas_por_fase_dia(titulo, df_filtrado_fase_dia)  

      # Condição Metereológica
      df_filtrado_condicaometereologica = df_acidentes_geral_por_condicaometereologica[(df_acidentes_geral_por_condicaometereologica[COLUNA_ANO] == int(ano_selecionado))]
      titulo = f'Barras Empilhadas por Condição Metereológica em {ano_selecionado}'
      grafico7 = grafico_barras_empilhadas_por_condicao_metereologica(titulo, df_filtrado_fase_dia)  

      # Dia da Semana
      df_filtrado_dia_semana = df_acidentes_geral_por_dia_semana[(df_acidentes_geral_por_dia_semana[COLUNA_ANO] == int(ano_selecionado))]
      titulo = f'Barras Empilhadas por Dia da Semana em {ano_selecionado}'
      grafico8 = grafico_barras_empilhadas_por_dia_semana(titulo, df_filtrado_dia_semana)  

      # Tipo de Veículo
      df_filtrado_tipo_veiculo = df_acidentes_geral_por_tipo_veiculo[(df_acidentes_geral_por_tipo_veiculo[COLUNA_ANO] == int(ano_selecionado))]
      titulo = f'Barras Empilhadas por Dia da Semana em {ano_selecionado}'
      grafico9 = grafico_barras_empilhadas_por_tipo_veiculo(titulo, df_filtrado_tipo_veiculo)  
    
    else:
      grafico1 = grafico_barras_empilhadas_por_uf('Barras Empilhadas por UF (2007 a 2024)', df_acidentes_geral_por_uf)            
      grafico2 = grafico_barras_empilhadas_por_br('Barras Empilhadas por BR (2007 a 2024)', df_acidentes_geral_por_br)  
      grafico3 = grafico_barras_empilhadas_por_tipo('Barras Empilhadas por Tipos de Acidentes (2007-2024)', df_acidentes_geral_por_tipo)    
      grafico4 = grafico_barras_empilhadas_por_causa('Barras Empilhadas por Causa de Acidentes (2007-2024)', df_acidentes_geral_por_causa)      
      grafico5 = grafico_barras_empilhadas_por_classificacao('Barras Empilhadas por Classificação de Acidentes (2007-2024)', df_acidentes_geral_por_classificacao)      
      grafico6 = grafico_barras_empilhadas_por_fase_dia('Barras Empilhadas por Fase do Dia de Acidentes (2007-2024)', df_acidentes_geral_por_fasedia)      
      grafico7 = grafico_barras_empilhadas_por_condicao_metereologica('Barras Empilhadas por Condição Metereológica de Acidentes (2007-2024)',                                                          df_acidentes_geral_por_condicaometereologica)      
      grafico8 = grafico_barras_empilhadas_por_dia_semana('Barras Empilhadas por Dia da Semana de Acidentes (2007-2024)', df_acidentes_geral_por_dia_semana)      
      grafico9 = grafico_barras_empilhadas_por_tipo_veiculo('Barras Empilhadas por Tipo de Veículo (2007-2024)', df_acidentes_geral_por_tipo_veiculo)      

    tab6_sub1, tab6_sub2, tab6_sub3, tab6_sub4, tab6_sub5, tab6_sub6, tab6_sub7, tab6_sub8, tab6_sub9  = st.tabs(
        [
            "por UF", "por BR", 
            "por Tipo", "por Causa", 
            "por Classificação", "por Fase do Dia", 
            "por Condição Metereológica", "por Dia da Semana",
            "por Tipo de Veículo",
        ]
    )

    with tab6_sub1:
        st.altair_chart(grafico1)                  
    with tab6_sub2:        
        st.altair_chart(grafico2)    
    with tab6_sub3:        
        st.altair_chart(grafico3)        
    with tab6_sub4:        
        st.altair_chart(grafico4)           
    with tab6_sub5:        
        st.altair_chart(grafico5)           
    with tab6_sub6:        
        st.altair_chart(grafico6)           
    with tab6_sub7:        
        st.altair_chart(grafico7)           
    with tab6_sub8:        
        st.altair_chart(grafico8) 
    with tab6_sub9:        
        st.altair_chart(grafico9)           

# ==============================================================================
with tab07:

    titulo = f'<H2> Distribuição de Acidentes por UF / por Tipo / por BR / por Classificação / por Causa / por Fase do Dia / por Condição Metereológica / por Dia da Semana / por Tipo de Veículo'
    st.markdown(titulo, unsafe_allow_html=True)

    grafico01 = alt.Chart(df_acidentes_geral_por_uf).mark_boxplot(extent='min-max').encode(
        alt.X('UF:N', title='Unidade Federativa (UF)'),
        alt.Y('Qtd:Q', title='Quantidade de Acidentes'),        
    ).properties(
        width=800,
        height=600,
        title='Distribuição de Acidentes por UF (2007 a 2024)'
    )

    grafico02 = alt.Chart(df_acidentes_geral_por_tipo).mark_boxplot(extent='min-max').encode(
        alt.X('tipo_acidente:N', title='Tipos de Acidentes'),
        alt.Y('qtd:Q', title='Quantidade de Acidentes')        
    ).properties(
        width=800,
        height=600,
        title='Distribuição de Acidentes por Tipo (2007 a 2024)'
    )

    grafico03 = alt.Chart(df_acidentes_geral_por_br).mark_boxplot(extent='min-max').encode(
        alt.X('br:N', title='Rodovias Federais (BR)'),
        alt.Y('qtd:Q', title='Quantidade de Acidentes')        
    ).properties(
        width=800,
        height=600,
        title='Distribuição de Acidentes por BR (2007 a 2024)'
    )

    grafico04 = alt.Chart(df_acidentes_geral_por_classificacao).mark_boxplot(extent='min-max').encode(
        alt.X('classificacao_acidente:N', title='Classificações de Acidentes'),        
        alt.Y('qtd:Q', title='Quantidade de Acidentes')        
    ).properties(
        width=800,
        height=600,
        title='Distribuição de Acidentes por Classificação (2007 a 2024)'
    )

    grafico05 = alt.Chart(df_acidentes_geral_por_causa).mark_boxplot(extent='min-max').encode(
        alt.X('causa_acidente:N', title='Causas de Acidentes'),  
        alt.Y('qtd:Q', title='Quantidade de Acidentes')        
    ).properties(
        width=800,
        height=600,
        title='Distribuição de Acidentes por Causa (2007 a 2024)'
    )

    grafico06 = alt.Chart(df_acidentes_geral_por_fasedia).mark_boxplot(extent='min-max').encode(
        alt.X('fase_dia:N', title='Fasos do Dia'), 
        alt.Y('qtd:Q', title='Quantidade de Acidentes')        
    ).properties(
        width=800,
        height=600,
        title='Distribuição de Acidentes por Fase do Dia (2007 a 2024)'
    )

    grafico07 = alt.Chart(df_acidentes_geral_por_condicaometereologica).mark_boxplot(extent='min-max').encode(
        alt.X('condicao_metereologica:N', title='Condições Metereológicas'), 
        alt.Y('qtd:Q', title='Quantidade de Acidentes')        
    ).properties(
        width=800,
        height=600,
        title='Distribuição de Acidentes por Condição Metereológica (2007 a 2024)'
    )
    
    grafico08 = alt.Chart(df_acidentes_geral_por_dia_semana).mark_boxplot(extent='min-max').encode(
        alt.X('dia_semana:N', title='Dia da Semana'), 
        alt.Y('qtd:Q', title='Quantidade de Acidentes')        
    ).properties(
        width=800,
        height=600,
        title='Distribuição de Acidentes por Dia da Semana (2007 a 2024)'
    )

    grafico09 = alt.Chart(df_acidentes_geral_por_tipo_veiculo).mark_boxplot(extent='min-max').encode(
        alt.X('tipo_veiculo:N', title='Tipo de Veículo'), 
        alt.Y('qtd:Q', title='Quantidade de Acidentes')        
    ).properties(
        width=800,
        height=600,
        title='Distribuição de Acidentes por Tipo de Veículo (2007 a 2024)'
    )

    tab7_sub1, tab7_sub2, tab7_sub3, tab7_sub4, tab7_sub5, tab7_sub6, tab7_sub7, tab7_sub8, tab7_sub9  = st.tabs(
        [
            "por UF", "por Tipo", 
            "por BR", "por Classificação", 
            "por Causa", "por Fase do Dia", 
            "por Condição Metereológica", 
            'por Dia da Semana', 'por Tipo de Veículo'
        ]
    )

    with tab7_sub1:
        st.altair_chart(grafico01)
    with tab7_sub2:    
        st.altair_chart(grafico02)
    with tab7_sub3:    
        st.altair_chart(grafico03)
    with tab7_sub4:    
        st.altair_chart(grafico04)
    with tab7_sub5:        
        st.altair_chart(grafico05)
    with tab7_sub6:    
        st.altair_chart(grafico06)
    with tab7_sub7:    
        st.altair_chart(grafico07)
    with tab7_sub8:    
        st.altair_chart(grafico08)
    with tab7_sub9:    
        st.altair_chart(grafico09)
    
# ==============================================================================  
with tab09:    

    # ================================
    # Aba 09 - constantes
    # ================================
    escala_cores = [
        # min, max, cor
        ( 1,  10, '#ffffcc'),
        (11,  20, '#ffeda0'),
        (21,  30, '#fed976'),
        (31,  40, '#feb24c'),
        (41,  50, '#fd8d3c'),
        (51,  60, '#fc4e2a'),
        (61,  70, '#e31a1c'),
        (71,  80, '#bd0026'),
        (81, 900, '#800026'),
        
    ]
    lista_brs = [101, 116, 381,  40, 153, 163, 364, 376, 262, 230, 470, 316, 282, 70,  60,  20, 158, 369,  50]

    # ===========================
    # Funções
    # ===========================
    def definir_cor(acidentes):
        cor_secionada = ''
        for i,item in enumerate(escala_cores):
            if item[0] <= acidentes <= item[1]:
                cor_secionada = item[2]
                break
                
        return cor_secionada
    # ===========================
    def definir_tamanho(acidentes):
        return acidentes * 10
    # ===========================

    left, middle, right = st.columns(3)
    
    # Filtro de ano
    mapa_ano_selecionado = left.selectbox(
        'Selecione o ano:', ('2024', '2023', '2022', '2021', '2020', '2019', '2018', '2017', OPCAO_TODOS))
    print(f'Mapa - Ano Selecionado = {mapa_ano_selecionado}')


    if mapa_ano_selecionado == '2017':
        df_coordenadas = pd.read_csv('geo/acidentes_localizacao_processado_2017.csv', sep=';', decimal='.')   
    elif mapa_ano_selecionado == '2018':
        df_coordenadas = pd.read_csv('geo/acidentes_localizacao_processado_2018.csv', sep=';', decimal='.')   
    elif mapa_ano_selecionado == '2019':
        df_coordenadas = pd.read_csv('geo/acidentes_localizacao_processado_2019.csv', sep=';', decimal='.')   
    elif mapa_ano_selecionado == '2020':
        df_coordenadas = pd.read_csv('geo/acidentes_localizacao_processado_2020.csv', sep=';', decimal='.')   
    elif mapa_ano_selecionado == '2021':
        df_coordenadas = pd.read_csv('geo/acidentes_localizacao_processado_2021.csv', sep=';', decimal='.')   
    elif mapa_ano_selecionado == '2022':
        df_coordenadas = pd.read_csv('geo/acidentes_localizacao_processado_2022.csv', sep=';', decimal='.')   
    elif mapa_ano_selecionado == '2023':
        df_coordenadas = pd.read_csv('geo/acidentes_localizacao_processado_2023.csv', sep=';', decimal='.')   
    elif mapa_ano_selecionado == '2024':
        df_coordenadas = pd.read_csv('geo/acidentes_localizacao_processado_2024.csv', sep=';', decimal='.')       
        
    mapa_br_selecionada = middle.selectbox('Selecione a rodovia:', (lista_brs))       
    
    # Exibir o quadro com as legendas
    titulo = f'<H2>Acidentes reportados na BR {mapa_br_selecionada} no ano de {mapa_ano_selecionado}'
    st.markdown(titulo, unsafe_allow_html=True)    

    df_coordenadas_filtrado = df_coordenadas[(df_coordenadas['br'] == int(mapa_br_selecionada))]       
    df_coordenadas_filtrado['cor'] = df_coordenadas_filtrado['acidentes'].apply(definir_cor)    
    df_coordenadas_filtrado['tamanho'] = df_coordenadas_filtrado['acidentes'].apply(definir_tamanho)
    
    # Criar duas colunas para colocar os componentes lado a lado
    col1, col2 = st.columns([8,2])
    
    # Adicionar o gráfico à primeira coluna
    with col1:

        st.map(df_coordenadas_filtrado,
            latitude='latitude',
            longitude='longitude',
            size='tamanho',
            color='cor',
            use_container_width=False)

    with col2:

        # Conteúdo HTML das legendas
        # solid
        legendas = ['<br><br>', 
                    '<span style="display:inline-block;width:20px;height:20px;border-radius:50%;background:#ffffcc;margin-right:5px;"></span> Entre  1 e  10 acidentes',
                    '<span style="display:inline-block;width:20px;height:20px;border-radius:50%;background:#ffeda0;margin-right:5px;"></span> Entre 11 e  20 acidentes',
                    '<span style="display:inline-block;width:20px;height:20px;border-radius:50%;background:#fed976;margin-right:5px;"></span> Entre 21 e  30 acidentes',
                    '<span style="display:inline-block;width:20px;height:20px;border-radius:50%;background:#feb24c;margin-right:5px;"></span> Entre 31 e  40 acidentes',
                    '<span style="display:inline-block;width:20px;height:20px;border-radius:50%;background:#fd8d3c;margin-right:5px;"></span> Entre 41 e  50 acidentes',
                    '<span style="display:inline-block;width:20px;height:20px;border-radius:50%;background:#fc4e2a;margin-right:5px;"></span> Entre 51 e  60 acidentes',
                    '<span style="display:inline-block;width:20px;height:20px;border-radius:50%;background:#e31a1c;margin-right:5px;"></span> Entre 61 e  70 acidentes',
                    '<span style="display:inline-block;width:20px;height:20px;border-radius:50%;background:#bd0026;margin-right:5px;"></span> Entre 71 e  80 acidentes',
                    '<span style="display:inline-block;width:20px;height:20px;border-radius:50%;background:#800026;margin-right:5px;"></span> 81 acidentes ou mais',                    
                   ]
                
        # Exibir o quadro com as legendas
        st.markdown('<br>'.join(legendas), unsafe_allow_html=True)     

# ==============================================================================  