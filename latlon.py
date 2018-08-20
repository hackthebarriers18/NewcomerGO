import urllib.request, re, json

headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'

apikey = "760628d5decbc2753ef07b989107005a"

ipa = "https://www.iplocation.net/find-ip-address"

req = urllib.request.Request(ipa, headers = headers)
f = urllib.request.urlopen(req)
x = f.read().decode("utf-8")
ip = re.findall(r'\d{3}\.\d{3}\.\d{3}\.\d{2,3}', x)

baseurl = "http://api.ipstack.com/%s?access_key=760628d5decbc2753ef07b989107005a" % ip[0]
# info
f = urllib.request.urlopen(baseurl)
json_string = json.loads(f.read())
# print(json_string['latitude'])
# print(json_string['longitude'])
lat = json_string['latitude']
lon = json_string['longitude']
f.close()

with open("out.txt", 'w') as f:
    f.write(str(lat) + '\n' + str(lon))
f.close()
