import os
import comtypes
import comtypes.client
com_module =  comtypes

# message name, comnames
items = [
		('TEM Scripting', ('Tecnai.Instrument', 'TEMScripting.Instrument.1')),
		('TOM Moniker', ('TEM.Instrument.1',)),
		('TEM Advanced Scripting',('TEMAdvancedScripting.AdvancedInstrument.1', 'TEMAdvancedScripting.AdvancedInstrument.2')),
		('Tecnai Low Dose Kit', ('LDServer.LdSrv',)),
		#('Gatan CCD Camera', ('TecnaiCCD.GatanCamera.2',)),
		('TIA', ('ESVision.Application',)),
		('TVIPS EmMenu', ('EMMENU4.EMMENUApplication.1',)),

]

def getTlbFromComname(comname):
	try:
		comobj = comtypes.client.CreateObject(comname)
		return comname, comobj
	except:
		pass
	return None

def makeFile(item):
	typelibInfo = None
	message, comnames = item
	for i, comname in enumerate(comnames):
		typelibInfo = getTlbFromComname(comname)
		if typelibInfo is not None:
			print('\nFound COM typelib named: %s' % comname)
			break
	if typelibInfo is None:
		print('\nError, cannot find typelib for "%s"\n' % (message,))
		return

def run():
	print('Looking for COM module files from type libraries...\n')
	for item in items:
		print('checking', item[0], end=' ')
		makeFile(item)
		print('\n')
	input('enter to quit.')

if __name__ == '__main__':
	run()

