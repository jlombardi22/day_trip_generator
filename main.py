import random_generator


random_generator.trip_generator(list=['CA', 'NM', 'CO', 'WA'], decision=(
    print('Is this where you would like to travel too?: ')))

random_generator.trip_generator(
    list=['IHOP', 'Dennys', 'Maccas', 'Juniors'], decision=(
        print('Is this where you would like to eat?: ')))

random_generator.trip_generator(
    list=['Car', 'Boat', 'Plane', 'Train'], decision=(
        print('Is this mode of transportation accceptable?: ')))

random_generator.trip_generator(
    list=['Movie', 'Show', 'Game', 'Race'], decision=(
        print('We have planned this for after dinner, does this sound like fun?: ')))


# random_generator.dest_generator(destinations=[
#                                 'CA', 'NM', 'CO', 'WA'])

# random_generator.food_generator(
#     restaurants=['IHOP', 'Dennys', 'Maccas', 'Juniors'])

# random_generator.trans_generator(
#     transportations=['Car', 'Boat', 'Plane', 'Train'])

# random_generator.enertain_generator(
#     entertainment=['Movie', 'Show', 'Game', 'Race'])
