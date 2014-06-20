# Pythonista editor action to outdent selected lines.
#
# See also companion script to indent selected lines.

import editor

text = editor.get_text()
selection = editor.get_line_selection()
selected_text = text[selection[0]:selection[1]]

replacement = ''
for line in selected_text.splitlines():
    if line.startswith('    '):
        replacement += line[4:] + '\n'
    else:
        replacement += line + '\n'

editor.replace_text(selection[0], selection[1], replacement)
editor.set_selection(selection[0], selection[0] + len(replacement) - 1)
