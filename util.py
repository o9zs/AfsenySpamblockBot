def data_dict(data: str) -> dict:
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