# Advanced Technique for Assessment of Spatially Averaged Dosimetric Quantities on Nonplanar Surfaces

Code and files for my doctoral thesis "Advanced Technique for Assessment of Spatially Averaged Dosimetric Quantities on Nonplanar Surfaces."

To reproduce some of the results and visuals in the thesis, the easiest way is to first create a local environment using `conda`
```shell
conda create --name phd-thesis python=3.9.15
```
and, inside the environment, run the following command in `python` repository to install all dependencies
```shell
pip install -r requirements.txt
```

Other results are related to published papers, which the thesis itself is based on:
1. A. Kapetanovic and D. Poljak, "Assessment of Incident Power Density on Spherical Head Model up to 100 GHz," in *IEEE Transactions on Electromagnetic Compatibility*, vol. 64, no. 5, pp. 1296-1303, 2022, doi: [10.1109/TEMC.2022.3183071](https://ieeexplore.ieee.org/document/9814964)
2. A. Kapetanovic and D. Poljak, “Machine Learning-Assisted Antenna Modelling for Realistic Assessment of Incident Power Density on Nonplanar Surfaces above 6 GHz," in *Radiation Protection Dosimetry*, vol. 199, no. 8-9, pp. 826–834, 2023, doi: [10.1093/rpd/ncad114](https://academic.oup.com/rpd/article-abstract/199/8-9/826/7177465)
3. A. Kapetanovic, G. Sacco, D. Poljak and M. Zhadobov, “Area-Averaged Transmitted and Absorbed Power Density on a Realistic Ear Model,” in *IEEE Journal of Electromagnetics, RF, and Microwaves in Medicine and Biology*, vol. 7, no. 1, pp. 39-45, 2023, doi: [10.1109/JERM.2022.3225380](https://ieeexplore.ieee.org/document/9993744)
4. M. Cvetkovic, D. Poljak, A. Kapetanovic and H. Dodig, “On the Applicability of Numerical Quadrature for Double Surface Integrals at 5G Frequencies,” in *Journal of Communications Software and System*, vol. 18, no. 1, pp. 42-53, 2022, doi: [10.24138/jcomss-2021-0183](https://jcoms.fesb.unist.hr/10.24138/jcomss-2021-0183/)

The source code for all the aforementioned papers is available in `playground` repository at [akapet00/EMF-exposure-analysis](https://github.com/akapet00/EMF-exposure-analysis).


## Contents

| Directory | Subdirectory/Contents | Description |
|:---:|:---:|:---:|
| `defense` |  | Slides for the defense of the doctoral thesis. |
| `docs` |  | Documents for the evaluation and defense of the doctoral thesis. |
| `latex` |  | LaTeX files. |
| `python` |  | Python scripts for generating some of the figures in the thesis. |
| 1 | `data` | Placeholder for datasets. |
| 2 | `figures` | Placeholder for visuals. |
| 3 | `misc` | Various helper functionalities for data processing, plotting, postprocessing, etc. |
| 4 | normal_estimation.py | Figure 4.2: The unit binormal, tangent and normal vector at the query point with respect to the local neighborhood surrounding that point. |
| 5 | penetration_depth.py | Figure 2.4: Power transmission coefficient and power penetration depth into dry skin as a function of frequency. |
| 6 | power_density_absorption.py | Figure 3.1: Power density as a function of frequency at the skin surface and at 1 mm depth in homogeneous dry skin. |
| 7 | reference_levels.py | Figure 2.5: Incident power density as a function of frequency for general public and occupational exposures at 6-300 GHz. |
| 8 | research_compilation.py | Figure 2.3: Papers published between 1950 and 2022 related to research on bioeffects of radio frequency electromagnetic fields and/or mobile communications. |


 ## License

 [MIT](https://en.wikipedia.org/wiki/MIT_License) except for published papers in `docs/papers` and `latex/papers` which are protected under [CC-BY](https://en.wikipedia.org/wiki/Creative_Commons_license) license protection.

 ## Contact
 Ante Kapetanovic, \<my GitHub username\>@gmail.com
