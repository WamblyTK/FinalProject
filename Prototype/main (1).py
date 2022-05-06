# imports
import requests
import json

# Personal API KEY
api_key = 'GHNXaxsTmnroXTDG3O-v_pV3dV-yzraTyR_GbGsttZww8dRASFHsRqkvaQQMRIKgARvQk0AIfkF9m_-8Wfuc3XrUkr-FanBkgBpKJ8z6gKniuz-PdyptiHsids-gYXYx'
headers = {'Authorization': 'Bearer %s' % api_key}
# URL
url = 'https://api.yelp.com/v3/businesses/search'

# Main Loop
print("\n------------ Welcome to Restuarant Decider ------------\n")


def main():
    # Location of user
    Usr_Location = input("\nPlease enter your location to get started: ")

    # Distance from location (radius)
    Usr_Distance = float(input("\nHow far would you like us to check (in miles, max = 25): "))
    if Usr_Distance > 25.0:
        Usr_Distance = float(25.0)

    # change miles to meters (as thats what the API takes in)
    Usr_Distance = round(Usr_Distance * 1609.34)
    print(Usr_Distance , "converted to meters")

    # Price
    Price_Range = int(input("""\nPrice Range\n1). £ (inexpensive) \n2). ££ (moderate) \n3). £££ (pricey) \n4). ££££ (Ultra High-End)

                            \nPlease select a number for your price range (up to choice): """))

    # Price can be a comma delimited list e.g. 1,2,3 = between £ and £££
    Price_levels = []
    for i in range(Price_Range):
        Price_levels.append(str(i + 1))
    print(Price_levels, "price ranges")
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
        print("Distance:", business["distance"], "m")
        print("Address:", " ".join(business["location"]["display_address"]))
        print("Phone:", business["phone"])
        print("\n")

    print("only " + str(len(businesses)) + " displayed")


main()

# Links
# https://python.gotrained.com/yelp-fusion-api-tutorial/


