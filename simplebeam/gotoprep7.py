from ansys.mapdl.core import launch_mapdl
import ansys.mapdl.core as pymapdl
import os

beamlength = 1
beamwidth = 0.01
beamheight = 0.01

mapdl = launch_mapdl()

mapdl.prep7()
status = mapdl.run('status')
status.replace('\n', os.linesep)
print(status)

mapdl.exit(save=False)
