# Band Structure Plot

## 1. Ground state calculation

* First run a ground state calculation with `PRINT_DENSITY` flag open and state the kpoint grid size, for example:

```shell
KPOINT_GRID: 5 5 5 
PRINT_DENSITY: 1
```

## 2. Band Structure Calculation

* Set the band structure plot flag `BAND_STRUC_PLOT` to 1
```shell
BAND_STRUC_PLOT: 1
```

* Band structure calculation requires density file(s). Normally, the `.dens` file(`.dens`,`.densUp`, and `.densDwn` files if `SPIN_TYP` is set to 1) from previous GS calculation is used, but you can use your own density file.

If no spin polarization is applied:
```shell
SPIN_TYP: 0
DENS_FILE_NAME: 1 [density file name]
```

If spin polarization is applied:
```shell
SPIN_TYP: 1
DENS_FILE_NAME: 3 [total spin density file name] [up spin density file name] [down spin density file name] 
```


* `KPT_PER_LINE:` is the number of points in one path(starting point and ending point included) and `KPT_NUMLINES:` is the number of paths. Put the coordinates $(x,y,z)$ of the starting point and ending point for every path right after `KPT_NUMLINES:`. The coordinates are given in fraction of $\mathbf{b}_1 , \mathbf{b}_2, \mathbf{b}_3$, for example:
```shell 
KPT_PER_LINE: 10
KPT_NUMLINES: 3
0.0 0.0 0.0 #Gamma
0.5 0.0 0.0 #M

0.5 0.0 0.0 #M
0.333333333333 0.333333333333 0.0 #K

0.333333333333 0.333333333333 0.0 #K
0.0 0.0 0.0 #Gamma
```

The above input will calculate the path `$ \Gamma $ - M - K - $ \Gamma $` of a HEX lattice.

* Results can be found as the `.eigen` file.  
