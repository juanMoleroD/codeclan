def get_name(person):
    return person["name"]

def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

def likes_to_eat(person, food):
    return food in person["favourites"]["snacks"]

def add_friend(person, new_friend):
    person["friends"].append(new_friend)

def remove_friend(person, friend_to_be_removed):
    person["friends"].remove(friend_to_be_removed)

def total_money(people):
    sum = 0
    for person in people:
        sum += person["monies"]
    return sum