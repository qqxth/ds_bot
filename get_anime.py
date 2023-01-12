import json
import random
from pprint import pprint

import requests


ANIME_COUNT = 125000


def get_anime_data():
    random_anime_id = random.randint(10000, ANIME_COUNT)
    print(f'Anime ID is - {random_anime_id}')
    query = (
        """
        query ($id: Int) {
            Media (id: $id, type: ANIME) {
                title {
                    romaji
                }
            coverImage{
              large
            }
            genres
            isAdult
            seasonYear
            averageScore
          }
        }
        """
    )

    variables = {
        'id': random_anime_id
    }

    url = 'https://graphql.anilist.co'

    response = requests.post(
        url, json={
            'query': query,
            'variables': variables,
        }
    )

    json_response = json.loads(response.content)

    return json_response


def unpack_anime_data(year=2010):
    data = get_anime_data()['data']

    media_data = data['Media']

    while media_data is None or data is None:
        data = get_anime_data()['data']
        try:
            media_data = data['Media']
            if media_data['seasonYear'] < year:
                raise KeyError
        except KeyError:
            media_data = None
        except TypeError:
            media_data = None

    pprint(data)

    cover_image = media_data['coverImage']
    large_image = cover_image['large']

    title = media_data['title']
    romaji_title = title['romaji']

    genres = media_data['genres']

    score = media_data['averageScore']

    info = f"""
{romaji_title}
Genres - [{', '.join(genres)}]
"""

    return {'image': large_image, 'message':info}

