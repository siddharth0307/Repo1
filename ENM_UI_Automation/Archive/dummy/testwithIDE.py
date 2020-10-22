import requests
import urllib3
from requests_toolbelt.multipart import decoder
from requests_toolbelt import MultipartEncoder
# from cStringIO import StringIO
import json

url_path = "https://enmapache.athtem.eei.ericsson.se/login"
payload = {'IDToken1' : 'administrator', 'IDToken2' : 'TestPassw0rd'}


session = requests.Session()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
rest_res = session.post(url_path, payload, verify=False)
print(rest_res.text)
all_cookies = session.cookies.get_dict()


del all_cookies["AMAuthCookie"]
print(all_cookies)
headers = {'Accept': '*/*', 'Content-Type':'multipart/form-data; boundary=----WebKitFormBoundaryeiOhXc4s8rmxZxCs', 'Content-Length': '199', 'X-Requested-With': 'XMLHttpRequest', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8'}



# g = requests.get("https://enmapache.athtem.eei.ericsson.se/oss/idm/usermanagement/users/administrator", cookies=all_cookies, verify=False)
# # g = requests.get("https://enmapache.athtem.eei.ericsson.se/oss/idm/usermanagement/users/administrator", all_cookies, verify=False)
# print(g.text)


fields = {'command': 'cmedit get * GenericSnmpNodeConnectivityInformation'}
data = MultipartEncoder(fields=fields)
get_node = requests.post("https://enmapache.athtem.eei.ericsson.se/script-engine/services/command", cookies=all_cookies, headers=headers, files=fields, data=None, verify=False)
print(get_node.text)

# data=input_val,

# with_multipart_request = requests('POST', 'https://enmapache.athtem.eei.ericsson.se/script-engine/services/command', files={'name'})
#

