import pprint
import facebook
import json

token = "Enter your personal access token"
graph = facebook.GraphAPI(token)

# choose the fields you want to extract
all_fields = ['message','created_time','description','caption','link','place','status_type']
all_fields = ','.join(all_fields)
posts = graph.get_connections('me','posts',fields=all_fields)

#example for retrieving all the messages I posted on facebook
for postdescription in posts['data']:
    try:
        pprint.pprint(postdescription['message'])
    except:
        pass



