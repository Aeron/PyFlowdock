# PyFlowdock
Simple [Flowdock APIs](https://flowdock.com/api) wrapper with some useful helpers. Only [Push API](https://flowdock.com/api/push) (Team Inbox and Chat) and [Streaming API](https://flowdock.com/api/streaming) available at this time.
## Installation
You know how to do it… Right? Just `(sudo) pip install pyflowdock` (not in PyPI at this moment) it or use `(sudo) python setup.py install` inside **pyflowdock** folder.

## How to use it
Simple as a pie…

### Push API
#### Team Inbox

```python
from flowdock import TeamInbox
inbox = TeamInbox('your_flow_api_token')
# With all params
inbox.post('Source', 'from_address@example.com', 'Subject', '<p>Content.</p>', 'From Name', 'reply_to@example.com', 'Project', 'format', ['tags', '@tags', '#tags'], 'http://link.example.com')
# With required params only
inbox.post('Source', 'from_address@example.com', 'Subject', '<p>Content.</p>')
```
##### Required params

+ `source` Human readable identifier of the application that uses the Flowdock API. Only **alphanumeric** characters, **underscores** and **whitespace** can be used;
+ `from_address` Email address of the message sender. The email address is used to show a avatar (Gravatar) of the sender;
+ `subject` Subject line of the message, will be displayed as the title of Team Inbox message;
+ `content` Content of the message, will be displayed as the body of Team Inbox message.

##### Optional params

+ `from_name` Name of the message sender;
+ `reply_to` Email address for replies, will be used when replying to the message from Flowdock;
+ `project` Human readable identifier for more detailed message categorization. Only **alphanumeric** characters, **underscores** and **whitespace** can be used;
+ `format` Format of the message content, default value is "html". Only HTML is currently supported;
+ `tags` Tags of the message, separated by commas;
+ `link` Link associated with the message. This will be used to link the message subject in Team Inbox.


#### Chat

```python
from flowdock import Chat
chat = Chat('your_flow_api_token')
# With all params
chat.post('Content', 'External User Name', ['tags', '@tags', '#tags'])
# With required params only
chat.post('Content', 'External User Name')
```
##### Required params

+ `content` Content of the message. Tags will be automatically parsed from the message content. *Maximum length: 8096 characters*;
+ `external_user_name` Name of the “user” sending the message.

##### Optional params

+ `tags` Tags of the message, separated by commas.

### Streaming API
Streaming API supports two different content types, JSON stream and [Event-Stream](http://dev.w3.org/html5/eventsource/).

#### JSON stream and Event-Stream

```python
from flowdock import JSONStream, EventStream
stream = JSONStream('your_personal_api_token')
# Or
stream = EventStream('your_personal_api_token')
# With all params
gen = stream.fetch('organization/flow', active='idle')
# With required params only
gen = stream.fetch(['organization/flow', 'organization/main'])
for data in gen:
	# do something with `data`
	print data
```
##### Required params

+ `flows` Flow or list of flows to fetch. Only **strings** and **lists** can be used.

##### Optional params

+ `active` Show user as active in Flowdock. Defined values `True`, `'idle'` or `None`. If `None`, user will appear offline. *Default: `True`*;

### Helpers
#### Logging

```python
import logging
from flowdock.helpers import FlowdockTeamInboxLoggingHandler
# With all params
handler = FlowdockTeamInboxLoggingHandler('your_flow_api_token', 'Source', 'from_address@example.com', 'From Name')
# With required params only
handler = FlowdockTeamInboxLoggingHandler('your_flow_api_token')
logger = logging.getLogger('your_logger')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)
logger.debug('Content')
```
