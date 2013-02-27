# coding: utf-8
from traceback import format_exception
from logging import Handler, DEBUG
from ..push import TeamInbox


class FlowdockTeamInboxLoggingHandler(Handler):
	def __init__(self, flow_api_token, source="PyFlowdock Logging Helper", from_address='no-reply@example.com', from_name='Logger'):
		# super(FlowdockTeamInboxLoggingHandler, self).__init__()
		Handler.__init__(self)
		self.level = DEBUG
		self.api = TeamInbox(flow_api_token)
		self.source = source
		self.from_address = from_address
		self.from_name = from_name

	def emit(self, record):
		subject = "sent %s message" % record.levelname.lower()
		content = "\n".join(format_exception(*record.exc_info)) if record.exc_info else self.format(record)
		self.api.post(self.source, self.from_address, subject, content, self.from_name)

	def format(self, record):
		record.msg = "<p>%s</p>" % record.getMessage()
		return super(FlowdockTeamInboxLoggingHandler, self).format(record)
