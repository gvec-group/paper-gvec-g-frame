[![pipeline status](https://gitlab.mpcdf.mpg.de/gvec-group/paper-gvec-g-frame/badges/main/pipeline.svg)](https://gitlab.mpcdf.mpg.de/gvec-group/paper-gvec-g-frame/-/commits/main)



## Title: Computing MHD equilibria of stellarators with a flexible coordinate frame 

### [ ==> Download pdf <== ](https://gitlab.mpcdf.mpg.de/gvec-group/paper-gvec-g-frame/-/jobs/artifacts/master/raw/HINDENLANG_PLUNK_MAJ_varenna2024_frenet.pdf?job=pdflatex_final)
### [ ==> experimental html version <== ](https://gvec-group.pages.mpcdf.de/paper-gvec-g-frame)

## Authors: Florian Hindenlang , Gabriel Plunk , Omar Maj

## Citation

* Published in the Journal "Plasma Physics and Controlled Fusion". 
* DOI: [10.1088/1361-6587/adba11](https://doi.org/10.1088/1361-6587/adba11)  
* arXiv preprint: [arXiv:2410.17595](https://arxiv.org/abs/2410.17595)
* bibtex:
  ```
  @article{Hindenlang_2025,
  doi = {10.1088/1361-6587/adba11},
  year = {2025},
  publisher = {IOP Publishing},
  volume = {67},
  number = {4},
  pages = {045002},
  author = {Hindenlang, Florian and Plunk, Gabriel G and Maj, Omar},
  title = {Computing MHD equilibria of stellarators with a flexible coordinate frame},
  journal = {Plasma Physics and Controlled Fusion}
  }
  ```

## Abstract


For the representation of axi-symmetric plasma configurations (tokamaks), it is natural to use cylindrical coordinates (R,Z,\phi), where \phi is an independent coordinate. The same cylindrical coordinates have also been widely used for representing 3D MHD equilibria of non-axisymmetric configurations (stellarators), with cross-sections, defined in RZ-planes, that vary over \phi. 

Stellarator equilibria have been found, however, for which cylindrical coordinates are not at all a natural choice, for instance certain stellarators obtained using the near-axis expansion (NAE), defined by a magnetic axis curve and its Frenet frame.

In this contribution, we propose an alternative approach for representing the boundary in a fixed-boundary 3D MHD equilibrium solver, moving away from cylindrical coordinates. 
Instead, we use planar cross-sections whose orientation is determined by a general coordinate frame (G-Frame). This frame is similar to the conventional Frenet frame, but more flexible. 
As an additional part of the boundary representation, it becomes an input to the equilibrium solve, along with the geometry of the cross-sections.
We see two advantages: 1) the capability to easily represent configurations where the magnetic axis is highly non-planar or even knotted. 2) a reduction in the degrees of freedom needed for the boundary surface, and thus the equilibrium solver, enabling progress in optimization of these configurations.

We discuss the properties of the G-Frame, starting from the conventional Frenet frame. Then we show two exemplary ways of constructing it, first from a NAE solution and also from a given boundary surface. We present the details of the implementation of the new frame in the 3D MHD equilibrium solver GVEC. Furthermore, we demonstrate for a highly shaped QI-optimized stellarator that far fewer degrees of freedom are necessary to find a high quality equilibrium solution, compared to the solution computed in cylindrical coordinates.

## data

https://doi.org/10.5281/zenodo.14714598


## Acknowledgements
Thanks to the co-authors and: 

Robert Babin, Carolin Nuehrenberg ,  Tiago Ribeiro , Robert Köberl , Alan Goodman ,
Katia Camacho , Matt Landreman 


