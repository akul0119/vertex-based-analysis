The proposed method employs vertex-level analysis along fiber bundles to map structural differences between TBI and PTE groups with high spatial precision. Key steps include:

Data Preprocessing:

Diffusion MRI data are denoised, corrected for artifacts, and registered to a common atlas space.
Streamline tractography is used to reconstruct the left thalamic subcortical projection (thalsub) at 2 days post-injury, a pathway linked to epileptogenesis.
Vertex Extraction and Resampling:

Vertices along fiber bundles are extracted and resampled for uniform spacing.
Averaging of vertices across subjects is performed to generate group-level representations.
Vertex-Level Statistical Analysis:

Differences in vertex positions between TBI and PTE groups are statistically tested, identifying localized regions of significant divergence.
Visualization:

Significant segments are visualized on the fiber bundle, highlighting regions potentially associated with PTE risk.
This method demonstrates enhanced sensitivity for early, localized structural changes and offers promising insights for biomarker discovery in TBI and PTE research.

<img width="691" alt="Screen Shot 2025-01-16 at 9 49 30 PM" src="https://github.com/user-attachments/assets/b566226e-3680-41de-a65b-13b87a30fa27" />

Workflow Summary
Extract Vertices: extract.py
Compute Averages: averageVertices.py
Perform Quality Control: qc.py
Resample and Average VTK: avgVT.py
Stack and Resample Vertices: stack.py
Visualize Fiber Bundle: visualize.py
Convert CSV to VTK: vtkConvert.py
By following this sequence, you can process raw VTK files into actionable results, including statistical analysis and 3D visualization.
