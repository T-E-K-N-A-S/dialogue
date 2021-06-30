'''
code to parse  srt files

'''



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
        self.txt = ''.join(s for s in self.data[2:])
        return self



q = SRT("data/S04E01.srt")
data = q.parse()
print("parsed in data")
