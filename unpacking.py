teacher = {
    'name': 'Ashley',
    'job': 'Instructor',
    'topic': 'Python'
}


def print_teacher(name, job, topic):
    print(name)
    print(job)
    print(topic)


print_teacher(**teacher)
