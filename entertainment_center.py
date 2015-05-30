import fresh_tomatoes
import media
                     
ameadus = media.Movie("Amadeus",
                      "Mozart's short life, Did Salieri bring it to an end?",
                      "http://upload.wikimedia.org/wikipedia/en/2/2f/Amadeusmov.jpg",
                      "https://www.youtube.com/watch?v=yIzhAKtEzY0")
                      
big_hero_six = media.Movie("Big Hero Six",
                           "A boy and his friendly medical robot",
                           "http://upload.wikimedia.org/wikipedia/en/4/4b/Big_Hero_6_%28film%29_poster.jpg",
                           "http://www.youtube.com/watch?v=bT8qmoCgxZg")


star_wars_new_hope = media.Movie("Star Wars, A New Hope",
                                 "The force brings a new hero to balance the powers in the universe",
                                 "http://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",
                                 "http://www.youtube.com/watch?v=1g3_CFmnU7k")

fearless = media.Movie("Fearless",
                       "A hero, a teacher, a lost soul",
                       "http://upload.wikimedia.org/wikipedia/en/4/4a/Fearless_film.jpg",
                       "https://www.youtube.com/watch?v=23LxENZE8zo")

ong_bak = media.Movie("Ong-Bak",
                      "A village lost a precious treasure, A village hero will get it back",
                      "http://upload.wikimedia.org/wikipedia/en/1/11/ONG-BAK.jpg",
                      "http://www.youtube.com/watch?v=nAYUv9wjV48")

kungfu_hustle = media.Movie("Kung Fu Hustle",
                            "He always wanted to be a Kung Fu Master, little did he know he would be a Kung Fu Hero",
                            "http://upload.wikimedia.org/wikipedia/en/0/00/KungFuHustleHKposter.jpg",
                            "http://www.youtube.com/watch?v=PRbPXbgsKyE")

movies = [ameadus, big_hero_six, star_wars_new_hope, fearless, ong_bak, kungfu_hustle]
fresh_tomatoes.open_movies_page(movies)
