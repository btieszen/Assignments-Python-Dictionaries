# Python Programming Challenges for Customer Service Data Handling
# Task 1: Customer Service Ticket Tracker 
#Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
#Implement functions to:
#Open a new service ticket.
#Update the status of an existing ticket.
#Display all tickets or filter by status.
#Initialize with some sample tickets and include functionality for additional ticket entry.



def open_ticket(service_tickets,new_ticket):
    if new_ticket not in service_tickets:
        service_tickets[new_ticket]={}
        print(f"New Ticket: '{new_ticket}' had been added")
        



       

        
    
    
   
 
    


service_tickets = {"Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
                  "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}}


while True:
    print("\n Welcome to the Customer Service Ticket Tracker")
    print("1: Add New Ticket\n2: Update existing ticket\n3: Display all Tickets\n4: End")
    
    choice =input("Please make Your selection: ")
    if choice =="1":
        new_ticket=input ("What is the name of new ticket: ")
        customer_name =input("What is the name of the customer:  ")
        issue =input("What is the issue: ")
        status1 =input("Is the ticket still open(yes/no)").lower()
        if status1 !="yes":
            status ="closed"
        else: status ="open"
        service_tickets[new_ticket]={"Customer": customer_name,"Issue": issue,"Status": status}
    elif choice =="2":
        try:
            update=input("What ticket would you like to update: ")
            if update not in service_tickets:
                print(f"Sorry not in Ticket tracker")
            else:
                print(f"What would you like to update:")
                print(f"Customer\nIssue\nStatus ")
            update_choice=input("Please enter your selection:")
            if not ("Customer" or "Issue" or "Status"):
                print("Not a valid entry")
            if update_choice=="Customer":
                new_customer=input("What is the name of the new customer: ")
                service_tickets[update][update_choice]=(new_customer)
            elif update_choice=="Issue":
                new_issue=input("What is the new issue: ")
                service_tickets[update][update_choice]=(new_issue)
            elif update_choice=="Status":
                new_status=input("Is the ticket still open(yes,no)").lower()
                service_tickets[update][update_choice]=(new_status)
        except ValueError:
            print("Invalid entry plrease try again")
       
    elif choice =="3":
        print("The Customer Service Tickets are: ")
        print(service_tickets)
    elif choice =="4":
        print("Thank you for using the Customer Service Tractor, Goodbye")
        break
    

open_ticket(service_tickets,new_ticket)




    
                          













