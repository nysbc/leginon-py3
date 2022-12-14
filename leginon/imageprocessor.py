#
# COPYRIGHT:
#       The Leginon software is Copyright under
#       Apache License, Version 2.0
#       For terms of the license agreement
#       see  http://leginon.org
#

from leginon import leginondata
from leginon import event
import threading
from leginon import node
import leginon.gui.wx.ImageProcessor

class ImageProcessor(node.Node):
	eventinputs = node.Node.eventinputs + [event.TargetListDoneEvent]
	panelclass = leginon.gui.wx.ImageProcessor.Panel
	settingsclass = leginondata.ImageProcessorSettingsData
	defaultsettings = {
		'process': False,
	}
	def __init__(self, id, session, managerlocation, **kwargs):
		node.Node.__init__(self, id, session, managerlocation, **kwargs)
		self.addEventInput(event.TargetListDoneEvent, self.handleTargetListDone)
		self.start()

	def handleTargetListDone(self, evt):
		if not self.settings['process']:
			self.logger.info('processing turned off, ignoring event')
			return

		self.setStatus('processing')

		targetlistdata = evt['targetlist']
		# query images resulting from this targetlist
		tquery = leginondata.AcquisitionImageTargetData(list=targetlistdata)
		imquery = leginondata.AcquisitionImageData(target=tquery)

		## query, but don't read image files yet, or else run out of memory
		imagelist = imquery.query(readimages=False)
		## list is reverse chronological, so reverse it
		imagelist.reverse()
		self.processImageList(imagelist)
		self.setStatus('idle')

	def processImageList(self, imagelist):
		raise NotImplementedError()
