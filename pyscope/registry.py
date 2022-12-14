#
# COPYRIGHT:
#       The Leginon software is Copyright under
#       Apache License, Version 2.0
#       For terms of the license agreement
#       see  http://leginon.org
#

from . import config

temorder = []
tems = {}
ccdcameraorder = []
ccdcameras = {}

for c in config.getTEMClasses():
	temorder.append((c.name, c))
	tems[c.name] = c
for c in config.getCameraClasses():
	ccdcameraorder.append((c.name, c))
	ccdcameras[c.name] = c

def getClass(name):
	if name in tems:
		return tems[name]
	elif name in ccdcameras:
		return ccdcameras[name]
	else:
		return None

def getClasses():
	return temorder + ccdcameraorder

