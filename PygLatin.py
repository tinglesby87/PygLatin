


vowels= "a","e","i","o","u"




sentence = input("Enter your sentence")
sentence = sentence.split(' ')

for word in sentence:
    if word[0].lower in ["a","e","i","o","u"]:
        print(word[1:]+ 'say')
    else:
        print(word[1:]+word[0]+'ay ')

