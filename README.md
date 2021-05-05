# post-lib

Python 3.8 library that creates an API with Flask and allows the user to create easy redirects.

---Requirements---

-flask

-flask_restful

---Usage---

Create a server with: ``server = post_lib.Server()``

Server parameters:

-`host`: (String) specify the location of the API

-`port`: (Int) specify the port of the API

-`debug`: (Bool) run the server in debug mode

-`default_route`: (String) specify the route of the API

Add a responce to the API by: ``server.add_response()``

add_response() parameters:

-`function`: (Function) a function to be called on a POST request by the client. See line 15 in `example.py`

Run the API with: ``server.run()``

