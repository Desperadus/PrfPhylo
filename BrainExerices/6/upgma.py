import numpy as np
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor, DistanceMatrix
from Bio import Phylo

distance_matrix = np.array(
    [
        [0, 0.3, 0.62, 0.62, 0.62, 0.62],
        [0.3, 0, 0.52, 0.52, 0.52, 0.52],
        [0.62, 0.52, 0, 0.36, 0.36, 0.36],
        [0.62, 0.52, 0.36, 0, 0.3, 0.3],
        [0.62, 0.52, 0.36, 0.3, 0, 0.1],
        [0.62, 0.52, 0.36, 0.3, 0.1, 0],
    ]
)

names = ["A", "B", "C", "D", "E", "F"]

matrix = []
for i in range(len(distance_matrix)):
    row = []
    for j in range(i):
        row.append(distance_matrix[i][j])
    row.append(0.0)
    matrix.append(row)

print("Formatted Lower Triangular Matrix:")
for taxon, distances in zip(names, matrix):
    print(f"{taxon}: {distances}")

dm = DistanceMatrix(names, matrix)

constructor = DistanceTreeConstructor()
upgma_tree = constructor.upgma(dm)

Phylo.draw(upgma_tree)
Phylo.draw_ascii(upgma_tree)
