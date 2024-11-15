from Bio import Phylo
from io import StringIO
import numpy as np
import pandas as pd

# Stromy ze zadani
tree1_newick = "(((B:0.2, C:0.3):0.1, D:0.1):0.1, A:0.4);"
tree2_newick = "(((B:0.2, D:0.2):0.05, C:0.25):0.13, A:0.383);"

tree1 = Phylo.read(StringIO(tree1_newick), "newick")
tree2 = Phylo.read(StringIO(tree2_newick), "newick")

distance_data = {
    "A": {"A": 0.0, "B": 0.8, "C": 0.9, "D": 0.6},
    "B": {"A": 0.8, "B": 0.0, "C": 0.5, "D": 0.4},
    "C": {"A": 0.9, "B": 0.5, "C": 0.0, "D": 0.5},
    "D": {"A": 0.6, "B": 0.4, "C": 0.5, "D": 0.0},
}

distance_data_df = pd.DataFrame(distance_data)

latex_table = distance_data_df.to_latex()
print(latex_table)


def calculate_q_score(tree, distance_matrix, method="minimum_evolution"):
    terminals = tree.get_terminals()
    n = len(terminals)
    total_score = 0.0

    if method == "minimum_evolution":
        for clade in tree.find_clades():
            if clade.branch_length:
                total_score += clade.branch_length
            else:
                pass
    elif method == "least_squares":
        for i in range(n):
            for j in range(i + 1, n):
                clade1 = terminals[i]
                clade2 = terminals[j]
                path_length = tree.distance(clade1, clade2)
                observed_distance = distance_matrix[clade1.name][clade2.name]
                print(
                    (path_length - observed_distance) ** 2,
                    path_length,
                    observed_distance,
                )
                total_score += (path_length - observed_distance) ** 2

    return total_score


q_score_tree1_me = calculate_q_score(
    tree1, distance_data, method="minimum_evolution")
q_score_tree1_ls = calculate_q_score(
    tree1, distance_data, method="least_squares")
q_score_tree2_me = calculate_q_score(
    tree2, distance_data, method="minimum_evolution")
q_score_tree2_ls = calculate_q_score(
    tree2, distance_data, method="least_squares")

print("Tree 1 Minimum Evolution Q-score:", q_score_tree1_me)
print("Tree 1 Least Squares Q-score:", q_score_tree1_ls)
print("Tree 2 Minimum Evolution Q-score:", q_score_tree2_me)
print("Tree 2 Least Squares Q-score:", q_score_tree2_ls)

preferred_tree_me = "Tree 1" if q_score_tree1_me < q_score_tree2_me else "Tree 2"
preferred_tree_ls = "Tree 1" if q_score_tree1_ls < q_score_tree2_ls else "Tree 2"

print("Preferred Tree based on Minimum Evolution:", preferred_tree_me)
print("Preferred Tree based on Least Squares:", preferred_tree_ls)
