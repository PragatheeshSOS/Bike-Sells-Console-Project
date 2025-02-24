from bike import Bike
from customer import Customer
from order import Order
from admin import Admin
from payment import Payment

bikes = [Bike(1, "YZF R15", "Yamaha", 200000, "155cc", 5, "Available"),Bike(2, "Ninja 300", "Kawasaki", 500000, "300cc", 3, "Available")]
customers = []
admin = Admin(1, "Admin", "admin123")

while True:
    print("\n1. View Bikes\n2. Register Customer\n3. Login Customer\n4. Place Order\n5. View Orders\n6. Cancel Order\n7. Admin Panel\n8. Exit")
    choice = input("Enter choice: ")
    
    if choice == "1":
        print("\n\n--- BIKE DETAILS ---")
        for bike in bikes:
            bike.displayDetails()
    elif choice == "2":
        firstname = input("Enter First Name: ")
        while firstname.isalpha() == False:
            print("Name Should Only Contains Alphabets.")
            firstname = input("Enter First Name: ")
        lastname = input("Enter Last Name: ")
        while lastname.isalpha() == False:
            print("Name Should Only Contains Alphabets.")
            lastname = input("Enter Last Name: ")
        name = firstname+" "+lastname
        #Fix....👇🏻
        contact = input("Enter Contact: ")
        while len(contact) != 10 and contact.isnumeric() == False:
            print("Contact Number Should Only Contains Numbers And Verify Its Of 10 Digit.")
            contact = input("Enter Contact: ")
        emailverify = False
        email = input("Enter Gmail ID: ")
        while emailverify:
            if '@gmail.com' in email:
                emailverify = True
            else:
                print('Enter Correct Gmail ID.')
                email = input("Enter Gmail ID: ")
        #Fix....👇🏻
        password = input("Enter Password: ")
        while len(password) >=8 and password.isalnum() == False:
            print("Password Should Contain Both Numbers & Alphabets. It Should Be Length Of More Than 8.")
            password = input("Enter Password: ")
        customer = Customer(len(customers)+1,name,contact,email,password)
        customers.append(customer)
        customer.register()
        #Fix....👇🏻
    elif choice == "3":
        email,password = input("Enter Email: "),input("Enter Password: ")
        while Customer.login(email,password) == False:
            email,password = input("Enter Email: "),input("Enter Password: ")
    elif choice == "4":
        print('4')
    elif choice == "5":
        print('5')
    elif choice == "6":
        print('6')
    elif choice == "7":
        print('7')
    elif choice == "8":
        print("Why So Soon.........")
        break
    else:
        print("Invalid option! Try again.")