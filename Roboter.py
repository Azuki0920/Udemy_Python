import csv

print('こんにちは！私はRobokoです。あなたの名前は何ですか？')
name = str(input("Enter your name: "))

"""
csvファイルの中身があれば、オススメを勧める
その時、オススメ数の一番大きいものから選ぶ。
Yesを返されるまで、おすすめを繰り返す。
"""
with open('roboko_data/Ranking.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)

    l = [row for row in reader]

    sort = sorted(l, reverse=True, key=lambda row: row['Count'])

    for row in sort:
        print("私のオススメのレストランは、{}です。".format(row['Name']),
              "\nこのレストランは好きですか？[yes/no]")
        answer = str(input("Enter your answer:"))

        if answer == "yes" or answer == "Yes":
            break

print('{}さん。どこのレストランが好きですか？'.format(name))
rest = str(input("Enter you like restaurant: "))

print('{}ですね。ご回答ありがとうございます！'.format(rest))

"""
csvファイルに、オススメを記載し、すでに存在している名前であれば、カウントを増やす
名前はキャピタライズする。
"""

with open('roboko_data/Ranking.csv', 'r+', newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    SameName_exist = False

    for row in reader:
        if row['Name'] == rest:
            # カウントする

            SameName_exist = True
            break

    if not SameName_exist:
        fieldnames = ['Name', 'Count']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow({'Name': rest.capitalize(), 'Count': 1})

print('{}さん。ありがとうございました。'.format(name),
      '\n良い一日を！さようなら。')
