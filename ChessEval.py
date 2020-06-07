import chess.pgn
import chess.engine
# from chess import uci

# board = chess.Board()
pgn = open("/Users/liju_john01/Documents/github/chess-evaluation/resources/games1.pgn")
test_game = chess.pgn.read_game(pgn)

board = test_game.board()
for move in test_game.mainline_moves():
    board.push(move)
    print(board)
    input("press enter")

# engine = chess.engine.SimpleEngine.popen_uci("/usr/bin/stockfish")
# engine.uci()
# info_handler = chess.uci.InfoHandler()
# engine.info_handlers.append(info_handler)
# prev_eval = 0
# diff = 0
# for move in test_game.main_line():
#     print(move)
# engine.position(board)
# engine.go(movetime=2000)
# evaluation = info_handler.info["score"][1].cp
# if board.turn:
#     if prev_eval - evaluation > 0.3:
#         print("bad move")
#     else:
#         print("good move")
#
# if not board.turn:
#     evaluation *= -1
#     if evaluation - prev_eval > 0.3:
#         print("bad move")
#     else:
#         print("good move")
#
# prev_eval = evaluation
#
# board.push_uci(move.uci())
print(board)
