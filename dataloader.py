'''
code to parse  srt files

'''
from datetime import datetime,timedelta,time
from dateutil.parser import parse

class IncompleteDataError(Exception):
    '''some data is missing from the input. please check again'''
    pass

class SRT():
    def __init__(self,filename,movie="",series="",season="",episode=""):
        try:
            self.filename = filename
            if movie == "" and series == "":
                raise IncompleteDataError
            self.movie = movie
            self.series = series
            self.season = int(season)
            self.episode = int(episode)
            self.parsed_data = self.parse()
        except IncompleteDataError:
            print("enter movie or series")
            print("File could not be parsed.")

    def parse(self):
        with open(self.filename,"r", encoding='utf-8-sig') as file:
            data = file.read()
        data = data.split("\n\n")
        print("found {} dialoges".format(len(data)))
        data = [dialogue(d) for d in data if d != ""]
        return data

class dialogue():
    def __init__(self,d = None):
        if d is not None or d != "":
            self.data = d.split("\n")
            self.parse()
        else:
            print("please insert a string")
            return None

    def parse(self):
        # print("parsing.........",self.data)
        self.index = int(self.data[0])-1
        self.time_txt = self.data[1]
        time_txt = self.time_txt.split("-->")
        from_time = parse(time_txt[0].strip())
        self.from_time_txt = from_time.strftime('%H:%M:%S,%f')
        to_time = parse(time_txt[1].strip())
        self.to_time_txt = to_time.strftime('%H:%M:%S,%f')
        # display_time = to_time - from_time
        self.display_time_txt = str((to_time - from_time).total_seconds()) + 'secs'
        self.txt = ' '.join(s for s in self.data[2:]).strip()
        return self

# run inside python shell: exec(open("ingestES.py").read())