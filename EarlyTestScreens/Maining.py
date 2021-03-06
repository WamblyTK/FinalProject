# imports
from ast import alias
from glob import glob
import json
from webbrowser import get
import requests
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
from re import S
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QImage, QPixmap
import urllib.request

#Other files 
from RunScreen9Test import Ui_MainWindow

# Personal API KEY
api_key = 'GHNXaxsTmnroXTDG3O-v_pV3dV-yzraTyR_GbGsttZww8dRASFHsRqkvaQQMRIKgARvQk0AIfkF9m_-8Wfuc3XrUkr-FanBkgBpKJ8z6gKniuz-PdyptiHsids-gYXYx'
headers = {'Authorization': 'Bearer %s' % api_key}

# URL
url = 'https://api.yelp.com/v3/businesses/search'

#Global variables
BussinessList = 0
RestaurantNumber= 0
LikedList = []


#Main Window
class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)


        #signal listening, slot function

        #Menu Button
        self.ui.InstructionButton.clicked.connect(self.showInstructions)
        self.ui.SearchButton.clicked.connect(self.showSearch)
        self.ui.SortButton.clicked.connect(self.showSort)
        self.ui.RouletteButton.clicked.connect(self.showRoulette)
        #Search Page
        self.ui.SubmitButton.clicked.connect(self.SearchStage)
        #Sort Page
        self.ui.DislikeButton.clicked.connect(self.Disliked)
        self.ui.LikeButton.clicked.connect(self.Liked)
        self.ui.FinishSortButton.clicked.connect(self.Finished)


    def show(self):
        self.main_win.show()

    #Menu Buttons
    def showInstructions(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)
    def showSearch(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Search)
    def showSort(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Sort)
    def showRoulette(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Roulette)

    #Specific Functions
    def SearchStage(self):
        
        #Search with parameters Location, Distance and Price Range given.
        print("Searching with parameters: " + self.ui.LocLineEdit.text() + ", " + self.ui.DistLineEdit.text() + ", " + self.ui.PRComboBox.currentText())

        #Location
        UsrLocation = self.ui.LocLineEdit.text()

        #Distance from Location (radius in miles)
        UsrDistance = float(self.ui.DistLineEdit.text())
        if UsrDistance > 25.0:
            UsrDistance = 25.0
        UsrDistance = round(UsrDistance * 1609.34)
        print(UsrDistance, 'meters')

        #Price ?? = index 0, ???????? = index 3
        PriceRange = self.ui.PRComboBox.currentIndex()+1
        #Price taken as a comma delimited list --> 1,2,3 is price range ?? to ??????
        PriceLevels = []
        for i in range(PriceRange):
            PriceLevels.append(str(i+1))
        print("price range:" , PriceLevels)

        # Get restaurants at user location
        params = {'limit': 50, 'term': 'Restaurants', 'location': UsrLocation, 'radius': UsrDistance, 'price': PriceLevels}
        # making get request
        req = requests.get(url, params=params, headers=headers)
        # proceed with status code 200
        print('\nThe status code is {}'.format(req.status_code))
        print()
        # print text from response
        parsed = json.loads(req.text)
        # print(json.dumps(parsed, indent=4))
        
        # get all businesses
        
        #list of businesses
        businesses = parsed["businesses"]
        #global 
        global BussinessList
        BussinessList = businesses
        # for each business print name rating address and phone

        #for business in businesses:
            #print("Name:", business["name"])
            #print("Rating:", business["rating"])
            #print("Price:", business["price"])
            #print("Address:", " ".join(business["location"]["display_address"]))
            #print("Phone:", business["phone"])
            #print("image_url", business["image_url"])
            #print("\n")

        #amount of restaurants returned
        print("max requests: ", len(businesses))

        #Sort Phase
        self.displayRestaurants()
        
    
    def displayRestaurants(self):

    
        #CommandLine Test
        #print(type(BussinessList))
        #print("Type: ", BussinessList[RestaurantNumber]["categories"][0].get('title'))
        #print("Name: ", BussinessList[RestaurantNumber]["name"])
        #print("Price: ", BussinessList[RestaurantNumber]["price"])
        #print("Rating: ", BussinessList[RestaurantNumber]["rating"])
        #print("Address: ", ", ".join(BussinessList[RestaurantNumber]["location"]["display_address"]))
        #print("Phone: ", BussinessList[RestaurantNumber]["phone"])
        #print("Image: ", BussinessList[RestaurantNumber]["image_url"])

        #Set Sort page info for restaurants
        #Name
        self.ui.SortText.setText("Name: " + BussinessList[RestaurantNumber]["name"])
        #Type of food
        self.ui.SortText.append("Type: " + BussinessList[RestaurantNumber]["categories"][0].get('title'))
        #Price
        self.ui.SortText.append("Price: " + str(BussinessList[RestaurantNumber]["price"]))
        #Rating
        self.ui.SortText.append("Rating: " + str(BussinessList[RestaurantNumber]["rating"]))
        #Address
        self.ui.SortText.append("Address: " + ", ".join(BussinessList[RestaurantNumber]["location"]["display_address"]))
        #Phone Number
        self.ui.SortText.append("Phone Number: " +  BussinessList[RestaurantNumber]["phone"])
        #Image
        url_image = BussinessList[RestaurantNumber]["image_url"]    
        Restaurantimage = QImage()
        Restaurantimage.loadFromData(requests.get(url_image).content)
        self.ui.ImageLabel.setPixmap(QPixmap(Restaurantimage))
        self.ui.ImageLabel.setScaledContents(True)

    #If liked store in liked list and display next restaurant
    def Liked(self):
        global BussinessList
        global RestaurantNumber 
        global LikedList
        print("Restaurant Number ", RestaurantNumber)
        LikedList.append(BussinessList[RestaurantNumber]["name"])
        RestaurantNumber = RestaurantNumber + 1
        print("liked")
        

        self.displayRestaurants()
    
        
    #else if disliked store in disliked list and display next Restaurant
    def Disliked(self):
        global RestaurantNumber
        print("Restaurant Number ", RestaurantNumber)
        RestaurantNumber = RestaurantNumber + 1 
        print("disliked")
        

        self.displayRestaurants()

    def Finished(self):
        global LikedList
        count = 1
        for i in LikedList:
            
            self.ui.RouletteTextBrowser.append(str(count) + "). " +  i + "\n")
            count += 1
    
    def Spin(self):
        global LikedList
        url_image = BussinessList[LikedList]["image_url"]    
        Restaurantimage = QImage()
        Restaurantimage.loadFromData(requests.get(url_image).content)
        self.ui.RouletteImageLabel.setPixmap(QPixmap(Restaurantimage))
        self.ui.RouletteImageLabel.setScaledContents(True)
        
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())

