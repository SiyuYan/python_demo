from sshtunnel import SSHTunnelForwarder
import requests
# remote server address
remote_host = '192.168.1.143'
remote_port = 22
local_host = '127.0.0.1'
local_port = 8080

server = SSHTunnelForwarder(
   (remote_host, remote_port),
   ssh_username='root',
   ssh_password='admin',
   # remote API endpoint address
   remote_bind_address=(local_host, local_port),
   # local bind address
   local_bind_address=(local_host, local_port),
   )

server.start()

headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
r = requests.get('http://127.0.0.1:8080', headers=headers).content
print(r)
server.stop()

# https://blog.ruanbekker.com/blog/2018/04/23/setup-a-ssh-tunnel-with-the-sshtunnel-module-in-python/