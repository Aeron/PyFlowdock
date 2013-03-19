# coding: utf-8
import json
import requests
from .exceptions import FlowdockException


STREAMING_API_URL = 'https://stream.flowdock.com/flows'


class StreamingAPI(object):
	API_URL = STREAMING_API_URL
	ALLOWED_CONTENT_TYPE = ('application/json', 'text/event-stream')
	ALLOWED_STATUSES = (True, 'idle', None)

	def __init__(self, personal_api_token, flows, active=True, accept='application/json'):
		assert isinstance(flows, (list, basestring)), 'The `flows` argument must be string or list instance.'
		assert active in self.ALLOWED_STATUSES, 'The `active` argument must be in %s.' % str(self.ALLOWED_STATUSES)
		assert accept in self.ALLOWED_CONTENT_TYPE, 'The `accept` argument must be in %s.' % str(self.ALLOWED_CONTENT_TYPE)
		self.personal_api_token = personal_api_token
		self.flows = flows
		self.active = active
		self.accept = accept
		self.params = {
			'filter': ','.join(self.flows) if isinstance(self.flows, list) else self.flows
		}
		self.headers = {
			'content-type': self.ALLOWED_CONTENT_TYPE[0],
			'accept': self.accept,
		}
		self.auth = (self.personal_api_token, '')
		self.connection = None

	def __repr__(self):
		return "%s(%s, %s, %s, %s) instance at %s" % (self.__class__.__name__, self.personal_api_token, self.flows, self.active, self.accept, hex(id(self)))

	@property
	def stream(self):
		if not self.connection or not self.connection.ok:
			self.connection = requests.get(self.API_URL, params=self.params, headers=self.headers, auth=self.auth, stream=True)
			if not self.connection.ok:
				self.connection.raise_for_status()
		return self.connection

	def fetch(self, plain=False):
		for line in self.stream.iter_lines(128):
			if line and line != ':':
				if not plain and self.accept == self.ALLOWED_CONTENT_TYPE[0]:
					yield json.loads(line)
				yield line
