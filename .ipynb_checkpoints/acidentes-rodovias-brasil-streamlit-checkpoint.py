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
import matplotlib.pyplot as plt

from vega_datasets import data


# =======================================================
# Datasets
# =======================================================
df_acidentes_geral_ufs       = pd.read_csv('acidentes_geral_ufs.csv', sep=',', encoding="UTF-8") 
df_acidentes_geral_por_tipo  = pd.read_csv('acidentes_geral_por_tipo.csv', sep=',', encoding="UTF-8") 
df_acidentes_geral_por_br    = pd.read_csv('acidentes_geral_por_br.csv', sep=',', encoding="UTF-8") 
df_acidentes_geral_por_causa = pd.read_csv('acidentes_geral_por_causa.csv', sep=',', encoding="UTF-8") 

# =======================================================
# Rankings
# =======================================================
df_ranking_uf = pd.read_csv('ranking_acidentes_uf.csv', sep=',', encoding="UTF-8")
df_ranking_tipo = pd.read_csv('ranking_acidentes_tipo.csv', sep=',', encoding="UTF-8")
df_ranking_br = pd.read_csv('ranking_acidentes_br.csv', sep=',', encoding="UTF-8")

# =======================================================
# Funções
# =======================================================
def agrupamento_acidentes_por_ano_por_uf(df):
  contagem_por_uf = df['uf'].value_counts().reset_index()
  contagem_por_uf.columns = ['UF', 'Qtd']
  return contagem_por_uf
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
def contagem_por_tipo_acidente(df_ocorrencia_acidentes):
  contagem_por_tipo = df_ocorrencia_acidentes['tipo_acidente'].value_counts().reset_index(name='qtd').rename(columns={'index': 'UF'})
  contagem_por_tipo.columns = ['tipo_acidente', 'qtd']

  return contagem_por_tipo
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
      #title=f'Acidentes por Tipo no Ano de {ano}',
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
      #title=f'Acidentes por BR no Ano de {ano}'
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
def agrupamento_acidentes_por_ano_por_uf(df):
  contagem_por_uf = df['uf'].value_counts().reset_index()
  contagem_por_uf.columns = ['UF', 'Qtd']
  return contagem_por_uf
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

meses_selecionados = st.sidebar.multiselect(
    'Quais meses deseja visualizar?',
    [OPCAO_TODOS, 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro','Outubro','Novembro','Dezembro'],
  )

#st.sidebar.write("Meses selecionados:", meses_selecionados)
#print(f'Meses selecionados: {meses_selecionados}')

# Add a slider to the sidebar:
horario_acidente = st.sidebar.slider(
    'Horário do acidente:',
    0, 24, (0, 24)
)

# Definição de abas
tab01, tab02, tab03, tab04, tab05, tab06, tab07, tab08, tab09 = st.tabs(
  [
    "Acidentes por UF / por Tipo / por BR / por Causa",
    "Ranking por UF", 
    "Ranking por Tipo", 
    "Ranking por BR",
    "Streamgraph",
    "Stacked Bar Chart",
    "Mapa de Calor",
    "Mapa Interativo",
    "Scatter Plot"  
  ]
)

# ==============================================================================
with tab01:

    # aba 01
    if ano_selecionado != OPCAO_TODOS:
      df_filtrado_uf = df_acidentes_geral_ufs[(df_acidentes_geral_ufs[COLUNA_ANO] == int(ano_selecionado))]
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
        
    else:
      titulo = f'Acidentes por UF (Geral)'    
      grafico_aba_01 = gera_grafico_barras_horizontal_por_uf(titulo, df_acidentes_geral_ufs)

      titulo = f'Acidentes por Tipo (Geral)'    
      grafico_aba_02 = gera_grafico_barras_horizontal_por_tipo(titulo, df_acidentes_geral_por_tipo)

      titulo = f'Acidentes por BR (Geral)'    
      grafico_aba_03 = gera_grafico_barras_horizontal_por_br(titulo, df_acidentes_geral_por_br)

      titulo = f'Acidentes por Causa (Geral)'    
      grafico_aba_04 = gera_grafico_barras_horizontal_por_causa(titulo, df_acidentes_geral_por_causa)
    
    # Exibir o gráfico de barras empilhadas
    st.altair_chart(grafico_aba_01)
    st.altair_chart(grafico_aba_02)
    st.altair_chart(grafico_aba_03)
    st.altair_chart(grafico_aba_04)

# ==============================================================================
with tab02:

    # aba 02
    titulo = f'<h2> Ranking dos Acidentes por UF (2007 a 2024)'
    st.markdown(titulo, unsafe_allow_html=True)  
   
    grafico1 = alt.Chart(df_acidentes_geral_ufs).mark_line(point=True).encode(
        x=alt.X('ano:O', title='Ano'),
        y="rank:O",
        color=alt.Color("UF:N")
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

    # Ordenar o DataFrame por ano
    df_ordenado_ano = df_ranking_uf.sort_values('ano')
    
    # Criar o gráfico de linhas interativo
    grafico2 = alt.Chart(df_acidentes_geral_ufs).mark_line(point=True).encode(
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
   
    # Ordenar o DataFrame por ano
    df_ordenado_ano = df_ranking_uf.sort_values('ano')
    
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

    # Ordenar o DataFrame por ano
    df_ordenado_ano = df_ranking_br.sort_values('ano')
    
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
    titulo = f'https://altair-viz.github.io/gallery/streamgraph.html'
    st.markdown(titulo, unsafe_allow_html=True)

    source = data.unemployment_across_industries.url
    
    grafico = alt.Chart(source).mark_area().encode(
        alt.X('yearmonth(date):T').axis(format='%Y', domain=False, tickSize=0),
        alt.Y('sum(count):Q').stack('center').axis(None),
        alt.Color('series:N').scale(scheme='category20b')
    ).interactive()

    st.altair_chart(grafico)

# ==============================================================================
with tab06:

    # aba 06
    titulo = f'https://altair-viz.github.io/gallery/stacked_bar_chart.html'
    st.markdown(titulo, unsafe_allow_html=True)    
   
    source = data.barley()
    
    grafico = alt.Chart(source).mark_bar().encode(
        x='variety',
        y='sum(yield)',
        color='site'
    )

    st.altair_chart(grafico)

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