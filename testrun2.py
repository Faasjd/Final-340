import sqlite3
conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()
sql = "insert into celebs values (?, ?, ?, ?, ?, ?, ?)"
data = ((1, "Angelina", "Jolie", 40, "angie@hollywood.us", "http://www.nphinity.com/pics/aj.jpg", "Angelina Jolie is an American actress, filmmaker, and humanitarian. She has received an Academy Award, two Screen Actors Guild Awards, and three Golden Globe Awards"),
        (2, "Brad", "Pitt", 51, "brad@hollywood.us", "http://www.nphinity.com/pics/bp.jpg", "William Bradley Pitt is an American actor and film producer. He has received multiple awards and nominations including an Academy Award as producer under his own company Plan B Entertainment."),
        (3, "Snow", "White", 21, "sw@disney.us", "http://www.nphinity.com/pics/sw.jpg", "The Grimm fairy tale gets a Technicolor treatment in Disney's first animated feature. "),
        (4, "Darth", "Vader", 29, "dv@darkside.me", "http://www.nphinity.com/pics/dv.jpg", "Discovered as a slave on Tatooine by Qui-Gon Jinn and Obi-Wan Kenobi, Anakin Skywalker had the potential to become one of the most powerful Jedi ever, and was believed by some to be the prophesied Chosen One who would bring balance to the Force. "),
        (5, "Taylor", "Swift", 51, "ts@1989.us", "http://www.nphinity.com/pics/ts.jpg", "Taylor Alison Swift is an American singer-songwriter. One of the world's leading contemporary recording artists, she is known for narrative songs about her personal life, which have received widespread media coverage."),
        (6, "Beyonce", "Knowles", 34, "beyonce@jayz.me", "http://www.nphinity.com/pics/bk.jpg", "Beyoncé Giselle Knowles-Carter is an American singer, songwriter, actress, record producer, and dancer. Born and raised in Houston, Texas, Beyoncé performed in various singing and dancing competitions as a child. She rose to fame in the late 1990s as lead singer of the R&B girl-group Destiny's Child."),
        (7, "Selena", "Gomez", 23, "selena@hollywood.us", "http://www.nphinity.com/pics/sg.jpg", "Selena Marie Gomez is an American singer, actress, and producer. After appearing on the children's television series Barney & Friends, she received wider recognition for her portrayal of Alex Russo on the Disney Channel television series Wizards of Waverly Place,"),
        (8, "Stephen", "Curry", 27, "steph@golden.bb", "http://www.nphinity.com/pics/sc.jpg", "Wardell Stephen Curry II is an American professional basketball player for the Golden State Warriors of the National Basketball Association. Many players and analysts have called him the greatest shooter in NBA history."))


cursor.executemany(sql, data)
conn.commit()



conn.close()
