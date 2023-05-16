import pandas as pd

# Nutrient minimums.
nutrients = {
    'Calories (kcal)':          2300, 
    'Total Fat (g)':              60, 
    'Sodium (mg)':                500, 
    'Carbohydrates (g)':          250,
    'Protein (g)':                70 
}

# df = pd.read_csv('McDonaldsMenu.csv')
# # create an empty dictionary
# d = {}

# # iterate through the rows of the dataframe
# for index, row in df.iterrows():
#     # get the item name and the other columns as a list
#     item_name = row['Item']
#     item_values = [row['Price ($)'], row['Calories (kcal)'], row['Total Fat (g)'], row['Cholesterol (mg)'],
#                    row['Sodium (mg)'], row['Carbohydrates (g)'], row['Sugars (g)'], row['Protein (g)']]
    
#     # add the item and its values to the dictionary
#     d[item_name] = item_values

# # print the dictionary
# print(d)

commodities = {
    'Egg McMuffin':                                                     [4.48, 300, 13.0, 260, 750, 31, 3, 17],
    'Egg White Delight':                                                [3.9, 250, 8.0, 25, 770, 30, 3, 18],
    'Sausage McMuffin':                                                 [2.09, 370, 23.0, 45, 780, 29, 2, 14],
    'Sausage McMuffin with Egg':                                        [3.76, 450, 28.0, 285, 860, 30, 2, 21],
    'Sausage McMuffin with Egg Whites':                                 [3.76, 400, 23.0, 50, 880, 30, 2, 21],
    'Steak & Egg McMuffin':                                             [3.99, 430, 23.0, 300, 960, 31, 3, 26],
    'Bacon, Egg & Cheese Biscuit (Regular Biscuit)':                    [4.61, 460, 26.0, 250, 1300, 38, 3, 19],
    'Bacon, Egg & Cheese Biscuit (Large Biscuit)':                      [5.2, 520, 30.0, 250, 1410, 43, 4, 19],
    'Bacon, Egg & Cheese Biscuit with Egg Whites (Regular Biscuit)':    [4.61, 410, 20.0, 35, 1300, 36, 3, 20],
    'Bacon, Egg & Cheese Biscuit with Egg Whites (Large Biscuit)':      [5.2, 470, 25.0, 35, 1420, 42, 4, 20],
    'Sausage Biscuit (Regular Biscuit)':                                [2.01, 430, 27.0, 30, 1080, 34, 2, 11],
    'Sausage Biscuit (Large Biscuit)':                                  [3.9, 480, 31.0, 30, 1190, 39, 3, 11],
    'Sausage Biscuit with Egg (Regular Biscuit)':                       [4.22, 510, 33.0, 250, 1170, 36, 2, 18],
    'Sausage Biscuit with Egg (Large Biscuit)':                         [5.4, 570, 37.0, 250, 1280, 42, 3, 18],
    'Sausage Biscuit with Egg Whites (Regular Biscuit)':                [4.22, 460, 27.0, 35, 1180, 34, 3, 18],
    'Sausage Biscuit with Egg Whites (Large Biscuit)':                  [5.4, 520, 32.0, 35, 1290, 40, 3, 18],
    'Southern Style Chicken Biscuit (Regular Biscuit)':                 [4.22, 410, 20.0, 30, 1180, 41, 3, 17],
    'Southern Style Chicken Biscuit (Large Biscuit)':                   [5.4, 470, 24.0, 30, 1290, 46, 4, 17],
    'Bacon, Egg & Cheese McGriddles':                                   [4.64, 460, 21.0, 250, 1250, 48, 15, 19],
    'Bacon, Egg & Cheese McGriddles with Egg Whites':                   [4.64, 400, 15.0, 35, 1250, 47, 16, 20],
    'Sausage McGriddles':                                               [3.21, 420, 22.0, 35, 1030, 44, 15, 11],
    'Sausage, Egg & Cheese McGriddles':                                 [4.63, 550, 31.0, 265, 1320, 48, 15, 20],
    'Sausage, Egg & Cheese McGriddles with Egg Whites':                 [4.63, 500, 26.0, 50, 1320, 46, 15, 21],
    'Bacon, Egg & Cheese Bagel':                                        [4.81, 620, 31.0, 275, 1480, 57, 7, 30],
    'Bacon, Egg & Cheese Bagel with Egg Whites':                        [4.81, 570, 25.0, 60, 1480, 55, 8, 30],
    'Steak, Egg & Cheese Bagel':                                        [5.51, 670, 35.0, 295, 1510, 56, 7, 33],
    'Big Breakfast (Regular Biscuit)':                                  [5.32, 740, 48.0, 555, 1560, 51, 3, 28],
    'Big Breakfast with Hotcakes (Regular Biscuit)':                    [6.69, 1090, 56.0, 575, 2150, 111, 17, 36],
    'Hotcakes':                                                         [4.2, 350, 9.0, 20, 590, 60, 14, 8],
    'Hotcakes and Sausage':                                             [4.88, 520, 24.0, 50, 930, 61, 14, 15],
    'Sausage Burrito':                                                  [6.98, 300, 16.0, 115, 790, 26, 2, 12],
    'Hash Brown':                                                       [1.6, 150, 9.0, 0, 310, 15, 0, 1],
    'Cinnamon Melts':                                                   [1.8, 460, 19.0, 15, 370, 66, 32, 6],
    'Fruit & Maple Oatmeal':                                            [3.66, 290, 4.0, 5, 160, 58, 32, 5],
    'Fruit & Maple Oatmeal without Brown Sugar':                        [3.66, 260, 4.0, 5, 115, 49, 18, 5],
    'Big Mac':                                                          [5.53, 530, 27.0, 85, 960, 47, 9, 24],
    'Quarter Pounder with Cheese':                                      [5.65, 520, 26.0, 95, 1100, 41, 10, 30],
    'Quarter Pounder with Bacon & Cheese':                              [6.3, 600, 29.0, 105, 1440, 48, 12, 37],
    'Quarter Pounder with Bacon Habanero Ranch':                        [8.61, 610, 31.0, 105, 1180, 46, 10, 37],
    'Quarter Pounder Deluxe':                                           [9.61, 540, 27.0, 85, 960, 45, 9, 29],
    'Double Quarter Pounder with Cheese':                               [11.12, 750, 43.0, 160, 1280, 42, 10, 48],
    'Hamburger':                                                        [1.62, 240, 8.0, 30, 480, 32, 6, 12],
    'Cheeseburger':                                                     [1.88, 290, 11.0, 45, 680, 33, 7, 15],
    'Double Cheeseburger':                                              [5.99, 430, 21.0, 90, 1040, 35, 7, 24],
    'Bacon Clubhouse Burger':                                           [6.99, 720, 40.0, 115, 1470, 51, 14, 39],
    'McDouble':                                                         [2.6, 380, 17.0, 75, 840, 34, 7, 22],
    'Bacon McDouble':                                                   [3.37, 440, 22.0, 90, 1110, 35, 7, 27],
    'Daily Double':                                                     [3.34, 430, 22.0, 80, 760, 34, 7, 22],
    'Jalapeno Double':                                                  [4.34, 430, 23.0, 80, 1030, 35, 6, 22],
    'McRib':                                                            [4.5, 500, 26.0, 70, 980, 44, 11, 22],
    'Premium Crispy Chicken Classic Sandwich':                          [5.17, 510, 22.0, 45, 990, 55, 10, 24],
    'Premium Grilled Chicken Classic Sandwich':                         [5.17, 350, 9.0, 65, 820, 42, 8, 28],
    'Premium Crispy Chicken Club Sandwich':                             [5.17, 670, 33.0, 85, 1410, 58, 11, 36],
    'Premium Grilled Chicken Club Sandwich':                            [5.17, 510, 20.0, 105, 1250, 44, 9, 40],
    'Premium Crispy Chicken Ranch BLT Sandwich':                        [6.14, 610, 28.0, 70, 1400, 57, 11, 32],
    'Premium Grilled Chicken Ranch BLT Sandwich':                       [6.14, 450, 15.0, 90, 1230, 43, 9, 36],
    'Bacon Clubhouse Crispy Chicken Sandwich':                          [7.14, 750, 38.0, 90, 1720, 65, 16, 36],
    'Bacon Clubhouse Grilled Chicken Sandwich':                         [7.14, 590, 25.0, 110, 1560, 51, 14, 40],
    'Southern Style Crispy Chicken Sandwich':                           [6.78, 430, 19.0, 45, 910, 43, 7, 21],
    'McChicken':                                                        [2.08, 360, 16.0, 35, 800, 40, 5, 14],
    'Bacon Cheddar McChicken':                                          [3.18, 480, 24.0, 65, 1260, 43, 6, 22],
    'Bacon Buffalo Ranch McChicken':                                    [3.77, 430, 21.0, 50, 1260, 41, 6, 20],
    'Buffalo Ranch McChicken':                                          [2.98, 360, 16.0, 35, 990, 40, 5, 14],
    'Chicken McNuggets (4 piece)':                                      [2.64, 190, 12.0, 25, 360, 12, 0, 9],
    'Chicken McNuggets (6 piece)':                                      [3.62, 280, 18.0, 40, 540, 18, 0, 13],
    'Chicken McNuggets (10 piece)':                                     [6.72, 470, 30.0, 65, 900, 30, 0, 22],
    'Chicken McNuggets (20 piece)':                                     [6.99, 940, 59.0, 135, 1800, 59, 0, 44],
    'Chicken McNuggets (40 piece)':                                     [13.35, 1880, 118.0, 265, 3600, 118, 1, 87],
    'Filet-O-Fish':                                                     [4.98, 390, 19.0, 40, 590, 39, 5, 15],
    'Premium Bacon Ranch Salad (without Chicken)':                      [5.13, 140, 7.0, 25, 300, 10, 4, 9],
    'Premium Bacon Ranch Salad with Crispy Chicken':                    [6.45, 380, 21.0, 70, 860, 22, 5, 25],
    'Premium Bacon Ranch Salad with Grilled Chicken':                   [6.46, 220, 8.0, 85, 690, 8, 4, 29],
    'Premium Southwest Salad (without Chicken)':                        [5.19, 140, 4.5, 10, 150, 20, 6, 6],
    'Premium Southwest Salad with Crispy Chicken':                      [6.47, 450, 22.0, 50, 850, 42, 12, 23],
    'Premium Southwest Salad with Grilled Chicken':                     [6.89, 290, 8.0, 70, 680, 28, 10, 27],
    'Chipotle BBQ Snack Wrap (Crispy Chicken)':                         [2.39, 340, 15.0, 30, 780, 37, 8, 14],
    'Chipotle BBQ Snack Wrap (Grilled Chicken)':                        [2.43, 260, 8.0, 40, 700, 30, 7, 16],
    'Honey Mustard Snack Wrap (Crispy Chicken)':                        [2.39, 330, 15.0, 35, 730, 34, 3, 14],
    'Honey Mustard Snack Wrap (Grilled Chicken)':                       [2.43, 250, 8.0, 45, 650, 27, 2, 16],
    'Ranch Snack Wrap (Crispy Chicken)':                                [2.39, 360, 20.0, 40, 810, 32, 3, 15],
    'Ranch Snack Wrap (Grilled Chicken)':                               [2.43, 280, 13.0, 45, 720, 25, 2, 16],
    'Small French Fries':                                               [2.34, 230, 11.0, 0, 130, 30, 0, 2],
    'Medium French Fries':                                              [2.77, 340, 16.0, 0, 190, 44, 0, 4],
    'Large French Fries':                                               [3.57, 510, 24.0, 0, 290, 67, 0, 6],
    'Side Salad':                                                       [2.46, 20, 0.0, 0, 10, 4, 2, 1],
    'Apple Slices':                                                     [0.89, 15, 0.0, 0, 0, 4, 3, 0],
    "Fruit 'n Yogurt Parfait":                                          [2.12, 150, 2.0, 5, 70, 30, 23, 4],
    'Baked Apple Pie':                                                  [1.09, 250, 13.0, 0, 170, 32, 13, 2],
    'Chocolate Chip Cookie':                                            [0.88, 160, 8.0, 10, 90, 21, 15, 2],
    'Hot Fudge Sundae':                                                 [2.83, 330, 9.0, 25, 170, 53, 48, 8],
    'Strawberry Sundae':                                                [2.14, 280, 6.0, 25, 85, 49, 45, 6]
    }