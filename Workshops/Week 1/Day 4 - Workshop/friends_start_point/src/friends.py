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

def lend_money(lender, borrower, amount):
    lender["monies"] -= amount
    borrower["monies"] += amount

def all_favourite_foods(people):
    favfoods = []
    for person in people:
        for snack in person["favourites"]["snacks"]:
            favfoods.append(snack)
    return favfoods

def find_no_friends(people):
    people_with_no_friends = []
    for person in people:
        if person["friends"] == []:
            people_with_no_friends.append(person)
    return people_with_no_friends

def unique_favourite_tv_shows(people):
    unique_tv_shows = set()
    for person in people:
        unique_tv_shows.add(person["favourites"]["tv_show"])
    shows_list = []
    for show in unique_tv_shows:
        shows_list.append(show)
    return shows_list
