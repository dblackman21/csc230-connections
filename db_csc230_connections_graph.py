import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd
from matplotlib_venn import venn3, venn3_circles
import matplotlib.patches as patches

# import variables from db_cs230_connections_v3.py
from db_cs230_connections_v3 import (
    devon_sets,
    all_students,
    categories,
    bit_students,
    bit_counts,
    labels,
    sheet_names
)

seed = 0
random.seed(seed)
np.random.seed(seed)
G = nx.Graph()

# Add nodes for each student
for student in all_students:
    G.add_node(student)

# add edges based on my connections
for sheet in sheet_names:
    connections = devon_sets[sheet]
    for student in connections:
        G.add_edge('Devon', student)

# Define positions using spring layout for better visualization
pos = nx.spring_layout(G, seed=seed)

# Draw the graph
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
plt.title("Devon's Connections Graph")
plt.margins(0.1)
plt.show()