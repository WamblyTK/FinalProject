# imports
import json
import webbrowser
import requests
from PyQt5.QtCore import QTimer, QEventLoop
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QImage, QPixmap
import random
from PIL import Image

#Other files 
from RunScreen11Test import Ui_MainWindow

# Personal API KEY
api_key = 'GHNXaxsTmnroXTDG3O-v_pV3dV-yzraTyR_GbGsttZww8dRASFHsRqkvaQQMRIKgARvQk0AIfkF9m_-8Wfuc3XrUkr-FanBkgBpKJ8z6gKniuz-PdyptiHsids-gYXYx'
headers = {'Authorization': 'Bearer %s' % api_key}

# URL
url = 'https://api.yelp.com/v3/businesses/search'

#Global variables (placeholders)
BussinessList = 0
RestaurantNumber= 0
LikedList = []
LikedImageList = []
LikedWebsiteList = []
WinningRestaurantUrl= 0


#Main Window
class MainWindow:
    def __init__(self):
        #Main Window
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        #Stacked Widgets
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)



        #Menu Button
        self.ui.InstructionButton.clicked.connect(self.showInstructions)
        self.ui.SearchButton.clicked.connect(self.showSearch)
        self.ui.SortButton.clicked.connect(self.showSort)
        self.ui.RouletteButton.clicked.connect(self.showRoulette)

        self.ui.ResetButton.clicked.connect(self.Reset)
        #Search Page   
        self.ui.SubmitButton.clicked.connect(self.SearchStage)
        #Sort Page
        self.ui.DislikeButton.clicked.connect(self.Disliked)
        self.ui.LikeButton.clicked.connect(self.Liked)
        self.ui.FinishSortButton.clicked.connect(self.Finished)
        #Roulette Page
        self.ui.SpinButton.clicked.connect(self.Spin)
        self.ui.WebsiteButton.clicked.connect(self.Display)
        


    def show(self):
        self.main_win.show()

    #Menu Buttons
    #How to use
    def showInstructions(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)
    #Search
    def showSearch(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Search)
    #Sort
    def showSort(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Sort)
    #Roulette
    def showRoulette(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Roulette)
    #Reset (clear all user inputs)
    def Reset(self):

        global BussinessList
        global RestaurantNumber
        global LikedList
        global LikedImageList
        
        #Search
        self.ui.LocLineEdit.clear()
        self.ui.DistLineEdit.clear()
        #Sort
        self.ui.SortText.setText("No restaurants as of now...")
        self.ui.ImageLabel.setText("Image PlaceHolder")
        self.ui.RestaurantNoLabel.setText("No.")
        #Roulette
        self.ui.RouletteTextBrowser.setText("Picking From:")
        self.ui.RouletteImageLabel.setText("Picking From:")
        self.ui.RouletteNameLabel.setText("Picking From:")
        
        #Global Variables
        BussinessList = 0
        RestaurantNumber= 0
        LikedList = []
        LikedImageList = []


        

    #Specific Functions
    def SearchStage(self):
        try:
            
            #Initialise variables
            global BussinessList
            BussinessList = 0

            #Clear any errors
            self.ui.ErrorBoxSearch.clear()

            #Search with parameters Location, Distance and Price Range given.
            print("Searching with parameters: " + self.ui.LocLineEdit.text() + ", " + self.ui.DistLineEdit.text() + ", " + self.ui.PRComboBox.currentText())
            #Location
            UsrLocation = self.ui.LocLineEdit.text()
            #Distance from Location (radius in miles)
            UsrDistance = float(self.ui.DistLineEdit.text())
            #Max distance = 40000 meters
            if UsrDistance >= 24.9:
                UsrDistance = 40000
            else:
                UsrDistance = round(UsrDistance * 1609.34)
            print(UsrDistance, 'meters')

            #Price £ = index 0, ££££ = index 3
            PriceRange = self.ui.PRComboBox.currentIndex()+1
            #Price taken as a comma delimited list --> 1,2,3 is price range £ to £££
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
            BussinessList = businesses


            #amount of restaurants returned
            print("max requests: ", len(businesses))

            #Sort Phase
            self.displayRestaurants()
            #Move to next 'page'
            self.ui.stackedWidget.setCurrentIndex(2)
        except Exception as e:
            print(e, " error type ",  type(e))
            #if Distance has incorrect value, Location has incorrect value or Locaiton not found throw error
            if type(e) == ValueError:
                self.ui.ErrorBoxSearch.setText("Error: please enter a number for the distance!")
            if type(e) == KeyError:
                self.ui.ErrorBoxSearch.setText("Error: please enter a real location!")
            if type(e) == IndexError:
                self.ui.ErrorBoxSearch.setText("Error: No data found for this locaiton")

    
    def displayRestaurants(self):

        #variables
        global RestaurantNumber
        global BussinessList

        #Set Sort page info for restaurants
        #Restaurant Number
        self.ui.RestaurantNoLabel.setText(str( len(BussinessList) - RestaurantNumber))
        if  len(BussinessList) - RestaurantNumber > 0:
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
            ##Url of image
            url_image = BussinessList[RestaurantNumber]["image_url"] 
        
            #if there is a url_image
            if url_image != '':
                Restaurantimage = QImage()
                ##Load QImage with image in url
                Restaurantimage.loadFromData(requests.get(url_image).content)
                self.ui.ImageLabel.setPixmap(QPixmap(Restaurantimage))
                ##Rescale
                self.ui.ImageLabel.setScaledContents(True)

            #else replace with placeholder image
            else:
                url_image = ('https://previews.123rf.com/images/pavelstasevich/pavelstasevich1811/pavelstasevich181101028/112815904-no-image-available-icon-flat-vector-illustration.jpg')
                Restaurantimage = QImage()
                ##Load QImage with image in url
                Restaurantimage.loadFromData(requests.get(url_image).content)
                self.ui.ImageLabel.setPixmap(QPixmap(Restaurantimage))
                ##Rescale
                self.ui.ImageLabel.setScaledContents(True)

    #If liked store in liked list and display next restaurant
    def Liked(self):
        try:
            
            self.ui.ErrorBoxSort.clear()
            #Global variables
            global BussinessList
            global RestaurantNumber 
            global LikedList
            global LikedImageList
            global LikedWebsiteList
            #Local variables
            url_image = BussinessList[RestaurantNumber]["image_url"]


                


            if url_image == '':

                url_image = ('https://previews.123rf.com/images/pavelstasevich/pavelstasevich1811/pavelstasevich181101028/112815904-no-image-available-icon-flat-vector-illustration.jpg')
            if RestaurantNumber < 49:

                #print("Restaurant Number ", RestaurantNumber)
                #Add liked restaurant to Lists and increase RestaurantNumber
                LikedList.append(BussinessList[RestaurantNumber]["name"])
                LikedImageList.append(url_image)
                LikedWebsiteList.append(BussinessList[RestaurantNumber]["url"])

                RestaurantNumber = RestaurantNumber + 1
                #print("liked")
            
                #Display new Restaurant
            
                self.displayRestaurants()
        
            elif RestaurantNumber == 49:
                LikedList.append(BussinessList[RestaurantNumber]["name"])
                LikedImageList.append(url_image)
                
                RestaurantNumber += 1

                self.ui.RestaurantNoLabel.setText("0")
        except Exception as e:
            print (type(e))
            if type(e) == TypeError:
                self.ui.ErrorBoxSort.setText("Can't Like before completing the search stage go back to the Search Button and fill out the form!") 
            else:
                self.ui.ErrorBoxSort.setText('RUN OUT OF SWIPES!')       
            
    
        
    #else if disliked increase restaurant number and display next Restaurant
    def Disliked(self):
        try:
            self.ui.ErrorBoxSort.clear()
            global RestaurantNumber
            global BussinessList
            if RestaurantNumber < 49 and len(BussinessList) - RestaurantNumber > 0:
                print("disliked")
                RestaurantNumber = RestaurantNumber + 1 
                self.displayRestaurants()
            elif len(BussinessList) - RestaurantNumber == 0:
                self.ui.ErrorBoxSort.setText("RUN OUT OF SWIPES!")
            else:
                self.ui.RestaurantNoLabel.setText("0")
        except Exception as e:
            print(e)
            if type(e) == TypeError:
                self.ui.ErrorBoxSort.setText("Can't Dislike before completing the search stage go back to the Search Button and fill out the form!")
            
                

        
        

    #Finished Button
    def Finished(self):
        try:
            self.ui.ErrorBoxSort.clear()
            #variables
            global LikedList
            count = 1
            #For elements in LikedList add it to the display list on roulette screen
            for i in LikedList:
                if count <= 50:
                    self.ui.RouletteTextBrowser.append(str(count) + "). " +  i + "\n")
                    count += 1

            #Roulette placeholders
            self.ui.RouletteNameLabel.setText(LikedList[0])

            url_image = LikedImageList[0]    
            Restaurantimage = QImage()
            Restaurantimage.loadFromData(requests.get(url_image).content)
            self.ui.RouletteImageLabel.setPixmap(QPixmap(Restaurantimage))
            self.ui.RouletteImageLabel.setScaledContents(True)

            self.ui.stackedWidget.setCurrentIndex(3)
        except Exception as e:
            if len(LikedList) < 1:
                print(e)
                self.ui.ErrorBoxSort.setText("You have to like at least 1 restaurant before finishing!")
    #Spin Button
    def Spin(self):

        
        try:
            self.ui.ErrorBoxRoulette.clear()
            #variables
            global LikedList
            global LikedImageList
            global LikedWebsiteList
            global WinningRestaurantUrl
            counter = 0
            NewList = []
            NewImageList = []

            #Pick Random winner and get its index
            WinnerIndex = random.randrange(len(LikedList))
            WinningRestaurantUrl = LikedWebsiteList[WinnerIndex]
            print (WinnerIndex, LikedList[WinnerIndex])

            #Create copy of list bar the winner
            for i in LikedList:

                if counter != WinnerIndex:
                    NewList.append(i)
                    NewImageList.append(LikedImageList[counter])
                counter += 1
            
            #print(LikedList)
            #print(NewList)
            #print(NewImageList)

            #Randomise NewList
            random.shuffle(NewList)
            random.shuffle(NewImageList)
            #Add winner onto the end
            NewList.append(LikedList[WinnerIndex])
            NewImageList.append(LikedImageList[WinnerIndex])
            
            #Flip through list on a timer till you get to the end (winning restaurant)
            counter = 0
            speed = 101 - len(LikedList) * 2
        
            for i in NewList:
                

                self.ui.RouletteNameLabel.setText("WINNER: " + NewList[counter])

                url_image = NewImageList[counter]    
                Restaurantimage = QImage()
                Restaurantimage.loadFromData(requests.get(url_image).content)
                self.ui.RouletteImageLabel.setPixmap(QPixmap(Restaurantimage))
                self.ui.RouletteImageLabel.setScaledContents(True)
                #pause for 2 seconds
                counter += 1

                loop = QEventLoop()
            
                QTimer.singleShot(speed, loop.quit)
            
                loop.exec_()
        except Exception as e:
            print(e)
            self.ui.ErrorBoxRoulette.setText("You can't spin with no restaurants selected!")  

    def Display(self):
        try:
         webbrowser.open(WinningRestaurantUrl)
        except Exception as e:
            print(e)
            self.ui.ErrorBoxRoulette.setText("You can't display the website before a winner is selected!")
            
            
            
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())

