i = []
print(i, type(i), id(i))
i.append(10) #[10]
print(i, type(i), id(i))

i.append(20.5) #[10, 20.5]
print(i, type(i), id(i))

i.append('Sai') #[10, 20.5, 'Sai']
print(i, type(i), id(i))

i.append(True) #[10, 20.5, 'Sai', True]
print(i, type(i), id(i))

i.append(10+20j) #[10, 20.5, 'Sai', True, 10+20j]
print(i, type(i), id(i))

i.append('Sai')#[10, 20.5, 'Sai', True, 10+20j, 'Sai']
print(i, type(i), id(i))
