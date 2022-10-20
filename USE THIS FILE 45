from datetime import datetime
from datetime import timedelta
print('This is the Bracket Return Tool')
ord_num = input('Paste customers order number here: ')
given_date = input("Paste date order was placed from ticket:")
part_full = input("Type 'Full' or 'Part' for return order: ")

# Create datetime object from date string
date_format = '%m/%d/%Y'
dtObj = datetime.strptime(given_date, date_format)
# Add 45 days to a given datetime object
n = 45
future_date = dtObj + timedelta(days=n)
# print('Future Date: ', future_date)
# print('Future Date: ', future_date.date())
future_date_str = future_date.strftime(date_format)
#print('EMAIL: Once the label is printed you have till:', future_date_str)

from datetime import date

today = date.today()
print("Today's date:", today)
print('Date Order Was Placed:', given_date)
 
print('TICKET: Return by DATE ' , future_date_str + ' Emailed Customer. Return Label plus date for return sent to customer. Added price on Return_Shipment Item.' ,part_full,'Order :PC ')
print('E-MAIL COPY: This email confirms your request to return the brackets from order number' ,ord_num,': A shipping label will be sent via a separate email. The ability for you to print the label expires quickly, you only have 24 hours.  You would have to print the label in the next 24 hours.  Once the label is printed you have till' ,future_date_str, 'to ship them back to receive a full refund of the cost of the brackets.  You can drop off your brackets at your local FedEx store.')
