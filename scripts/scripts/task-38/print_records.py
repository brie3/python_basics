import fcntl


def print_records(path):
    f = open(path, 'r+', encoding='utf-8')
    fcntl.lockf(f, fcntl.LOCK_EX)
    lines = ''
    for line in f:
        lines += line
    print(lines)
