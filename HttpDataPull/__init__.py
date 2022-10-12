import datetime
import logging
import requests
import azure.functions as func
import re


def get_yesterday_day_number():
    d = datetime.date.today() - datetime.timedelta(days=1)
    return d.strftime("%d")


def bytes_to_csv(byte_data):
    csv = str(byte_data)[2:-1]
    csv = csv.replace('\\t', ';').replace('\\n', '\n').replace(',', ';')
    return csv


def remove_comment(csv_string):
    final_hash = [pos for pos, char in enumerate(csv_string) if char == '#'][-1]
    csv = csv_string[final_hash + 1:]
    return csv


def remove_spaces(csv_string):
    csv_list = re.split(r';|\n', csv_string)
    for i in range(len(csv_list)):
        csv_list[i] = csv_list[i].lstrip().rstrip()
        if (i + 1) % 5 == 0:
            csv_list[i] += '\n'
    csv = ';'.join(csv)list
    return csv

    
def main(trigger: func.HttpRequest, outputblob: func.Out[str]) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    
    yesterday = get_yesterday_day_number()
    
    data = requests.get('https://www.daggegevens.knmi.nl/klimatologie/uurgegevens',
                    params={'stns': 'ALL', 'start': '202210' + str(yesterday) + '01', 'end': '202210' + str(yesterday) + '24', 'vars': 'PRCP'})

    csv = bytes_to_csv(data.content)
    csv = remove_comment(csv)
    csv = remove_spaces(csv)

    outputblob.set(csv)

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
