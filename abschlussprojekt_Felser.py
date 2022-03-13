import wikipedia
import nltk
import codecs
from nltk.tokenize import sent_tokenize


f_in = codecs.open("wikipedia_articles.txt", "r", "utf-8")

f_out = codecs.open('abschlussprojekt_Felser.txt','w','utf-8')

inhalt = f_in.readlines()




for eintrag in inhalt:
    try:

        p = wikipedia.page(eintrag)

        l = wikipedia.page(eintrag)

        links = l.links

        text = p.content

        sentences = sent_tokenize(text)

        liste = text.split(" ")

        counter_male = 0

        counter_female = 0


        for satz in sentences:
            word_tokenized = nltk.word_tokenize(satz)
            pos = nltk.pos_tag(word_tokenized)



            for tag in pos:
                if tag[0] == "he":
                    counter_male += 1
                if tag[0] == "him":
                    counter_male += 1
                if tag[0] == "his":
                    counter_male += 1
                if tag[0] == "himself":
                    counter_male += 1


            for tag in pos:
                if tag[0] == "she":
                    counter_female += 1
                if tag[0] == "her":
                    counter_female += 1
                if tag[0] == "hers":
                    counter_female += 1
                if tag[0] == "herself":
                    counter_female += 1

        f_out.write("Der Wikipedia Artikel " + "'" + eintrag + "'" + " beinhaltet " + str(len(liste)) + " Woerter\n")
        f_out.write("Der Wikipedia Artikel " + "'" + eintrag + "'" + " beinhaltet " + str(len(links)) + " Links\n")
        f_out.write("Der Wikipedia Artikel " + "'" + eintrag + "'" + " beinhaltet " + str(counter_male) + " maennliche(s) Pronomen\n")
        f_out.write("Der Wikipedia Artikel " + "'" + eintrag + "'" + " beinhaltet " + str(counter_female) + " weibliche(s) Pronomen\n")


    except wikipedia.exceptions.WikipediaException as e:
        pass



    print(links)

  #  print("Der Wikipedia Artikel " + "'" + eintrag + "'" + " beinhaltet " + str(len(liste)) + " Woerter")
  #  print("Der Wikipedia Artikel " + "'" + eintrag + "'" + " beinhaltet " + str(len(links)) + " Links")
  #  print("Der Wikipedia Artikel " + "'" + eintrag + "'" + " beinhaltet " + str(counter_male) + " maennliche(s) Pronomen")
  #  print("Der Wikipedia Artikel " + "'" + eintrag + "'" + " beinhaltet " + str(counter_female) + " weibliche(s) Pronomen")


f_in.close()
f_out.close()


