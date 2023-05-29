import fcntl


def upsert_record(path):
    f = open(path, 'r+', encoding='utf-8')
    fcntl.lockf(f, fcntl.LOCK_EX)
    record = []
    record.append(input('input surname\n'))
    record.append(input('input name\n'))
    record.append(input('input phone number\n'))
    recordStr = '|'.join(record)+'\n'
    found = False
    lines = ''
    for line in f:
        check = line.split("|")
        if check[0] == record[0] and check[1] == record[1]:
            lines += line.replace(line, recordStr, 1)
            found = True
        else:
            lines += line
    if not found:
        lines += recordStr
    f.seek(0)
    f.write(lines)
    f.truncate()
