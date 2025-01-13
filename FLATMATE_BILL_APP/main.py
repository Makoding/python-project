from fpdf import FPDF
import webbrowser


class House:

    # Constructor of class House with parameters the number of rooms,
    # flatmates (list) the bill amount that flatmates have to share,
    # and the specific period (month) the bill is related to.
    def __init__(self, rooms, flatmates, bill_amount, bill_period):
        self.rooms = rooms
        self.flatmates = flatmates
        self.bill_amount = bill_amount
        self.bill_period = bill_period

    # Method for adding a new flatmate to the house
    # provided that the number of flatmates does not exceeding the number of rooms
    def add_flatmate(self, new_flatmate_name, stayed_in_house):
        if len(self.flatmates) == self.rooms:
            print("The rooms of the house are full! Can't accept new flatmates")
            return False
        else:
            new_flatmate = Flatmate(new_flatmate_name, stayed_in_house)
            self.flatmates.append(new_flatmate)


class Flatmate:
    # Constructor for the Flatmate class
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    # Method that returns the amount of money a given flatmate has to pay
    # based on the days he has stayed at the house
    def pays(self, bill, flatmates)->float:
        sum = 0
        for object in flatmates:
            sum += object.days_in_house
        weight =  self.days_in_house / sum
        return round(weight * bill,2)


class PdfReport:

    def __init__(self, filename, house):
        self.filename = filename
        self.house = house

    # method that generates the pdf
    # all the details about the pdf viewing on the users pc
    # are parametrized here as well
    def generate(self, house_flatmates):
        # Setting some variables for polishing the code
        flatmate_infos_width = 175
        period_infos_width = 175


        # 'P': Portrait mode, 'pt': font of the text (e.g. 12 point = 16 pixels
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icons
        pdf.image("house.png",w=50 , h=50)

        # Add some text ('B' is for bold)
        pdf.set_font(family='Times', size=24, style='B')

        # w: width, h:height,
        # align='C': align the text to the centre (on default is left)
        # ln=1: changes the line
        # so that the next cell can be created right beneath it
        # border=1 for viewing the txt inside a rectangle and 0 for not
        # Insert title
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, align='C', ln=1)

        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=period_infos_width, h=40, txt='Period:', border=1) #Insert period label
        # Insert period value
        pdf.cell(w=period_infos_width, h=40, txt=self.house.bill_period, border=1, ln=1)

        # Insert the flatmate Names
        for object in self.house.flatmates:
            pdf.cell(w=flatmate_infos_width, h=40, txt=object.name, border=1)
            pdf.cell(w=flatmate_infos_width, h=40,
                 txt=str(object.pays(self.house.bill_amount, house_flatmates)), border=1, ln=1)


        pdf.output(self.filename)

        webbrowser.open(self.filename)


# Creating the flatmates objects and adding them to a list
flatmates_list = []
rooms_amount = int(input("How many rooms does the house has? "))
residents = int(input("How many flatmates are currently sharing the rent?"))
while residents > rooms_amount:
    residents = int(input("""Its impossible to have more residents than rooms.
Please type again the number of residents: """))
for flatmate in range(residents):
    name = input(f"Give the name of the flatmate number {flatmate+1}: ")
    days_in_house = int(input(f"""Give the number of days 
{name} has lived in house this month: """))
    flatmate_object = Flatmate(name, days_in_house)
    flatmates_list.append(flatmate_object)
rent = int(input("Give the rent of the house: "))
month = input("Give the month that the rent has to be paid: ")
# Creating the house object with all the parameters the user gave.
house_object = House(rooms_amount, flatmates_list, rent, month)

house_object.add_flatmate("luca", 20)

# Creating the pdf report object and calling the method for generating the file
pdf_file = PdfReport("bill.pdf", house_object)
pdf_file.generate(house_object.flatmates)
