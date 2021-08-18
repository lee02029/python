#score_file = open("score.txt","a",encoding="utf8")
#score_file.write("\n과학 : 80")
#score_file.write("\n코딩 : 100")
#score_file.close()
#score_file = open("score.txt","r",encoding="utf8")
#print(score_file.readline(), end="")#줄별로 읽기, 한줄로 읽기
#score_file.close()
score_file = open("score.txt","r", encoding="utf8")
while True:
    line = score_file.readlline()
    if not line:
        break
    print(line, end="")
score_file.close()