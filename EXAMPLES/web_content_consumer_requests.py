import sys
import requests
from pprint import pprint

BASE_URL = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'  # <1>

API_KEY = 'b619b55d-faa3-442b-a119-dd906adc79c8' # <2>

# sample URL
# https://www.dictionaryapi.com/api/v3/references/collegiate/json/voluminous?key=your-api-key

def main(args):
    if len(args) < 1:
        print("Please specify a search term")
        sys.exit(1)

    # requests.post(url, data={....})  # create record
    # requests.put(url, data={...})    # update all fields in record
    # requests.patch(url, data={...})  # update some fields in record
    # requests.delete(url, params={id=1234})  # delete record
    # requests.get(url)  # get all records
    # requests.get(url, params={id=1234})  # get one record
    response = requests.get(
        BASE_URL + args[0],
        params={'key': API_KEY},  #  ?key=API_KEY
        # ssl, proxy, cookies, headers, etc.
    )  # <3>

    if response.status_code == requests.codes.OK:  # 200?
        print('=' * 50)
        print('=' * 50)
        print(response.text)
        print('=' * 50)
        print('=' * 50)
        data = response.json()  # <4>   # convert JSON to Python data structure (lists/dicts)
        print('-' * 60)
        print('-' * 60)
        pprint(data)
        print('-' * 60)
        print('-' * 60)
        for entry in data: # <5>
            if isinstance(entry, dict):
                meta = entry.get("meta")
                if meta:
                    part_of_speech = '({})'.format(entry.get('fl'))
                    word_id = meta.get("id")
                    print("{} {}".format(word_id.upper(), part_of_speech))
                if "shortdef" in entry:
                    print('\n'.join(entry['shortdef']))
                print()
            else:
                print(entry)

    else:
        print("Sorry, HTTP response", response.status_code)

if __name__ == '__main__':
    main(sys.argv[1:])
