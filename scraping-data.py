import requests
import xml.etree.ElementTree as ET
import urllib.request
import os
import tarfile

N = 1

# arXiv API for getting the math/physics paper ids
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
    
# Download the source files
for arxiv_id in arxiv_ids:
    url = 'https://arxiv.org/e-print/' + arxiv_id
    filename = arxiv_id + '.tar.gz'
    urllib.request.urlretrieve(url, filename)
    print('Downloaded ' + filename)

for filename in os.listdir('.'):
    print(filename)
    # TODO: error handling when .tar.gz file is not formatted correctly
    if filename.endswith('.tar.gz'):
        # Extract the .tar.gz file
        with tarfile.open(filename) as tar:
            # Find the .tex file in the archive
            tex_file = None
            for member in tar.getmembers():
                if member.name.endswith('.tex'):
                    tex_file = member
                    break
            # If a .tex file is found, extract the tikzpicture block
            if tex_file is not None:
                with tar.extractfile(tex_file) as tex:
                    # Read the .tex file and find the tikzpicture block
                    tikz = ''
                    output_filename = filename.replace('.tar.gz', '.tex')
                    in_tikz = False
                    for line in tex:
                        line = line.decode('utf-8')
                        if '\\begin{tikzpicture}' in line:
                            in_tikz = True
                        if in_tikz:
                            tikz += line
                        if '\\end{tikzpicture}' in line:
                            in_tikz = False
                    with open(output_filename, 'w') as output:
                        output.write(tikz)
                    print('Extracted TikZ code from ' + filename + ' to ' + output_filename)
            else:
                print('No .tex file found in ' + filename)        
