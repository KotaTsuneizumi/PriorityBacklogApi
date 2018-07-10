# -*- coding: utf-8 -*-

import json
import requests

url = 'https://kotatsu.backlog.jp/api/v2/issues?apiKey=JGKbqgXYOWuJBwKmnq023EnFdiHVG7kIzziEu1xhoIeW02kKJXHVgzLd9fvX1J13'

query = {
        'projectId': '22965', #プロジェクトのID
        }

r = requests.get(url)

print(r)
print(json.dumps(r.json(), sort_keys=True, indent=2))