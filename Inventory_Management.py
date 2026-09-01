import Database


Options = """
---------- Inventory Management System ----------

1. Add Product           2. Update Product
3. Remove Product        4. View Inventory
5. Search Product        6. Total Value Of Inventory
7. Exit

"""


App_On = True

while App_On:

    print(Options, "\n")

    User_Choice = input("Enter Your Choice (1-7): ")
    print("\n")


    # Add Product
    if User_Choice == "1":

        New_Product_Name = input("Enter Product Name: ")
        New_Product_Price = float(input("Enter Product Price: $"))
        New_Product_Quantity = float(input("Enter Product Quantity(Kg): "))

        Database.add_product(
            New_Product_Name,
            New_Product_Price,
            New_Product_Quantity
        )

        print("Product Added Successfully.\n")


    # Update Product
    elif User_Choice == "2":

        while True:

            Product_Name = input("Enter Product Name: ")

            Product = Database.get_product(Product_Name)

            if Product is not None:

                Product_Price = float(input("Enter Product Price: $"))
                Product_Quantity = float(input("Enter Product Quantity(Kg): "))

                Database.update_product(
                    Product_Name,
                    Product_Price,
                    Product_Quantity
                )

                print("Product Updated Successfully.\n")

                break

            else:

                print("Product Not Found.\n")


    # Remove Product
    elif User_Choice == "3":

        while True:

            Product_Name = input("Enter Product Name: ")

            Product = Database.get_product(Product_Name)

            if Product is not None:

                Database.remove_product(Product_Name)

                print("Product Removed Successfully.\n")

                break

            else:

                print("Product Not Found.\n")


    # View Inventory
    elif User_Choice == "4":

        Products = Database.get_products()

        print("Product\t\tPrice\t\t\tQuantity\n")

        for Product in Products:

            print(
                f"{Product[1]}\t\t"
                f"${Product[2]}\t\t\t"
                f"{Product[3]}Kg"
            )

            print("\n")


    # Search Product
    elif User_Choice == "5":

        while True:

            Product_Name = input("Enter Product Name: ")

            Product = Database.get_product(Product_Name)

            if Product is not None:

                Price = Product[2]
                Quantity = Product[3]

                print(
                    f"\nProduct: {Product_Name}"
                    f"\t\tPrice: ${Price}"
                    f"\t\tQuantity: {Quantity}Kg\n"
                )

                break

            else:

                print("Product Not Found.\n")


    # Total Value Of Inventory
    elif User_Choice == "6":

        Total_Value = Database.get_total_value()

        print(
            f"Total Value Of Inventory: ${Total_Value}\n"
        )


    # Exit
    elif User_Choice == "7":

        print("Exited !\n")

        App_On = False
