try:
    from flask import Flask, jsonify, request 
    from flask_restful import Resource, Api
except Exception as E:
    print("Can not import flask\n")
    print("Exception: ")
    print(E)

import _thread as thread

try:
    import json
except Exception as E:
    print("Could not import json\n")
    print("Exception: ")
    print(E)

class _Poster(Resource):
    def post(self):
        m = str(request.get_data().decode('utf-8')).replace("'",'"')
        try:
            data = json.loads(m)
        except Exception as E:
            print("Could not parse JSON")
            print("Exception: ")
            print(E)
            data = json.dumps("{}")
        return {},200


class Server():
    def __init__(self,host=None,port=None,debug = False, default_route='/'):
        super().__init__()
        self.default_route = default_route
        self.host = host
        self.port = port
        self.debug = debug
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_resource(_Poster, self.default_route)
        self.responses = []

    def run(self):
        def start():
            self.app.run(host=self.host,port=self.port,debug=self.debug)
        start()
        #thread.start_new_thread(start, ())


    def add_response(self,_callback=None):
        self.responses.append(_callback)
