def speeding_ticket(speed, is_birthday):
    # Adjust speed limits if it's the driver's birthday
    if is_birthday:
        speed -= 5

    # Check the speed and assign ticket accordingly
    if speed <= 60:
        return "No Ticket"
    elif speed <= 80:
        return "Small Ticket"
    else:
        return "Big Ticket"

# Example usage:
speed = int(input("Enter the driver's speed: "))
is_birthday = input("Is it the driver's birthday? (yes/no): ").lower() == 'yes'

ticket = speeding_ticket(speed, is_birthday)
print("The driver should receive a", ticket)
