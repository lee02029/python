def profile(name,age,*lang1):
    print("이름 : {0}\t나이 : \t{1}".format(name,age), end="")
    for lang in lang1:
        print(lang, end="")
    print()
