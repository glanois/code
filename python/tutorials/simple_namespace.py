""" Demonstrate use of types.SimpleNamespace.

This acts like a mutable collections.namedtuple.
"""

import types

settings = types.SimpleNamespace(
    screen_width=640,
    screen_height=480,
    bg_color=(0, 0, 255))

settings.screen_width, settings.screen_height = 1024, 768

print(settings)

import collections
Marriage = collections.namedtuple('Marriage', ['husband', 'wife'])

simpsons = Marriage(husband='Homer', wife='Marge')

# Error
# s.husband = 'Krusty'

print(simpsons)



