
from pbs import grep, git
import pprint


def get_authors():
    lines = grep(git("log"), "Author").split("\n")
    names = [' '.join(line.split()[1:-1]) for line in lines]
    garbage = ['', 'unknown', 'Ralph Bean']
    return [name for name in set(names) if name not in garbage]


def adjust_impact(impact):
    duplicates = {
        "posiden": "Ross Delinger",
        "kaeedo": "Kai Ito",
        "Rabenvald": "Ben Boozer",
        "Remy D": "Remy DeCausemaker",
        "Phil Moccio": "Philip Moccio",
    }
    for old, new in duplicates.iteritems():
        impact[new] = impact[new] + impact[old]
        del impact[old]
    return impact


def _get_impact_per(author):
    first = "c71f302cc5cbc9533b43fd076b76d006d08b6d30"
    last = "01cbd7a77cf3f6cdd4b238c475513252d5bc057b"
    opts = "--author='%s' --oneline --numstat --pretty=format:" % author
    span = "%s..%s" % (first, last)
    lines = git("log %s %s" % (opts, span)).split("\n")
    lines = [line.strip() for line in lines if line.strip()]
    total = 0
    for line in lines:
        try:
            total += sum(map(int, line.split()[:2]))
        except ValueError:
            print "(skipping)", line
    return total


def get_impact(authors):
    raw_impact = dict(zip(authors, map(_get_impact_per, authors)))
    impact = adjust_impact(raw_impact)
    return impact


def get_grades(impact):
    _min, _max = min(impact.values()), max(impact.values())
    for key in impact.keys():
        impact[key] = float(impact[key] - _min) / (_max - _min)
        impact[key] = 75 + impact[key] * 25
    return impact


def main():
    authors = get_authors()
    print "Found %i unique authors." % len(authors)

    impact = get_impact(authors)
    print
    print "Determined the following 'impact' per author:"
    for key, value in impact.iteritems():
        print "", key, value

    grades = get_grades(impact)
    print
    print "Got the following grades per student:"
    for key, value in grades.iteritems():
        print "", key, value


if __name__ == '__main__':
    main()
