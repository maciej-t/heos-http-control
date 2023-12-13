Simple python app to control Heos via HTTP calls instead of telnet.
Example usage:
- curl "http://127.0.0.1:8080?ip=192.168.200.206&port=1255&command=heos://players/get_play_state?pid=123456789"

Example response:
{"heos": {"command": "players/get_play_state", "result": "success", "message": "pid=123456789&state=stop"}}
