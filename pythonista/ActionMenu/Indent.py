# Pythonista editor action to indent selected lines.
#
# See also companion script to outdent selected lines.

import editor

text = editor.get_text()
selection = editor.get_line_selection()
selected_text = text[selection[0]:selection[1]]

replacement = ''
for line in selected_text.splitlines():
    replacement += '    ' + line + '\n'

editor.replace_text(selection[0], selection[1], replacement)
editor.set_selection(selection[0], selection[0] + len(replacement) - 1)
