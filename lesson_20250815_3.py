# f = open('test.txt', 'w')
# f.write('Test\n')
import csv

# 下記でも書けるが、あまり使わない
# print('My', 'name', 'is', 'Mike', sep='#', end='!', file=f)

# f.close()

s = """\
AAA
BBB
CCC
DDD
"""

# with を使って書けば、close漏れを防げる
with open('test.txt', 'w+') as f:
    f.write(s)
    f.seek(0)
    print(f.read())

# with open('test.txt', 'r') as f:
    # while True:
    #     chunk = 2
    #     line = f.read(chunk)
    #     print(line)
    #     if not line:
    #         break

    # テキストの位置を指定する（あまり使わないかも）
    # f.seek(5)

import string

with open('design/email_temp.txt') as f:
    t = string.Template(f.read())

contests = t.substitute(name='Mike', contents='How are you?')
print(contests)

with open('test2.csv', 'w', newline='') as csv_file:
    fieldnames = ['Name', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Name': 'Mike', 'Count': 5})
    writer.writerow({'Name': 'Nance', 'Count': 2})

with open('test2.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row['Name'], row['Count'])

import os

# print(os.path.exists('test2.csv'))
# print(os.path.isfile('test2.csv'))
# print(os.path.isdir('design'))

# os.rename('test.txt', 'test3.txt')
# os.symlink('test3.txt', 'symlink.txt')

"""
ファイル操作でよく使うライブラリ
import os
import partlib
import glob
import shutil
"""

import tarfile

# with tarfile.open('design.tar.gz', 'w:gz') as tar:
#    tar.add('design')

with tarfile.open('design.tar.gz', 'r:gz') as tar:
    # 以下は全展開
    # tar.extractall(path='design')

    with tar.extractfile('design/email_temp.txt') as f:
        print(f.read())

import glob
import zipfile

with zipfile.ZipFile('design2.zip', 'w') as zip:
    for f in glob.glob('design/**', recursive=True):
        zip.write(f)

with zipfile.ZipFile('design2.zip', 'r') as zip:
    with zip.open('design/email_temp.txt') as f:
        print(f.read())

import datetime

now = datetime.datetime.now()
print(now)
print(now.isoformat())
print(now.strftime('%a, %d %b %Y %H:%M:%S GMT'))

today = datetime.date.today()
print(today)

print(now)
d = datetime.timedelta(weeks=-1)
print(now + d)