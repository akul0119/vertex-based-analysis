### Quality Control: qc.py ###
import vtk
import numpy as np
import gzip

def print_vertex_distance_stats(vertices):
    distances = np.linalg.norm(np.diff(vertices, axis=0), axis=1)
    print(f"Mean: {np.mean(distances):.4f}, Std: {np.std(distances):.4f}")

vtk_files = ["file1.vtk.gz", "file2.vtk.gz"]
for file in vtk_files:
    vertices = load_vtk_vertices(file)
    print_vertex_distance_stats(vertices)
