'''
code to parse  srt files

'''



class SRT():
    def __init__(self,filename) -> None:
        self.filename = filename

    def parse(self):
        with open(self.filename,"r", encoding='utf-8-sig') as file:
            data = file.read()
        return data





