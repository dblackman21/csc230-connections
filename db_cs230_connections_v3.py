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

for bit_id, students in bit_students.items():
    label_obj = v.get_label_by_id(bit_id)
    if label_obj:
        names_str = '\n'.join(students)
        label_obj.set_text(names_str)
        label_obj.set_fontsize(7)

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