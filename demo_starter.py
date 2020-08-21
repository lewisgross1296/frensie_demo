import numpy
import os
import sys
import PyFrensie.Geometry as Geometry
import PyFrensie.Geometry.DagMC as DagMC
import PyFrensie.Utility as Utility
import PyFrensie.Utility.MPI as MPI
import PyFrensie.Utility.Prng as Prng
import PyFrensie.Utility.Coordinate as Coordinate
import PyFrensie.Utility.Distribution as Distribution
import PyFrensie.MonteCarlo as MonteCarlo
import PyFrensie.MonteCarlo.Collision as Collision
import PyFrensie.MonteCarlo.ActiveRegion as ActiveRegion
import PyFrensie.MonteCarlo.Event as Event
import PyFrensie.MonteCarlo.Manager as Manager
import PyFrensie.Data as Data
import PyFrensie.Data.Native as Native



##---------------------------------------------------------------------------##
## Harcode the required parameters
##---------------------------------------------------------------------------##
# sim_name is of type string
sim_name = "sphere"

# db_path is of type string
db_path = ""

# num_particles is of type float
num_particles = float(1e6)

# source_energy is of type float
source_energy = float(1)

# energy_bins is a double array
energy_bins = []

# thread is of type "int"
threads = int(4)

# not sure if we need
log_file = None 

##---------------------------------------------------------------------------##
## Initialize the MPI Session
##---------------------------------------------------------------------------##

##---------------------------------------------------------------------------##
## Set the simulation properties
##---------------------------------------------------------------------------##

##---------------------------------------------------------------------------##
## Set up the materials
##---------------------------------------------------------------------------##

##---------------------------------------------------------------------------##
## Set up the geometry
##---------------------------------------------------------------------------##

##---------------------------------------------------------------------------##
## Set up the source
##---------------------------------------------------------------------------##

##---------------------------------------------------------------------------##
## Set up the event handler
##---------------------------------------------------------------------------##

##---------------------------------------------------------------------------##
## Set up the simulation manager
##---------------------------------------------------------------------------##

##---------------------------------------------------------------------------##
## Run the simulation
##---------------------------------------------------------------------------##


