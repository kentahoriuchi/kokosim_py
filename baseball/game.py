import os
from datetime import datetime, date, timedelta


class Game:
    def __init__(self):
        self.today = date.today()
        self.save_text_path = "save.txt"

    def start(self):
        if os.path.exists(self.save_text_path):
            with open(self.save_text_path) as f:
                st = f.read()
                try:
                    self.today = datetime.strptime(st, '%Y-%m-%d')
                except ValueError as e:
                    print(e)

    def do(self):
        while True:
            print("本日は" + self.today.strftime('%Y-%m-%d'))
            command = input("コマンドを入力してください \n 1.次の日に進む \n 2.終了する \n 入力：")
            if command == str(1):
                self.today += timedelta(days=1)
            elif command == str(2):
                break

    def finish(self):
        with open(self.save_text_path, mode='w') as f:
            f.write(self.today.strftime('%Y-%m-%d'))
