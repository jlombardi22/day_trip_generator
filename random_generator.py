import random


def dest_generator(destinations):
    new_dest = random.choice(destinations)
    for new_dest in destinations:
        print(new_dest)
        decision = (
            input('Is this where you would like to travel too?: '))
        if(decision == 'no'):
            print(new_dest)
        elif(decision == 'yes'):
            print(f'We are going to {new_dest}')
            return new_dest
    else:
        print('Please enter yes or no.')


def food_generator(restaurants):
    new_food = random.choice(restaurants)
    for new_food in restaurants:
        print(new_food)
        decision = (
            input('Is this where you would like to eat?: '))
        if(decision == 'no'):
            print(new_food)
        elif(decision == 'yes'):
            print(f'We are going to {new_food}')
            return new_food

    else:
        print('Please enter yes or no.')
    print(new_food)


def trans_generator(transportations):
    new_trans = random.choice(transportations)
    print(new_trans)


def enertain_generator(entertainment):
    new_entertain = random.choice(entertainment)
    print(new_entertain)
