import numpy as np
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor, DistanceMatrix
from Bio import Phylo
from upgma import distance_matrix, names


def test_upgma_nj_trees():
    matrix = []
    for i in range(len(distance_matrix)):
        row = []
        for j in range(i):
            row.append(distance_matrix[i][j])
        row.append(0.0)
        matrix.append(row)

    dm = DistanceMatrix(names, matrix)

    constructor = DistanceTreeConstructor()
    upgma_tree = constructor.upgma(dm)

    print("UPGMA Tree with branch lengths:")
    for clade in upgma_tree.find_clades():
        print(f"{clade.name}: {clade.branch_length}")

    Phylo.write(upgma_tree, "upgma_tree.newick", "newick")

    nj_tree = constructor.nj(dm)

    print("NJ Tree with branch lengths:")
    for clade in nj_tree.find_clades():
        print(f"{clade.name}: {clade.branch_length}")

    Phylo.write(nj_tree, "nj_tree.newick", "newick")


if __name__ == "__main__":
    test_upgma_nj_trees()
