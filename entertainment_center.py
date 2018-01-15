import fresh_tomatoes
import media

# instances for class Movie
inception = media.Movie("Inception", "Dom Cobb (Leonardo DiCaprio) is a thief with the rare ability to enter people's dreams and steal their secrets from their subconscious. His skill has made him a hot commodity in the world of corporate espionage but has also cost him everything he loves. Cobb gets a chance at redemption when he is offered a seemingly impossible task: Plant an idea in someone's mind. If he succeeds, it will be the perfect crime, but a dangerous enemy anticipates Cobb's every move.",
						"https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
						"https://www.youtube.com/watch?v=YoHD9XEInc0")

up = media.Movie("Up", "Carl Fredricksen (Ed Asner), a 78-year-old balloon salesman, is about to fulfill a lifelong dream. Tying thousands of balloons to his house, he flies away to the South American wilderness. But curmudgeonly Carl's worst nightmare comes true when he discovers a little boy named Russell is a stowaway aboard the balloon-powered house.",
				"https://images-na.ssl-images-amazon.com/images/M/MV5BMTk3NDE2NzI4NF5BMl5BanBnXkFtZTgwNzE1MzEyMTE@._V1_UY1200_CR83,0,630,1200_AL_.jpg",
				"https://www.youtube.com/watch?v=ORFWdXl_zJ4")

love_actually = media.Movie("Love Actually", "Nine intertwined stories examine the complexities of the one emotion that connects us all: love. Among the characters explored are David (Hugh Grant), the handsome newly elected British prime minister who falls for a young junior staffer (Martine McCutcheon), Sarah (Laura Linney), a graphic designer whose devotion to her mentally ill brother complicates her love life, and Harry (Alan Rickman), a married man tempted by his attractive new secretary.",
							"http://t1.gstatic.com/images?q=tbn:ANd9GcR-yz1sgpd6sn0JuYHhl6JTUNZT6tpe0Jv8znAb7yn7yrGOD3lK",
							"https://www.youtube.com/watch?v=ZmUaH-n_wbA")

life_of_pi = media.Movie("Life Of Pi", "After deciding to sell their zoo in India and move to Canada, Santosh and Gita Patel board a freighter with their sons and a few remaining animals. Tragedy strikes when a terrible storm sinks the ship, leaving the Patels' teenage son, Pi (Suraj Sharma), as the only human survivor. However, Pi is not alone; a fearsome Bengal tiger has also found refuge aboard the lifeboat. As days turn into weeks and weeks drag into months, Pi and the tiger must learn to trust each other if both are to survive.",
						"http://t2.gstatic.com/images?q=tbn:ANd9GcQLik2EaN6bm4GQBKTvI7uIlH4b5kQ29IhY1Tqh_nEoHkUsru82",
						"https://www.youtube.com/watch?v=j9Hjrs6WQ8M")

call_me_by_your_name = media.Movie("Call Me by Your Name", "It's the summer of 1983, and precocious 17-year-old Elio Perlman is spending the summer with his family at their 17th-century villa in Lombardy, Italy. He soon meets Oliver, a handsome doctoral student who's working as an intern for Elio's father. Amid the sun-drenched splendor of their surroundings, Elio and Oliver discover the heady beauty of awakening desire over the course of a summer that will alter their lives forever.",
									"https://i0.wp.com/teaser-trailer.com/wp-content/uploads/Call-Me-By-Your-Name-Movie-2.jpg?ssl=1",
									"https://www.youtube.com/watch?v=5rgO_TyyOoU")

momento = media.Movie("Momento", "Leonard is tracking down the man who raped and murdered his wife. The difficulty, however, of locating his wife's killer is compounded by the fact that he suffers from a rare, untreatable form of memory loss. Although he can recall details of life before his accident, Leonard cannot remember what happened fifteen minutes ago, where he's going, or why.",
					  "http://www.gstatic.com/tv/thumb/movieposters/28578/p28578_p_v8_af.jpg", 
					  "https://www.youtube.com/watch?v=0vS0E9bBSL0")

# making a list of movie
movies = [inception, up, love_actually, life_of_pi, call_me_by_your_name, momento]

fresh_tomatoes.open_movies_page(movies)


