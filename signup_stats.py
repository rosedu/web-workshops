import sys
from collections import defaultdict
import yaml


mail_blacklist = ['google@gigibecali.ro']


def main():
    count = defaultdict(int)
    for document in list(yaml.load_all(sys.stdin))[5:-1]:
        if document['email'] in mail_blacklist:
            continue
        count['_total'] += 1
        value_sunt = document['sunt']
        count['sunt', value_sunt] += 1
        if value_sunt == 'student':
            facultate = document['student-facultate']
            if ('automatica' in facultate.lower() or
                'calculatoare' in facultate.lower()):
                facultate = 'ACS'
            an = document.get('student-an')
            if an == 'I':
                an = '1'
            if an == 'II':
                an = '2'
            if an == 'III':
                an = '3'
            if an and an[0] == '3':
                an = '3'
            count['sunt-student',
                  facultate,
                  an] += 1

        for name in document['topic-stiu']:
            count['stiu', name] += 1

        for name in document['topic-vreau']:
            count['vreau', name] += 1

    from pprint import pprint
    pprint(dict(count))


if __name__ == '__main__':
    main()
