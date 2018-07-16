import pandas as pd
import datetime
data_store = pd.read_csv("sales_train_v2.csv", delimiter=",")
day = [datetime.datetime.strptime(x, '%d.%m.%Y').strftime('%d') for counter, x in enumerate(date)]
month = [datetime.datetime.strptime(x, '%d.%m.%Y').strftime('%m') for counter, x in enumerate(date)]
data_store["month"] = month
data_store["day"] = day
data_store.head(3)
