import pandas as pd

initial_date = "09/26/2022"
req_date = pd.to_datetime(initial_date) + pd.DateOffset(days=45)
print(req_date)
