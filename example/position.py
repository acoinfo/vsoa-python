import socket
import vsoa

def onquery(search: dict, reply: callable):
	if search['name'] == 'pyserver':
		reply({ 'addr': '127.0.0.1', 'port': 3005, 'domain': socket.AF_INET })
	else:
		reply(None)

pserv = vsoa.Position(onquery)

pserv.run('0.0.0.0', 3000) # Position server run, never return