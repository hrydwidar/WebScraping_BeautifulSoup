from bs4 import BeautifulSoup
# # For disable Typo in comments in PyCharm
# # File -> Settings -> Editor -> Inspections -> Proofreading -> Typo -> From options -> uncheck  Process comments
# import os
# import pathlib
# from IPython import get_ipython  # for magic commands and must run with ipython
# ipython = get_ipython()
# ipython.magic("ls")

# # For the directory of the script being run:
# print(os.path.dirname(os.path.abspath(__file__)))
# print(pathlib.Path(__file__).parent.absolute())
# # For the current working directory:
# print(os.path.abspath(os.getcwd()))
# print(pathlib.Path().absolute())

with open('./home.html', 'r') as html_file:
    content = html_file.read()
    # print(content)

    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())
    # tags = soup.find('h5')
    # courses_html_tags = soup.find_all('h5')
    course_cards = soup.find_all('div', class_='card')
    # for course in courses_html_tags:
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        print(f'{course_name} costs {course_price}')
        print('{} costs {}'.format(course_name, course_price))
