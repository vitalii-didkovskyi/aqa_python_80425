adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
print('Issue №1')
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(f"{adwentures_of_tom_sawer}\n")
print('Issue №2')
# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(f"{adwentures_of_tom_sawer}\n")
print('Issue №3')
# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("   ", " ")
print(f"{adwentures_of_tom_sawer}\n")
print('Issue №4')
# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print (f"Літера 'h' зустрічається - {adwentures_of_tom_sawer.count("h")} разів в даному тексті.\n")
print('Issue №5')
# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
count_words = 0
for word in adwentures_of_tom_sawer.split():
    if word.istitle():
        # print(word)
        count_words += 1
print(f"В даному списку {count_words} слів починається з великої літери\n")
print('Issue №6')
# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
find_start_with = adwentures_of_tom_sawer.find('Tom')
index = adwentures_of_tom_sawer.find('Tom', adwentures_of_tom_sawer.find('Tom') + 1)
print(f"Слово 'Tom' має наступний індекс - {index}\n")
# print(f"{index}\n{adwentures_of_tom_sawer[find_start_with:index]}") # w-check
print('Issue №7')
# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('.')
adwentures_of_tom_sawer_sentences = [k.strip() for k in adwentures_of_tom_sawer_sentences if k.strip()]
print(f"{adwentures_of_tom_sawer_sentences}\n")
print('Issue №8')
# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
index3 = 3
print(f"4те речення зі списку - {adwentures_of_tom_sawer_sentences[index3]}")
print(f"Все 4те речення у нижньому регістру - {adwentures_of_tom_sawer_sentences[index3].lower()}\n")
# lover_case = adwentures_of_tom_sawer_sentences[index3].lower()
# print(f"Додатковий приклад 4того речення у нижньому регістрі - {lover_case}\n")
print('Issue №9')
# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
for sentece in adwentures_of_tom_sawer_sentences:
    if sentece.startswith('By the time'):
        print(f"Вивели речення, яке починається з 'By the time':\n{sentece}\n")
print('Issue №10')
# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentence = adwentures_of_tom_sawer_sentences[-1]
print(f"Вивели останне речення зі списку:\n{last_sentence}")
# print(last_sentence.split())
count_words = len(last_sentence.split())
print(f"В даному реченні кількість слів - {count_words}.")
# word_count = len(adwentures_of_tom_sawer_sentences[-1].split())
# print(word_count)
