import random


def trip_generator(list, decision):
    item = random.choice(list)
    print(item)
    for item in list:
        decision = (
            input()
        )
        if(decision == 'no'):
            print('sorry that didnt work how about this instead?')
        elif(decision == 'yes'):
            print(f'We are going to {item}')
            return item
        else:
            print('Please enter yes or no.')


# def dest_generator(destinations):
#     dest = random.choice(destinations)
#     for dest in destinations:
#         print(dest)
#         decision = (
#             input('Is this where you would like to travel too?: '))
#         if(decision == 'no'):
#             print(dest)
#         elif(decision == 'yes'):
#             print(f'We are going to {dest}')
#             return dest
#         else:
#             print('Please enter yes or no.')


# def food_generator(restaurants):
#     food = random.choice(restaurants)
#     for food in restaurants:
#         print(food)
#         decision = (
#             input('Is this where you would like to eat?: '))
#         if(decision == 'no'):
#             print(food)
#         elif(decision == 'yes'):
#             print(f'We are going to be dining at {food}')
#             return food
#         else:
#             print('Please enter yes or no.')


# def trans_generator(transportations):
#     trans = random.choice(transportations)
#     for trans in transportations:
#         print(trans)
#         decision = (
#             input('Is this mode of transportation accceptable?: '))
#         if(decision == 'no'):
#             print(trans)
#         elif(decision == 'yes'):
#             print(f'We will be taking a {trans}')
#             return trans
#         else:
#             print('Please enter yes or no.')


# def enertain_generator(entertainment):
#     entertain = random.choice(entertainment)
#     for entertain in entertainment:
#         print(entertain)
#         decision = (
#             input('We have planned this for after dinner, does this sound like fun?: '))
#         if(decision == 'no'):
#             print(entertain)
#         elif(decision == 'yes'):
#             print(f'We are going to a {entertain}')
#             return entertain
#         else:
#             print('Please enter yes or no.')
