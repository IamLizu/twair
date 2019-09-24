#! /usr/bin/python
# libraries
import tweepy
import sys

# twiiter application details
cKey = 'GSzQ8YmJeKWbcil1uKlA3jKMK'
cSecret = 'yRBxQDfwVZHixfBx5MUSyOdw6pzKCPkyzM4camaejeg2L9lgq0'
aToken = '1482468246-AtHZS5XV2MLw242xSecW9S9nIFms90oa1SqIc52'
aTokenSecret = 'JGiQoBsj5D8j0InFT9VS60fS5NAD8LUWEN7wgotbaaLKz'

# authentication
auth = tweepy.OAuthHandler(cKey, cSecret)
auth.set_access_token(aToken, aTokenSecret)
tw = tweepy.API(auth)

u = sys.argv[1]
# saves the following list in a variable
uFriends = tw.friends_ids(u)
# saves the follower list in a variable
uFollowers = tw.followers_ids(u)
# count total  following
uFriendsC = tw.get_user(u).friends_count
# count total followers
uFollowersC = tw.get_user(u).followers_count
# list to save verfied twitter followers
vFs = []


# prints the following list of a user
def listFollowing():
    print("Printing users, please wait.../\n")
    for user in uFriends:
        print(tw.get_user(user).screen_name + ',  ',end='', flush=True)


# prints the followers list  of a user
def listFollowers():
    print("Printing users, please wait.../\n")
    for user in uFollowers:
        print(tw.get_user(user).screen_name + ',  ',end='', flush=True)


# prints followers of a user who are following back
def doFollow():
    print("Printing users, please wait.../\n")
    for user in uFriends:
        if user in uFollowers:
            print(tw.get_user(user).screen_name + ',  ',end='', flush=True)


# count the users who are following back
def doFollowC():
    doFollowCount = 0
    for user in uFriends:
        if user in uFollowers:
            doFollowCount += 1;
    return doFollowCount


# prints followers a user who are not following back
def doNotFollow():
    print("Printing users, please wait.../\n")
    for user in uFriends:
        if user not in uFollowers:
            print(tw.get_user(user).screen_name + ',  ',end='', flush=True)


# count the users who are following back
def noFollowC():
    nFollowCount = 0
    for user in uFriends:
        if user not in uFollowers:
            nFollowCount += 1;
    return nFollowCount


# count the veified user who are following back
def verifiedFollowers():
    vFC = 0
    for user in uFriends:
        if user in uFollowers:
            if tw.get_user(user).verified == 1:
                # save the verified user in vFs list
                vFC += 1;
                vFs.append(tw.get_user(user).screen_name)
                # increment value of vFC if verfied == true
    return vFC


# prints saved list of verified followers
def liVFs():
    print("Printing users, please wait.../\n")
    print (','.join(map(str, vFs)))


# calls various type of list functions
def viewList():
    print("     \nGet list of,\n")
    print("         Following [1] ")
    print("         Followers [2] ")
    print("         Following back [3] ")
    print("         !Following back [4] ")
    print("         Verified followers [5]")
    print("         Exit [6] ")
    print("     \nYour choice: ", end = '', flush=True)

    d = input()

    if d == '1':
        listFollowing()
    elif d == '2':
        listFollowers()
    elif d == '3':
        doFollow()
    elif d == '4':
        doNotFollow()
    elif d == '5':
        liVFs()
    elif d == '6':
        system(exit)
    else:
        wrC()

    print("\nSee the list again? [Y/n]: ", end='', flush=True)
    dA = input()
    while dA == 'Y' or dA == 'y':
        viewList()
        break


# prints wrong choice message
def wrC():
    print("\nIt seems you have chosed a wrong option!")
    viewList()


# basic information print
def printBasic(u):
    print("     Name: " + tw.get_user(u).name)
    print("     Username: " + u)
    print("     Following: " + str(uFriendsC))
    print("         Following back: " + str(doFollowC()))
    print("         !Following back: " + str(noFollowC()))
    print("     Followers: " + str(uFollowersC))
    print("        ———————————————————————————————————————————————————————————————")
    print("        Please wait till I check how many celebrities are following you,")
    print("        the more follower you have the more time I take../")
    print("        ———————————————————————————————————————————————————————————————")
    print("         Verified: " + str(verifiedFollowers()))


# main function
def main():
    print("\nTwitter Account Information Retreiver\n")
    printBasic(u)
    viewList()
    print("\nMy functions are limited, perhaps that's it for now!")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nWhy cancel btw! Anyways, run again if you want../')
