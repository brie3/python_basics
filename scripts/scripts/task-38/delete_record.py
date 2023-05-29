import fcntl


def delete_record(path):
    f = open(path, 'r+', encoding='utf-8')
    fcntl.lockf(f, fcntl.LOCK_EX)
    record = []
    record.append(input('input surname\n'))
    record.append(input('input name\n'))
    lines = ''
    for line in f:
        check = line.split("|")
        if check[0] == record[0] and check[1] == record[1]:
            continue
        else:
            lines += line
    f.seek(0)
    f.write(lines)
    f.truncate()
