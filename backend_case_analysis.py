import requests, json

def get_response(url, headers=None):
    """Api çağrısı ve response"""
    r = requests.get(url, headers)
    return r

def get_dict(r):
    """Return a set of dicts representing the most popular repositories."""
    response_dict = r.json()
    return response_dict

def get_content_type(r):
    content_type = r.headers["Content-Type"]
    return content_type

if __name__ == '__main__':
    api_url = f'https://flights-api.buraky.workers.dev/'

    r = get_response(api_url)
    json_dict = get_dict(r)

    filename = 'api_dump.json'
    with open(filename, 'w') as f:
        json.dump(json_dict, f, indent=4)


    