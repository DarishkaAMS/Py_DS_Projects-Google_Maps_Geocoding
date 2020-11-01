import os
import datetime
import requests
import pandas as pd
from requests_html import HTML

BASE_DIR = os.path.dirname(__file__)


def url_to_txt(url, filename='world.html', save=False):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        html_text = html_text.encode('utf-8').decode('ascii', 'ignore') # to en/decode
        if save:
            with open(f'world-{year}.html', 'w') as f:
                f.write(html_text)
        return html_text
    return ""

url = "https://www.boxofficemojo.com/year/world/2020"


def parse_and_extract(url, name='2020'):
    html_text = url_to_txt(url)
    r_html = HTML(html=html_text)
    table_class = '.imdb-scroll-table'
    # "a-section imdb-scroll-table mojo-gutter imdb-scroll-table-styles"
    r_table = r_html.find(table_class)

    # print(r_table)

    table_data = []
    header_names = []

    if len(r_table) == 1:
        # print(r_table[0].text)
        parsed_table = r_table[0]
        rows = parsed_table.find('tr')
        # print(rows)
        header_row = rows[0]
        header_columns = header_row.find('th')
        header_names = [data.text for data in header_columns]

        for row in rows[1:]:
            # print(row.text)
            columns = row.find('td')
            row_data = []
            for i, column in enumerate(columns):
                # print(i, column.text, '\n\n')
                row_data.append(column.text)
            table_data.append(row_data)
        df = pd.DataFrame(table_data, columns=header_names)
        path = os.path.join(BASE_DIR, 'data')
        os.makedirs(path, exist_ok=True)
        file_path = os.path.join('data', f'{name}.csv')
        df.to_csv(file_path, index=False)


def run(start_year=None, years_ago=10):
    if start_year == None:
        now = datetime.datetime.now()
        start_year = now.year
    assert isinstance(start_year, int)
    assert isinstance(start_ago, int)
    assert len(f"{start_year}") == 4
    for i in range(0, years_ago + 1):
        url = f"https://www.boxofficemojo.com/year/world/{start_year}/"
        parse_and_extract(url, name=start_year)
        print(f"Finished {start_year}")
        start_year -=1


if __name__ == "__main__":
    run()
    # try:
    #     start = int(sys.argv[1])
    # except:
    #     start = None
    # try:
    #     count = int(sys.argv[2])
    # except:
    #     count = 0
    # run(start_year=start, years_ago=count)
