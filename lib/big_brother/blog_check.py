import yaml
import feedparser
from datetime import datetime, timedelta
import time


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

def check_blogs():
    with open(yaml_file) as students:
        student_data = yaml.load(students)

    student_posts = {}
    target = datetime(2011, 11, 28)
    for student in student_data:
        when = []
        if student.get('feed'):
            print('Checking %s' % student['irc'])

            feed = feedparser.parse(student['feed'])

            size = len(feed.entries)
            for item in feed.entries:
                publish_time = datetime.fromtimestamp(time.mktime(item.date_parsed))
                if publish_time < target:
                    #print('%s is older than %s, ignoring' % (publish_time, target))
                    continue
                when.append(item.updated)

        else:
            print('No feed listed for %s!' % student['irc'])

        student_posts[student['irc']] = len(when)

    target_number = (datetime.today() - target).total_seconds() /\
        timedelta(weeks=1).total_seconds() - 3
    for student, count in student_posts.items():
        if count > target_number:
            print('+++%d %s' % (count, student))
        elif count < target_number:
            print('---%d %s' % (count, student))
        else:
            print('===%d %s' % (count, student))


#ini_to_yaml()
check_blogs()
