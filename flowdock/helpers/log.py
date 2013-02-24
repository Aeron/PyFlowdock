# coding: utf-8
from logging import Handler, DEBUG
from ..push import TeamInbox


class FlowDockTeamInboxLoggingHandler(Handler):
	def __init__(self, flow_api_token, source="PyFlowDock Logging Helper", from_address='no-reply@example.com', from_name='Logger'):
		super(FlowDockTeamInboxLoggingHandler, self).__init__()
		self.level = DEBUG
		self.api = TeamInbox(flow_api_token)
		self.source = source
		self.from_address = from_address
		self.from_name = from_name

	def emit(self, record):
		subject = "sent %s message" % record.levelname.lower()
		content = record.exc_info or record.msg
		self.api.post(self.source, self.from_address, subject, content, self.from_name)
