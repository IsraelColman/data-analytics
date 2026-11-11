# Description: This script is to use tuples and sets
# Author: Israel Colman

# Creating Tuples and set
candy = ('Jolly Rancher', 'Starburst', 'Laffy Taffy')
candy_flavor = ('Bannana', 'Green Apple', 'Strawberry')
candy_combinations = {candy_flavor[1] + ' ' + candy[0], \
                      candy_flavor[2] + ' ' + candy[1], \
                        candy_flavor[0] + ' ' + candy[2]}
print(f"Today's candy options include: {candy_combinations}")

# I noticed that every time I print the output the order of the candy_combinations change each time.