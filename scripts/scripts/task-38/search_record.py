import fcntl


def search_record(path):
    f = open(path, 'r+', encoding='utf-8')
    fcntl.lockf(f, fcntl.LOCK_EX)
    record = []
    record.append(input('input surname\n'))
    record.append(input('input name\n'))
    found = ''
    for line in f:
        check = line.split("|")
        if check[0] == record[0] and check[1] == record[1]:
            found = line[:len(line)-1]
    if len(found) > 0:
        print("record '" + found + "' found.")
    else:
        print("record not found.")
