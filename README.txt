# OpenSEMBA
# Copyright (C) 2015 Salvador Gonzalez Garcia                    (salva@ugr.es)
#                    Luis Manuel Diaz Angulo          (lmdiazangulo@semba.guru)
#                    Miguel David Ruiz-Cabello Nuñez        (miguel@semba.guru)
#                    Alejandra Lopez de Aberasturi Gomez (aloaberasturi@ugr.es)
#                    
# This file is part of OpenSEMBA.
#
# OpenSEMBA is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# OpenSEMBA is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with OpenSEMBA. If not, see <http://www.gnu.org/licenses/>.



%------------------------------------------------------------------------------%


#It's mandatory to choose among the following to select the KIND OF TEST to be  
#performed (i.e: equality test or almost-equality test): 
#   -For equality test: isEqual
#   -For almost equality test: isAlmostEqual
#Either lower, upper or mixed case can be used indistinctly.
#
#
#Described below are the accepted entries for the keywords:
#
#    -[filters][keyWords][materials] can either have value "PEC", "SGBC" or 
#     "NIBC"
#
#    -[filters][keyWords][excitation] can either have value "planeWave", 
#     "thinWire" or "dipole"
#
#    -[filters][keyWords][mesh] can either have value "conformal" or "staircased"

#    -[filters][keyWords][boundaryConditions] can either be "PMLBC" or "PECBC"
#
#These filters can be changed directly in data/Cases/case.gid/case.test.json , 
#under the [filters][comparison] flag and [filters][keyWords] flag respectively.
#
#
#
#
#It is also possible to choose to launch a case with an .nfde, .cmsh and .conf 
#files as input (i.e, skipping the call to SEMBA). For that purpose, an
#["execution"] flag is suplied: 
#    -[execution] : "normal"  --will launch BOTH semba and ugrfdtd
#    -[execution] : "ugrfdtd" --will just lunch ugrfdtd
#
#
#Before execution, please remember to add semba and ugrfdtd executables (or links)
#in the /bin folder.
#
#For further information, please contact aloaberasturi@ugr.es



