class Checklist:

    def generate_checklist(self, country_name):

        checklist = [
            "Passport",
            "Visa",
            "Flight Ticket",
            "Accommodation",
            "Travel Insurance"
        ]

        print(f"\nTravel Checklist for {country_name}")

        with open("travel_checklists.txt", "a") as file:
            file.write(
                f"\nTravel Checklist for {country_name}\n"
            )

            for item in checklist:
                print(f"[ ] {item}")
                file.write(f"[ ] {item}\n")

guide = Checklist()
guide.generate_checklist("nigeria")