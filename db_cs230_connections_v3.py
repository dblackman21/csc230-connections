import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd
from matplotlib_venn import venn3, venn3_circles
import matplotlib.patches as patches

from csc230_connections_data import (
    devon_sets,
    all_students,
    categories,
    bit_students,
    bit_counts,
    labels,
    sheet_names
)

# create venn3 diagram
v = venn3(subsets=(1, 1, 1, 1, 1, 1, 1), set_labels=('A', 'B', 'C'))

# exclude label for 000 since it is not shown in venn3 natively
valid_bit_ids = ['100', '010', '001', '110', '101', '011', '111']

for bit_id in valid_bit_ids:
    if bit_id in bit_students:
        students = bit_students[bit_id]
        label_obj = v.get_label_by_id(bit_id)
        if label_obj:
            names_str = '\n'.join(students)
            label_obj.set_text(names_str)
            label_obj.set_fontsize(7)


# handling 000 case separately
if bit_students.get('000'):
    outside_students = '\n'.join(bit_students['000'])
    plt.text(0.02, 0.98, f"Outside all sets (000):\n{outside_students}", 
             transform=plt.gca().transAxes, fontsize=8, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

"""  old code to set labels with student counts
v.get_label_by_id('100').set_text(f"{bit_counts['100']}")
v.get_label_by_id('010').set_text(f"{bit_counts['010']}")
v.get_label_by_id('001').set_text(f"{bit_counts['001']}")
v.get_label_by_id('110').set_text(f"{bit_counts['110']}")
v.get_label_by_id('011').set_text(f"{bit_counts['011']}")
v.get_label_by_id('101').set_text(f"{bit_counts['101']}")
v.get_label_by_id('111').set_text(f"{bit_counts['111']}")
"""

plt.title("Devon's Connections in CSC 230")
plt.show()