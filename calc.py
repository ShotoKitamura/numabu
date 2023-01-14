from math import ceil, floor
get_points = [200, 120, 40, -40, -120, -200]
itemize = ["①", "②", "③", "④", "⑤", "⑥"]
stack_str = ""

#出力する関数
def output_s(output, s):
    output += s
    return output

#目無しかどうか判定する
def is_menasi(basin, num):
  for i in range(num - 1):
    if sum(x >= 6 - num + 1 - i for x in basin) > i:
      print("No menasi-A:num={}, i={}".format(num, i))
      return True
    if sum(x >= 1 - num + i for x in basin) > 6 - i:
      print("No menasi-D:num={}, i={}".format(num, i))
      return True
  if sum(x >= 0 for x in basin) > 6 - num + 1:
    print("No menasi-C:num={}".format(num))
    return True
  for i in range(6 - num):
    if sum(x >= i + 2 for x in basin) > 4 - i:
      print("No menasi-B:num={},i={}".format(num, i))
      return True
  return False

def YushoSentence(now_points, player_num, names):
    target = player_num - 1     #出力するプレイヤー
    basin = []                  
    sentence = ""               #output_sentenceへ出力するメッセージ
    output_sentence = ""        #returnするメッセージ
    i_num = 0                   #itemizeの添え字
    first_and = False           #初めて「かつ」が出た

    #馬身を計算する
    for i in range(len(now_points)):
        basin.append(ceil((now_points[i] - now_points[target]) / (get_points[0] - get_points[1])))
    print(basin)

    for k in range(6):
        if is_menasi(basin, k + 1):
            if k == 0:
                output_sentence = output_s(sentence, "優勝不可能\n(´・ω・｀)")
                first_and = True
            continue
        else:
            sentence = output_s(sentence, itemize[i_num] + str(k + 1) + "位獲得") #ここをコメント
            i_num += 1
            for i in range(len(basin)):
                if i != target:
                    p = 1 - k #修正済み
                    if basin[i] >= p:
                        if basin[i] == 0:
                            if k != 0 or k + 2 + basin[i] != 2:  #←1位のときに2位以下とは出さない
                                if first_and == False:  #←初めてかつ書き込みがあったときの特別処理
                                    if k > 0:
                                        i_num += -1
                                        message = itemize[i_num] + str(k) + "位獲得\n" if k == 1 else itemize[i_num] + str(k) + "位以上獲得\n"
                                        output_sentence = output_s("", message)
                                        i_num += 1
                                        sentence = ""
                                        sentence = output_s(sentence, itemize[i_num] + str(k + 1) + "位獲得") #ここをコメント
                                        i_num += 1
                                    first_and = True
                                if k + 2 + basin[i] != 6:
                                    sentence = output_s(sentence, " かつ {}が{}位以下".format(names[i], k + 2 + basin[i]))
                                else:
                                    sentence = output_s(sentence, " かつ {}が{}位".format(names[i], k + 2 + basin[i]))
                        else:
                            if k != 0 or k + 1 + basin[i] != 2:  #←1位のときに2位以下とは出さない
                                if first_and == False:  #←初めてかつ書き込みがあったときの特別処理
                                    if k > 0:
                                        i_num += -1
                                        message = itemize[i_num] + str(k) + "位獲得\n" if k == 1 else itemize[i_num] + str(k) + "位以上獲得\n"
                                        output_sentence = output_s("", message)
                                        i_num += 1
                                        sentence = ""
                                        sentence = output_s(sentence, itemize[i_num] + str(k + 1) + "位獲得") #ここをコメント
                                        i_num += 1
                                    first_and = True
                                if k + 1 + basin[i] != 6:
                                    sentence = output_s(sentence, " かつ {}が{}位以下".format(names[i], k + 1 + basin[i]))
                                else:
                                    sentence = output_s(sentence, " かつ {}が{}位".format(names[i], k + 1 + basin[i]))
            sentence = output_s(sentence, "\n")
        if first_and == True:
            output_sentence += sentence
        else:
            i_num -= 1
        sentence = ""
    if first_and == False:  #←無条件順位のケース
        temp = now_points.copy()
        del temp[target]
        r = int((now_points[target] - sorted(temp)[-2]) / (get_points[0] - get_points[1])) + 1
        if r == 0:
            r = 1
        if r >= 6:
            output_sentence += "優勝確定!!"
        else:
            output_sentence += "①{}位獲得".format(r)
    return output_sentence