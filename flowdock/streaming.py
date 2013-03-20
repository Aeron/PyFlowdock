# coding: utf-8
import json
import requests

STREAMING_API_URL = 'https://stream.flowdock.com/flows'
DEFAULT_CONTENT_TYPE = 'application/json'


class StreamingAPI(object):
	API_URL = STREAMING_API_URL
	ALLOWED_STATUSES = (True, 'idle', None)
	STREAM_CHUNK_SIZE = 128

	def __init__(self, personal_api_token, accept=DEFAULT_CONTENT_TYPE):
		self.personal_api_token = personal_api_token
		self.accept = accept
		self.flows = None
		self.active = None
		self.headers = {
			'content-type': DEFAULT_CONTENT_TYPE,
			'accept': self.accept,
		}
		self.auth = (self.personal_api_token, '')
		self.connection = None

	def __repr__(self):
		return "%s(%s, %s, %s, %s) instance at %s" % (self.__class__.__name__, self.personal_api_token, self.flows, self.active, self.accept, hex(id(self)))

	@property
	def params(self):
		params = {
			'filter': ','.join(self.flows) if isinstance(self.flows, list) else self.flows,
			'active': self.active,
		}
		return params

	@property
	def stream(self):
		if not self.connection or not self.connection.ok:
			self.connection = requests.get(self.API_URL, params=self.params, headers=self.headers, auth=self.auth, stream=True)
			if not self.connection.ok:
				self.connection.raise_for_status()
		return self.connection

	def fetch(self, flows, active=None, plain=False):
		assert isinstance(flows, (list, basestring)), 'The `flows` argument must be string or list instance.'
		assert active in self.ALLOWED_STATUSES, 'The `active` argument must be in %s.' % str(self.ALLOWED_STATUSES)
		self.flows = flows
		self.active = active
		for line in self.stream.iter_lines(self.STREAM_CHUNK_SIZE):
			if line and line != ':':
				if not plain and self.accept == DEFAULT_CONTENT_TYPE:
					yield json.loads(line)
				yield line


def JSONStream(personal_api_token):
	return StreamingAPI(personal_api_token)


def EventStream(personal_api_token):
	return StreamingAPI(personal_api_token, accept='text/event-stream')
