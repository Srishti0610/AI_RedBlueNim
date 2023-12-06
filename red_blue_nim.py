import sys

numRed=int(sys.argv[1])
numBlue=int(sys.argv[2])

version = 'standard'
firstPlayer = 'computer'
depth = float('inf')

if len(sys.argv) >= 4:
    version = "misere" if sys.argv[3].lower() == "misere" else "standard"

if len(sys.argv) >= 5:
    firstPlayer = "human" if sys.argv[4].lower() == "human" else "computer"

if len(sys.argv) >= 6:
    depth = int(sys.argv[5])


def gameDecision(red, blue, maxPlayer):
    score = 2 * red + 3 * blue
    if maxPlayer:
        return -score
    return score

def finalDecision(player, version, red, blue):
    score = 2 * red + 3 * blue
    if version == "standard":
        message = "{0} loses {1} points".format(player, score)
    else:
        message = "{0} wins {1} point".format(player, score)
    return message

def updatedMarbles(marbleColor, redMarb, blueMarb):
    marbles = [redMarb - 1 if marbleColor == 1 else redMarb, blueMarb - 1 if marbleColor != 1 else blueMarb]
    return marbles[0], marbles[1]

def alphaBetaMinMax(redMarblePile, blueMarblePile, depth, alpha, beta, maxPlayer):
    if depth == 0 or redMarblePile == 0 or blueMarblePile == 0:
        return gameDecision(redMarblePile, blueMarblePile, maxPlayer)
    depth = depth - 1
    if maxPlayer:
        optimalScore = float('-inf')
        for marbleColor, number_of_marbles_left in [(1, redMarblePile), (2, blueMarblePile)]:
            if number_of_marbles_left > 0:
                red, blue = updatedMarbles(marbleColor, redMarblePile, blueMarblePile)
                updatedScore = alphaBetaMinMax(red, blue, depth, alpha, beta, False)
                optimalScore = max(optimalScore, updatedScore)
                alpha = max(alpha, optimalScore)
                if beta <= alpha:
                    break
        return optimalScore
    else:
        optimalScore = float('inf')
        for marbleColor, number_of_marbles_left in [(1, redMarblePile), (2, blueMarblePile)]:
            if number_of_marbles_left > 0:
                red, blue = updatedMarbles(marbleColor, redMarblePile, blueMarblePile)
                updatedScore = alphaBetaMinMax(red, blue, depth, alpha, beta, True)
                optimalScore = min(optimalScore, updatedScore)
                beta = min(beta, optimalScore)
                if beta <= alpha:
                    break
        return optimalScore
    
    
def getComputerMove(numRed, numBlue, firstPlayer):
    optimalScore = float('-inf')
    optimalMove = None
    playerValue = True if firstPlayer.lower() == "computer" else False
    for marbleColor, number_of_marbles_left in [(1, numRed), (2, numBlue)]:
        if number_of_marbles_left > 0:
            red, blue = updatedMarbles(marbleColor, numRed, numBlue)
            updatedScore = alphaBetaMinMax(red, blue, depth, float('-inf'), float('inf'), playerValue)
            if updatedScore > optimalScore:
                optimalScore = updatedScore
                optimalMove = marbleColor

    move = "red" if optimalMove == 1 else "blue"
    return move



def gamePlay(numRed, numBlue, version, firstPlayer, depth):
    print("Game started!!!")
    print("Version - {0}".format(version))
    currentPlayer = firstPlayer
    while numRed > 0 and numBlue > 0:
        print("Red Marbles: {0}  Blue Marbles: {1}".format(numRed, numBlue))
        if(currentPlayer == "human"):
            print("Your turn")
            while True:
                move = input("Enter your move red or blue: ")
                if move.lower() == "red":
                    numRed -= 1
                    print("You picked Red")
                    break;
                elif move.lower() == "blue":
                    numBlue -= 1
                    print("You picked Blue")
                    break;
                else:
                    print("invalid Move! Please enter red or blue.")
        else:
            print("Computer's turn")
            move = getComputerMove(numRed, numBlue, firstPlayer)
            if move == "red":
                numRed -= 1
                print("Computer picked Red")
            else:
                numBlue -= 1
                print("Computer picked Blue")

        currentPlayer = "human" if currentPlayer == "computer" else "computer"
    print(finalDecision(currentPlayer, version, numRed, numBlue))



gamePlay(numRed, numBlue, version, firstPlayer, depth)

