# HaddockRestraints
Simple python script to generate unambiguous/ambiguous distance restraints files for [HADDOCK](https://wenmr.science.uu.nl/haddock2.4/)

The HADDOCK docking protein-protein docking web server allows for the selection of "active" and "passive" residues for the proteins being docked in its interactive
interface. But if you ever want to specify specific *pairwise* interactions, this interface is fairly restrictive. But at the "Expert" level of the HADDOCK interface, you can
upload "restraints" files in the "tbl" file format which can specify specific pairs of residues and specific distance restraints for both ambiguous and unambigous protein 
interactions. The documentation for this format is a little hard to find, so I made this interactive script to produce such restraints quickly.

To run (assuming you have Python 3) simply launch the script like so: `python make_haddock_restraints.py`.

The script will then walk you through the restraints process. 

## Notes
* `segid` is synonymous with chain IDs in pdb files. 
* `residue number` refers to the position of a residue according to the PDB file. 
* `distance restraints` - The tbl format allows for some flexibility, but for the simplicity of the script it only supports the most common usage: pairwise interactions from 0 to N angstroms distance where N is the distance restraint.

This script produces restraints that have been tested to work as of HADDOCK 2.4. 
