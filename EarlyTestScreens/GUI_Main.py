# imports
import json
import requests
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

# Personal API KEY
api_key = 'GHNXaxsTmnroXTDG3O-v_pV3dV-yzraTyR_GbGsttZww8dRASFHsRqkvaQQMRIKgARvQk0AIfkF9m_-8Wfuc3XrUkr-FanBkgBpKJ8z6gKniuz-PdyptiHsids-gYXYx'
headers = {'Authorization': 'Bearer %s' % api_key}
# URL
url = 'https://api.yelp.com/v3/businesses/search'

#Setup Window
class MainWindow(qtw.QWidget):
    #class intialisation
    def __init__(self):
        super().__init__()
        #Title

        self.setWindowTitle("Restaurant Deciding App (V1.0)")

        #Set QForm layout
        form_layout = qtw.QFormLayout()
        self.setLayout(form_layout)

        #labels

        my_label = qtw.QLabel("Fill out the form to get started!")

        #Font
        my_label.setFont(qtg.QFont('Helvetica', 20))
        self.layout().addWidget(my_label)

        #Entry Boxes
        Loc = qtw.QLineEdit()
        Loc.setObjectName("Location")
        Loc.setPlaceholderText("e.g. London or PostCode")
        form_layout.addRow("Location: ", Loc)

        Dist = qtw.QLineEdit()
        Dist.setObjectName("Distance")
        Dist.setPlaceholderText("e.g. (within) 5 (miles)")
        form_layout.addRow("Distance: ", Dist)

        #combo boxes
        Price = qtw.QComboBox(self)
        ##add items with data
        Price.addItem("£", 1)
        Price.addItem("££", 2)
        Price.addItem("£££", 3)
        Price.addItem("££££", 4)
        form_layout.addRow("Price Range: ", Price)

        #Button
        my_button = qtw.QPushButton("Submit!", clicked= lambda: pressed(Loc.text(),Dist.text(),Price.currentData()))
        self.layout().addWidget(my_button)

        #Show = true
        self.show()

        #functions
        def pressed(Loc, Dist, Price):
            my_label.setText('Loading... Restaurants')

            print("Searching with parameters " + f'{Loc},{Dist},{Price}')


            # Location of user
            Usr_Location = Loc

            # Distance from location (radius)
            Usr_Distance = float(Dist)
            if Usr_Distance > 25.0:
                Usr_Distance = float(25.0)

            # change miles to meters (as thats what the API takes in)
            Usr_Distance = round(Usr_Distance * 1609.34)
            print(Usr_Distance, 'meters')

            # Price
            Price_Range = Price

            # Price can be a comma delimited list e.g. 1,2,3 = between £ and £££
            Price_levels = []
            for i in range(Price_Range):
                Price_levels.append(str(i + 1))
            print("price range:" , Price_levels)
            # Get restaurants at user location
            params = {'term': 'Restaurants', 'location': Usr_Location, 'radius': Usr_Distance, 'price': Price_levels}

            # making get request
            req = requests.get(url, params=params, headers=headers)
            # proceed with status code 200
            print('\nThe status code is {}'.format(req.status_code))
            print()
            # print text from response
            parsed = json.loads(req.text)
            # print(json.dumps(parsed, indent=4))

            # get all businesses
            ##list of businesses
            businesses = parsed["businesses"]
            # for each business print name rating address and phone

            for business in businesses:
                print("Name:", business["name"])
                print("Rating:", business["rating"])
                print("Price:", business["price"])
                print("Address:", " ".join(business["location"]["display_address"]))
                print("Phone:", business["phone"])
                print("\n")

            print("20 max requests", len(businesses))


#App instance
myapp = qtw.QApplication([])
#Window
window = MainWindow()
#Run
myapp.exec_()







#Links
# https://python.gotrained.com/yelp-fusion-api-tutorial/
#https://www.yelp.com/developers/documentation/v3/business_search

