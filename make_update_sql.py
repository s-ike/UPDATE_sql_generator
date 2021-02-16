import sys
import datetime as dt

prg_name = "make_update_sql"


def open_file(filename, mode):
    try:
        f = open(filename, mode, encoding="UTF-8")
    except OSError as e:
        print(e)
        return None
    else:
        return f


def make_file(filename):
    return open_file(filename, "w")


def read_file(filename):
    return open_file(filename, "r")


def make_sql(filename, table, column, value, ext_where=None):
    input = read_file(filename)
    if not input:
       sys.exit(1)
    now = dt.datetime.now()
    output_filename = prg_name + now.strftime('_%Y%m%d%H%M%S') + '.txt'
    output = make_file(output_filename)
    if not value:
        value = '""'
    output.write('''
UPDATE {table}
SET {column} = {value}
WHERE
email IN (
'''.format(table=table, column=column, value=value).strip())
    for line in input:
        line = line.replace("\n", "\",")
        output.write(f'"{line}')
    output.write(
        '"sXNGzuWwOHjumVGY6KzamxKa0ivBBh@DE3KeS9WayYTvzzWQMFK0kJFXaAxd0"')  # nonce
    output.write(')')
    if ext_where:
        output.write('\nAND ' + ext_where)
    output.write(';')
    input.close()
    output.close()


arg = sys.argv
if 5 <= len(arg) <= 6:
    if len(arg) == 5:
        make_sql(arg[1], arg[2], arg[3], arg[4])
    else:
        make_sql(arg[1], arg[2], arg[3], arg[4], arg[5])
else:
    print("Invalid argument")
