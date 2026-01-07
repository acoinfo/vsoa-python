import time
import vsoa
from typing import Union

header, payload, errcode = vsoa.fetch(url = 'vsoa://pyserver/echo', passwd='123456', payload = { 'param': { 'hello': 'world' }})
if header:
	print(dict(header), dict(payload))
else:
	print('fetch error:', errcode) # `errcode` is same as client connect error code

client = vsoa.Client()

def onconnect(self, conn: bool, info: Union[str, dict, list]):
	if conn:
		print('Connected, server info:', info)
	else:
		print('disconnected')

client.onconnect = onconnect
client.robot('vsoa://127.0.0.1:3005', '123456')

while True:
	time.sleep(1)

	header, payload, errcode = client.fetch('/echo', payload = { 'param': { 'a': 3 }})
	if header:
		print(dict(header), dict(payload))
	else:
		print('fetch error:', errcode) # `errcode` is same as client connect error code


