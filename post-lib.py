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

