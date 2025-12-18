import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd
from matplotlib_venn import venn3, venn3_circles
import matplotlib.patches as patches

# import variables from csc230_connections_data.py
from csc230_connections_data import (
    devon_sets,
    all_students,
    categories,
    bit_students,
    bit_counts,
    labels,
    sheet_names,
    bit_weights,
    bit_to_category
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

# Define positions using circular layout
pos = nx.spring_layout(G, seed=seed)

# Place Devon in the center
pos['Devon'] = np.array([0, 0])

# Place other students in a circle around Devon
# Filter out NaN and non-string values
valid_students = [s for s in all_students if isinstance(s, str)]
num_students = len(valid_students)
radius = 2
for i, student in enumerate(sorted(valid_students)):
    angle = 2 * np.pi * i / num_students
    pos[student] = np.array([radius * np.cos(angle), radius * np.sin(angle)])

# Create node sizes based on bit weights
node_sizes = []
for student in G.nodes():
    if student == 'Devon':
        node_sizes.append(1000)  # Devon stays large
    else:
        # Find which bit category this student belongs to
        for bit_id, category_name in bit_to_category.items():
            if student in bit_students.get(bit_id, []):
                weight = bit_weights.get(bit_id, 1)
                # Scale weight to node size (multiply by 200 for visibility)
                node_sizes.append(weight * 200)
                break
        else:
            node_sizes.append(50)  # Default size if not found

# Draw the graph
plt.figure(figsize=(9, 9))
nx.draw_networkx_nodes(G, pos, node_color='lightgreen', node_size=node_sizes)
nx.draw_networkx_labels(G, pos, font_size=10)
nx.draw_networkx_edges(G, pos, width=1.5)

plt.title("Devon's Connections Graph")
plt.axis('off')
plt.margins(0.1)
plt.show()