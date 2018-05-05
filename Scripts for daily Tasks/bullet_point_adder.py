
# addes bullets and spaces in front of list copied in clipboard
import pyperclip

text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):
	lines[i] = '* ' + lines[i]
text = '\n'.join(lines)

pyperclip.copy(text)
