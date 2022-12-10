movies = {}
movies['pushpa'] = ["Allu arjun", "rashmika Mandanna"]
movies['brahmastra'] = ["Ranbir Kapur", "Alia Butt"]
movies['Ram setu'] = ["Akshay Kumar", "Nusrratt"]
movies['KGF'] = ["Yesh", "Shriniddi Shetty"]
movies["Marri"] = ["Dhanush", "kajal Agrawal"]
pr = movies['brahmastra']
re = pr[-1]
usr_list = list(re)
# print(usr_list)
usr_list[1] = 'z'
print(usr_list)
print(movies)