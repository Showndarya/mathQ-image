import requests
import xml.etree.ElementTree as ET
import urllib.request

N = 10

url = 'http://export.arxiv.org/api/query'

params = {
    'search_query': 'cat:math* OR cat:physics*',
    'start': '0',
    'max_results': str(N),
    'sortBy': 'submittedDate',
    'sortOrder': 'descending'
}

response = requests.get(url, params=params)
root = ET.fromstring(response.content)

arxiv_ids = []
for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
    arxiv_id = entry.find('{http://www.w3.org/2005/Atom}id').text.split('/')[-1]
    arxiv_ids.append(arxiv_id)

for arxiv_id in arxiv_ids:
    url = 'https://arxiv.org/e-print/' + arxiv_id
    filename = 'archives/'+arxiv_id + '.tar.gz'
    urllib.request.urlretrieve(url, filename)
    print('Downloaded ' + filename)