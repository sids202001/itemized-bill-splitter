def main():
    print("========================================")
    print("   🛒 Shared Bill & Expense Splitter    ")
    print("========================================")
    
    people_input = input("\nEnter the names of the 3 people sharing (comma separated, e.g. Me, Friend1, Friend2): ")
    people = [p.strip() for p in people_input.split(',') if p.strip()]
    
    if not people:
        print("You need to enter at least one person! Exiting.")
        return

    totals = {person: 0.0 for person in people}
    
    print("\n--- Let's add the items from the bill ---")
    print("Type 'done' as the item name when you are finished adding items.\n")
    
    while True:
        item = input("\nItem name (or 'done'): ")
        if item.lower() == 'done':
            break
            
        try:
            price = float(input(f"How much did '{item}' cost? $"))
        except ValueError:
            print("❌ Invalid price. Please enter a valid number.")
            continue
            
        print(f"Who is sharing this? (Type 'all' or enter specific names: {', '.join(people)})")
        split_input = input("Shared by: ")
        
        if split_input.lower().strip() == 'all':
            shared_by = people
        else:
            shared_by = [p.strip() for p in split_input.split(',') if p.strip()]
            
            # Check if names are valid
            invalid_names = [p for p in shared_by if p not in people]
            if invalid_names:
                print(f"❌ Error: Names not recognized -> {', '.join(invalid_names)}")
                print(f"Please use the exact names you provided: {', '.join(people)}")
                continue
                
        if not shared_by:
            print("❌ No one selected. Item not added.")
            continue
            
        split_amount = price / len(shared_by)
        for person in shared_by:
            totals[person] += split_amount
            
        print(f"✅ Added! ${price:.2f} split between {', '.join(shared_by)} (${split_amount:.2f} each).")

    # Handle Taxes/Tip globally
    try:
        tax_tip = float(input("\nAny total Tax, Tip, or Bag Fees to add? $"))
    except ValueError:
        tax_tip = 0.0
        
    if tax_tip > 0:
        tax_split = tax_tip / len(people)
        for person in people:
            totals[person] += tax_split
        print(f"✅ Added ${tax_tip:.2f} tax/tip split evenly (${tax_split:.2f} each).")

    print("\n========================================")
    print("             💰 FINAL AMOUNTS           ")
    print("========================================")
    total_bill = 0
    for person, amount in totals.items():
        print(f"👤 {person}: ${amount:.2f}")
        total_bill += amount
        
    print("-" * 40)
    print(f"🧾 Total Bill Computed: ${total_bill:.2f}")
    print("========================================\n")

if __name__ == "__main__":
    main()
