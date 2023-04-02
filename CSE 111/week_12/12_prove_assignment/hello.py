import requests

url = "https://shazam.p.rapidapi.com/search"

querystring = {"term":"Twenty One Pilots - Christmas Saves the Year (Audio)","locale":"en-US","offset":"0","limit":"1"}

headers = {
	"X-RapidAPI-Key": "b02f54d464mshe8ac5bbdebef614p18f6aajsn6439caf64698",
	"X-RapidAPI-Host": "shazam.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)