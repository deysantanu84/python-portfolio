# There is a football event going on in your city. In this event,
# you are given A passes and players having ids between 1 and 10^6.
# Initially some player with a given id had the ball in his possession.
# You have to make a program to display the id of the player who possessed the ball
# after exactly A passes.
# There are two kinds of passes:
# 1) ID
# 2) 0
# For the first kind of pass, the player in possession of the ball passes
# the ball "forward" to player with id = ID.
# For the second kind of a pass, the player in possession of the ball passes
# the ball back to the player who had forwarded the ball to him.
# In the second kind of pass "0" just means Back Pass.
# Return the ID of the player who currently possesses the ball.
# 1 <= A <= 100000
# 1 <= B <= 100000
# |C| = A
# The first argument of the input contains the number A.
# The second argument of the input contains the number B
# ( id of the player possessing the ball in the very beginning).
# The third argument is an array C of size A having (ID/0).
# Return the "ID" of the player who possesses the ball after A passes.
def passingGame(A, B, C):
    passStack = [B]
    for item in C:
        if item != 0:
            passStack.append(item)
        else:
            passStack.pop()

    return passStack[-1]


print(passingGame(10, 23, [86, 63, 60, 0, 47, 0, 99, 9, 0, 0]))  # 63
print(passingGame(1, 1, [2]))  # 2
print(passingGame(10, 38, [23, 0, 2, 0, 39, 28, 19, 0, 0, 0]))  # 38
