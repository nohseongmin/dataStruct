def dup(cities):
    result_city = []
    s = set()
    for city in cities:
        l1 = len(s)
        s.add(city)
        l2 = len(s)
        if l1 == l2:
            result_city.append(city)
    return result_city

cities = ['incheon', 'seoul', 'incheon', 'gwangju']
# cities = set(cities)    #set으로 변경
# cities.add('incheon')   #set 전용 추가함수
cities.append('incheon')
cities.append('seoul')
print(cities)
print(set(dup(cities))) #중복값이 발생하므로 set을 한번더해서 제거
