# =======================================================
# Imports
# =======================================================
import pandas as pd
import numpy as np
import streamlit as st
import altair as alt
import numpy as np
import geopandas as gpd

from vega_datasets import data

# =======================================================
# Constantes
# =======================================================

lista_cores_graficos = [
    '#007bff', '#28a745', '#ffc107', '#dc3545', '#6c757d', '#d95b43', '#5bc0de', '#4caf50', '#ffeb3b', '#c497d9',
    '#00BFFF', '#32CD32', '#FF00FF', '#FFA500', '#5A87E8', '#00CED1', '#FF7F50', '#228B22', '#FFD700', '#000080',
    '#FF1493', '#4B0082', '#8A2BE2', '#7FFF00', '#00FFFF', '#008000'
]

# =======================================================
# Gráficos
# =======================================================
def gera_grafico_barras_horizontal_por_uf(titulo, contagem_por_uf_ano):

    lista_cores = alt.Scale(domain=contagem_por_uf_ano['uf'].unique(), range=lista_cores_graficos)

    chart_uf = alt.Chart(contagem_por_uf_ano).mark_bar().encode(
        y=alt.Y('uf:N', title='Unidade Federativa (UF)', sort='-x', axis=alt.Axis(labelLimit=200)),
        x=alt.X('qtd:Q', title='Quantidade de Acidentes', axis=alt.Axis(labelAngle=-45)),
        tooltip=['uf', 'qtd'],      
        color=alt.Color('uf:N', scale=lista_cores)     

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

    lista_cores = alt.Scale(domain=contagem_por_tipo_ano['tipo_acidente'].unique(), range=lista_cores_graficos)    
    
    chart_tipo = alt.Chart(contagem_por_tipo_ano).mark_bar().encode(
        y=alt.Y('tipo_acidente:N', title='Tipos de Acidentes',  sort='-x', axis=alt.Axis(labelLimit=200)),
        x=alt.X('qtd:Q', title='Quantidade de Acidentes', axis=alt.Axis(labelAngle=-45)),
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

    lista_cores = alt.Scale(domain=contagem_por_br_ano['br'].unique(), range=lista_cores_graficos)
                                
    chart_br = alt.Chart(contagem_por_br_ano).mark_bar().encode(
        y=alt.Y('br:N', title='Rodovia Federal (BR)', sort='-x', axis=alt.Axis(labelLimit=200)),
        x=alt.X('qtd:Q', title='Quantidade de Acidentes', axis=alt.Axis(labelAngle=-45)),
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

    lista_cores = alt.Scale(domain=contagem_por_causa_ano['causa_acidente'].unique(), range=lista_cores_graficos)
                                
    chart = alt.Chart(contagem_por_causa_ano).mark_bar().encode(
        y=alt.Y('causa_acidente:N', title='Causas de Acidentes', sort='-x', axis=alt.Axis(labelLimit=200)),
        x=alt.X('qtd:Q', title='Quantidade de Acidentes', axis=alt.Axis(labelAngle=-45)),
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

    lista_cores = alt.Scale(domain=contagem_por_classificacao_ano['classificacao_acidente'].unique(), range=lista_cores_graficos)
                                
    chart = alt.Chart(contagem_por_classificacao_ano).mark_bar().encode(
        y=alt.Y('classificacao_acidente:N',title='Classificações de Acidentes', sort='-x', axis=alt.Axis(labelLimit=200)),
        x=alt.X('qtd:Q', title='Quantidade de Acidentes', axis=alt.Axis(labelAngle=-45)),
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

    lista_cores = alt.Scale(domain=contagem_por_fase_dia['fase_dia'].unique(), range=lista_cores_graficos)
                                
    chart = alt.Chart(contagem_por_fase_dia).mark_bar().encode(
        y=alt.Y('fase_dia:N', title='Fases do Dia',  sort='-x', axis=alt.Axis(labelLimit=200)),
        x=alt.X('qtd:Q', title='Quantidade de Acidentes',  axis=alt.Axis(labelAngle=-45)),
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
    range=lista_cores_graficos)
                                
    chart = alt.Chart(contagem_por_condicao_metereologica).mark_bar().encode(
        y=alt.Y('condicao_metereologica:N', title='Condições Metereológicas',  sort='-x', axis=alt.Axis(labelLimit=200)),
        x=alt.X('qtd:Q', title='Quantidade de Acidentes',  axis=alt.Axis(labelAngle=-45)),
        tooltip=['condicao_metereologica', 'qtd'],
        color=alt.Color('condicao_metereologica:N', scale=lista_cores)

    ).properties(
        title=titulo,
        width=800,
        height=600         
    ).interactive()

    return chart
# =======================================================    
def gera_grafico_por_dia_semana(titulo, contagem_por_dia_semana):

    lista_cores = alt.Scale(domain=contagem_por_dia_semana['dia_semana'].unique(),
    range=lista_cores_graficos)
                                
    chart = alt.Chart(contagem_por_dia_semana).mark_bar().encode(
        y=alt.Y('dia_semana:N', title='Dia da Semana',  sort='-x', axis=alt.Axis(labelLimit=200)),
        x=alt.X('qtd:Q', title='Quantidade de Acidentes',  axis=alt.Axis(labelAngle=-45)),
        tooltip=['dia_semana', 'qtd'],
        color=alt.Color('dia_semana:N', scale=lista_cores)

    ).properties(
        title=titulo,
        width=800,
        height=600         
    ).interactive()

    return chart
# =======================================================    
def gera_grafico_por_tipo_veiculo(titulo, contagem_por_tipo_veiculo):

    lista_cores = alt.Scale(domain=contagem_por_tipo_veiculo['tipo_veiculo'].unique(),
    range=lista_cores_graficos)
                                
    chart = alt.Chart(contagem_por_tipo_veiculo).mark_bar().encode(
        y=alt.Y('tipo_veiculo:N', title='Tipo de Veículo',  sort='-x', axis=alt.Axis(labelLimit=200)),
        x=alt.X('qtd:Q', title='Quantidade de Acidentes',  axis=alt.Axis(labelAngle=-45)),
        tooltip=['tipo_veiculo', 'qtd'],
        color=alt.Color('tipo_veiculo:N', scale=lista_cores)

    ).properties(
        title=titulo,
        width=800,
        height=600         
    ).interactive()

    return chart
# =======================================================
# ==========================================================================
# Funções da Aba 06 
# ==========================================================================
def grafico_barras_empilhadas_por_uf(titulo, df):
    grafico = alt.Chart(df).mark_bar(width=20).encode(
        alt.X('ano', title='Ano'),
        alt.Y('sum(qtd)', title='Soma das Quantidades'),
        color='uf'
    ).properties(
            title=titulo,
            width=800, height=600
    ).interactive()   
    
    return grafico
# ==========================================================================
def grafico_barras_empilhadas_por_br(titulo, df):
    grafico = alt.Chart(df).mark_bar(width=20).encode(
        alt.X('ano', title='Ano'),
        alt.Y('sum(qtd)', title='Soma das Quantidades'),
        color='br:N'
    ).properties(
            title=titulo,
            width=800, height=600
    ).interactive()   

    return grafico
# ==========================================================================
def grafico_barras_empilhadas_por_tipo(titulo, df):

    grafico = alt.Chart(df).mark_bar(width=20).encode(
        alt.X('ano', title='Ano'),
        alt.Y('sum(qtd)', title='Soma das Quantidades'),
        color='tipo_acidente'
    ).properties(
            title=titulo,
            width=800, height=600
    ).interactive()   

    return grafico
# ==========================================================================
def grafico_barras_empilhadas_por_causa(titulo, df):
        
    grafico = alt.Chart(df).mark_bar(width=20).encode(
        alt.X('ano', title='Ano'),
        alt.Y('sum(qtd)', title='Soma das Quantidades'),
        color='causa_acidente'
    ).properties(
            title=titulo,
            width=800, height=600
    ).interactive()   

    return grafico
# ==========================================================================
def grafico_barras_empilhadas_por_classificacao(titulo, df):
        
    grafico = alt.Chart(df).mark_bar(width=20).encode(
        alt.X('ano', title='Ano'),
        alt.Y('sum(qtd)', title='Soma das Quantidades'),
        color='classificacao_acidente'
    ).properties(
            title=titulo,
            width=800, height=600
    ).interactive()   

    return grafico
# ==========================================================================
def grafico_barras_empilhadas_por_fase_dia(titulo, df):
        
    grafico = alt.Chart(df).mark_bar(width=20).encode(
        alt.X('ano', title='Ano'),
        alt.Y('sum(qtd)', title='Soma das Quantidades'),
        color='fase_dia'
    ).properties(
            title=titulo,
            width=800, height=600
    ).interactive()   

    return grafico
# ==========================================================================
def grafico_barras_empilhadas_por_condicao_metereologica(titulo, df):
        
    grafico = alt.Chart(df).mark_bar(width=20).encode(
        alt.X('ano', title='Ano'),
        alt.Y('sum(qtd)', title='Soma das Quantidades'),
        color='condicao_metereologica'
    ).properties(
            title=titulo,
            width=800, height=600
    ).interactive()   

    return grafico
# ==========================================================================
def grafico_barras_empilhadas_por_dia_semana(titulo, df):
        
    grafico = alt.Chart(df).mark_bar(width=20).encode(
        alt.X('ano', title='Ano'),
        alt.Y('sum(qtd)', title='Soma das Quantidades'),
        color='dia_semana'
    ).properties(
            title=titulo,
            width=800, height=600
    ).interactive()   

    return grafico
# ==========================================================================
def grafico_barras_empilhadas_por_tipo_veiculo(titulo, df):
        
    grafico = alt.Chart(df).mark_bar(width=20).encode(
        alt.X('ano', title='Ano'),
        alt.Y('sum(qtd)', title='Soma das Quantidades'),
        color='tipo_veiculo'
    ).properties(
            title=titulo,
            width=800, height=600
    ).interactive()   

    return grafico
    
# ==========================================================================

# ==========================================================================
# Gráficos de Ranking
# ==========================================================================

# ==========================================================================
def gera_grafico_ranking_uf_01(df_acidentes_geral_por_uf):

    grafico1 = alt.Chart(df_acidentes_geral_por_uf).mark_line(point=True).encode(
        x=alt.X('ano:O', title='Ano'),
        y=alt.Y("rank:O", title='Posição do Ranking'),
        color=alt.Color("uf:N") 
    ).transform_window(
        rank="rank()",
        sort=[alt.SortField("qtd", order="descending")],
        groupby=["ano"]
    ).properties(
        title="Ranking das 10 UFs com mais Acidentes (2007 a 2024)",
        width=800,
        height=600,
    )
    return grafico1
# ==========================================================================
def gera_grafico_ranking_uf_02(df_acidentes_geral_por_uf):

    grafico2 = alt.Chart(df_acidentes_geral_por_uf).mark_line(point=True).encode(
        x=alt.X('ano:N', axis=alt.Axis(title='Ano')),
        y=alt.Y('qtd:Q', axis=alt.Axis(title='Quantidade de Acidentes')),
        color='uf:N',
        tooltip=['uf', 'qtd', 'ano']
    ).properties(
        title='Evolução da Quantidade de Acidentes por UF  (2007 a 2024)',
        width=800, height=600
    ).add_selection(
        alt.selection_single(fields=['ano'], bind='legend')
    ).interactive()
    return  grafico2
# ==========================================================================
def gera_grafico_ranking_tipo_01(df_acidentes_geral_por_tipo):
    grafico1 = alt.Chart(df_acidentes_geral_por_tipo).mark_line(point=True).encode(
        x=alt.X('ano:O', title='Ano'),
        y=alt.Y("rank:O", title='Posição do Ranking'),
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
    return grafico1
# ==========================================================================
def gera_grafico_ranking_tipo_02(df_acidentes_geral_por_tipo):
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

    return grafico2
# ==========================================================================
def gera_grafico_ranking_br_01(df_acidentes_geral_por_br):
    grafico_ranking_br_01 = alt.Chart(df_acidentes_geral_por_br).mark_line(point=True).encode(
        x=alt.X('ano:O', title='Ano'),
        y=alt.Y("rank:O", title='Posição do Ranking'),
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
    return grafico_ranking_br_01
# ==========================================================================
def gera_grafico_ranking_br_02(df_acidentes_geral_por_br):
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
    return grafico_ranking_br_02      
# ==========================================================================
def gera_grafico_ranking_classificacao_01(df_acidentes_geral_por_classificacao):

    grafico_ranking_classif_01 = alt.Chart(df_acidentes_geral_por_classificacao).mark_line(point=True).encode(
        x=alt.X('ano:O', title='Ano'),
        y=alt.Y("rank:O", title='Posição do Ranking'),
        color=alt.Color("classificacao_acidente:N")
    ).transform_window(
        rank="rank()",
        sort=[alt.SortField("qtd", order="descending")],
        groupby=["ano"]
    ).properties(
        title="Ranking das Classificações dos Acidentes (2007 a 2024)",
        width=800, height=600,
    )
    return grafico_ranking_classif_01
# ==========================================================================
def gera_grafico_ranking_classificacao_02(df_acidentes_geral_por_classificacao):

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

    return grafico_ranking_classif_02
# ==========================================================================
def gera_grafico_ranking_fasedia_01(df_acidentes_geral_por_fasedia):
    grafico_ranking_fasedia_01 = alt.Chart(df_acidentes_geral_por_fasedia).mark_line(point=True).encode(
        x=alt.X('ano:O', title='Ano'),
        y=alt.Y("rank:O", title='Posição do Ranking'),
        color=alt.Color("fase_dia:N")
    ).transform_window(
        rank="rank()",
        sort=[alt.SortField("qtd", order="descending")],
        groupby=["ano"]
    ).properties(
        title="Ranking das Fases dos Acidentes (2007 a 2024)",
        width=800, height=600,
    )
    return grafico_ranking_fasedia_01
# ==========================================================================
def gera_grafico_ranking_fasedia_02(df_acidentes_geral_por_fasedia):
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
    return grafico_ranking_fasedia_02
# ==========================================================================
def gera_grafico_ranking_diasemana_01(df_acidentes_geral_por_dia_semana):

    grafico_ranking_dia_semana_01 = alt.Chart(df_acidentes_geral_por_dia_semana).mark_line(point=True).encode(
        x=alt.X('ano:O', title='Ano'),
        y=alt.Y("rank:O", title='Posição do Ranking'),
        color=alt.Color("dia_semana:N")
    ).transform_window(
        rank="rank()",
        sort=[alt.SortField("qtd", order="descending")],
        groupby=["ano"]
    ).properties(
        title="Ranking dos dos Acidentes por Dia da Semana (2007 a 2024)",
        width=800, height=600,
    )
    return grafico_ranking_dia_semana_01
# ==========================================================================
def gera_grafico_ranking_diasemana_02(df_acidentes_geral_por_dia_semana):

    grafico_ranking_dia_semana_02 = alt.Chart(df_acidentes_geral_por_dia_semana).mark_line(point=True).encode(
    x=alt.X('ano:N', axis=alt.Axis(title='Ano')),
    y=alt.Y('qtd:Q', axis=alt.Axis(title='Quantidade de Acidentes')),
    color='dia_semana:N',
    tooltip=['dia_semana', 'qtd', 'ano']
        
    ).properties(
    title='Evolução da Quantidade de Acidentes por Dia da Semana (2007-2024)',
    width=800, height=600
        
    ).add_selection(
    alt.selection_single(fields=['ano'], bind='legend')
        
    ).interactive()
    return grafico_ranking_dia_semana_02
# ==========================================================================
def gera_grafico_ranking_tipoveiculo_01(df_acidentes_geral_por_tipo_veiculo):
    grafico_ranking_tipo_veiculo_01 = alt.Chart(df_acidentes_geral_por_tipo_veiculo).mark_line(point=True).encode(
        x=alt.X('ano:O', title='Ano'),
        y=alt.Y("rank:O", title='Posição do Ranking'),
        color=alt.Color("tipo_veiculo:N")
    ).transform_window(
        rank="rank()",
        sort=[alt.SortField("qtd", order="descending")],
        groupby=["ano"]
    ).properties(
        title="Ranking dos dos Acidentes por Tipo de Veículo (2007 a 2024)",
        width=800, height=600,
    )
    return grafico_ranking_tipo_veiculo_01     
# ==========================================================================
def gera_grafico_ranking_tipoveiculo_02(df_acidentes_geral_por_tipo_veiculo):
    grafico_ranking_tipo_veiculo_02 = alt.Chart(df_acidentes_geral_por_tipo_veiculo).mark_line(point=True).encode(
    x=alt.X('ano:N', axis=alt.Axis(title='Ano')),
    y=alt.Y('qtd:Q', axis=alt.Axis(title='Quantidade de Acidentes')),
    color='tipo_veiculo:N',
    tooltip=['tipo_veiculo', 'qtd', 'ano']
        
    ).properties(
    title='Evolução da Quantidade de Acidentes por Tipo de Veículo (2007-2024)',
    width=800, height=600
        
    ).add_selection(
    alt.selection_single(fields=['ano'], bind='legend')
        
    ).interactive()
    return grafico_ranking_tipo_veiculo_02
# ==========================================================================
