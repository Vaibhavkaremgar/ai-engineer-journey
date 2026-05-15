# User Input and f-Strings

name = input("enter your name:- ")
age = int(input("enter your age:- "))
if age < 18:
    print(f"{name} is a minor with age {age}")
elif age >= 18 and age < 60:
    print(f"{name} is a adult with age {age}")
else:
    print(f"{name} is a senior citizen with age {age}")
# List and Loop

cinemas = ["KA","chennai love story","sr kalyanamandapam","mem famous","godari gattu paina"]

total_cinemas = 0

for cinema in cinemas:
    if len(cinema) > 10:
        print(f"{name} love's this move called {cinema}")
        total_cinemas+=1
print(f"total movies liked by {name} are {total_cinemas}")

new_movie = input("enter a movie you like:- ")
cinemas.append(new_movie)
for index, cinema in enumerate(cinemas, start=1):
    print(f"{index}.{cinema} ")

print(len(cinemas))


recommendations = {
    "happy": ["Hukum", "Butta Bomma"],
    "sad": ["Roja", "Samajavaragamana"],
    "motivated": ["Hall of Fame", "Believer"]
}

def songs(mood):
    if mood in recommendations:
        return recommendations[mood]
    else:
        return f"not in the playlist!!!  Sorry"
mood = input("enter your mood:- ").lower()

recommend_song = songs(mood)

print(f"{name} your recommended songs are {recommend_song}")

behaviour = {
    "childish" : ["confused", "annoying"],
    "teenager" : ["syck", "reckless"],
    "adult" : ["focused","youthfull"],
    "men" : ["mature", "stressed"],
    "senior" : ["wise","responsible"]
}

if age < 10:
    print(f"{name} is a {behaviour['childish']} person")
elif age >10 and age<18:
    print(f"{name} is a {behaviour['teenager']} person")
elif age>=18 and age<30:
    print(f"{name} is a {behaviour['adult']} person")
elif age>30 and age <=60:
    print(f"{name} is a {behaviour['men']} person")
else:
    print(f"{name} is a {behaviour['senior']} person")


