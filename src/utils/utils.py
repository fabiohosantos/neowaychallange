import json
import os
from flask import make_response


JSON_MIME_TYPE = 'application/json'

def json_response(data=None, status=200, headers=None):
    data = data or {}
    headers = headers or {}
    if 'Content-Type' not in headers:
        headers['Content-Type'] = JSON_MIME_TYPE

    return make_response(json.dumps(data), status, headers)


def error_response(error, status=400, headers=None):
    return json_response({'error': error}, status, headers)

def listfiles(path):
	files = []
	for r, d, f in os.walk(path):
		for file in f:
			files.append(os.path.join(r, file))
    if len(files) <= 0 :
        print('Files not found')
            
	return files