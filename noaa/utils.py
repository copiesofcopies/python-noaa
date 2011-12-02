import sys
import urllib


def colorize(text, color, stream=sys.stdout):
    if not stream.isatty():
        return text
    if color == "default":
        return text
    COLORS = {"black": 30,
              "red": 31,
              "green": 32,
              "yellow": 33,
              "blue": 34,
              "magenta": 35,
              "cyan": 36,
              "white": 37}
    color_code = COLORS[color]
    return "\x1b[%(color_code)s;1m%(text)s\x1b[0m" % locals()


def any_none(L):
    return any(map(lambda x: x is None, L))


def all_numbers(L):
    try:
        map(float, L)
        return True
    except ValueError:
        return False


def print_tree(tree, indent=4):
    """Print an ElementTree for debugging purposes."""
    def print_elem(elem, level):
        print " " * (indent * level),
        print 'tag="%s"' % elem.tag,
        print 'text="%s"' % elem.text.strip() if elem.text is not None else "",
        print 'attrib=%s' % elem.attrib
        for child in elem.getchildren():
            print_elem(child, level + 1)
    print_elem(tree.getroot(), 0)


def open_url(url, params=None):
    if params:
        query_string = urllib.urlencode(params)
        url = "?".join([url, query_string])

    resp = urllib.urlopen(url)
    return resp
