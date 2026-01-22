from customer import Customer
from staff import Staff
from vehicle import Vehicle
from rental_order import RentalOrder
from rental_detail import RentalDetail
from payment import Payment

def main():
    print("VEHICLE RENTAL SYSTEM")

    customer = Customer("1", "Nguyen Van A", "a@gmail.com", "123",
                        "0909", "HN", "2025-01-01", "customer")

    print("\n1. VIEW VEHICLE LIST")
    vehicles = Vehicle.load_all()
    for v in vehicles:
        print(v.vehicle_id, v.name, v.price_per_day, v.status)

    print("\n2. BOOK VEHICLE")
    order = RentalOrder("101", customer.user_id,
                        "2025-01-10", "2025-01-12",
                        "200", "new")
    order.save()

    detail = RentalDetail("1", "101", "V01", 100, 2)
    detail.save()

    print("Order created")

    print("\n3. MAKE PAYMENT")
    payment = Payment("1", "101", "cash", "2025-01-10", "paid")
    payment.save()
    order.update_status("confirmed")

    print("Payment successful")

    print("\n4. STAFF CREATE CONTRACT")
    staff = Staff("2", "Tran Staff", "s@gmail.com", "123",
                  "0999", "HN", "2025-01-01", "staff")

    staff.create_contract(
        "C01", "101", customer.user_id,
        "V01", "2025-01-10", "2025-01-12"
    )

    staff.print_contract("C01")

    print("\n5. VEHICLE HANDOVER")
    staff.handover_vehicle("C01")

    print("\n6. VEHICLE RETURN")
    staff.receive_vehicle("C01")

    print("\nEND SYSTEM")

if __name__ == "__main__":
    main()
