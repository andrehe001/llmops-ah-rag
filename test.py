import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
data = {
"question": "How can I request a refill for my prescription at Lamna Healthcare?", 
"chat_history": []
}

body = str.encode(json.dumps(data))

url = 'https://rag-0313-endpoint.eastus2.inference.ml.azure.com/score'
# Replace this with the primary/secondary key, AMLToken, or Microsoft Entra ID token for the endpoint
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjNQYUs0RWZ5Qk5RdTNDdGpZc2EzWW1oUTVFMCIsImtpZCI6IjNQYUs0RWZ5Qk5RdTNDdGpZc2EzWW1oUTVFMCJ9.eyJhdWQiOiJodHRwczovL21sLmF6dXJlLmNvbSIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzE2YjNjMDEzLWQzMDAtNDY4ZC1hYzY0LTdlZGEwODIwYjZkMy8iLCJpYXQiOjE3Mjk1MTM2NzEsIm5iZiI6MTcyOTUxMzY3MSwiZXhwIjoxNzI5NTE4ODU5LCJhY3IiOiIxIiwiYWlvIjoiQWZRQUMvOFlBQUFBeEsxdUp3ZW9rbVFUblc3SU1OVmpPSWZYM2llZ05HZkVNS2RqWkJjbkd4NTJVQmNZR285SHU1WFB3RjJsRXllbWt4MVdlQ1QyZWo0dDVCYXh3S1JCMGRZNnVwNHlIMG03ZTlxT2NISWMvR2pmaTZvVEd4VHdOUEZ3aksxTTVXWFc5VmdnQld2akg1Z2JzNHpma3RFMVpJT3FkN1VydmlLWmZGZ3pvdFBBalJiS2RBWUhRNXZlMVI5Y2tBT2tpQTJLbjRBTFpGdTVWdXV6Yk5FajRHZEFXSDJtdUZOUitBNnlhYzRoMXdFcUJ6QVBvQkc3Z2JqeWVtSXRZRktxeFN0LytLUmthSWJTRVAzZTZPTGNDM3cyMzZxT3IzS3FlUDA0L0VvZnNFWitPZU9pY1BtUGFIZHZvWnRadDA3OGJGbE0iLCJhbHRzZWNpZCI6IjU6OjEwMDMwMDAwODAxQzI1REQiLCJhbXIiOlsicHdkIiwiZmlkbyIsInJzYSIsIm1mYSJdLCJhcHBpZCI6ImNiMmZmODYzLTdmMzAtNGNlZC1hYjg5LWEwMDE5NGJjZjZkOSIsImFwcGlkYWNyIjoiMCIsImRldmljZWlkIjoiMmQ1MWFlMmEtYzRlYy00NThmLTg2YzYtOWI3MDExMWMzYjVlIiwiZW1haWwiOiJBbmRyZS5IZWltQG1pY3Jvc29mdC5jb20iLCJmYW1pbHlfbmFtZSI6IkhlaW0iLCJnaXZlbl9uYW1lIjoiQW5kcmUiLCJncm91cHMiOlsiYjEzMDQwMjItMDhlNi00NDdkLWIwOTQtMTUzNzA1OTdjNmI2IiwiMDk1MzFhNzItMmMzZS00ZTA2LWJlMWUtMjU5NmJkMDhkY2RkIiwiZDM0YzRlYmUtNDk4NC00OTAzLWE2NGQtOGMyMDI4M2Q1MTZiIiwiZTMwOTZkZjctYjY1Yy00ZTMyLWFiMWEtN2EzNWRjNjg0ZjBhIl0sImlkcCI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzcyZjk4OGJmLTg2ZjEtNDFhZi05MWFiLTJkN2NkMDExZGI0Ny8iLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiIyMC4xMDcuNDYuMjA5IiwibmFtZSI6IkFuZHJlIEhlaW0iLCJvaWQiOiJjYzIzMDNmYy00MGQ5LTQxMGYtYWI2Ny1hOTU2NjFiNDZlM2YiLCJwdWlkIjoiMTAwMzIwMDIwQkYwMzAzNiIsInJoIjoiMC5BVVlBRThDekZnRFRqVWFzWkg3YUNDQzIwMTl2cGhqZjJ4ZE1uZGNXTkhFcW5MN3hBS2suIiwic2NwIjoidXNlcl9pbXBlcnNvbmF0aW9uIiwic3ViIjoib2FWLTIyOW91TDVUa1NlNVVlNXBUOGtCUTZTb2JhWlZMcks2MXlzMDlSRSIsInRpZCI6IjE2YjNjMDEzLWQzMDAtNDY4ZC1hYzY0LTdlZGEwODIwYjZkMyIsInVuaXF1ZV9uYW1lIjoiQW5kcmUuSGVpbUBtaWNyb3NvZnQuY29tIiwidXRpIjoibXJLZ1VNcUo4a09wYm1RQWdqSXRBQSIsInZlciI6IjEuMCIsInhtc19pZHJlbCI6IjEgMjYifQ.FC5QnB0p4EmoNnLlMFKYuLvoxla5YMQyvpsnry2QBncvdo_08Pq5GHE7orJkeC1gVw729Dv-EmqTf32FXLHFTVRFSdd-4KUjzW30P1NPdn_X-2-QIBKoK_8bftorvYpTf0NRsyB2pwYuL3fkfyYQRpFd8dxXRzv7ZNNJaOPxpR51tYMsTScx4Uc-sP8mF3_QWyJnYF8tNiJtWC5BMzSTVZ-iJL1N4t0jI7u8hf8ME9lHoKbekleZQ5ZI9_DQW1E78J_CoWPT12RVOa1tQBISAN8Sm81s9tm5mdHl6YOp9YjkjYlua1igjw7ZePHb23vXpRl_2xneFEA01F2dYOYXHg'
if not api_key:
    raise Exception("A key should be provided to invoke the endpoint")


headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))