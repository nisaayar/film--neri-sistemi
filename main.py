import sqlite3


conn = sqlite3.connect('movies.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY,
    title TEXT,
    genres TEXT,
    description TEXT
)
''')


movies_data = [
    ('The Shawshank Redemption', 'Drama', 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.'),
    ('The Godfather', 'Crime, Drama', 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.'),
    ('The Dark Knight', 'Action, Crime, Drama', 'When the menace known as The Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham.'),
    ('Pulp Fiction', 'Crime, Drama', 'The lives of two mob hitmen, a boxer, a gangster’s wife, and a pair of diner bandits intertwine in four tales of violence and redemption.'),
    ('The Lord of the Rings: The Return of the King', 'Action, Adventure, Drama', 'Gandalf and Aragorn lead the World of Men against Sauron’s army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.'),
    ('Inception', 'Action, Adventure, Sci-Fi', 'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.'),
    ('Interstellar', 'Adventure, Drama, Sci-Fi', 'A team of explorers travel through a wormhole in space in an attempt to ensure humanity\'s survival.'),
    ('Forrest Gump', 'Drama, Romance', 'The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal and other historical events unfold from the perspective of an Alabama man with an extraordinary low IQ.'),
    ('The Matrix', 'Action, Sci-Fi', 'A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.'),
    ('The Lion King', 'Animation, Adventure, Drama', 'A young lion prince is cast out of his pride by his cruel uncle, who claims he killed his father. While the uncle rules with an iron fist, the young prince makes friends and grows up in exile.'),
    ('The Avengers', 'Action, Adventure, Sci-Fi', 'Earth\'s mightiest heroes must come together and learn to fight as a team if they are to stop the mischievous Loki and his alien army from enslaving humanity.'),
    ('Fight Club', 'Drama', 'An insomniac office worker, looking for a way to change his life, crosses paths with a devil-may-care soapmaker, forming an underground fight club.'),
    ('Avatar', 'Action, Adventure, Sci-Fi', 'A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.')
]



cursor.executemany('INSERT INTO movies (title, genres, description) VALUES (?, ?, ?)', movies_data)


conn.commit()


conn.close()