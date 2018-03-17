from instagram.client import InstagramAPI

access_token = "253561795.758979a.b253259bec024176942b35c93e66c9c3"
client_secret = "e2637540166643cc92c30870af0493fe"

api = InstagramAPI(access_token=access_token, client_secret=client_secret)

recent_media, next_ = api.user_recent_media(user_id="userid", count=10)
for media in recent_media:
   print (media.caption.text)