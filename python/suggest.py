import sys
import http.client
import json
import sys
import os
import requests

def suggest(host, tactic_state, prefix, context):
    print('[SUGGESTION]')
    try:
        data = {'tactic_state': tactic_state, 'prefix': prefix, 'context': context}
        response = json.loads(requests.post(host, json=data).content)
        print('[SUGGESTION]'.join(response['suggestions']))
    except Exception as e:
        print('[ERROR] %s' % str(e))

if __name__ == "__main__":
    HOST = os.environ.get('LLMSTEP_HOST', 'localhost')
    PORT = os.environ.get('LLMSTEP_PORT', 6000)
    SERVER = os.environ.get('LLMSTEP_SERVER', 'DEFAULT')
    if SERVER == 'COLAB':
        URL = HOST
    else:
        URL = f'http://{HOST}:{PORT}'

    suggest(URL, sys.argv[1], sys.argv[2], sys.argv[3])
