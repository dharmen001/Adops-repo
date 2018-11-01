import json
import requests
from requests.auth import HTTPBasicAuth


url = "https://<jira-url>/rest/api/2/issue"
header = {'Content-Type': 'application/json'}
#set the user name and password values
user = https://neomediaworld.atlassian.net/secure/BrowseProjects.jspa?page=1&selectedCategory=all&selectedProjectType=all&sortKey=name&sortOrder=ASC

# block for setting the JIRA password
password = <passwd>

#setting the file from which to read the JSON which will be passed into the JIRA API
jiraF=open("/root/data.txt","r")
jira_load=jiraF.read()
#make the authenticated request to the JIRA API
r = requests.post(url, data=jira_load, headers=header, auth=HTTPBasicAuth(user, password))
print ("HERE's the JSON RESPONSE\n\n ", r.status_code, r.headers)
print ("The response content is\n\n", r.content)