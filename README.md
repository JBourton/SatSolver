# SatSolver
This sat solver implements well-known sat solving techniques including unit propagation and branching on partial truth assignements in order to determine whether an input, given in [CNF](https://en.wikipedia.org/wiki/Conjunctive_normal_form), is satisfiable.

Optimisation has been a key aspect of devlopment; the sat solver presented in this project runs several orders of magnitude times faster than the basic intial implementation initially written up, which uses brute force.
