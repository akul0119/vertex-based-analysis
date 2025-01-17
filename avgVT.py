
### Resampling and Averaging VTK: avgVT.py ###
import vtk
import numpy as np
import gzip
import shutil
import os

def load_vtk_vertices(file):
    decompressed_file = file.replace(".vtk.gz", ".vtk")
    with gzip.open(file, 'rb') as f_in:
        with open(decompressed_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    
    reader = vtk.vtkPolyDataReader()
    reader.SetFileName(decompressed_file)
    reader.Update()
    polydata = reader.GetOutput()

    points = polydata.GetPoints()
    vertices = [points.GetPoint(i) for i in range(points.GetNumberOfPoints())]

    os.remove(decompressed_file)
    return np.array(vertices)

vtk_files = ["file1.vtk.gz", "file2.vtk.gz"]
all_vertices = [load_vtk_vertices(f) for f in vtk_files]
all_vertices_stack = np.stack(all_vertices)
average_vertices = np.mean(all_vertices_stack, axis=0)
