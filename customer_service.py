'''Develop a program that:

Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
Implement functions to:

Open a new service ticket.
Update the status of an existing ticket  to "closed".
Display all tickets.
(Bonus) filter by status

Initialize with some sample tickets and include functionality for additional ticket entry.'''

import os

def clear():

    os.system('cls' if os.name == 'nt' else 'clear')

service_tickets = {
    1: {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    2: {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}


def next_id(): # created a function that will return an id for the next service ticket
    last_id = 0
    for id in service_tickets.keys():
        if id > last_id:
            last_id = id

    return last_id + 1

def new_ticket():
    while True:
        new_id = next_id()
        customer = input("Enter the customer's name: \n")
        issue = input("Enter the issue: \n")
        print(f"Customer: {customer}, Issue: {issue}")
        
        correct = input('Does this information look correct? (y/n)')
        correct = correct.lower()
        if correct == 'y':
                service_tickets[new_id] = {"Customer": customer, "Issue": issue, "Status": "open"}
                print(f"Service ticket {new_id} created.")
        elif correct == 'n':
                print("Service ticket not created.")
        else:
                print("Invalid input. Please enter 'y' or 'n'.")   
                continue 
        
        break 

def update_ticket():
    while True:
        ticket_id = int(input("Enter the ticket ID: "))
        if ticket_id in service_tickets.keys():
            service_tickets[ticket_id]["Status"] = "closed"
            print(f"Service ticket {ticket_id} updated to closed.")
        else:
            print(f"Ticket ID {ticket_id} not found.")
        break
    
def display_tickets():
    for ticket_id, ticket in service_tickets.items():
        print(f"Ticket ID: {ticket_id}")
        for key, value in ticket.items():
            print(f"{key}: {value}")

def filter_tickets(status):
    for ticket_id, ticket in service_tickets.items():
        if ticket["Status"] == status:
            print(f"Ticket ID: {ticket_id}")
            for key, value in ticket.items():
                print(f"{key}: {value}")

def quit():
    print("Thank you for using the service ticket management system. Goodbye.")
    exit()

def main():
    while True:
        try:    
            ans = int(input('''
SERVICE TICKET MANAGEMENT SYSTEM
Enter the corresponding number for the action you'd like to take:
1- Open a new service ticket.
2- Update the status of an existing ticket to "closed".
3- Display all tickets.
4- Filter by status.
5- Quit\n'''))
        
            if ans == 1:
                clear()
                new_ticket()
            elif ans == 2:
                clear()
                update_ticket()
            elif ans == 3:
                clear()
                display_tickets()
            elif ans == 4:
                filter_tickets("open")
                filter_tickets("closed")
            elif ans == 5:
                quit()
            else:
                print("Invalid input. Please enter a number between 1 and 5.")
                continue
        except ValueError:
            print("Incorrect value type. Please enter a number between 1 and 5.")
            continue

main()

