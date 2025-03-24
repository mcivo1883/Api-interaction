'''api demonstration'''

#Help page import
import argparse

#3rd party import
import wikipedia





#Additonal line if you prefer user input
# suggestion = input ("What do you want to search for")

#First initial Query
results = wikipedia.search("Raith Rovers UEFA")

#
#results = wikipedia.search(suggestion)


#Spit out history
print(wikipedia.summary(results[0]))


#Default help page
parser=argparse.ArgumentParser(
    description='''Welcome to my api help page  ''',
    epilog="""If you have any questions check out my README file.""")
parser.add_argument('--version', type=int, default=42, help=' Version 6.9')
parser.add_argument('bar', nargs='*', default=[1, 2, 3], help='BAR!')
args=parser.parse_args()






#Now look for the next european away day



#Look at ryanair flights to europe
#from ryanair import Ryanair

#In british pounds
# #api = Ryanair("GBP")


#from datetime import datetime, timedelta
#from ryanair import Ryanair
#from ryanair.types import Flight

#api = Ryanair(currency="GBP")  # Euro currency, so could also be GBP etc. also
#tomorrow = datetime.today().date() + timedelta(days=1)

#flights = api.get_cheapest_flights("EDI", tomorrow, tomorrow + timedelta(days=1))

# Returns a list of Flight namedtuples
#flight: Flight = flights[0]
#print(flight)  # Flight(departureTime=datetime.datetime(2023, 3, 12, 17, 0),
# flightNumber='FR9717', price=31.99, currency='EUR' origin='DUB', originFull='Dublin, Ireland',
# destination='GOA', destinationFull='Genoa, Italy')
#print(flight.price)  # 9.78
