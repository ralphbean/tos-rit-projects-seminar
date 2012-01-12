import pprint as pp
import yaml


planet_file = '../../planet/config.ini'
yaml_file = '../../data/students.yaml'

def ini_to_yaml():
    feeds = {}
    with open(planet_file) as planet:
        planet_data = iter(planet.readlines())

    while not planet_data.next() == '####\n':
        pass

    current = {}
    for line in planet_data:
        if line[0] == '[':
            current['feed'] = line[1:-2]
        elif not line == '\n':
            bits = line.split(' = ')[1].split(None, 1)
            handle = bits[0]
            current['name'] = bits[1].strip('()\n')
            feeds[handle] = current
            current = {}

    with open(yaml_file) as students:
        student_data = yaml.load(students.read(-1))

    for student in student_data:
        if not student['irc'] in feeds:
            print('Student %s not found!' % student['irc'])
            continue

        student['feed'] = feeds[student['irc']]['feed']

    with open(yaml_file, 'w') as students:
        yaml.dump(student_data, students, default_flow_style=False)

ini_to_yaml()
