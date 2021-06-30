'''
code to parse  srt files

'''
from datetime import datetime,timedelta,time
from dateutil.parser import parse

class SRT():
    def __init__(self,filename) -> None:
        self.filename = filename

    def parse(self):
        with open(self.filename,"r", encoding='utf-8-sig') as file:
            data = file.read()
        data = data.split("\n\n")
        print("found {} dialoges".format(len(data)))
        data = [dialogue(d).parse() for d in data if d != ""]
        return data

class dialogue():
    def __init__(self,d = None) -> None:
        if d is not None or d != "":
            self.data = d.split("\n")
        else:
            print("please insert a string")

    def parse(self):
        print("parsing.........",self.data)
        self.index = int(self.data[0])-1
        self.time_txt = self.data[1]
        time_txt = self.time_txt.split("-->")
        self.from_time = parse(time_txt[0].strip())
        self.from_time_txt = self.from_time.strftime('%H:%M:%S::%f')
        self.to_time = parse(time_txt[1].strip())
        self.to_time = self.to_time.strftime('%H:%M:%S---%f')
        # self.display_time = self.to_time - self.from_time
        # self.display_time_txt = self.display_time.strftime('%M:%S::%f')
        self.txt = ''.join(s for s in self.data[2:])
        
        return self



q = SRT("data/S04E01.srt")
data = q.parse()
print("parsed in data")

# exec(open("parser.py").read())