def rename_key(dictionary):
    dictionary['location'] = dictionary.pop("city")
    return dictionary


sampleDict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
print("Old dictionary : ", sampleDict)
print("New dictionary : ", rename_key(sampleDict))
