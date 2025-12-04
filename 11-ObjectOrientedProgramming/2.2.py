class Music():
    def __init__(self,performer,title,album,year):
        self.performer = performer
        self.title = title
        self.album = album
        self.year = year
    def __str__(self):
        return f'Performer: {self.performer}\nTitle: {self.title}\nAlbum: {self.album}\nYear: {self.year}'
m1 = Music('Ed Sheeren','Hearts Dont Break Around Here','Divide',2017)
print(m1)
print()
m2 = Music('Queen','Bohemian Rhapsody','A Night at the Opera',1975)
print(m2)