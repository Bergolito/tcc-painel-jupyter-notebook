# =======================================================
# Imports
# =======================================================
import pandas as pd
import numpy as np
import streamlit as st
import altair as alt

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
tab01, tab02, tab03, tab04, tab05, tab06, tab07, tab08, tab09, tab10, tab11, tab12, tab13, tab14 = st.tabs(
  [
    #"Acidentes por UF / por Tipo / por BR / por Causa / por Classificação / por Fase do Dia",  
    "Acidentes por Critérios",
    "Ranking UF", 
    "Ranking Tipo", 
    "Ranking BR",
    "Ranking Classificação",
    "Ranking Fase do Dia",
    "Mapa de Calor",
    "Mapa Interativo",
    "Scatter Plot",
    "Gráficos Fluxo",
    "Gráficos Barras Empilhadas",
    "Gráficos Boxplots",
    "Mapa do Brasil",
    "Teste Map",
  ]
)

# ==============================================================================
with tab01:

    # =======================================================
    # Funções da aba 01
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
    # aba 01
    # =======================================================
    titulo = f'<h2> Acidentes por UF / por Tipo / por BR / por Causa / por Classificação / por Fase do Dia / por Condição Metereológica'
    st.markdown(titulo, unsafe_allow_html=True)  
    
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
    titulo = f'<H2> Gráficos de Fluxo por UF / por Tipo / por BR / por Causa / por Classificação'
    st.markdown(titulo, unsafe_allow_html=True)

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
    
    st.altair_chart(grafico1)
    st.altair_chart(grafico2)
    st.altair_chart(grafico3)
    st.altair_chart(grafico4)
    st.altair_chart(grafico5)
    
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
with tab12:

    # aba 10
    titulo = f'<H2> Distribuição de Acidentes por UF / por Tipo / por BR / por Classificação / por Fase do Dia / por Condição Metereológica '
    st.markdown(titulo, unsafe_allow_html=True)

    grafico01 = alt.Chart(df_acidentes_geral_por_uf).mark_boxplot(extent='min-max').encode(
        x='UF:N',
        y='Qtd:Q'        
    ).properties(
        width=800,
        height=600,
        title='Distribuição de Acidentes por UF (2007 a 2024)'
    )

    grafico02 = alt.Chart(df_acidentes_geral_por_tipo).mark_boxplot(extent='min-max').encode(
        x='tipo_acidente:N',
        y='qtd:Q'
    ).properties(
        width=800,
        height=600,
        title='Distribuição de Acidentes por Tipo (2007 a 2024)'
    )

    grafico03 = alt.Chart(df_acidentes_geral_por_br).mark_boxplot(extent='min-max').encode(
        x='br:N',
        y='qtd:Q'
    ).properties(
        width=800,
        height=600,
        title='Distribuição de Acidentes por BR (2007 a 2024)'
    )

    grafico04 = alt.Chart(df_acidentes_geral_por_classificacao).mark_boxplot(extent='min-max').encode(
        x='classificacao_acidente:N',
        y='qtd:Q'
    ).properties(
        width=800,
        height=600,
        title='Distribuição de Acidentes por Classificação (2007 a 2024)'
    )

    grafico05 = alt.Chart(df_acidentes_geral_por_causa).mark_boxplot(extent='min-max').encode(
        x='causa_acidente:N',
        y='qtd:Q'
    ).properties(
        width=800,
        height=600,
        title='Distribuição de Acidentes por Causa (2007 a 2024)'
    )

    grafico06 = alt.Chart(df_acidentes_geral_por_fasedia).mark_boxplot(extent='min-max').encode(
        x='fase_dia:N',
        y='qtd:Q'
    ).properties(
        width=800,
        height=600,
        title='Distribuição de Acidentes por Fase do Dia (2007 a 2024)'
    )

    grafico07 = alt.Chart(df_acidentes_geral_por_condicaometereologica).mark_boxplot(extent='min-max').encode(
        x='condicao_metereologica:N',
        y='qtd:Q'
    ).properties(
        width=800,
        height=600,
        title='Distribuição de Acidentes por Condição Metereológica (2007 a 2024)'
    )
    
    st.altair_chart(grafico01)
    st.altair_chart(grafico02)
    st.altair_chart(grafico03)
    st.altair_chart(grafico04)
    st.altair_chart(grafico05)
    st.altair_chart(grafico06)
    st.altair_chart(grafico07)
# ==============================================================================
with tab13:
    
    import streamlit as st
    import altair as alt
    import pandas as pd
    import numpy as np
    from urllib.request import urlopen
    import json
    
    #Layout da página
    #st.set_page_config(
    #    page_title="Título da Página",
    #    layout="wide",
    #    initial_sidebar_state="expanded",
    #    page_icon = "🗳️"
    #)
    #alt.themes.enable("dark")
    
    ##########################################################################################
    ##                                     Funções úteis                                    ##
    ##########################################################################################
    #Baixa os arquivos do drive e converte em dataframe
    def get_df(url):
        url='https://drive.google.com/uc?id=' + url.split('/')[-2]
        return pd.read_csv(url, sep=",")
    
    @st.cache_data
    def get_estados():    
        #df_estados= get_df("https://drive.google.com/file/d/1qPMUuto04pQVnxaayg7Ubs9ZlxfiDwcX/view?usp=sharing")
        df_estados= pd.read_csv("mapa_brasil/estados.csv", sep=",")
        df_estados.rename(columns={"nome":"NM_UF"}, inplace=True)
        return df_estados
    
    @st.cache_data    
    def get_municipios_ibge():
        #df_municipios_ibge = get_df("https://drive.google.com/file/d/1gcbOM3S0un4xTUxgXxp0be1MzyFHWRoi/view?usp=sharing")
        df_municipios_ibge = pd.read_csv("mapa_brasil/municipios_ibge_lat_long.csv", sep=",")
        return df_municipios_ibge
    
    @st.cache_data    
    def get_municipios_tse():
        #df_municipios_tse = get_df("https://drive.google.com/file/d/1NJvtXR9BBMSi-Y5511RS5nObbgLQdsSm/view?usp=sharing")
        df_municipios_tse = pd.read_csv("mapa_brasil/municipios_brasileiros_tse.csv", sep=",")
        return df_municipios_tse
    ##########################################################################################
    ##                               Carga de dados regionais                               ##
    ##########################################################################################
    #Estados brasileiros
    df_estados = get_estados()
    
    #Municípios código tse
    df_municipios_tse = get_municipios_tse()
    
    #municípios do ibge
    df_municipios_ibge = get_municipios_ibge()
    df_municipios = pd.merge(df_municipios_tse, df_municipios_ibge, on=['codigo_ibge'], how="inner")
    df_municipios = df_municipios[['codigo_tse','nome_municipio','uf','capital_x','latitude','longitude']]
    
    #apenas as capitais 
    df_capitais= pd.merge(
        df_municipios_tse, 
        df_municipios_ibge[df_municipios_ibge['capital'] == 1], 
        on=['codigo_ibge'], 
        how="inner")[['uf','codigo_tse','nome_municipio','latitude','longitude']]
    
    
    @st.cache_data
    def plot_br_map(title="Título do Mapa"):
        map = alt.Chart(alt.Data(
                url="https://raw.githubusercontent.com/giuliano-macedo/geodata-br-states/main/geojson/br_states.json",
                format=alt.DataFormat(property='features')
            )) \
        .mark_geoshape(
            stroke='#fff', strokeWidth=1.5
        ).project(
            type="equirectangular"  
        ).properties(
            title="Título do meu mapa",
            width=600,
            height=500
        )
        
        text_est = alt.Chart(df_capitais) \
            .mark_text(
                dx=alt.expr(
                    alt.expr.if_(
                        alt.datum.uf == 'PA', -50, 
                            alt.expr.if_(alt.datum.uf == 'RO',10,
                                alt.expr.if_(alt.datum.uf == 'AC',-40,
                                    alt.expr.if_(alt.datum.uf == 'AM',-60,
                                        alt.expr.if_(alt.datum.uf == 'RR',-5,                                            
                                            alt.expr.if_(alt.datum.uf == 'AP',-10,
                                                alt.expr.if_(alt.datum.uf == 'MT',0,
                                                    alt.expr.if_(alt.datum.uf == 'MA',-10,
                                                        alt.expr.if_(alt.datum.uf == 'PI',8,
                                                            alt.expr.if_(alt.datum.uf == 'CE',-12,
                                                                alt.expr.if_(alt.datum.uf == 'RN',-20,
                                                                    alt.expr.if_(alt.datum.uf == 'PB',-30,
                                                                        alt.expr.if_(alt.datum.uf == 'PE',-40,
                                                                            alt.expr.if_(alt.datum.uf == 'AL',14,
                                                                                alt.expr.if_(alt.datum.uf == 'SE',15,
                                                                                    alt.expr.if_(alt.datum.uf == 'BA',-40,
                                                                                        alt.expr.if_(alt.datum.uf == 'TO',0,
                                                                                            alt.expr.if_(alt.datum.uf == 'GO',-15,
                                                                                                alt.expr.if_(alt.datum.uf == 'DF',5,
                                                                                                    alt.expr.if_(alt.datum.uf == 'RJ',10,
                                                                                                        alt.expr.if_(alt.datum.uf == 'SP',-25,
                                                                                                            alt.expr.if_(alt.datum.uf == 'PR',-25,
                                                                                                                alt.expr.if_(alt.datum.uf == 'SC',-25,
                                                                                                                    alt.expr.if_(alt.datum.uf == 'RS',-20,-5)
                                                                                                            )
                                                                                                        )
                                                                                                    )
                                                                                                )
                                                                                            )
                                                                                        )
                                                                                    )
                                                                                )
                                                                            )
                                                                        )
                                                                    )
                                                                )
                                                            )
                                                        )
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                ), 
                dy=alt.expr(
                    alt.expr.if_(alt.datum.uf == 'PA', 50, 
                        alt.expr.if_(alt.datum.uf == 'RO',30,
                            alt.expr.if_(alt.datum.uf == 'AC',-15,
                                alt.expr.if_(alt.datum.uf == 'AM',10,
                                    alt.expr.if_(alt.datum.uf == 'RR',20,
                                        alt.expr.if_(alt.datum.uf == 'AP',-15,
                                            alt.expr.if_(alt.datum.uf == 'MT',-30,
                                                alt.expr.if_(alt.datum.uf == 'MA',30,
                                                    alt.expr.if_(alt.datum.uf == 'PI',30,
                                                        alt.expr.if_(alt.datum.uf == 'CE',20,
                                                            alt.expr.if_(alt.datum.uf == 'RN',-2,
                                                                alt.expr.if_(alt.datum.uf == 'PB',0,
                                                                    alt.expr.if_(alt.datum.uf == 'PE',5,
                                                                        alt.expr.if_(alt.datum.uf == 'AL',0,
                                                                            alt.expr.if_(alt.datum.uf == 'SE',2,
                                                                                alt.expr.if_(alt.datum.uf == 'BA',0,
                                                                                    alt.expr.if_(alt.datum.uf == 'TO',-10,
                                                                                        alt.expr.if_(alt.datum.uf == 'GO',-10,
                                                                                            alt.expr.if_(alt.datum.uf == 'DF',-10,
                                                                                                alt.expr.if_(alt.datum.uf == 'SC',-5,
                                                                                                    alt.expr.if_(alt.datum.uf == 'RS',-10,
                                                                                                        alt.expr.if_(alt.datum.uf == 'MS',-17,-5)
                                                                                                    )
                                                                                                )
                                                                                            )
                                                                                        )
                                                                                    )
                                                                                )
                                                                            )
                                                                        )
                                                                    )            
                                                                )
                                                            )
                                                        )
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                ), 
                fontSize=12
            ) \
            .encode(
                latitude="latitude:Q",
                longitude="longitude:Q",
                text="uf:N"
            )
        
        text_munic = alt.Chart(df_capitais) \
            .mark_text(dx=-6, dy=8, fontSize=7) \
            .encode(
                latitude="latitude:Q",
                longitude="longitude:Q",
                text="nome_municipio:N"
            )
        
        point = alt.Chart(df_capitais) \
            .mark_circle(dx=-5, size=25) \
            .encode(        
                latitude="latitude:Q",
                longitude="longitude:Q",
                color=alt.value("orange"),
            )
        
        return (map + text_est + text_munic + point).configure_title(
            fontSize=15
        )
    
    ##########################################################################################
    ##                                       Layout                                         ##
    ##########################################################################################
    st.title("Side Bar")
    
    topo = st.columns(1)
    with topo[0]:
        st.altair_chart(plot_br_map(title="Título do Mapa"), use_container_width=True)


# ==============================================================================  
with tab14:    

    # ver https://folium.streamlit.app/draw_support
    # Função para mapear os valores de acidentes para cores
    def definir_cor(acidentes):
        if 1 <= acidentes <= 10:
            return '#00FF00'  # Verde
        elif 11 <= acidentes <= 20:
            return '#FFFF00'  # Amarelo
        else:
            return '#FF0000'  # Vermelho

    ano_selecionado = '2024'
    if ano_selecionado == OPCAO_TODOS:
       coluna_dados = 'acidentes_total'
    else:
       coluna_dados = f'acidentes_{ano_selecionado}'

    # Exibir o quadro com as legendas
    titulo = f'<H2>Acidentes reportados na BR 101 em ({ano_selecionado})'
    st.markdown(titulo, unsafe_allow_html=True)

    # Conteúdo HTML das legendas
    legendas = ['<br><br><span style="display:inline-block;width:20px;height:20px;border-radius:50%;background:#00FF00;margin-right:5px;"></span> Entre 1 e 10 acidentes',
                '<span style="display:inline-block;width:20px;height:20px;border-radius:50%;background:#FFFF00;margin-right:5px;"></span> Entre 11 e 20 acidentes',
                '<span style="display:inline-block;width:20px;height:20px;border-radius:50%;background:#FF0000;margin-right:5px;"></span> Mais de 20 acidentes']

    # Criar duas colunas para colocar os componentes lado a lado
    col1, col2 = st.columns([8,2])

    # Adicionar o gráfico à primeira coluna
    with col1:

        df_pontos_2024 = pd.read_csv('geo/acidentes_localizacao_processado_2024.csv', sep=';', decimal='.')   
        df_pontos_2024_filtrado = df_pontos_2024[(df_pontos_2024['br'] == 101)]       
        df_pontos_2024_filtrado['cor'] = df_pontos_2024_filtrado[coluna_dados].apply(definir_cor)

        st.map(df_pontos_2024_filtrado,
            latitude='latitude',
            longitude='longitude',
            size=coluna_dados,
            color='cor',
            use_container_width=False)

    with col2:

        # Exibir o quadro com as legendas
        st.markdown('<br>'.join(legendas), unsafe_allow_html=True)
    

    