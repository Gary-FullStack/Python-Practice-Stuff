def print_teacher(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}:{value}')


print_teacher(name='bob', job='ninja', topic='sword', topic2='knives')
