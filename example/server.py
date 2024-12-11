from vsoa.server import Server, Client

data = { "foo": 0 }
server = Server(info='Python VSOA Server', passwd='123456')

def onclient(cli: Client, connect):
	ip, port = cli.address()
	event = "connect" if connect else "disconnect"
	print(f'Client {ip}:{port} {event}')

@server.command('/echo')
def echo(cli, request, payload):
	cli.reply(request.seqno, payload)

@server.command('/foo')
def echo(cli, request, payload):
	print("foo", payload["param"])
	cli.reply(request.seqno, payload)

server.onclient = onclient
server.run('localhost', 3005)