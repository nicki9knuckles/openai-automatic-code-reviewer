from collections import Counter

input_text = """
DISPLAYED MENU
SALADS 
Build you own salad ……………………………………………………………………Small $10………. Large $13

 Add Protein $4

Extra cheese $2
Extra grains $2

SANDWICH
The Club ……………………………………………………………………………………………………………..…………… $13
Roasted chicken, tomato, bacon, aioli, swiss cheese. 
Vegetarian (VG/V) ……………………………………………………………………………………………..……………. $11
Roasted vegetables, tofu, hummus. 
The Argentinian …………………………………………………………………………………………….……….……….. $15
Chimichurri steak, aioli, Monterey-Jack cheese. 
The American …………………………………………………………………………………………………………..……… $11
Slow roasted pulled pork.
Ultimate Caprese …………………………………………………………………………………………………………….. $13
Prosciutto, salami, fior de latte cheese, pesto sauce. 
Turkey Brie ………………………………………………………………………………………………..……………….……. $12
Turkey, brie cheese, apricot compote, mayo. 
Green Goddess (VG) ………………………………………………………………………………………………………… $11
Ricotta cheese, smashed avocado, caramelized onions. 
       ** Make it a combo!!
Half sandwich + small soup …………………………………………………………………………………………..…. $12
Half sandwich + small salad ……………………………………………………………………………………..……… $15
Small salad + small soup …………………………………………………………………………………….…………... $14
Sandwich + kettle chips ………………………………………………………………………………..………..… Add $2

SOUP OF THE DAY ……………………………………….……….…… Small $5.5 ……. Large $7.5

COFFEE BAR ……………………………………………………………………12oz … 16oz …. 20oz
Brewed coffee ………………………………………………………………………………… $2.5….…. $3 …….. $3.5
Americano ……………………………………………………………………………………… $2.5   …... $3 ……… $3.5
Espresso ………………………………………………………………………………………….. Corto $2.5 …. Longo $3
Latte ……………………………………………………………………………………………….. $3.5 ….… $4 ……… $4.5
Cappuccino ……………………………………………………………………………………… $3.5 ……. $4 ……… $4.5
Mochaccino …………………………………………………………………………………….. $3.5 …... $4………. $4.5
London Fog ……………………………………………………………………………………… $3.5 …… $4.5 …… $5.5
Iced coffee ………………………………………………………………………………………. $2.5 …… $3 ……… $3.5
Chai Latte ………………………………………………………………………………………… $3 ………. $3.5 …… $4.5  
Organic tea ……………………………………………………………………………………… $2.25 ….. $2.5 ……. $3
Hot chocolate …………………………………………………………………………………. $3.5 ……… $4.5 …… $5.5
**SUB: Almond $0.9   - Soy $0.5     - Oat $0.9
BREAKFAST OPTIONS
Breakfast Croissant ……………………………………………………………………………………………..…………. $9
Turkey, egg, cheddar cheese, Dijon mustard, mayo. 
English Muffin …………………………………………………………………………………………………….…………. $6.5
Bacon, egg, cheddar cheese. 
BLT Bagel ……………………………………………………………………………………………………………..………... $6
Bacon, lettuce, tomato. 
BLK Bagel ……………………………………………………………………………………………………………..………… $6
Bacon, cheddar cheese, fig-vanilla compote. 
Add Fried Egg ……………………………………………………………………………………………………….……….. $1.3
Parfait ………………………………………………………………………………………………………………….……….. $6
Fresh Fruit Bowl ………………………………………………………………………….……Small $6.5 ………. Large $12
Seasonal fruit, berries. 
Oatmeal …………………………………………………………………………………………………………………………. $4.5
Maple syrup, brown sugar, dried fruit - nuts. 

SMOOTHIES …………………………………………………………………SMALL ……… LARGE
Tropical twist ………………………………………………………………………………… $6.5……………….. $8
Pineapple, mango, peach, strawberry, orange juice. 
Berry-berry ………………………………………………………………………………… … $7.5 ………………. $9
Strawberry, blueberry, blackberries, cherries, cranberry juice. 
PBS ………………………………………………………………………………………………… $7 …………………  $8.5
Peanut butter, banana, almonds, milk, yogurt. 
Green …………………………………………………………………………………………….. $7 ………………… $8.5
Kale, green grapes, pineapple, chia seeds, apple juice. 
Detox …………………………………………………………………………………………….. $8 ………………… $9.5
Apple, pineapple, banana, ginger, spinach, lime juice. 
Matcha ………………………………………………………………………………………….. $8 ………………… $9.5
Banana, matcha powder, spinach, milk. 
Double roast …………………………………………………………………………………. $6.5 ……………… $8
Banana, oats, yogurt, espresso, cinnamon, milk. 
SUB: Non-dairy options (Almond, oat, soy) $0.8
Add powdered protein to any smoothie $1.3
ASIAN
Tandoori chicken kebab …………………………………………………………………………………………... $16
Bread, papadum, raita, chutney. 
Seek kebab ……………………………………………………………………………………………………………….. $18
Lamb, bread, papadum, raita, chutney.
Butter chicken ………………………………………………………………………………………………………….. $17
Rice, bread, raita, papadum.
Chickpea curry (VG) ………………………………………………………………………………………………….. $12
Rice, bread, raita, papadum.
Tandoori kebab basket (chicken and lamb) …………………………………………………….………… $17
bread, raita, papadum, chutney.
Thai coconut curry …………………………………………….….…………………. Chicken $10 ………… Shrimp $13
Rice.
Bami goreng noodles ………………………………………………………………. Chicken $10 ……….… Shrimp $13
Teriyaki stir fry ……………………………………………………………………..…. Chicken $14 ……….… Shrimp $16 
Rice, sesame seeds. 
Sweet and sour ……………………………………………………………………….. Chicken $10 …………. Shrimp $13
Rice.
Vegetable Samosa (2- pieces) ………………………………………………………………………………… $7.99
Chickpea, raita, chutney. 
Vegetable spring roll …………………………..………………………………………………….………………. $3 each
Sweet chili sauce. 
Tandoori breadbasket ……………………………………………………………………………………………….. $6
Bread, raita, chutney. 

AMERICAN
BLK beef burger ………………….………………..…... Single $13 …….. Fries $15.5 …….. House salad $17.5
Smoked cheddar, caramelized onions, tomato, arugula, chipotle aioli. 
Black bean burger (VG) ……………………………… Single $13 .….... Fries $12 …….…. House salad $14 
Lettuce, tomato, onion, spicy hummus spread. 
Chimichurri steak …………………………………………………………….…. Fries $15.5 …..... House salad $17.5
Beer batter Fish & Chips ……………………………………………….. 1- piece $12 ………..……. 2- pieces $18
Causa Limeña ……………………………………………………………………………………………………………..…….. $12
Mashed potato, shrimp, avocado, house salad.
Pulled pork Taco (2- 6” corn tortilla) ………..…………………………………………………………………….…. $11
Grilled pineapple, cheese, jalapeno sour crème sauce. 
Fish Taco (2- 6” corn tortilla) ………………………………………………..…………………………………………… $12
Fried haddock, feta cheese, pico de gallo, cilantro-lime sauce. 
Steak Taco (2- 6” corn tortilla) …………………………………………………………………………………………… $15
Steak, cheese, mole, jalapeno sour crème sauce. 
French fries ……………………………………………………………………………………………………………………….. $5
Truffle fries ……………………………………………………………………………………………………………………….. $6 
Poutine ………………………………………………………………………………………………..…………………………... $6.5
Cheese curds, gravy. 

MEDITERRANEAN

Build your own Pizza …………………………………..…………………………………………………………….……… $11
Tomato sauce or pesto sauce, mozzarella. 
	Add protein $1.5 				Add cheese $2
Signature Pizzas
Deluxe ………………………………..…………………………………………………….……………………………….……… $14
Tomato sauce, mozzarella cheese, gorgonzola, prosciutto, caramelized pear.  
Margherita ……………………………………………………………………………………………………………….……….. $11
Tomato sauce, fior de latte, parmesan cheese, basil. 
Funghi ……………………………………………………………………………………………………………………….…….… $14
Olive oil, fontina cheese, roasted mushrooms, truffle oil. 
Eggplant Parmigiana …………………………………………………………………………………………………….……. $12
Tomato sauce, mozzarella cheese, fior de latte, basil. 
Vegetarian Lasagna (personal) …………………………………………………………………………………………… $13
Tomato sauce, three cheeses, roasted vegetables. 

      Shawarma  	Donair 	 Falafel (VG)
Plate ……………………………………………………………. $16 ………………. $15 ………...……. $13
Salad, hummus, garlic sauce, crispy chickpeas, pita , rice, or fries.  
Bowl ……………………..……………………………..….…. $10.5 ………..…. $10.5 ………..….. $9.5
Hummus, garlic sauce, pita, crispy chickpeas.
Wrap ……………………………………………………..……. $9.5 …………….. $9.5 ………………. $8.5 
Vegetables, hummus, garlic sauce.
Hummus + toasted pita ……………………………………………………………………………………………………. $6

BAR
White Wine per glass
	House wine, Pinot Grigio, Argentina ……………………………………………………………………… $8	
Benjamin Bridge Tidal Bay, Nova Scotia .………………………………………………………….……. $11
Pendfold’s Rawson, Chardonnay, Australia ..………………………………………………………….. $9
Beringer, Sauvignon Blanc, United States ………………………………………………………………. $10
Red Wine per glass
	House wine, Syrah, Argentina .…………………………..…………………………………………………... $8
Grand Pre Baco Noir, Nova Scotia ………………………………………………………………………….. $11
	Monte Give Sangiovese, Merlot, Italy …………………………………………………………………….. $8
	Confessions, Cabernet Sauvignon, United States ……………..…………………………………….. $10
Rose and Sparkling wine
	Claude Val Rose ……………………………………………………………………………………………………… $10
	Poema Cava Brut ……………………………………………………………………………………………………. $12
Cocktails
	Caesar	……………………………………………………………………………………………………………………. $10
	Apple Martini ……………………………………………………………………………………………………….… $14
	BLK G&T …………………………………………………………………………………………………………………. $16
	Blackberry Margarita ……………………………………………………………………………………………… $16
	Passion fruit Mojito ………………………………………………………………………………………………... $16
	Lavender Pisco sour ………………………………………………………………………………………………… $16
	Old Fashioned …………………………………………………………………………………………………………. $16
	Sangria ……………………………………………………………………………………………………………………. $11
Mocktails
	Thai fruit cocktail …………………………………………………………………………………………………….. $7
Pink fizz …………………………………………………………………………………………………………………… $6
Sober Sunday ………………………………………………………………………………………………………….. $6

















Pastries Display (small business card size with holder): 
Not going up on the board
	•	Apple strudel $5
	•	Croissant $3.75 
	•	Pan au chocolat $3.95 
	•	Almond $4.50
	•	Muffins (banana, carrot, blueberry, cranberry lemon) $2.50
	•	Cookies $3.50
	•	Vanilla yogurt cheesecake $8.50
	•	Millefeuilles $8
	•	Berries merengue roll $5.50 per piece.
	•	Fruit mousse $4
	•	Linzer tart $8.50
	•	Lemon merengue pie portion $6
	•	Éclair (chocolate or coffee) $3 
	•	Coconut cake portion $7
	•	Red velvet cake $7
 
"""
# Convert the text to lowercase and remove whitespace
input_text_lower = "".join(input_text.lower().split())

# Count the frequency of each character
character_counts = Counter(input_text_lower)

# Separate the alphabetical and numerical characters
alphabetical_counts = {
    key: value for key, value in character_counts.items() if key.isalpha()
}
numerical_counts = {
    key: value for key, value in character_counts.items() if key.isdigit()
}
other_counts = {
    key: value
    for key, value in character_counts.items()
    if not key.isalpha() and not key.isdigit()
}

# Sort the characters alphabetically and numerically
sorted_alphabetical = sorted(alphabetical_counts.items())
sorted_numerical = sorted(numerical_counts.items())
sorted_other = sorted(other_counts.items())

# Print the results
for item in sorted_other:
    print(f"{item[0]}: {item[1]}")
for item in sorted_alphabetical:
    print(f"{item[0]}: {item[1]}")
for item in sorted_numerical:
    print(f"{item[0]}: {item[1]}")
