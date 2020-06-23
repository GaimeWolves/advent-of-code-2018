ta = 9
tb = 5
tc = 18
td = '92510'

rc = '157901'

amount = rc

recipes = [3, 7, 1, 0]
elfA = 0
elfB = 1

def printRecipes(recipes, elfA, elfB):
        for i, recipe in enumerate(recipes):
                if i == elfA:
                        print('({})'.format(recipe), end='')
                elif i == elfB:
                        print('[{}]'.format(recipe), end='')
                else:
                        print(' {} '.format(recipe), end='')
        print()

#printRecipes(recipes, elfA, elfB)
#while len(recipes) < amount + 10:
while True:
#for x in range(2500):
        oldlen = len(recipes)
        if (len(recipes) % 100000) == 0:
                print('{}/{}'.format(len(recipes), '~20000000'))
        combinedScore = recipes[elfA] + recipes[elfB]
        recipes.append(int(str(combinedScore)[0]))

        Found = True
        for y in range(len(amount)):
                #print(len(recipes) - len(amount) - 1 + y)
                if amount[y] != str(recipes[len(recipes) - len(amount) - 1 + y]):
                        Found = False
        if Found == True:
                print('x: {}'.format(len(recipes) - len(amount) - 1))
                exit()

        if combinedScore >= 10:
                recipes.append(int(str(combinedScore)[1]))
                Found = True
                for y in range(len(amount)):
                        #print(len(recipes) - len(amount) - 1 + y)
                        if amount[y] != str(recipes[len(recipes) - len(amount) - 1 + y]):
                                Found = False
                if Found == True:
                        print('x: {}'.format(len(recipes) - len(amount) - 1))
                        exit()

        elfA = (elfA + 1 + recipes[elfA]) % len(recipes)
        elfB = (elfB + 1 + recipes[elfB]) % len(recipes)
        #printRecipes(recipes, elfA, elfB)

print()
for x in range(amount, amount + 10):
        print(recipes[x], end='')