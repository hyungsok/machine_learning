import requests

app_id = '500984196594569'
app_secret = 'e041e513960dbe03ae32784fdf01ae28'

payload = {
	'grant_type': 'client_credentials', 
	'client_id': app_id, 
	'client_secret': app_secret
}

file = requests.post('https://graph.facebook.com/oauth/access_token?', params = payload)    
access_token = file.text

print(access_token)