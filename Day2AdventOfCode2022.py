
with open('day2.in') as file:
    strategy = [round.replace(" ", "") for round in file.read().strip().split("\n")]

print(strategy)

outcomes = {
    "AX":4, "AY":8, "AZ":3,
    "BX":1, "BY":5, "BZ":9,
    "CX":7, "CY":2, "CZ":6
}

def rock_paper_scissors_strategy(strategy):
    my_total_score = 0
    for round in strategy:
        my_total_score += outcomes[round]
    return my_total_score


print(rock_paper_scissors_strategy(strategy))


# def rock_paper_scissors_score(strategy):
#     opponent_move = ''
#     my_move_score = 0
#     my_move = ''
#     total_score = 0
#     for move in strategy:
#         if move in 'A':
#             opponent_move = 'Rock'
#         elif move in 'B':
#             opponent_move = 'Paper'
#         elif move in 'C':
#             opponent_move = 'Scissors'
#         if move in 'X':
#             my_move = 'Rock'
#             my_move_score = 1
#         elif move in 'Y':
#             opponent_move = 'Paper'
#             my_move_score = 2
#         elif move in 'Z':
#             opponent_move = 'Scissors'
#             my_move_score = 3
#         if my_move == opponent_move:
#             total_score += 1 + my_move_score
#         elif my_move == 'Rock' and opponent_move == 'Scissors':
#             total_score += 3 + my_move_score
#         elif my_move == 'Paper' and opponent_move == 'Rock':
#             total_score += 3 + my_move_score
#         elif my_move == 'Scissors' and opponent_move == 'Paper':
#             total_score += 3 + my_move_score
#         else:
#             total_score += my_move_score
#         return total_score
#
# print(rock_paper_scissors_score(strategy))

