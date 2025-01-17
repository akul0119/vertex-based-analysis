### CSV to VTK Conversion: vtkConvert.py ###
import vtk
import pandas as pd

data = pd.read_csv("average_vertices.csv")
points = vtk.vtkPoints()
for i in range(len(data)):
    points.InsertNextPoint(data.iloc[i]['x'], data.iloc[i]['y'], data.iloc[i]['z'])

polydata = vtk.vtkPolyData()
polydata.SetPoints(points)
writer = vtk.vtkPolyDataWriter()
writer.SetFileName("average.vtk")
writer.SetInputData(polydata)
writer.Write()
