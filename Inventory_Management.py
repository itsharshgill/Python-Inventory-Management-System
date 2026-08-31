Product = {"Apple":{"Price":7.99, "Quantity": 250}, "Banana":{"Price":2.99, "Quantity": 150}, "Orange":{"Price":5.95, "Quantity": 75}, "Mango":{"Price":9.99, "Quantity": 80}}

App_On = True
Options = """ 
 ---------- Inventory Management System ----------
 
 1. Add Product           2. Update Product
 3. Remove Product        4. View Inventory
 5. Search Product        6. Total Value Of Inventory
 7. Exit
 """
while App_On: 
  print(Options,"\n")

  User_Choice = input("Enter Your Choice (1-7): ")
  print("\n")

  if User_Choice == "1":
      New_Product_Name = input("Enter Product Name: ") 
      New_Product_Price = eval(input("Enter Product Price: $"))
      New_Product_Quantity = eval(input("Enter Product Quantity(Kg): "))
      Product.update({New_Product_Name:{"Price":New_Product_Price, "Quantity":New_Product_Quantity}})
      print("Product Added Successfully.\n")

  elif User_Choice == "2":
    while True:
      Product_Name = input("Enter Product Name: ")
      if Product_Name in Product:
        Product_Price = eval(input("Enter Product Price: $"))
        Product_Quantity = eval(input("Enter Product Quantity(Kg): "))
        Product.update({Product_Name:{"Price":Product_Price, "Quantity":Product_Quantity}})
        print("Product Updated Successfully.\n")
        break
      else:
        print("Product Not Found.\n")
        
  elif User_Choice == "3":
    while True:
      Product_Name1 = input("Enter Product Name: ")
      if Product_Name1 in Product:
          Product.pop(Product_Name1)
          print("Product Removed Successfully.\n")
          break
      else:
        print("Product Not Found.\n")

    
  elif User_Choice == "4":
   Sorted_Items = sorted(Product.items())  
   print("Product\t\tPrice\t\t\tQuantity\n")
   for Product_Name, Product_Info in Sorted_Items:
    print(f"{Product_Name}\t\t${Product_Info['Price']}\t\t\t{Product_Info['Quantity']}Kg")
    print("\n")


  elif User_Choice == "5":
    while True:
      Product_Name2 = input("Enter Product Name: ")
      if Product_Name2 in Product:
       Price = Product[Product_Name2]['Price']
       Quantity = Product[Product_Name2]['Quantity']
       print(f"\nProduct: {Product_Name2}\t\tPrice: ${Price}\t\tQuantity: {Quantity}Kg\n")
       break
      else:
        print("Product Not Found.\n")
      
  elif User_Choice == "6":
    Product_Value_List = []
    for Num1 in Product.values():
      Product_Value = Num1['Price'] * Num1['Quantity']
      Product_Value_List.append(Product_Value)
    print("Total Value Of Inventory: $",sum(Product_Value_List),"\n")

  elif User_Choice == "7":
    print("Exited !\n")
    exit()
  

    