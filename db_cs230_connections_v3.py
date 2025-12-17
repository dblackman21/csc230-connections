import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd
from matplotlib_venn import venn3, venn3_circles
import matplotlib.patches as patches

# Read all three sheets
xls = pd.ExcelFile('discrete projects/graphs/p8/sfsu_fall25_csc230_graph_project.xlsx')
print(f"Sheet names: {xls.sheet_names}")

# Extract my connections from each sheet
devon_sets = {}
sheet_names = xls.sheet_names

for sheet in sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet, index_col=0)
    devon_row = df.loc['Devon']
    devon_sets[sheet] = set(devon_row[devon_row == 1].index.tolist())
    print(f"\n{sheet}:")
    print(devon_sets[sheet])

# Get all unique students
all_students = set()
for s in devon_sets.values():
    all_students.update(s)

# Categorize students by their relationships using bit notation
categories = {}

for student in all_students:
    in_A = student in devon_sets[sheet_names[0]]  # Knows Name
    in_B = student in devon_sets[sheet_names[1]]  # Helped in Class
    in_C = student in devon_sets[sheet_names[2]]  # Talked Outside Class
    
    # Create category string for display
    category = ""
    category += "An" if in_A else "_An"
    category += "Bn" if in_B else "_Bn"
    category += "C" if in_C else "_C"
    
    if category not in categories:
        categories[category] = []
    categories[category].append(student)

# Print all categories and their students
print("\n\n=== CATEGORIZED STUDENTS ===")
for category in sorted(categories.keys()):
    print(f"\n{category}: {categories[category]}")

# Map categories to venn3 bit notation (001, 010, 011, 100, 101, 110, 111)
# Bit order: A, B, C
bit_to_category = {
    '100': 'An_Bn_C',   # only A
    '010': '_AnBn_C',    # only B
    '001': '_An_BnC',    # only C
    '110': 'AnB_nC',     # A and B, not C
    '011': '_AnBnC',     # B and C, not A
    '101': 'An_BnC',     # A and C, not B
    '111': 'AnBnC',      # all three
}

# Count students in each bit category
bit_counts = {
    '100': len(categories.get('An_Bn_C', [])),
    '010': len(categories.get('_AnBn_C', [])),
    '001': len(categories.get('_An_BnC', [])),
    '110': len(categories.get('AnBn_C', [])),
    '011': len(categories.get('_AnBnC', [])),
    '101': len(categories.get('An_BnC', [])),
    '111': len(categories.get('AnBnC', [])),
}

# Get student names for each bit category
bit_students = {
    '100': categories.get('An_Bn_C', []),
    '010': categories.get('_AnBn_C', []),
    '001': categories.get('_An_BnC', []),
    '110': categories.get('AnBn_C', []),
    '011': categories.get('_AnBnC', []),
    '101': categories.get('An_BnC', []),
    '111': categories.get('AnBnC', []),
}

print("\n\n=== BIT NOTATION COUNTS ===")
for bit, count in bit_counts.items():
    print(f"{bit}: {count} students")

# Assign meaningful labels
labels = ['Knows Name (A)', 'Helped in Class (B)', 'Talked Outside Class (C)']

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