questions = [
    ["What is the color of the sky?","Green","Blue","Red","Yellow",2],
    ["How many legs does a cat have?","Two","Four","Six","Eight",2],
    ["What do bees make?","Milk","Honey","Water","Bread",2],
    ["Which shape has three sides?","Square","Circle","Triangle","Rectangle",3],
    ["What is the opposite of hot?","Cold","Warm","Boiling","Spicy",1],
    ["Which animal barks?","Cat","Cow","Dog","Sheep",3],
    ["What is 2 + 2?","3","4","5","6",2],
    ["What color are bananas?","Red","Blue","Yellow","Purple",3],
    ["Which planet do we live on?","Mars","Earth","Venus","Jupiter",2],
    ["What do you use to write on paper?","Spoon","Pencil","Plate","Cup",2]
]


for question in questions:
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")
    
    
    a = int(input("Enter a number 1 for a, 2 for b, 3 for c and 4 for d"))