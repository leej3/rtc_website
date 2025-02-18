AUTHOR = 'John Lee'
SITENAME = 'Rockfield Tennis Club'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

THEME = "themes/bootstrap-5"

STATIC_PATHS = ['images', 'static']

MARKDOWN = {
    'extensions': ['extra', 'codehilite', 'toc'],
    'output_format': 'html5',
}


# Activate the plugin
PLUGINS = []
SITEURL = 'http://localhost:8000'

# Add EXTRA_PATH_METADATA to ensure favicon.ico is copied to the root
EXTRA_PATH_METADATA = {
    'static/favicon.ico': {'path': 'favicon.ico'}
}

def parse_memberships(membership_list):
    memberships = []
    current_membership = {}

    for item in membership_list:
        if item.startswith('- name:'):
            if current_membership:
                memberships.append(current_membership)
            current_membership = {'name': item.split(': ', 1)[1]}
        elif item.startswith('description:'):
            current_membership['description'] = item.split(': ', 1)[1]
        elif item.startswith('price:'):
            current_membership['price'] = item.split(': ', 1)[1]
        elif item.startswith('image:'):
            current_membership['image'] = item.split(': ', 1)[1]

    if current_membership:
        memberships.append(current_membership)

    return memberships

JINJA_FILTERS = {
    'parse_memberships': parse_memberships,
}


# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
