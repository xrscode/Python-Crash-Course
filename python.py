# print(favorite_fruit[:4])
# # Output: blue
 
# print (favorite_fruit[4:])
# # Output: berry

# fruit_prefix = "blue"
# fruit_suffix = "berries"
# favorite_fruit = fruit_prefix + fruit_suffix
 
# print(favorite_fruit)
# # Output: blueberries

# favorite_fruit = 'blueberry'
# print(favorite_fruit[-1])
# # => 'y'
 
# print(favorite_fruit[-2])
# # => 'r'
 
# print(favorite_fruit[-3:])
# # => 'rry'

# company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

# second_to_last = company_motto[-2]
# final_word = company_motto[-4:]

# favorite_fruit_conversation = "He said, \"blueberries are my favorite!\""

# def print_each_letter(word):
#   for letter in word:
#     print(letter)

# favorite_fruit = "blueberry"
# counter = 0
# for character in favorite_fruit:
#   if character == "b":
#     counter = counter + 1
# print(counter)

# print("e" in "blueberry")
# # => True
# print("a" in "blueberry")
# # => False

# print("blue" in "blueberry")
# # => True
# print("blue" in "strawberry")
# # => False

# print("e" in "blueberry" and "e" in "carrot")
# # => False
# print("e" in "blueberry" and not "e" in "carrot")
# # => True

# def contains(big_string, little_string):
#   return little_string in big_string

# def common_letters(string_one, string_two):
#   common = []
#   for letter in string_one:
#     if (letter in string_two) and not (letter in common):
#       common.append(letter)
#   return common

# def username_generator(first_name, last_name):
#     if len(first_name) < 3:
#         user_name = first_name
#     else:
#         user_name = first_name[0:3]
#     if len(last_name) < 4:
#         user_name += last_name
#     else:
#         user_name += last_name[0:4]
#     return user_name
  
    
# def password_generator(user_name):
#     password = ""
#     for i in range(0, len(user_name)):
#         password += user_name[i-1]
#     return password

# favorite_song = 'SmOoTH'
# favorite_song_lowercase = favorite_song.lower()
# print(favorite_song_lowercase)
# # => 'smooth

# string_name.split(delimiter)

# man_its_a_hot_one = "Like seven inches from the midday sun"
# print(man_its_a_hot_one.split())
# # => ['Like', 'seven', 'inches', 'from', 'the', 'midday', 'sun']

# greatest_guitarist = "santana"
# print(greatest_guitarist.split('n'))
# # => ['sa', 'ta', 'a']

# print(greatest_guitarist.split('a'))
# # => ['s', 'nt', 'n', '']

# authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

# author_names = authors.split()
# print(author_names)

# author_last_names = []
# for name in author_names:
#   author_last_names.append(name.split()[-1])
  
# print(author_last_names)

# smooth_chorus = \
# """And if you said, "This life ain't good enough."
# I would give my world to lift you up
# I could change my life to better suit your mood
# Because you're so smooth"""
 
# chorus_lines = smooth_chorus.split('\n')
 
# print(chorus_lines)

# 'delimiter'.join(list_you_want_to_join)

# my_munequita = ['My', 'Spanish', 'Harlem', 'Mona', 'Lisa']
# print(' '.join(my_munequita))
# # => 'My Spanish Harlem Mona Lisa'

# print(''.join(my_munequita))
# # => 'MySpanishHarlemMonaLisa'

# santana_songs = ['Oye Como Va', 'Smooth', 'Black Magic Woman', 'Samba Pa Ti', 'Maria Maria']

# santana_songs_csv = ','.join(santana_songs)
# print(santana_songs_csv)
# => 'Oye Como Va,Smooth,Black Magic Woman,Samba Pa Ti,Maria Maria'

# smooth_fifth_verse_lines = ['Well I\'m from the barrio', 'You hear my rhythm on your radio', 'You feel the turning of the world so soft and slow', 'Turning you \'round and \'round']
 
# smooth_fifth_verse = '\n'.join(smooth_fifth_verse_lines)
 
# print(smooth_fifth_verse)

# featuring = "           rob thomas                 "
# print(featuring.strip())
# # => 'rob thomas'

# featuring = "!!!rob thomas       !!!!!"
# print(featuring.strip('!'))
# # => 'rob thomas       '

# love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

# print(love_maybe_lines[0])
# print(love_maybe_lines[3])

# print(love_maybe_lines[0])
# print('.')
# print(love_maybe_lines[3])
# print('.')
# print(love_maybe_lines[5])


# love_maybe_lines_stripped = []

# for i in love_maybe_lines:
#   love_maybe_lines_stripped.append(i.strip())

#   love_maybe_full = '\n'.join(love_maybe_lines_stripped)

#   print(love_maybe_full)

# string_name.replace(substring_being_replaced, new_substring)

# with_spaces = "You got the kind of loving that can be so smooth"
# with_underscores = with_spaces.replace(' ', '_')
# print(with_underscores)
# # 'You_got_the_kind_of_loving_that_can_be_so_smooth'

# print('smooth'.find('t'))
# # => '4'

# print("smooth".find('oo'))
# # => '2'

# def favorite_song_statement(song, artist):
#   return "My favorite song is {} by {}.".format(song, artist)

# print(favorite_song_statement("Smooth", "Santana"))
# # => "My favorite song is Smooth by Santana."

# def poem_title_card(title, poet):
#   poem_desc = "The poem \"{}\" is written by {}.".format(title, poet)
#   return poem_desc

# def favorite_song_statement(song, artist):
#   return "My favorite song is {song} by {artist}.".format(song=song, artist=artist)

# def favorite_song_statement(song, artist):
#   # this will have the same output as the above example
#   return "My favorite song is {song} by {artist}.".format(artist=artist, song=song)
# highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# print(highlighted_poems)

# highlighted_poems_list = highlighted_poems.split(',')

# highlighted_poems_stripped = []

# for i in highlighted_poems_list:
#   highlighted_poems_stripped.append(i.strip())

# highlighted_poems_details = []

# for i in highlighted_poems_stripped:
#   highlighted_poems_details.append(i.split(':'))

# titles = []
# poets = []
# dates = []

# for i in highlighted_poems_details:
#   titles.append(i[0])
#   poets.append(i[1])
#   dates.append(i[2])

# for i in range(0,len(highlighted_poems_details)):
#     print('The poem {} was published by {} in {}'.format(titles[i], poets[i], dates[i]))

end