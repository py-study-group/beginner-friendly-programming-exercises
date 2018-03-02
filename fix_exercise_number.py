import fileinput
counter = 1

input_file = input('Please enter the name of the file you want to edit: ')

# fileinput module let us do changes in the same file
with fileinput.FileInput(files=input_file, inplace=True) as f:
	for line in f:
		if line.startswith('# ex.'):
			replace_line = line
			new_line = ('# ex.{}'.format(counter))
			print(line.replace(replace_line, new_line))
			counter += 1
		else:
			print(line.strip())  # .strip() remove the extra blank lines

print('Editing {} successfully'.format(input_file))
