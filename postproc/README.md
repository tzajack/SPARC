## BandStrPlot requirements and usage
### (1) Brief:
* BandStrPlot.py is a python script that reads `.eigen` file and plot the band structure of a given system.
* Energy unit using is eV.
* Resultant plot is stored with the file name `BandStructure.eps`.

### (2) Requriement Libraries of Python
* numpy and matplotlib are the two libraries required. One can install them by the following commands

```shell
pip install numpy
pip install matplotlib
```

### (3) Execution
* Assign the path of your `.eigen` file to `path` in `main()`.
* Assign your high symmetry points string to `highsym_point` in `main()`. The default value of `highsym_point` is empty.
* Assign your fermi energy value to `fermi_energy`. Use the default unit (Hartree) of SPARC.
* Run the script with 
```shell
python BandStrPlot.py
```
the resultant vector graph is saved as `BandStructure.eps`.

### (4) Example
* An example of CdS system can be found under the folder `Example`.
