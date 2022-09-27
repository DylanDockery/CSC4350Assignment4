#CSC435Assignment4

Simple web server that handles one HTTP request at a time.

Methods:
Handles only GET requests
Returns a HTTP response 200 OK and the requested resource if successful and 404 Not Found  in the event the resource is unavailable.

Instructions:
Server is to be launched from the command line and has the following command line flags.
-p used to declare the port the server will be bound to and is required
-h used to give the help menu to explain operation and other command line flags

Notes:
Potential areas for improvement are the handling of the GET request. There may be a more efficient way to parse the incoming request aside from the string proceiing done in the current version.

Likewise the construction of the GET response may be better handled than the try except structure and the string manipulation currently used. 
