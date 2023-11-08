import requests
import json


def get_vacancies():
    company_id = [1655047, 3737733, 2509634, 42080, 10482480, 5591530, 842621, 853281, 1334502, 1054992]

    all_vacancies = []

    for id in company_id:
        url = f'https://api.hh.ru/vacancies?employer_id={id}&per_page=10'

        response = requests.get(url)
        if response.status_code == 200:
            vacancies = response.json()['items']
            if len(vacancies) > 10:
                vacancies = vacancies[:10]
            all_vacancies.extend(vacancies)
        else:
            print(f'Error: {response.status_code} - {response.reason}')

    with open('all_vacancies.json', 'w', encoding='utf-8') as f:
        json.dump(all_vacancies, f, ensure_ascii=False, indent=4)
get_vacancies()