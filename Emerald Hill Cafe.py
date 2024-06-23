# Bran Odom
# Feb 18, 2024
# HW Assignment 3: Snack bar menu program.

#Define the main function.
def main():
    
    #Declare and initialize constants.
    TAX = 0.07
    CHILI_DOG = 13.0
    STEW = 17.5
    SANDWICH = 10.5
    BENEDICT = 14.5
    SALAD = 12.0
    DUCK = 28.5
    ONION_RINGS = 6.0
    SPRITZ = 5.0
    #Declare and initialize variables.
    user_name = ""
    order_again = "yes"
    selection = 0
    total_tax = 0.0
    subtotal = 0.0
    total = 0.0
    #Display intro.
    print("-"*45)
    print("""\tWelcome to
\t __   __          __  .  __  
\t/__` /  \\ |\\ | | /  ` ' /__` 
\t.__/ \\__/ | \\| | \\__,   .__/

\t\tEmerald Hill Cafe!
""")
    print("-"*45)

    #Outer loop to order again.
    while order_again == "yes":
        
        #Prompt for name.
        user_name = input("\nWhat's the name for your order?\t")

        #Reset totals.
        total_tax = 0.0
        subtotal = 0.0

        #Re-seed inner loop.
        selection = 0

        #Inner loop to display menu and subtotals.
        print("\nGreat! Take a look at our menu and select what you'd like.")

        while selection != 9:
            print("\nHere's what we have:")
            print(f"""
        1. Sonic's Signature Chili Dog - ${CHILI_DOG:,.2f}
        2. FoxTails Stew - ${STEW:,.2f}
        3. Knuckles Sandwich - ${SANDWICH:,.2f}
        4. Eggman's Benedict - ${BENEDICT:,.2f}
        5. Chao Garden Salad - ${SALAD:,.2f}
        6. Duck à la Rouge - ${DUCK:,.2f}
        7. Gold Ring Onions - ${ONION_RINGS:,.2f}
        8. Amy Rosewater Spritz - ${SPRITZ:,.2f}
        9. Complete Order""")

            #Prompt for selection.
            selection = int(input("\nPlease enter the number of the item you want to select:\t"))

            #Selection structure to calculate subtotal.
            if selection == 1:
                total_tax += CHILI_DOG * TAX
                subtotal += CHILI_DOG
                print(f"\nYour subtotal is: ${subtotal:,.2f}")
            elif selection == 2:
                total_tax += STEW * TAX
                subtotal += STEW
                print(f"\nYour subtotal is: ${subtotal:,.2f}")
            elif selection == 3:
                total_tax += SANDWICH * TAX
                subtotal += SANDWICH
                print(f"\nYour subtotal is: ${subtotal:,.2f}")
            elif selection == 4:
                total_tax += BENEDICT * TAX
                subtotal += BENEDICT
                print(f"\nYour subtotal is: ${subtotal:,.2f}")
            elif selection == 5:
                total_tax += SALAD * TAX
                subtotal += SALAD
                print(f"\nYour subtotal is: ${subtotal:,.2f}")
            elif selection == 6:
                total_tax += DUCK * TAX
                subtotal += DUCK
                print(f"\nYour subtotal is: ${subtotal:,.2f}")
            elif selection == 7:
                total_tax += ONION_RINGS * TAX
                subtotal += ONION_RINGS
                print(f"\nYour subtotal is: ${subtotal:,.2f}")
            elif selection == 8:
                total_tax += SPRITZ * TAX
                subtotal += SPRITZ
                print(f"\nYour subtotal is: ${subtotal:,.2f}")
                
            #Calculate total.
            elif selection== 9:
                if subtotal == 0.0:
                    order_again = input("\nYour order is empty. Type 'yes' to try again.\t") 
                else:
                    print("\n Calculating total...\n")

                    total = subtotal + total_tax
                    print(f"Subtotal: ${subtotal:,.2f}")
                    print(f"Taxes: ${total_tax:,.2f}")
                    print("-"*25)
                    print(f"Total: ${total:,.2f}")
                    print(f"\nThank you {user_name} for your patronage!")
                    order_again = input("\nWould you like to place an order for somebody else? Type 'yes' or 'no'.\t").lower()
                    
            else:
                print("\nYou must enter a number 1-9. Please try again.")

            
    #Display outro.
    if subtotal == 0.0:
        print(f"\nSorry to see you go, {user_name}. Come back soon!")
    else:
        print(f"\nThanks {user_name} for dining at the Emerald Hill Cafe!")

#Call the main function.
main()
