import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd
from matplotlib_venn import venn3, venn3_circles
import matplotlib.patches as patches

# import variables from csc230_connections_data.py
from csc230_connections_data import (
    all_students,
    sheet_names,
    bit_weights,
    bit_to_category,
    xls
)

seed = 0
random.seed(seed)
np.random.seed(seed)
G = nx.Graph()

# Add nodes for each student
valid_students = [s for s in all_students if isinstance(s, str)]
for student in valid_students:
    G.add_node(student)

# Read connections for ALL students
connection_counts = {}

for sheet in sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet, index_col=0)
    
    for student_row in df.index:
        if not isinstance(student_row, str) or student_row not in valid_students:
            continue
        
        # Get all students this person connects to
        connections = set(df.loc[student_row][df.loc[student_row] == 1].index.tolist())
        
        for connected_student in connections:
            # Filter out self-loops (student connecting to themselves)
            if isinstance(connected_student, str) and connected_student in valid_students and connected_student != student_row:
                edge = tuple(sorted([student_row, connected_student]))
                connection_counts[edge] = connection_counts.get(edge, 0) + 1
                G.add_edge(student_row, connected_student, weight=connection_counts[edge])

# Define positions using circular layout
pos = {}

# Place all students in a circle
num_students = len(G.nodes())
radius = 3
for i, student in enumerate(sorted(valid_students)):
    angle = 2 * np.pi * i / num_students
    pos[student] = np.array([radius * np.cos(angle), radius * np.sin(angle)])

# Create node sizes based on connection degree
node_sizes = []
for student in G.nodes():
    # Size based on number of connections
    degree = G.degree(student)
    node_sizes.append(degree * 150 + 300)  # Base size + scaled by connections

# Create edge widths based on connection counts
edge_widths = [G[u][v]['weight'] * 0.7 for u, v in G.edges()]

# Draw the graph
plt.figure(figsize=(14, 14))
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=node_sizes)
nx.draw_networkx_labels(G, pos, font_size=8)
nx.draw_networkx_edges(G, pos, width=edge_widths, alpha=0.6)

plt.title("All Class Connections Graph")
plt.axis('off')
plt.tight_layout()
plt.show()

