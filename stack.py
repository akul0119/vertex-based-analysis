### Stacking and Averaging Vertices: stack.py ###
import vtk
import numpy as np
from scipy.interpolate import interp1d

def resample_vertices(vertices, num_points):
    t = np.linspace(0, 1, len(vertices))
    t_new = np.linspace(0, 1, num_points)
    resampled_vertices = np.vstack((
        interp1d(t, vertices[:, 0], kind='linear')(t_new),
        interp1d(t, vertices[:, 1], kind='linear')(t_new),
        interp1d(t, vertices[:, 2], kind='linear')(t_new)
    )).T
    return resampled_vertices

num_resampled_points = 5000
vtk_files = ["file1.vtk.gz", "file2.vtk.gz"]
all_vertices_resampled = [resample_vertices(load_vtk_vertices(f), num_resampled_points) for f in vtk_files]
all_vertices_stack = np.stack(all_vertices_resampled)
average_vertices = np.mean(all_vertices_stack, axis=0)
