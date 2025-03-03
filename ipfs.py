import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	json_payload = json.dumps(data)
	pinata_url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"

	headers = {
		"Content-Type": "application/json",
		"pinata_api_key": "e3605dfe9f4726f40fb9",
		"pinata_secret_api_key": "e0910fd751f0d6dd7969b1442bf78936a573e36e97f86d342446e5fe0dd18d96"
	}

	try: 
		response = requests.post(pinata_url, data=json_payload, headers=headers)

		if response.ok: 
			cid = response.json().get("IpfsHash", None)
		
		else: 
			raise Exception(f"failed to pin data: {response.text}")

	except requests.exceptions.RequestException as e: 
		raise Exception(f"error: {e}")

	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	
	ipfs_gateway_url = f"https://gateway.pinata.cloud/ipfs/{cid}"
	
	try:
    response = requests.get(ipfs_gateway_url)

    if response.ok:
      if content_type == "json":
        data = response.json()  
      else:
        data = response.text 
    else:
      raise Exception(f"Failed to get data: {response.text}")

	except requests.exceptions.RequestException as e:
    raise Exception(f"Error: {e}")

	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data
