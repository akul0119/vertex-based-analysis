### Extracting Vertices: extract.py ###
import vtk
import pandas as pd
import os

def extract_vertices(vtk_file, output_csv):
    reader = vtk.vtkPolyDataReader()
    reader.SetFileName(vtk_file)
    reader.Update()

    output = reader.GetOutput()
    points = output.GetPoints()

    vertices = []
    for i in range(points.GetNumberOfPoints()):
        vertices.append(points.GetPoint(i))

    df = pd.DataFrame(vertices, columns=['x', 'y', 'z'])
    df.to_csv(output_csv, index=False)
    print(f"Saved {vtk_file} vertices to {output_csv}")

input_dir = "/path/to/vtk/files/"
vtk_files = ["file1.vtk", "file2.vtk"]

for vtk_file in vtk_files:
    input_path = os.path.join(input_dir, vtk_file)
    output_csv = vtk_file.replace(".vtk", "_vertices.csv")
    extract_vertices(input_path, output_csv)

### Averaging Vertices: averageVertices.py ###
import pandas as pd
import glob

csv_files = glob.glob("/path/to/csvs/*_vertices.csv")
dataframes = [pd.read_csv(file) for file in csv_files]
average_vertices = pd.concat(dataframes).groupby(level=0).mean()
average_vertices.to_csv("/path/to/output/average_vertices.csv", index=False)
