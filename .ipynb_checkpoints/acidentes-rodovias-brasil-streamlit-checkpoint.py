# =======================================================
# Instalando dependências
# =======================================================
#!pip install vega_datasets

# =======================================================
# Imports
# =======================================================
import pandas as pd
import numpy as np
import streamlit as st
import altair as alt
#import matplotlib.pyplot as plt

from vega_datasets import data

# =======================================================
# Datasets
# =======================================================
df_acidentes_geral_por_uf    = pd.read_csv('acidentes_geral_por_uf.csv', sep=',', encoding="UTF-8") 
df_acidentes_geral_por_tipo  = pd.read_csv('acidentes_geral_por_tipo.csv', sep=',', encoding="UTF-8") 
df_acidentes_geral_por_br    = pd.read_csv('acidentes_geral_por_br.csv', sep=',', encoding="UTF-8") 
df_acidentes_geral_por_causa = pd.read_csv('acidentes_geral_por_causa.csv', sep=',', encoding="UTF-8") 
df_acidentes_geral_por_classificacao = pd.read_csv('acidentes_geral_por_classificacao.csv', sep=',', encoding="UTF-8") 
df_acidentes_geral_por_fasedia = pd.read_csv('acidentes_geral_por_fase_dia.csv', sep=',', encoding="UTF-8") 
df_acidentes_geral_por_condicaometereologica = pd.read_csv('acidentes_geral_por_condicao_metereologica.csv', sep=',', encoding="UTF-8") 

# =======================================================
# Rankings
# =======================================================
df_ranking_uf = pd.read_csv('ranking_acidentes_uf.csv', sep=',', encoding="UTF-8")
df_ranking_tipo = pd.read_csv('ranking_acidentes_tipo.csv', sep=',', encoding="UTF-8")
df_ranking_br = pd.read_csv('ranking_acidentes_br.csv', sep=',', encoding="UTF-8")

# =======================================================
# Funções
# =======================================================
def gera_grafico_barras_horizontal_por_uf(titulo, contagem_por_uf_ano):

  lista_cores = alt.Scale(domain= contagem_por_uf_ano['UF'].unique(),
      range=[
        '#007bff', '#28a745', '#ffc107', '#dc3545', '#6c757d', '#d95b43', '#5bc0de', '#4caf50', '#ffeb3b', '#c497d9',
        '#00BFFF', '#32CD32', '#FF00FF', '#FFA500', '#5A87E8', '#00CED1', '#FF7F50', '#228B22', '#FFD700', '#000080',
        '#FF1493', '#4B0082', '#8A2BE2', '#7FFF00', '#00FFFF', '#008000'
      ])

  chart_uf = alt.Chart(contagem_por_uf_ano).mark_bar().encode(
      y=alt.Y('UF:N', sort='-x', axis=alt.Axis(labelLimit=200)),
      x=alt.X('Qtd:Q', axis=alt.Axis(labelAngle=-45)),
      tooltip=['UF', 'Qtd'],      
      color=alt.Color('UF:N', scale=lista_cores)     

  ).properties(
      title=alt.Title(
        text=titulo  
      ),
      width=800,
      height=600
  ).interactive()

  return chart_uf
# =======================================================
def gera_grafico_barras_horizontal_por_tipo(titulo, contagem_por_tipo_ano):

  lista_cores = alt.Scale(domain=contagem_por_tipo_ano['tipo_acidente'].unique(),
      range=[
        '#007bff', '#28a745', '#ffc107', '#dc3545', '#6c757d', '#d95b43', '#5bc0de', '#4caf50', '#ffeb3b', '#c497d9',
        '#00BFFF', '#32CD32', '#FF00FF', '#FFA500', '#5A87E8', '#00CED1', '#FF7F50', '#228B22', '#FFD700', '#000080',
        '#FF1493', '#4B0082', '#8A2BE2', '#7FFF00', '#00FFFF', '#008000'
      ])

  chart_tipo = alt.Chart(contagem_por_tipo_ano).mark_bar().encode(
      y=alt.Y('tipo_acidente:N', sort='-x', axis=alt.Axis(labelLimit=200)),
      x=alt.X('qtd:Q', axis=alt.Axis(labelAngle=-45)),
      tooltip=['tipo_acidente', 'qtd'],
      color=alt.Color('tipo_acidente:N', scale=lista_cores)

  ).properties(
      title=titulo,
      width=800,
      height=600           
  ).interactive()

  return chart_tipo
# =======================================================
def gera_grafico_barras_horizontal_por_br(titulo, contagem_por_br_ano):

  lista_cores = alt.Scale(domain=contagem_por_br_ano['br'].unique(),
      range=[
        '#007bff', '#28a745', '#ffc107', '#dc3545', '#6c757d', '#d95b43', '#5bc0de', '#4caf50', '#ffeb3b', '#c497d9',
        '#00BFFF', '#32CD32', '#FF00FF', '#FFA500', '#5A87E8', '#00CED1', '#FF7F50', '#228B22', '#FFD700', '#000080',
        '#FF1493', '#4B0082', '#8A2BE2', '#7FFF00', '#00FFFF', '#008000'
      ])

  chart_br = alt.Chart(contagem_por_br_ano).mark_bar().encode(
      y=alt.Y('br:N', sort='-x', axis=alt.Axis(labelLimit=200)),
      x=alt.X('qtd:Q', axis=alt.Axis(labelAngle=-45)),
      tooltip=['br', 'qtd'],
      color=alt.Color('br:N', scale=lista_cores)

  ).properties(
      title=titulo,
      width=800,
      height=600           
  ).interactive()

  return chart_br
# =======================================================
def gera_grafico_barras_horizontal_por_causa(titulo, contagem_por_causa_ano):

  lista_cores = alt.Scale(domain=contagem_por_causa_ano['causa_acidente'].unique(),
      range=[
        '#007bff', '#28a745', '#ffc107', '#dc3545', '#6c757d', '#d95b43', '#5bc0de', '#4caf50', '#ffeb3b', '#c497d9',
        '#00BFFF', '#32CD32', '#FF00FF', '#FFA500', '#5A87E8', '#00CED1', '#FF7F50', '#228B22', '#FFD700', '#000080',
        '#FF1493', '#4B0082', '#8A2BE2', '#7FFF00', '#00FFFF', '#008000'
      ])

  chart = alt.Chart(contagem_por_causa_ano).mark_bar().encode(
      y=alt.Y('causa_acidente:N', sort='-x', axis=alt.Axis(labelLimit=200)),
      x=alt.X('qtd:Q', axis=alt.Axis(labelAngle=-45)),
      tooltip=['causa_acidente', 'qtd'],
      color=alt.Color('causa_acidente:N', scale=lista_cores)

  ).properties(
      title=titulo,
      width=800,
      height=600         
  ).interactive()

  return chart
# =======================================================
def gera_grafico_por_classificacao(titulo, contagem_por_classificacao_ano):

  lista_cores = alt.Scale(domain=contagem_por_classificacao_ano['classificacao_acidente'].unique(),
      range=[
        '#007bff', '#28a745', '#ffc107', '#dc3545', '#6c757d', '#d95b43', '#5bc0de', '#4caf50', '#ffeb3b', '#c497d9',
        '#00BFFF', '#32CD32', '#FF00FF', '#FFA500', '#5A87E8', '#00CED1', '#FF7F50', '#228B22', '#FFD700', '#000080',
        '#FF1493', '#4B0082', '#8A2BE2', '#7FFF00', '#00FFFF', '#008000'
      ])

  chart = alt.Chart(contagem_por_classificacao_ano).mark_bar().encode(
      y=alt.Y('classificacao_acidente:N', sort='-x', axis=alt.Axis(labelLimit=200)),
      x=alt.X('qtd:Q', axis=alt.Axis(labelAngle=-45)),
      tooltip=['classificacao_acidente', 'qtd'],
      color=alt.Color('classificacao_acidente:N', scale=lista_cores)

  ).properties(
      title=titulo,
      width=800,
      height=600         
  ).interactive()

  return chart    
# =======================================================
def gera_grafico_por_fase_dia(titulo, contagem_por_fase_dia):

  lista_cores = alt.Scale(domain=contagem_por_fase_dia['fase_dia'].unique(),
      range=[
        '#007bff', '#28a745', '#ffc107', '#dc3545', '#6c757d', '#d95b43', '#5bc0de', '#4caf50', '#ffeb3b', '#c497d9',
        '#00BFFF', '#32CD32', '#FF00FF', '#FFA500', '#5A87E8', '#00CED1', '#FF7F50', '#228B22', '#FFD700', '#000080',
        '#FF1493', '#4B0082', '#8A2BE2', '#7FFF00', '#00FFFF', '#008000'
      ])

  chart = alt.Chart(contagem_por_fase_dia).mark_bar().encode(
      y=alt.Y('fase_dia:N', sort='-x', axis=alt.Axis(labelLimit=200)),
      x=alt.X('qtd:Q', axis=alt.Axis(labelAngle=-45)),
      tooltip=['fase_dia', 'qtd'],
      color=alt.Color('fase_dia:N', scale=lista_cores)

  ).properties(
      title=titulo,
      width=800,
      height=600         
  ).interactive()

  return chart
# =======================================================
def gera_grafico_por_condicao_metereologica(titulo, contagem_por_condicao_metereologica):

  lista_cores = alt.Scale(domain=contagem_por_condicao_metereologica['condicao_metereologica'].unique(),
      range=[
        '#007bff', '#28a745', '#ffc107', '#dc3545', '#6c757d', '#d95b43', '#5bc0de', '#4caf50', '#ffeb3b', '#c497d9',
        '#00BFFF', '#32CD32', '#FF00FF', '#FFA500', '#5A87E8', '#00CED1', '#FF7F50', '#228B22', '#FFD700', '#000080',
        '#FF1493', '#4B0082', '#8A2BE2', '#7FFF00', '#00FFFF', '#008000'
      ])

  chart = alt.Chart(contagem_por_condicao_metereologica).mark_bar().encode(
      y=alt.Y('condicao_metereologica:N', sort='-x', axis=alt.Axis(labelLimit=200)),
      x=alt.X('qtd:Q', axis=alt.Axis(labelAngle=-45)),
      tooltip=['condicao_metereologica', 'qtd'],
      color=alt.Color('condicao_metereologica:N', scale=lista_cores)

  ).properties(
      title=titulo,
      width=800,
      height=600         
  ).interactive()

  return chart
# =======================================================


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

#meses_selecionados = st.sidebar.multiselect(
#    'Quais meses deseja visualizar?',
#    [OPCAO_TODOS, 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro','Outubro','Novembro','Dezembro'],
#  )

#st.sidebar.write("Meses selecionados:", meses_selecionados)
#print(f'Meses selecionados: {meses_selecionados}')

# Add a slider to the sidebar:
#horario_acidente = st.sidebar.slider(
#    'Horário do acidente:',
#    0, 24, (0, 24)
#)

# Definição de abas
tab01, tab02, tab03, tab04, tab05, tab06, tab07, tab08, tab09, tab10, tab11 = st.tabs(
  [
    #"Acidentes por UF / por Tipo / por BR / por Causa / por Classificação / por Fase do Dia",  
    "Acidentes por Critérios",
    "Ranking por UF", 
    "Ranking por Tipo", 
    "Ranking por BR",
    "Ranking por Classificação",
    "Ranking por Fase do Dia",
    "Mapa de Calor",
    "Mapa Interativo",
    "Scatter Plot",
    "Gráficos de Fluxo",
    "Gráficos de Barras Empilhadas",
  ]
)

# ==============================================================================
with tab01:

    # aba 01
    titulo = f'<h2> Acidentes por UF / por Tipo / por BR / por Causa / por Classificação / por Fase do Dia / por Condição Metereológica '
    st.markdown(titulo, unsafe_allow_html=True)  
    
    # aba 01
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

    # Exibir o gráfico de barras empilhadas
    st.altair_chart(grafico_aba_01)
    st.altair_chart(grafico_aba_02)
    st.altair_chart(grafico_aba_03)
    st.altair_chart(grafico_aba_04)
    st.altair_chart(grafico_aba_05)
    st.altair_chart(grafico_aba_06)
    st.altair_chart(grafico_aba_07)

# ==============================================================================
with tab02:

    # aba 02
    titulo = f'<h2> Ranking dos Acidentes por UF (2007 a 2024)'
    st.markdown(titulo, unsafe_allow_html=True)  
   
    grafico1 = alt.Chart(df_acidentes_geral_por_uf).mark_line(point=True).encode(
        x=alt.X('ano:O', title='Ano'),
        y="rank:O",
        color=alt.Color("UF:N") #.scale(scheme='category20b')
    ).transform_window(
        rank="rank()",
        sort=[alt.SortField("Qtd", order="descending")],
        groupby=["ano"]
    ).properties(
        title="Ranking das 10 UFs com mais Acidentes (2007 a 2024)",
        width=800,
        height=600,
    )

    st.altair_chart(grafico1)
    
    # Criar o gráfico de linhas interativo
    grafico2 = alt.Chart(df_acidentes_geral_por_uf).mark_line(point=True).encode(
      x=alt.X('ano:N', axis=alt.Axis(title='Ano')),
      y=alt.Y('Qtd:Q', axis=alt.Axis(title='Quantidade de Acidentes')),
      color='UF:N',
      tooltip=['UF', 'Qtd', 'ano']
    ).properties(
      title='Evolução da Quantidade de Acidentes por UF  (2007 a 2024)',
      width=800, height=600
    ).add_selection(
      alt.selection_single(fields=['ano'], bind='legend')
    ).interactive()
    
    st.altair_chart(grafico2)

# ==============================================================================
with tab03:

    # aba 03
    titulo = f'<h2> Ranking dos Acidentes por Tipo (2007 e 2024)'
    st.markdown(titulo, unsafe_allow_html=True)   
   
    grafico1 = alt.Chart(df_acidentes_geral_por_tipo).mark_line(point=True).encode(
        x=alt.X('ano:O', title='Ano'),
        y="rank:O",
        color=alt.Color("tipo_acidente:N")
    ).transform_window(
        rank="rank()",
        sort=[alt.SortField("qtd", order="descending")],
        groupby=["ano"]
    ).properties(
        title="Ranking dos Tipos de Acidentes (2007 a 2024)",
        width=800,
        height=600,
    )

    st.altair_chart(grafico1)   
    
    # Criar o gráfico de linhas interativo
    grafico2 = alt.Chart(df_acidentes_geral_por_tipo).mark_line(point=True).encode(
      x=alt.X('ano:N', axis=alt.Axis(title='Ano')),
      y=alt.Y('qtd:Q', axis=alt.Axis(title='Quantidade de Acidentes')),
      color='tipo_acidente:N',
      tooltip=['tipo_acidente', 'qtd', 'ano']
    ).properties(
      title='Evolução da Quantidade de Acidentes por Tipo  (2007 a 2024)',
      width=800, height=600
    ).add_selection(
      alt.selection_single(fields=['ano'], bind='legend')
    ).interactive()
    
    st.altair_chart(grafico2)
    
# ==============================================================================
with tab04:

    # aba 04
    titulo = f'<h2> Ranking dos Acidentes por BR (2007 e 2024)'
    st.markdown(titulo, unsafe_allow_html=True)
  
    grafico_ranking_br_01 = alt.Chart(df_acidentes_geral_por_br).mark_line(point=True).encode(
        x=alt.X('ano:O', title='Ano'),
        y="rank:O",
        color=alt.Color("br:N")
    ).transform_window(
        rank="rank()",
        sort=[alt.SortField("qtd", order="descending")],
        groupby=["ano"]
    ).properties(
        title="Ranking das 20 BRs com mais acidentes  (2007 a 2024)",
        width=800,
        height=600,
    )

    st.altair_chart(grafico_ranking_br_01)
   
    # Criar o gráfico de linhas interativo
    grafico_ranking_br_02 = alt.Chart(df_acidentes_geral_por_br).mark_line(point=True).encode(
      x=alt.X('ano:N', axis=alt.Axis(title='Ano')),
      y=alt.Y('qtd:Q', axis=alt.Axis(title='Quantidade de Acidentes')),
      color='br:N',
      tooltip=['br', 'qtd', 'ano']
    ).properties(
      title='Evolução da Quantidade de Acidentes por BR (2007-2023)',
      width=800, height=600
    ).add_selection(
      alt.selection_single(fields=['ano'], bind='legend')
    ).interactive()
    
    st.altair_chart(grafico_ranking_br_02)

# ==============================================================================
with tab05:

    # aba 05
    titulo = f'<H2> Ranking por Classificação'
    st.markdown(titulo, unsafe_allow_html=True)

    grafico_ranking_classif_01 = alt.Chart(df_acidentes_geral_por_classificacao).mark_line(point=True).encode(
        x=alt.X('ano:O', title='Ano'),
        y="rank:O",
        color=alt.Color("classificacao_acidente:N")
    ).transform_window(
        rank="rank()",
        sort=[alt.SortField("qtd", order="descending")],
        groupby=["ano"]
    ).properties(
        title="Ranking das Classificações dos Acidentes (2007 a 2024)",
        width=800, height=600,
    )

    st.altair_chart(grafico_ranking_classif_01)
    
    # Criar o gráfico de linhas interativo
    grafico_ranking_classif_02 = alt.Chart(df_acidentes_geral_por_classificacao).mark_line(point=True).encode(
      x=alt.X('ano:N', axis=alt.Axis(title='Ano')),
      y=alt.Y('qtd:Q', axis=alt.Axis(title='Quantidade de Acidentes')),
      color='classificacao_acidente:N',
      tooltip=['classificacao_acidente', 'qtd', 'ano']
        
    ).properties(
      title='Evolução da Quantidade de Acidentes por Classificação (2007-2024)',
      width=800, height=600
        
    ).add_selection(
      alt.selection_single(fields=['ano'], bind='legend')
        
    ).interactive()
    
    st.altair_chart(grafico_ranking_classif_02)
    
# ==============================================================================
with tab06:
    
    # aba 06
    titulo = f'<H2> Ranking por Fase do Dia'
    st.markdown(titulo, unsafe_allow_html=True)

    grafico_ranking_fasedia_01 = alt.Chart(df_acidentes_geral_por_fasedia).mark_line(point=True).encode(
        x=alt.X('ano:O', title='Ano'),
        y="rank:O",
        color=alt.Color("fase_dia:N")
    ).transform_window(
        rank="rank()",
        sort=[alt.SortField("qtd", order="descending")],
        groupby=["ano"]
    ).properties(
        title="Ranking das Fases dos Acidentes (2007 a 2024)",
        width=800, height=600,
    )

    st.altair_chart(grafico_ranking_fasedia_01)
    
    # Criar o gráfico de linhas interativo
    grafico_ranking_fasedia_02 = alt.Chart(df_acidentes_geral_por_fasedia).mark_line(point=True).encode(
      x=alt.X('ano:N', axis=alt.Axis(title='Ano')),
      y=alt.Y('qtd:Q', axis=alt.Axis(title='Quantidade de Acidentes')),
      color='fase_dia:N',
      tooltip=['fase_dia', 'qtd', 'ano']
        
    ).properties(
      title='Evolução da Quantidade de Acidentes por Fase do Dia (2007-2024)',
      width=800, height=600
        
    ).add_selection(
      alt.selection_single(fields=['ano'], bind='legend')
        
    ).interactive()
    
    st.altair_chart(grafico_ranking_fasedia_02)

    
# ==============================================================================
with tab07:

    # aba 07
    titulo = f'https://altair-viz.github.io/gallery/annual_weather_heatmap.html'
    st.markdown(titulo, unsafe_allow_html=True)  

    source = data.seattle_weather()
    
    grafico = alt.Chart(source, title="Daily Max Temperatures (C) in Seattle, WA").mark_rect().encode(
        alt.X("date(date):O").title("Day").axis(format="%e", labelAngle=0),
        alt.Y("month(date):O").title("Month"),
        alt.Color("max(temp_max)").title(None),
        tooltip=[
            alt.Tooltip("monthdate(date)", title="Date"),
            alt.Tooltip("max(temp_max)", title="Max Temp"),
        ],
    ).configure_view(
        step=13,
        strokeWidth=0
    ).configure_axis(
        domain=False
    )
    
    st.altair_chart(grafico)

    df_envolvidos = pd.read_csv('correlacao_classificacao_2023.csv')
    
    # Define os dados
    dados = df_envolvidos.set_index('classificacao').T.reset_index().melt(id_vars='index', var_name='classificacao', value_name='value')

    # Cria o gráfico de calor
    heatmap = alt.Chart(dados).mark_rect().encode(
        x=alt.X('index:O', title=None, axis=alt.Axis(orient='top')),  # Define a orientação do eixo x como 'top'
        y=alt.Y('classificacao:O', title=None),
        color=alt.Color('value:Q'),
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
        title=f'Mapa de Calor dos Envolvidos nos acidentes (aaa)'
    )

    # Exibe o gráfico    
    st.altair_chart(heatmap_with_text)

# ==============================================================================
with tab08:

    # aba 08
    titulo = f'https://altair-viz.github.io/gallery/airport_connections.html'
    st.markdown(titulo, unsafe_allow_html=True)  
    
    # Since these data are each more than 5,000 rows we'll import from the URLs
    airports = data.airports.url
    flights_airport = data.flights_airport.url
    
    states = alt.topo_feature(data.us_10m.url, feature="states")
    
    # Create pointerover selection
    select_city = alt.selection_point(
        on="pointerover", nearest=True, fields=["origin"], empty=False
    )
    
    # Define which attributes to lookup from airports.csv
    lookup_data = alt.LookupData(
        airports, key="iata", fields=["state", "latitude", "longitude"]
    )
    
    background = alt.Chart(states).mark_geoshape(
        fill="lightgray",
        stroke="white"
    ).properties(
        width=750,
        height=500
    ).project("albersUsa")
    
    connections = alt.Chart(flights_airport).mark_rule(opacity=0.35).encode(
        latitude="latitude:Q",
        longitude="longitude:Q",
        latitude2="lat2:Q",
        longitude2="lon2:Q"
    ).transform_lookup(
        lookup="origin",
        from_=lookup_data
    ).transform_lookup(
        lookup="destination",
        from_=lookup_data,
        as_=["state", "lat2", "lon2"]
    ).transform_filter(
        select_city
    )
    
    points = alt.Chart(flights_airport).mark_circle().encode(
        latitude="latitude:Q",
        longitude="longitude:Q",
        size=alt.Size("routes:Q").legend(None).scale(range=[0, 1000]),
        order=alt.Order("routes:Q").sort("descending"),
        tooltip=["origin:N", "routes:Q"]
    ).transform_aggregate(
        routes="count()",
        groupby=["origin"]
    ).transform_lookup(
        lookup="origin",
        from_=lookup_data
    ).transform_filter(
        (alt.datum.state != "PR") & (alt.datum.state != "VI")
    ).add_params(
        select_city
    )
    
    grafico = (background + connections + points).configure_view(stroke=None)
    
    st.altair_chart(grafico)

# ==============================================================================
with tab09:

    # aba 09
    titulo = f'https://altair-viz.github.io/gallery/scatter_matrix.html'
    st.markdown(titulo, unsafe_allow_html=True)  
    
    source = data.cars()
    
    grafico = alt.Chart(source).mark_circle().encode(
        alt.X(alt.repeat("column"), type='quantitative'),
        alt.Y(alt.repeat("row"), type='quantitative'),
        color='Origin:N'
    ).properties(
        width=150,
        height=150
    ).repeat(
        row=['Horsepower', 'Acceleration', 'Miles_per_Gallon'],
        column=['Miles_per_Gallon', 'Acceleration', 'Horsepower']
    ).interactive()

    st.altair_chart(grafico)
    
# ==============================================================================
with tab10:

    # aba 10
    titulo = f'<H2> Gráficos de Fluxo'
    st.markdown(titulo, unsafe_allow_html=True)

    grafico1 = alt.Chart(df_acidentes_geral_por_tipo).mark_area().encode(
        alt.X('ano:Q').axis(domain=False, tickSize=0),
        alt.Y('sum(qtd):Q').stack('center').axis(None),
        alt.Color('tipo_acidente:N').scale(scheme='category20b')
    ).properties(
      title='Gráfico de Fluxo - Tipos de Acidentes (2007 a 2024)',
      width=800, height=600
            
    ).interactive()

    st.altair_chart(grafico1)
    
# ==============================================================================  
with tab11:
    
    # ==========================================================================
    # Funções da Aba 11 
    # ==========================================================================
    def grafico_barras_empilhadas_por_uf(titulo, df):
        grafico = alt.Chart(df).mark_bar(width=20).encode(
            x='ano',
            y='sum(Qtd)',
            color='UF'
        ).properties(
              title=titulo,
              width=800, height=600
        ).interactive()   
        
        return grafico
    # ==========================================================================
    def grafico_barras_empilhadas_por_br(titulo, df):
        grafico = alt.Chart(df).mark_bar(width=20).encode(
            x='ano',
            y='sum(qtd)',
            color='br:N'
        ).properties(
              title=titulo,
              width=800, height=600
        ).interactive()   

        return grafico
    # ==========================================================================
    def grafico_barras_empilhadas_por_tipo(titulo, df):

        grafico = alt.Chart(df).mark_bar(width=20).encode(
            x='ano',
            y='sum(qtd)',
            color='tipo_acidente'
        ).properties(
              title=titulo,
              width=800, height=600
        ).interactive()   
    
        return grafico
    # ==========================================================================
    def grafico_barras_empilhadas_por_causa(titulo, df):
            
        grafico = alt.Chart(df).mark_bar(width=20).encode(
            x='ano',
            y='sum(qtd)',
            color='causa_acidente'
        ).properties(
              title=titulo,
              width=800, height=600
        ).interactive()   

        return grafico
    # ==========================================================================
            
    # aba 06
    titulo = f'<H2> Gráficos de Barras Empilhadas'
    st.markdown(titulo, unsafe_allow_html=True)    

    # aba 06
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

    else:
      grafico1 = grafico_barras_empilhadas_por_uf('Barras Empilhadas por UF (2007 a 2024)', df_acidentes_geral_por_uf)            
      grafico2 = grafico_barras_empilhadas_por_br('Barras Empilhadas por BR (2007 a 2024)', df_acidentes_geral_por_br)  
      grafico3 = grafico_barras_empilhadas_por_tipo('Barras Empilhadas por Tipos de Acidentes (2007-2024)', df_acidentes_geral_por_tipo)    
      grafico4 = grafico_barras_empilhadas_por_causa('Barras Empilhadas por Causa de Acidentes (2007-2024)', df_acidentes_geral_por_causa)      
    
    st.altair_chart(grafico1)                  
    st.altair_chart(grafico2)     
    st.altair_chart(grafico3)        
    st.altair_chart(grafico4)           

# ==============================================================================
