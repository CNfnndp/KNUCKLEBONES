from random import choice
import random
"""                                                         #################################################################################################################
┌───┬───┬───┐                                                                                                 距骨骰                    
│ 1 │ 5 │ 1 │                                                                                             by 冯奶奶打牌                
├───┼───┼───┤                                                                                             version: 0.1
│ 4 │ 3 │ 2 │                                                  
├───┼───┼───┤                                                     版本说明：
│ 6 │ 5 │ 2 │                                                         第一个版本，第一次做python项目，共计耗时3天， 这项目也是我学习这门语言之初想做的，完成之后时非常愉悦了。
└───┴───┴───┘                                               #################################################################################################################
  11  23  9
                                        说明：双方的棋盘有九个格子，每一个格子相加，得到的和最大者获胜
  18  22  27                                九个格子分别由三列组成，其中每一列中的数字都可能被影响
┌───┬───┬───┐                                   双方每回合掷一次骰子，之后可以选择将其放入三列中其中一列
│ 2 │ 4 │ 3 │                                       如果自己的某一列出现相同的两个数字，该数字记为自己的两倍
├───┼───┼───┤                               
│ 2 │ 6 │ 6 │                                   双方的每一列都和对方的每一列对应
├───┼───┼───┤                                       如果对方的任意列出现和你对应的列相同数字，则会消除你的该数字
│ 2 │ 0 │ 6 │
└───┴───┴───┘
  ↑   ↑   ↑ ← ← ← # 如果一方中的某一列中出现了相同数字(x)，计算这一列的结果时，该数字记为自己的两倍(x *= 2)
  ↑   ↑
  ↑   ↑ ← ← ← ← ← # 如果对方回合时，选择将数字放入我方同样拥有的该数字的一列，则会消除我方的数字，反之亦然
  ↑
  ↑ ← ← ← ← ← ← ← # 如果一方中的某一列中出现了相同数字三次(x)，计算这一列的结果时，该数字记为自己的三倍(x *= 3)
"""


def coin_winner():
    """抛硬币决定玩家(i = 1)或是电脑先手(i = 0)"""
    # 获取玩家输入
    coin_choose = input ("please choose coin's head or tail\n(1) head\n(2) tail\n>>>")
    if int(coin_choose) == 1:
        print("your choose is head")
        coin_choose = "head"
    elif int(coin_choose) == 2:
        print("your choose is tail")
        coin_choose = "tail"
    
    # 硬币面随机结果反馈给玩家
    coin_result = ["head", "tail"]
    coin_result = choice(coin_result)
    if coin_choose == coin_result:
        print("the coin is %s, you win!" % coin_result)
        return 1
    elif coin_choose != coin_result:
        print("bad luck, the coin is %s" % coin_result)
        return 0


def roll_dice():
    """返回1-6任意数字"""
    return random.randint(1, 6)


def player_which_list():
    """选择要将掷出的点数填入哪一列"""
    global player_which_list1_count, player_which_list2_count, player_which_list3_count, ratau_which_list1_count, ratau_which_list2_count, ratau_which_list3_count, player_list1, player_list2, player_list3
    while True:
        w = input("which list you wish put %d to\n" % player_dice)
        if w == "1":
            if player_which_list1_count < 3:
                player_list1.insert(player_which_list1_count, player_dice)
                remove_same(player_list1, ratau_list1)
                ratau_which_list1_count -= c
                player_which_list1_count += 1
                player_list1.pop()
                
                break
            else:
                print("the list is full")

        elif w == "2":
            if player_which_list2_count < 3:
                player_list2.insert(player_which_list2_count, player_dice)
                remove_same(player_list2, ratau_list2)
                ratau_which_list2_count -= c
                player_which_list2_count += 1
                player_list2.pop()
                
                break
            else:
                print("the list is full")

        elif w == "3":
            if player_which_list3_count < 3:
                player_list3.insert(player_which_list3_count, player_dice)
                remove_same(player_list3, ratau_list3)
                ratau_which_list3_count -= c
                player_which_list3_count += 1
                player_list3.pop()
                
                break
            else:
                print("the list is full")
        else:
            print("don't know what you mean, please choose: left, center, right")


def bot_random_list():
    """随机选择一列为机器人填入"""
    global ratau_which_list1_count, ratau_which_list2_count, ratau_which_list3_count, player_which_list1_count, player_which_list2_count, player_which_list3_count
    while True:
        w = random.randint(1, 3)

        if w == 1:
            if ratau_which_list1_count < 3:
                ratau_list1.insert(ratau_which_list1_count, bot_dice)
                remove_same(ratau_list1, player_list1)
                player_which_list1_count -= c
                ratau_which_list1_count += 1
                ratau_list1.pop()
                
                break
            else:
                print

        elif w == 2:
            if ratau_which_list2_count < 3:
                ratau_list2.insert(ratau_which_list2_count, bot_dice)
                remove_same(ratau_list2, player_list2)
                player_which_list2_count -= c
                ratau_which_list2_count += 1
                ratau_list2.pop()
                
                break
            else:
                print

        elif w == 3:
            if ratau_which_list3_count < 3:
                ratau_list3.insert(ratau_which_list3_count, bot_dice)
                remove_same(ratau_list3, player_list3)
                player_which_list3_count -= c
                ratau_which_list3_count += 1
                ratau_list3.pop()
                
                break
            else:
                print


def turn_to_player():
    """轮到玩家掷骰子，并选择将骰子放入哪一列"""
    global player_colour, bot_colour, player_dice, bot_dice

    player_colour = "roll"
    bot_colour = "next"

    player_dice = roll_dice()
    bot_dice = 0

    input("press enter to roll the dice")
    

def turn_to_ratau():
    """轮到电脑掷骰子，并选择将骰子放入哪一列"""
    global player_colour, bot_colour, player_dice, bot_dice

    bot_colour = "roll"
    player_colour = "next"

    bot_dice = roll_dice()
    player_dice = 0


def sum_multi_same(n):
    """如果一方中的某一列中出现相同数字，进行相加和相乘的计算"""
    if n[0] == n[1] == n[2]:
        same_num = n[0] * 9

    elif n[0] != n[1] != n[2] and n[0] != n[2]:
        same_num = sum(n)
        

    elif n[0] == n[1] or n[0] == n[2]:
        same_num = sum(n) + n[0] * 2

    elif n[1] == n[2]:
        same_num = sum(n) + n[1] * 2 

    return same_num


def chess_board():
    """布置棋盘"""
    global ratau_score, player_score
    ratau_list1_add = sum_multi_same(ratau_list1)
    ratau_list2_add = sum_multi_same(ratau_list2)
    ratau_list3_add = sum_multi_same(ratau_list3)
    ratau_score = sum_multi_same(ratau_list1) + sum_multi_same(ratau_list2) + sum_multi_same(ratau_list3)
    player_list1_add = sum_multi_same(player_list1)
    player_list2_add = sum_multi_same(player_list2)
    player_list3_add = sum_multi_same(player_list3)
    player_score = sum_multi_same(player_list1) + sum_multi_same(player_list2) + sum_multi_same(player_list3)

    ratau_board = ("""
    ┌───┬───┬───┐
    │ %d │ %d │ %d │
    ├───┼───┼───┤
    │ %d │ %d │ %d │   Ratau(%s):
    ├───┼───┼───┤       %d
    │ %d │ %d │ %d │
    └───┴───┴───┘       score: %d
      %d   %d   %d
    """ % (ratau_list1[2], ratau_list2[2], ratau_list3[2], ratau_list1[1], ratau_list2[1], ratau_list3[1],bot_colour, bot_dice, ratau_list1[0], ratau_list2[0], ratau_list3[0],ratau_score, ratau_list1_add, ratau_list2_add, ratau_list3_add))
    
    player_board = ("""
      %d   %d   %d
    ┌───┬───┬───┐
    │ %d │ %d │ %d │
    ├───┼───┼───┤
    │ %d │ %d │ %d │   fnndp(%s):
    ├───┼───┼───┤       %d
    │ %d │ %d │ %d │
    └───┴───┴───┘       score: %d
    """ % (player_list1_add, player_list2_add, player_list3_add, player_list1[0], player_list2[0], player_list3[0], player_list1[1], player_list2[1], player_list3[1], player_colour, player_dice, player_list1[2], player_list2[2], player_list3[2], player_score))
    print("\n\n\n\n" + ratau_board + "\n\n\n" + player_board)
    

def remove_same(witch_list, another_list):
    """如果我方某一列出现，敌方对应列的相同数字，移除掉敌方相同数字"""
    global c
    c = 0
    for i in witch_list:
        for o in another_list:
            if i == o and i != 0:
                another_list.remove(o)
                another_list.append(0)
                c += 1
            
    for i in witch_list:
        for o in another_list:
            if i == o and i != 0:
                another_list.remove(o)
                another_list.append(0)
                c += 1
        
    for i in witch_list:
        for o in another_list:
            if i == o and i != 0:
                another_list.remove(o)
                another_list.append(0)
                c += 1


player_list1 = [0, 0, 0]
player_list2 = [0, 0, 0]
player_list3 = [0, 0, 0]

ratau_list1 = [0, 0, 0]
ratau_list2 = [0, 0, 0]
ratau_list3 = [0, 0, 0]

player_which_list1_count = 0
player_which_list2_count = 0
player_which_list3_count = 0

ratau_which_list1_count = 0
ratau_which_list2_count = 0
ratau_which_list3_count = 0


i = coin_winner()
# 选择硬币正反面，玩家选择正反面后抛出，猜对即玩家获胜
while (player_which_list1_count + player_which_list2_count + player_which_list3_count) < 9 and (ratau_which_list1_count + ratau_which_list2_count + ratau_which_list3_count) < 9:

    if ( i % 2 ) == 1:
        # 玩家回合
        turn_to_player()

        chess_board()
        player_which_list()

        chess_board()
        
        i += 1

    elif ( i % 2 ) == 0:
        # 电脑回合
        turn_to_ratau()

        chess_board()
        bot_random_list()

        chess_board()

        i += 1

else:
    # 游戏结束
    if player_score > ratau_score:
        print("\n\n*************************\ncongratulations, you win!\n*************************\n\n")
    elif player_score < ratau_score:
        print("\n\n*************************\n sadly, you got bad luck\n*************************\n\n")
    else:
        print("\n\n*************************\n the game end in the draw\n*************************\n\n")

# archive date: 2022/11/1 23:24