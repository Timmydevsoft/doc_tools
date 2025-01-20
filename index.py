shopping_cart = {}
def add_to_cart(item_name, price, *args, **kwargs):
    if item_name in shopping_cart:
        print(f"{item_name} already added to cart")
        return
    total_price = price
    if len(args) !=0:
        for discount in args:
            total_price *=(1-discount/100)
    shopping_cart[item_name]={
        "item_name": item_name,
        "total_price": total_price,
        "description": kwargs
    }
def display_Summary():
    print("----Cart Summary---")
    i=0
    total_price=0
    for item, details in shopping_cart.items():
        i+=1
        total_price+= details['total_price']
        if details["description"]:
            description_texts= ", ".join(f"{key}-{value}" for key, value in details["description"].items() )
            print(f"{i}:  {item} ${details['total_price']} description: {description_texts}")
        else:
            print(f"{i}: {item} ${details["total_price"]}")    
    print(f"Total Price: ${total_price}")
while True:
    item_name= input("Enter the name of item or done to done: ")   
    if item_name == "done":
        break
    try:
        price= float(input("Enter price: ").strip()) 
    except ValueError:
        print("Invalid price! Please enter a numeric value.")
        continue
    discount_input = input("Enter discount if there is any seperated by spaces or none to continue: ")
    discounts=[]
    if discount_input and discount_input != 'none':
        discounts = [float(d) for d in discount_input.split() ]
    else:
        discounts=[]
    description={}
    add_description = input("Do you want to add description yes/no: ").strip().lower()
    if add_description == "yes":
        while True:
            key= input("Enter description name or done to finish: ").strip()
            if key=="done":
                break
            else:
                value = input("Enter description value: ")
                description[key]=value
    add_to_cart(item_name, price, *discounts, **description)

display_Summary()