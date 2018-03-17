import facebook

graph = facebook.GraphAPI(access_token="500984196594569|Pa44ZmiZXoBc7kLH-DB0jrL_nF0", version="2.7")

# Search for places near 1 Hacker Way in Menlo Park, California.
places = graph.search(type='place',
                      center='37.4977339, 127.02821990000007',
                      distance=1000,
                      fields='name,location')

# Each given id maps to an object the contains the requested fields.
for place in places['data']:
    print('%s %s' % (place['name'], place['location'].get('zip')))
    
print("----------------------------------------------------------------------")

# Search for places near 1 Hacker Way in Menlo Park, California.
places = graph.search(type='place', q='커피', fields='name, location')

# Each given id maps to an object the contains the requested fields.
for place in places['data']:
    print('%s %s' % (place['name'], place['location'].get('zip')))
