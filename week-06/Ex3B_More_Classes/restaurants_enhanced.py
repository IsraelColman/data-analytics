# Israel Colman
# 11/18/2026


# Create Class
class Restaurant:
    '''describe and determine restaurant details'''

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []

    def describe_rest(self):
        print(f'===== Restaurant Details =====')
        print(f'{self.rest_name} serves {self.food_type}')

    def rest_open(self):
        print(f'{self.rest_name} is open')

    def add_num_served(self):
        customers = int(input('How many customers served today? '))
        self.number_served += customers

    def print_num_served(self):
        print(f'{self.rest_name} has served {self.number_served} customers')

    def customer_rating(self):

        rating = input(
            'How would you rate your experience today on a scale of 1-5 (5 being excellent)? '
        )

        while rating not in ['1', '2', '3', '4', '5']:
            print('Invalid rating. Please enter a whole number from 1 to 5.')
            rating = input(
                'How would you rate your experience today on a scale of 1-5 (5 being excellent)? '
            )

        rating = int(rating)

        self.customer_ratings.append(rating)

        average_rating = sum(self.customer_ratings) / len(self.customer_ratings)

        print(f'Your rating was {rating}.')
        print(f'The average rating for this restaurant is {average_rating:.2f}')
        print('=' * 30)
        print()


# Create three restaurant instances
restaurant1 = Restaurant("Taco Baco", "Mexican food")
restaurant2 = Restaurant("McNaldo's", "American food")
restaurant3 = Restaurant("Texas Roadhouse", "Steakhouse food")


# Restaurant 1
restaurant1.describe_rest()
restaurant1.rest_open()
restaurant1.print_num_served()
restaurant1.add_num_served()
restaurant1.add_num_served()
restaurant1.print_num_served()

restaurant1.customer_rating()
restaurant1.customer_rating()
restaurant1.customer_rating()


# Restaurant 2
restaurant2.describe_rest()
restaurant2.rest_open()
restaurant2.print_num_served()
restaurant2.add_num_served()
restaurant2.add_num_served()
restaurant2.print_num_served()

restaurant2.customer_rating()
restaurant2.customer_rating()
restaurant2.customer_rating()


# Restaurant 3
restaurant3.describe_rest()
restaurant3.rest_open()
restaurant3.print_num_served()
restaurant3.add_num_served()
restaurant3.add_num_served()
restaurant3.print_num_served()

restaurant3.customer_rating()
restaurant3.customer_rating()
restaurant3.customer_rating()