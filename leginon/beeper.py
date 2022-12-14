#
# COPYRIGHT:
#       The Leginon software is Copyright under
#       Apache License, Version 2.0
#       For terms of the license agreement
#       see  http://leginon.org
#

'''
'''

from leginon import node
from leginon import leginondata
from leginon import event
import leginon.gui.wx.Beeper
import threading

class Beeper(node.Node):
	panelclass = leginon.gui.wx.Beeper.Panel
	settingsclass = leginondata.BeeperSettingsData
	eventinputs = node.Node.eventinputs + [event.TargetListDoneEvent]
										
	def __init__(self, id, session, managerlocation, **kwargs):
		node.Node.__init__(self, id, session, managerlocation, **kwargs)

		self.addEventInput(event.TargetListDoneEvent, self.handleTargetListDone)

		self.stopevent = threading.Event()
		self.start()

	def handleTargetListDone(self, pubevent=None):
		self.setStatus('user input')
		while True:
			self.beep()
			time.sleep(0.5)
			if self.stopevent.isSet():
				break
		self.setStatus('idle')

	def stop(self):
		self.stopevent.set()

	def test(self):
		self.handleTargetListDone()
