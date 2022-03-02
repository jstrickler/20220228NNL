import requests
from pprint import pprint
import argparse

BASE_URL = "http://www.omdbapi.com"

API_KEY = '55795d93' # <2>


def main():
    args = get_args()

    raw_data = do_search(args)
    pprint(raw_data)
    # do something with the data ...

def do_search(args):
    requests_params = {'apikey': API_KEY}
    if args.title:
        requests_params['t'] = args.title
    elif args.imdb_id:
        requests_params['i'] = args.imdb_id

    if args.full_plot:
        requests_params['plot'] = 'full'

    response = requests.get(
        BASE_URL,
        params=requests_params,
    )

    if response.status_code == requests.codes.OK:
        # print(response.text)  # raw JSON
        data = response.json()
        return data

    else:
        print("Sorry, HTTP response", response.status_code)

def get_args():
    parser = argparse.ArgumentParser(description="Movie Search")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-t", dest="title", help="search by title")
    group.add_argument("-i", dest="imdb_id", help="search by IMDB ID")
    parser.add_argument("-full_plot", help="Show entire plot", default=False,
                        action="store_true")

    return parser.parse_args()

if __name__ == '__main__':
    main()
