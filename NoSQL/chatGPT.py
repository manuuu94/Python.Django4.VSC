import requests
import json
import sseclient
 
def gptMethod(question):
    API_KEY = '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'

    def performRequestWithStreaming():
        newtext = ""
        reqUrl = 'https://api.openai.com/v1/completions'
        reqHeaders = {
            'Accept': 'text/event-stream',
            'Authorization': 'Bearer ' + API_KEY
        }
        reqBody = {
        "model": "text-davinci-003",
        "prompt": question,
        "max_tokens": 100,
        "temperature": 0,
        "stream": True,
        }
        request = requests.post(reqUrl, stream=True, headers=reqHeaders, json=reqBody)
        client = sseclient.SSEClient(request)
        for event in client.events():
            if event.data != '[DONE]':
                # print(json.loads(event.data)['choices'][0]['text'], end="", flush=True),
                newtext = f"{newtext}{json.loads(event.data)['choices'][0]['text']}"
            
        return newtext    

    result = performRequestWithStreaming()
    print(str(result))

gptMethod("What is a doberman?")