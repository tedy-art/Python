movies = {'pushpa': ['Allu arjun', 'rashmika Mandanna'],
          'brahmastra': ['Ranbir Kapur', 'Alia Butt'],
          'Ram setu': ['Akshay Kumar', 'Nusrratt'],
          'KGF': ['Yesh', 'Shriniddi Shetty'],
          'Marri': ['Dhanush', 'kajal Agrawal']}

print("Access movies name : "+'*'*50)
for i in movies:
    print(i)

print('\n')
print("Access movies cast : ",'*'*50)
for i in movies:
    print(movies[i])

print('\n')
print("Access movies name in sequence : ",'*'*50)
for i in movies:
    for j in i:
        print(j , i)