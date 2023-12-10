from flask import Flask, request
import telnetlib

app = Flask(__name__)

DENON_IP = '192.168.200.206' #Set your Denon Heos player IP if you do not want to use 'ip' in every query
DENON_PORT = 1255 #Default port for Denon Heos, change if needed
DENON_CMD = 'heos://players/get_players' #Default command that will be used if no command specified

def execute_denon_command(command, ip, port):
    try:
        with telnetlib.Telnet(ip, port) as tn:
            tn.write(command.encode('ascii') + b'\r\n')
            response = tn.read_until(b'\r\n', timeout=2).decode('utf-8')
        return response.strip()
    except Exception as e:
        return f"Error: {str(e)}"


@app.route('/', methods=['GET'])
def execute():
    denon_cmd = request.args.get('command', DENON_CMD)
    denon_ip = request.args.get('ip', DENON_IP)
    denon_port = request.args.get('port', DENON_PORT)

    result = execute_denon_command(denon_cmd, denon_ip, denon_port)
    return result+"\r\n";


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
