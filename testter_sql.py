import chardet

with open('data.json', 'rb') as f:
    raw_data = f.read()
    result = chardet.detect(raw_data)
    print(result)