score = []
total = inscore = 0
num1=num2=num3=0
while(inscore != -1):
    inscore=int(input("請輸入學生成績："))
    score.append(inscore)
numofstudent=len(score)-1
print("共有 %d 位學生" % (numofstudent))
for i in range(0, numofstudent):
    total += score[i]
average = total / numofstudent
score.sort()
score.reverse()
num1=score[0]
num2=score[1]
num3=score[2]
print("本班總成績：%d 分，平均成績：%5.2f 分" % (total, average))
print("本班前三名分數：第一名 %d分 第二名 %d分 第三名 %d分" % (num1,num2,num3))
