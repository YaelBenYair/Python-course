# import json
#
import os
import json
import pprint
import base64
import requests
#
# #
# #
# url_id = base64.urlsafe_b64encode("https://www.youtube.com/watch?v=gyt14K0-Pjg&list=RDMM7bnX-6sJZBw&index=8".encode()).decode().strip("=")
# print(url_id)
#
# #
# # pprint.pprint(os.environ['VT_API'])
# with open(os.environ['VT_API']) as fh:
#     key = json.load(fh)
#
# #
# # url_id = 'u-7c258856e3bda2fd372b101207c98bfc0165066b100154f77a455c5b4977069f-1673548531'
# url = f"https://www.virustotal.com/api/v3/urls/{url_id}"
#
# headers = {
#     "accept": "application/json",
#     "x-apikey": key['VT_API']
# }
#
# response = requests.get(url, headers=headers)
#
#
# print(response.status_code)
# print(response.json())
# print(type(response))



# import requests
#
# url = "https://www.virustotal.com/api/v3/urls"
#
# payload = "url=https://www.youtube.com/watch?v=gyt14K0-Pjg&list=RDMM7bnX-6sJZBw&index=8"
# headers = {
#     "accept": "application/json",
#     "x-apikey": "9cae9eddd5c3536f7d033433a13a4e4774d5b51e17e0fe4aa25fcb703d0276ce",
#     "content-type": "application/x-www-form-urlencoded"
# }
#
# response = requests.post(url, data=payload, headers=headers)
#
# print(response.text)

# {
#     "data": {
#         "type": "analysis",
#         "id": "u-3fc486246509cffffc261793b3463d5dfcf520acbc724897a0e2afa9ebea2f07-1673549124"
#     }
# }


# #{
#     "error": {
#         "message": "URL \"aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g_dj1neXQxNEswLVBqZyZsaXN0PVJETU03Ym5YLTZzSlpCdyZpbmRleD04\" not found",
#         "code": "NotFoundError"
#     }
# }
# #
# # # חישוב מתי עשו אנליזה לקישור
# #
from datetime import datetime, timedelta
#
ts = int('1673549492')
#
# if you encounter a "year is out of range" error the timestamp
# may be in milliseconds, try `ts /= 1000` in that case
last_analysis_date = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
print(last_analysis_date)
days_analysis = datetime.utcnow() - datetime.strptime(last_analysis_date, '%Y-%m-%d %H:%M:%S')
print(datetime.utcnow() - datetime.strptime(last_analysis_date, '%Y-%m-%d %H:%M:%S'))
t = timedelta(days=182)
print(t > days_analysis)
#
#
#
#
# import math
# import argparse
#
#
# parser = argparse.ArgumentParser(description='Calculate volume of a Cylinder')
# parser.add_argument('-r', '--radius', type=int, required=True, help='Radius of Cylinder')
# parser.add_argument('-H', '--height', type=int, required=True, help='Height of Cylinder')
#
# args = parser.parse_args()
#
# def cylinder_volume(radius, height):
#     vol = (math.pi) * (radius ** 2) * (height)
#     return vol
#
# if __name__ == '__main__':
#     print(cylinder_volume(args.radius, args.height))














