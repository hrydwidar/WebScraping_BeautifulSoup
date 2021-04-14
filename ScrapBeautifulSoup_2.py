# %% Run_cell
from bs4 import BeautifulSoup
import requests
import time


def find_jobs(html_URL, unfamiliar_skills):
    html_text = requests.get(html_URL).text       # print(html_request)
    soup = BeautifulSoup(html_text, 'lxml')
    '''1. Just put # noqa at the end of the line and the linters will ignore the line.'''
    '''2. There is a problem in printing Jobs becaues there is something character which'''  # noqa
    '''   'charmap' codec can't encode characters the following two solution for that '''  # noqa
    # jobs = [x.encode('utf-8') for x in jobs]    # print(jobs)
    ''' OR '''
    # print(str(jobs).encode('utf-8'))
    counts = 0
    # %% Run cell
    print(counts)
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        # job = soup.find('li', class_='clearfix job-bx wht-shd-bx')
        published_date = job.find('span', class_='sim-posted').span.text  # print(published_date)  # noqa
        if 'few' in published_date or '1' in published_date or '2' in published_date:  # noqa
            skills = job.find('span', class_='srp-skills').text.strip().split(',')  # noqa
            skills = [x.strip() for x in skills]
            ''' OR  but bad'''
            # skills = job.find('span', class_='srp-skills').text.replace(' ', '').split(',')  # noqa
            ''' https://www.techbeamers.com/program-python-list-contains-elements/ '''  # noqa
            '''
            For debug use breakpoint then
            n (next)  – Continues execution until the next line in the
            current function is reached or it returns
            s (step) – Executes the current line and stop at the first
            possible occasion. This is equivalent to step into on most
            GUI based debuggers
            c (continue) – Continues execution and stops only when
            another breakpoint is encountered.
            p (print) – Takes an expression and prints its output
            l (list) – Lists the source code of the current file
            '''
            # breakpoint()
            if not any(item in skills for item in unfamiliar_skills):
                with open(f'posts/{index}.txt', 'w') as fil:
                    counts += 1
                    company_name = job.find('h3', class_='joblist-comp-name').text.strip()  # noqa
                    more_info = job.header.h2.a['href']
                    # print(f'''
                    #    Company Name : {company_name}
                    #    Required Skills : {skills}
                    #    More info : {more_info}
                    #    ''')
                    fil.write(f"Company Name : {company_name}\n")
                    fil.write(f"Required Skills : {skills}\n")
                    fil.write(f"More info : {more_info}\n")
                print(f'File saved : {index}')
        '''
        To get the table data is pretty straightforward, all the data is inside the div
        with the css classes "table.table--hcs":
        # halo = requests.get("https://www.halowaypoint.com/en-us/esports/standings")
        # page = BeautifulSoup(halo.content, "html.parser")
        # table = page.select_one("div.table.table--hcs")
        # print(",".join([td.text for td in table.select("header div.td")]))
        # for row in table.select("div.tr"):
        #     rank,team = row.select_one("span.numeric--medium.hcs-trend-neutral").text,  # noqa
                            row.select_one("div.td.hcs-title").span.a.text
        #     wins, losses = [div.span.text for div in row.select("div.td.em-7")]
        #     print(rank,team, wins, losses)
        '''
    print(counts)


'''For use of __name__ and '__main__'  '''
'''https://www.freecodecamp.org/news/if-name-main-python-example'''
if __name__ == '__main__':
    unfamiliar_skills = input('Put skills that are not familiar with >').split(',')
    unfamiliar_skills = [item.strip() for item in unfamiliar_skills]
    print(f'Filtering out {unfamiliar_skills} ..............')
    HTML_URL = 'https://www.timesjobs.com/candidate/job-search.html?'\
        'searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='  # noqa
    while True:
        find_jobs(HTML_URL, unfamiliar_skills)
        time_wait = 10
        print(f'Wating {time_wait} minutes....')
        time.sleep(time_wait * 60)
