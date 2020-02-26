import json


def post_json_header(client, url, json_dict, token):
    """send post request with header"""
    return client().post(
        url,
        json=json_dict,
        headers={'Authorization': 'Bearer ' + token})
