def data_dict(data: str) -> dict:
	"""
	Turns a CallbackQuery's data into a dictionary.

	### Parameters
	data : str
		Should be in format: `"name=key1:value1,key2:value2"`

	### Returns
	dict
		Dictionary generated from data:  `{key1: value1, key2: value2}`
	"""
	
	data = data.split("=")
	data = data[len(data) - 1]
	
	entries = data.split(",")

	dictionary = {}

	for entry in entries:
		key = entry.split(":")[0]
		value = entry.split(":")[1]

		try:
			value = int(value)
		except ValueError:
			pass

		dictionary[key] = value

	return dictionary