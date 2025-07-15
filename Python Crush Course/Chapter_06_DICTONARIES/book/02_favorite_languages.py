favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
# print(favorite_languages)
# print(f"Sarah's favorite language is {favorite_languages['sarah'].title()}.")

# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")

# for name in favorite_languages.keys():
#     print(name.title())
# print("\n\n")
# for language in favorite_languages.values():
#     print(language.title())

# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(name.title())  
#     if name in friends:
#         print(f" Hi {name.title()}, I see your favorite language is {favorite_languages[name].title()}!")

# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for haking the poll.")

print("The following languages have been mentioned")
for language in set(favorite_languages.values()):
    print(language.title())