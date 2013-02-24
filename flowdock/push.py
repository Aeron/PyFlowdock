# coding: utf-8
import requests
from re import match, IGNORECASE
from .exceptions import FlowDockException

PUSH_TEAM_INBOX_API_URL = "https://api.flowdock.com/v1/messages/team_inbox/%s"
PUSH_CHAT_API_URL = "https://api.flowdock.com/v1/messages/chat/%s"

EMAIL = r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
ALPHANUMERIC_UNDERSCORES_WHITESPACE = r'^[a-z0-9_ ]+$'


class PushAPI(object):
	API_URL = None

	def __init__(self, flow_api_token):
		self.flow_api_token = flow_api_token
		self.api_url = self.API_URL % self.flow_api_token

	def __repr__(self):
		return "%s(%s) instance at %s" % (self.__class__.__name__, self.flow_api_token, hex(id(self)))

	def post(self, data):
		data = dict((k, v) for k, v in data.iteritems() if k != 'self' and v is not None)
		response = requests.post(self.api_url, data=data)
		if response.status_code == 500:
			raise FlowDockException(response.content)
		elif response.status_code // 100 == 4:  # all 4xx HTTP errors
			raise FlowDockException(response.json)
		elif response.status_code == 200:
			return True
		response.raise_for_status()


class TeamInbox(PushAPI):
	API_URL = PUSH_TEAM_INBOX_API_URL

	def post(self, source, from_address, subject, content, from_name=None, reply_to=None, project=None, format='html', tags=None, link=None):
		assert match(ALPHANUMERIC_UNDERSCORES_WHITESPACE, source, IGNORECASE), 'The `source` argument must contain only alphanumeric characters, underscores and whitespace.'
		assert match(EMAIL, from_address), 'The `from_address` argument must be a valid email address.'
		return super(TeamInbox, self).post(locals())


class Chat(PushAPI):
	API_URL = PUSH_CHAT_API_URL

	def post(self, content, external_user_name, tags=None):
		assert len(content) <= 8096, 'The `content` argument length must be 8096 characters or less.'
		return super(Chat, self).post(locals())
