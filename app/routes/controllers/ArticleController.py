from flask import jsonify, request
import requests
from ...config import main_config as conf


def getArticles():
    perPage = (
        int(request.args.get('perPage'))
        if request.args.get('perPage') is not None
        else 5
    )
    api_key = conf['SEARCH_ENGINE_KEY']
    se_id = conf['SEARCH_ENGINE_ID']
    s_query = 'Artikel Stunting'
    url = conf['SEARCH_ENGINE_URL']
    params = {
        'q': s_query,
        'key': api_key,
        'cx': se_id,
        'lr': 'lang_id',
        'gl': 'ID',
        'num': perPage,
        'filter': 0
        # 'searchType': 'link'
    }

    response = requests.get(url, params=params)
    results = response.json()['items']

    mapped_result = []

    for row in results:
        mapped_result.append(
            {
                'title': row['title'],
                'description': row['snippet'],
                'thumbnail': (
                    row['pagemap']['cse_thumbnail'][0]['src']
                    if 'cse_thumbnail' in row['pagemap']
                    else None
                ),
                'link': row['link'],
            }
        )
    mapped_result = sorted(mapped_result, key=lambda x: x['thumbnail'] is None)

    return jsonify({'results': mapped_result}), 200
