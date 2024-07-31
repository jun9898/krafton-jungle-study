# 돌이 겹치면 잘못된 결과가 나오고 코드가 너무 복잡함
# import sys
# input = sys.stdin.readline

# board = [list([0]*8) for _ in range(8)]
# print(board)

# king, pawn, n = input().split()

# n = int(n)

# kingLo = []
# pawnLo = []

# for i in king[::-1]:
#     if i == 'A': kingLo.append(0)
#     elif i == 'B': kingLo.append(1)
#     elif i == 'C': kingLo.append(2)
#     elif i == 'D': kingLo.append(3)
#     elif i == 'E': kingLo.append(4)
#     elif i == 'F': kingLo.append(5)
#     elif i == 'G': kingLo.append(6)
#     elif i == 'H': kingLo.append(7)
#     elif i == '1': kingLo.append(0)
#     elif i == '2': kingLo.append(1)
#     elif i == '3': kingLo.append(2)
#     elif i == '4': kingLo.append(3)
#     elif i == '5': kingLo.append(4)
#     elif i == '6': kingLo.append(5)
#     elif i == '7': kingLo.append(6)
#     elif i == '8': kingLo.append(7)

# for i in pawn[::-1]:
#     if i == 'A': pawnLo.append(0)
#     elif i == 'B': pawnLo.append(1)
#     elif i == 'C': pawnLo.append(2)
#     elif i == 'D': pawnLo.append(3)
#     elif i == 'E': pawnLo.append(4)
#     elif i == 'F': pawnLo.append(5)
#     elif i == 'G': pawnLo.append(6)
#     elif i == 'H': pawnLo.append(7)
#     elif i == '1': pawnLo.append(0)
#     elif i == '2': pawnLo.append(1)
#     elif i == '3': pawnLo.append(2)
#     elif i == '4': pawnLo.append(3)
#     elif i == '5': pawnLo.append(4)
#     elif i == '6': pawnLo.append(5)
#     elif i == '7': pawnLo.append(6)
#     elif i == '8': pawnLo.append(7)

# kingY = kingLo[0]
# kingX = kingLo[1]
# pawnY = pawnLo[0]
# pawnX = pawnLo[1]
# board[kingY][kingX] = 1
# board[pawnY][pawnX] = 2
# """
# """
# for i in range(n):
#     commend = input().rstrip()
# # R : 한 칸 오른쪽으로
#     if commend == 'R':
#         if kingX < 7 and pawnX < 7:
#             board[kingY][kingX], board[kingY][kingX+1] = board[kingY][kingX+1], board[kingY][kingX]
#             board[pawnY][pawnX], board[pawnY][pawnX+1] = board[pawnY][pawnX+1], board[pawnY][pawnX]
#             kingX += 1
#             pawnX += 1
#         elif kingX < 7:
#             board[kingY][kingX], board[kingY][kingX+1] = board[kingY][kingX+1], board[kingY][kingX]
#             kingX += 1
#         elif pawnX < 7:
#             board[pawnY][pawnX], board[pawnY][pawnX+1] = board[pawnY][pawnX+1], board[pawnY][pawnX]
#             pawnX += 1
#         else:
#             continue
# # L : 한 칸 왼쪽으로
#     elif commend == 'L':
#         if kingX > 0 and pawnX > 0:
#             board[kingY][kingX], board[kingY][kingX-1] = board[kingY][kingX-1], board[kingY][kingX]
#             board[pawnY][pawnX], board[pawnY][pawnX-1] = board[pawnY][pawnX-1], board[pawnY][pawnX]
#             kingX -= 1
#             pawnX -= 1
#         elif kingX > 0:
#             board[kingY][kingX], board[kingY][kingX-1] = board[kingY][kingX-1], board[kingY][kingX]
#             kingX -= 1
#         elif pawnY > 0:
#             board[pawnY][pawnX], board[pawnY][pawnX-1] = board[pawnY][pawnX-1], board[pawnY][pawnX]
#             pawnX -= 1
#         else:
#             continue
# # B : 한 칸 아래로
#     elif commend == 'B':
#         if kingY > 0 and pawnY > 0:
#             board[kingY][kingX], board[kingY-1][kingX] = board[kingY-1][kingX], board[kingY][kingX]
#             board[pawnY][pawnX], board[pawnY-1][pawnX] = board[pawnY-1][pawnX], board[pawnY][pawnX]
#             kingY -= 1
#             pawnY -= 1
#         else:
#             continue
# # T : 한 칸 위로
#     elif commend == 'T':
#         if kingY < 7 and pawnY < 7:
#             board[kingY][kingX], board[kingY+1][kingX] = board[kingY+1][kingX], board[kingY][kingX]
#             board[pawnY][pawnX], board[pawnY+1][pawnX] = board[pawnY+1][pawnX], board[pawnY][pawnX]
#             kingY += 1
#             pawnY += 1
#         else:
#             continue
# # RT : 오른쪽 위 대각선으로
#     if commend == 'RT':
#         if kingX < 7 and pawnX < 7 and kingY < 7 and pawnY < 7:
#             board[kingY][kingX], board[kingY+1][kingX+1] = board[kingY+1][kingX+1], board[kingY][kingX]
#             board[pawnY][pawnX], board[pawnY+1][pawnX+1] = board[pawnY+1][pawnX+1], board[pawnY][pawnX]
#             kingX += 1
#             pawnX += 1
#             kingY += 1
#             pawnY += 1
#         else:
#             continue
# # LT : 왼쪽 위 대각선으로
#     elif commend == 'LT':
#         if kingX > 0 and pawnX > 0 and kingY < 7 and pawnY < 7:
#             board[kingY][kingX], board[kingY+1][kingX-1] = board[kingY+1][kingX-1], board[kingY][kingX]
#             board[pawnY][pawnX], board[pawnY+1][pawnX-1] = board[pawnY+1][pawnX-1], board[pawnY][pawnX]
#             kingX -= 1
#             pawnX -= 1
#             kingY += 1
#             pawnY += 1
#         else:
#             continue
# # RB : 오른쪽 아래 대각선으로
#     if commend == 'RB':
#         if kingX < 7 and pawnX < 7 and kingY > 0 and pawnY > 0:
#             board[kingY][kingX], board[kingY-1][kingX+1] = board[kingY-1][kingX+1], board[kingY][kingX]
#             board[pawnY][pawnX], board[pawnY-1][pawnX+1] = board[pawnY-1][pawnX+1], board[pawnY][pawnX]
#             kingX += 1
#             pawnX += 1
#             kingY -= 1
#             pawnY -= 1
#         else:
#             continue
# # LB : 왼쪽 아래 대각선으로
#     elif commend == 'LB':
#         if kingX > 0 and pawnX > 0 and kingY > 0 and pawnY > 0:
#             board[kingY][kingX], board[kingY-1][kingX-1] = board[kingY-1][kingX-1], board[kingY][kingX]
#             board[pawnY][pawnX], board[pawnY-1][pawnX-1] = board[pawnY-1][pawnX-1], board[pawnY][pawnX]
#             kingX -= 1
#             pawnX -= 1
#             kingY -= 1
#             pawnY -= 1
#         else:
#             continue

# for i in range(8):
#     for j in range(8):
#         if board[i][j] == 1:
#             answerKing = [str(i+1),str(j)]
#         elif board[i][j] == 2:
#             answerPawn = [str(i+1),str(j)]

# answerKing.reverse()
# answerPawn.reverse() 

# if answerKing[0] == '0': answerKing[0] = 'A'
# elif answerKing[0] == '1': answerKing[0] = 'B'
# elif answerKing[0] == '2': answerKing[0] = 'C'
# elif answerKing[0] == '3': answerKing[0] = 'D'
# elif answerKing[0] == '4': answerKing[0] = 'E'
# elif answerKing[0] == '5': answerKing[0] = 'F'
# elif answerKing[0] == '6': answerKing[0] = 'G'
# elif answerKing[0] == '7': answerKing[0] = 'H'

# if answerPawn[0] == '0': answerPawn[0] = 'A'
# elif answerPawn[0] == '1': answerPawn[0] = 'B'
# elif answerPawn[0] == '2': answerPawn[0] = 'C'
# elif answerPawn[0] == '3': answerPawn[0] = 'D'
# elif answerPawn[0] == '4': answerPawn[0] = 'E'
# elif answerPawn[0] == '5': answerPawn[0] = 'F'
# elif answerPawn[0] == '6': answerPawn[0] = 'G'
# elif answerPawn[0] == '7': answerPawn[0] = 'H'

# print("".join(answerKing))
# print("".join(answerPawn))


