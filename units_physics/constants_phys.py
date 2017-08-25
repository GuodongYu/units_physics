from units_physics.unit_convert import *

# SI: international unit
kb_SI = 1.38064852e-23 # Boltzmann constant
c_SI = 2.99792458e+8 # speed of light in vacuum








# Hau: Hartree atomic unit
kb_Hau = kb_SI * Joule_to_Hau / Kelvin_to_Hau
c_Hau = c_SI * meter_to_Hau/ second_to_Hau
