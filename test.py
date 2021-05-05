import post_lib
import json

def relay(data):
    if 'type' in data.keys():
        if data['type'] == 'request':
            return json.dumps("{'type':'relay','relay':[]}")
        else:
            return False
    else:
        return False

if __name__=="__main__":
    server = post_lib.Server(host="127.0.0.1",port=5000,debug=True)
    server.add_response(relay)
    server.run()