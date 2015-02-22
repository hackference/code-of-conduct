#  -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
try:
    from jinja2 import Template
except:
    print('Something went wrong finding jinja!')
    print('Please run `sudo easy_install jinja2` and try again.')

try: # Py2 hacks
    input = raw_input
except:
    pass

PATH = os.path.dirname(os.path.abspath(__file__))
coc_file = os.path.join(PATH, 'code-of-conduct.md')
with open(coc_file, 'r') as f:
    template = Template(f.read())
    name = input('Event name: ')
    description = input('Event description: ')
    type = input('Enter the type of event (user group, conference): ')
    organiser_name = input('Enter an organiser name: ')
    organiser_number = input('Enter their contact number: ')
    organiser_2_name = input('Enter another organiser name: ')
    organiser_2_number = input('Enter their contact number: ')
    law = input('Enter local law enforcement number: ')
    template = template.render(
        name=name,
        description=description,
        type=type,
        contact_name=organiser_name,
        contact_number=organiser_number,
        second_contact_name=organiser_2_name,
        second_contact_number=organiser_2_number,
        law_enforcement_number=law
    )
with open(coc_file, 'w') as f:
    f.write(template)
print('All done! Be sure to check the document for spelling mistakes.')
