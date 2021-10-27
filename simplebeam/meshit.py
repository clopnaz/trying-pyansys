from ansys.mapdl.core import launch_mapdl
import ansys.mapdl.core as pymapdl
import os

beamlength = 1
beamwidth = 0.01
beamheight = 0.01
ex = 62e9
esize = 0.1

pymapdl.close_all_local_instances()
mapdl.exit(save=False)
mapdl = launch_mapdl()

mapdl.prep7()
status = mapdl.run('status')
status.replace('\n', os.linesep)
print(status)

mapdl.k(1,0,0,0)
mapdl.k(2,beamlength,0,0)
mapdl.l(1,2)

# mapdl.lplot(cpos="xy")

mapdl.et(1,'beam189')
mapdl.sectype(1,'beam','rect')
mapdl.secdata(1,beamwidth,beamheight)
mapdl.mat(1)
mapdl.mp('ex',ex)
mapdl.esize(esize)
mapdl.lmesh('all')
# mapdl.eplot(cpos="xy")

print(mapdl.nlist().replace('\n', os.linesep))
# mapdl.exit(save=False)
