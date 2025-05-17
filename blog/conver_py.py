import chardet

with open('data_utf8.json', 'rb') as f:
    raw_data = f.read()
    result = chardet.detect(raw_data)
    print(result)