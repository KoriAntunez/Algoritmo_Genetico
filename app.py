import random

import numpy as np
import pandas as pd
import streamlit as st

from streamlit_solver import genetic_tsp
from utils import read_input

st.set_page_config(layout="wide")

"""
# Algoritmo Genético

Algoritmo genético aplicado en encontrar el camino más óptimo dada una lista de coordenada de ciudades

Puede configurar los parámetro de la barra lateral para que pueda interactuar

"""

with st.sidebar:
    select_dataset = st.selectbox(
        label="Seleccione el dataset",
        options=("p01.in", "dj15.in", "dj38.in", "att48.in", "qa194.in"),
    )

    num_generations = st.number_input(
        "Número de generaciones", min_value=10, max_value=5000, step=10
    )

    population_size = st.number_input(
        "Tamaño de población", min_value=10, max_value=5000, step=10
    )

    mutation_prob = st.number_input(
        "Probabilidad de mutación", min_value=0.0, max_value=1.0, value=0.1
    )

    random_seed_checkbox = st.checkbox("Establecer una semilla aleatoria?")

    if random_seed_checkbox:
        random_seed = st.number_input("semilla aleatoria", min_value=0, step=1, value=42)
        random.seed(random_seed)
        np.random.seed(random_seed)

col1, col2 = st.beta_columns(2)

col1.header("Mejor Solución")
progress_bar = st.empty()
current_distance = st.empty()
plot = col1.empty()
done = st.empty()
final_distance = st.empty()

optimal_distances = {
    "p01.in": 284,
    "dj15.in": 3172,
    "dj38.in": 6656,
    "att48.in": 33523,
    "qa194.in": 9352,
}
optimal_distance = st.write(
    f"**Optimal Distance:** {optimal_distances[select_dataset]}"
)

col2.header("Distancia en el tiempo")
df = pd.DataFrame({"Distancia": []})
chart = col2.empty()


## Run the Genetic Algorithm
best_solution, best_distance = genetic_tsp(
    select_dataset,
    num_generations,
    population_size,
    mutation_prob,
    chart,
    plot,
    progress_bar,
    current_distance,
)

progress_bar.empty()
current_distance.empty()

cities = read_input(f"data/{select_dataset}")


done.write("**Hecho**!")
final_distance.write(f"**Final Distance:** {best_distance}")
