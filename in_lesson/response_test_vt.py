import os
import pprint
import base64


url_id = base64.urlsafe_b64encode("https://www.clalit.co.il/".encode()).decode().strip("=")
print(url_id)



pprint.pprint(os.environ['VT_API'])





