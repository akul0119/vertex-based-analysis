### Visualization: visualize.py ###
import vtk
reader = vtk.vtkPolyDataReader()
reader.SetFileName("average.vtk")
reader.Update()

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(reader.GetOutputPort())
actor = vtk.vtkActor()
actor.SetMapper(mapper)

renderer = vtk.vtkRenderer()
renderer.AddActor(actor)
renderer.SetBackground(1, 1, 1)
render_window = vtk.vtkRenderWindow()
render_window.AddRenderer(renderer)
render_interactor = vtk.vtkRenderWindowInteractor()
render_interactor.SetRenderWindow(render_window)
render_window.Render()
render_interactor.Start()
