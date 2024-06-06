import requests, json, time, random

zip_list = [
	"11120", "11320", "11365", "11526", "11863", "12065", "12347", "12454", 
	"12743", "14152", "14175", "17267", "18139", "18248", "18440", "19147", 
	"19461", "21119", "21120", "21146", "21214", "21368", "21762", "22351", 
	"24191", "24330", "25232", "26132", "26433", "27539", "30292", "34132", 
	"35251", "37162", "39239", "39356", "41101", "41327", "41502", "42836", 
	"43442", "43530", "43653", "44537", "50433", "52230", "53140", 
	"59362", "63219", "64130", "64531", "64547", "69230", "70217", 
	"72470", "73131", "74531", "74935", "75319", "75321", "75323", "76130", 
	"76430", "92131"
]

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
	}

results_list = []

for zip in zip_list:
	url = f"https://dozapotek.se/rest/V1/cepdtech/local-store-catalog/find-by-post-code/1/{zip}/042620/"
	r = requests.get(url, headers=headers)
	response_data = json.loads(r.text)
	inner_json_string = response_data["content"][0]
	inner_data = json.loads(inner_json_string)
	stock_availability = inner_data["stock_availability"]
	print(f"{zip}: {stock_availability}")
	if stock_availability == "Ej i lager":
		stock_availability = 0
	results_list.append((zip, stock_availability))
