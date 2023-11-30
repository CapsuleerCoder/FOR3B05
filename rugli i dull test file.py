# text = ""

# while(len(text) < 1):
#     text = input("Sláðu inn texta: ")

# if text.isdigit():
#     print("Textinn inniheldur bara tölustafi")
# elif text.isalpha():
#     print("Textinn inniheldur bara bókstafi")
# else:
#     print("þú ert kex")

# if __name__ == '__main__':
#     n = int(input())
#     string = ""

#     for i in range(1, n):
#         string = string +str(i)

#     print (string)

# listinn = [[], [], []]

# for t in range(9):
#     if t % 2 == 0:
#         listinn[t%3].append("X")
#     if t % 2 != 0:
#         listinn[t%3].append("O")
# for x in range(3):
#     print (*listinn[x], sep="")



# hofudborgir = ["Róm", "Washington", "Reykjavík", "París", "Kaupamannahöfn"]

# user_city = input("Settu inn nafn höfuðborgar: ")

# if user_city in hofudborgir:
#     print("Er þarna")
# else:
#     add_or_not = input("Þessi borg er ekki í listanum\nViltu bæta henni við? 'J' eða 'N': ").capitalize()
#     if add_or_not == "J":
#         hofudborgir.append(user_city)

# print(hofudborgir)




# grade_list = []
# the_sum = int()
# count_ten = int()
# number_of_students = int(input("Hversu margir nemendur eru? "))

# for i in range(0, number_of_students):
#     user_input = int(input("Settu inn einkun næsta nemanda: "))
#     grade_list.append(user_input)

# for i in grade_list:
#     the_sum += i
#     if i == 10:
#         count_ten += 1

# average_grade = the_sum / user_input
# highest_grade = grade_list[-1]
# lowest_grade = grade_list[0]

# print("Meðaleinkunn var {:.1f}".format(average_grade))
# print(f"Hæðsta einkun var {highest_grade}")
# print(f"Lægsta einkun var {lowest_grade}")
# print(f"Fjöldi nemenda með einkunn '10' var {count_ten}")


word_list = []
cleaned_word_list = []
word_count_dict = dict()
word_set = set()
key_word_list = []

input_file = open("BorgesTilvitnun.txt", "r")
text_string = input_file.read()
input_file.close()

word_list = text_string.split()

for word in word_list:
    cleaned_word = word.strip(",.: ")
    cleaned_lineline = word.split()
    cleaned_word_list.append(cleaned_word)
    word_set.add(cleaned_word)
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1

for key, val in word_count_dict.items():
    key_word_list.append((val, key))
    key_word_list.sort(reverse=True)

commonest_word = key_word_list[0]
unique_words = len(word_set)

print(f"{unique_words} ólík orð eru í skránni og orðið '{commonest_word[1]}' var algengasta orðið og birtist {commonest_word[0]} sinnum")
































