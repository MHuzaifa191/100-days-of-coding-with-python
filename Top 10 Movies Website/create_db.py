import sqlite3

db = sqlite3.connect("movies-list.db")
cursor = db.cursor()
cursor.execute("CREATE TABLE movies (id INT PRIMARY KEY NOT NULL, title varchar(250), year INT, description varchar(250), rating FLOAT, ranking INT, review varchar(250), img_url varchar(250))")
db.commit()

cursor.execute("""INSERT INTO movies (id, title, year, description, rating, ranking, review, img_url) 
               VALUES (1, 
               'Shutter Island', 
               2010, 
               'Teddy Daniels and Chuck Aule, two US marshals, are sent to an asylum on a remote island in order to investigate the disappearance of a patient, where Teddy uncovers a shocking truth about the place.',
                8.2, 
                1,
               'Amazing Movie', 
               'https://static1.cbrimages.com/wordpress/wp-content/uploads/2020/05/shutter-island.jpg')
               """)
db.commit()


res = cursor.execute("SELECT * FROM movies")
movies = res.fetchall()
print(movies)