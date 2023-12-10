from flask import Flask, request
import telnetlib

app = Flask(__name__)

denon_ip = '192.168.200.206'
denon_port = 1255

def execute_denon_command(command, ip=denon_ip, port=denon_port):
    try:
        with telnetlib.Telnet(ip, port) as tn:
            tn.write(command.encode('ascii') + b'\r\n')
            response = tn.read_until(b'\r\n', timeout=2).decode('utf-8')
        return response.strip()
    except Exception as e:
        return f"Error: {str(e)}"


@app.route('/', methods=['GET'])
def execute():
    if 'command' in request.args:
         command = request.args.get('command', '')
    if 'ip' in request.args:
         denon_ip = request.args.get('ip', '')
    if 'port' in request.args:
         denon_port = request.args.get('port', '')

    if not command:
       return "[ERROR]: Command is required"+"\r\n", 400

    result = execute_denon_command(command, denon_ip, denon_port)
    return result+"\r\n";


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
