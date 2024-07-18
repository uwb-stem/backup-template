import sys
import re
import os
from bs4 import BeautifulSoup

def update_html(filename):
    
    with open(filename, 'r', encoding='latin-1') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    links = soup.find_all('a', href=re.compile(r'^https://depts\.washington\.edu/stemadv/'))

    for link in links:
        current_href = link['href']
        
        relative_path = re.sub(r'^https://depts\.washington\.edu/stemadv/', './', current_href)
        relative_path = relative_path.split('/')
        link['href'] = relative_path[-1]

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(str(soup))

    print(f"'{filename}' has been updated.")

def get_html_files(directory):
    html_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    return html_files

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python prep.py <<html dir>>")
        sys.exit(1)
    
    html_files_dir = sys.argv[1]
    html_file_list = get_html_files(html_files_dir)
    for file in html_file_list:
        update_html(file)

