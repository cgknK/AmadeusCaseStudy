import requests, json

def get_request_response(url):
    #r_list.append(requests.get(url, headers=headers))
    r = requests.get(url)

    # Store API response in a variable.
    response_dict = r.json()
    #print(type(response_dict))
    #repo_dicts = response_dict['items']

    status_code = r.status_code
    """
    if r.status_code == 200:
        status_code = 200
    elif r.status_code // 100 == 2:
        status_code = 2
    else:
        pass
    """

    response_content_type = r.headers["Content-Type"]

    return response_dict, status_code, response_content_type

if __name__ == '__main__':
    api_url = f'https://flights-api.buraky.workers.dev/'
    sonuclar, durum, content_type = get_request_response(api_url)
    print(durum, content_type)
    
    filename = 'api_dump.json'
    with open(filename, 'w') as f:
        json.dump(sonuclar, f, indent=4)