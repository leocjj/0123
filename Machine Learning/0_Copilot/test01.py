# My name is leo and I have 3 years of experience in python
# I am 25 years old
# I am a python developer

def create_file_by_name(name, years):
    with open(name + '.py', 'w') as f:
        f.write(f'# Path: {name}.py')

        f.write(f'# My name is {name} and I have {years} years of experience in python')

        f.write(f'# I am {25} years old')

        f.write(f'# I am a python developer')

create_file_by_name('leo', 3)
create_file_by_name('john', 5)
