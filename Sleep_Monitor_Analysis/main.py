import calendar
from time import strptime
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
from bar_graph_plot import plot_bar_graph
from scattered_graph_plot import plot_scattered_graph
from user_input import input_given

plt.style.use("bmh")
data_frame = pd.read_csv("sleep_monitor.csv")
all_series = data_frame['Date']
valid_data_series = list(set(all_series))
print("\nTotal Days of Data We have "+str(len(valid_data_series)))

current_month = datetime.now().month
month_list = list(range(1, current_month+1))

month_list_name = [calendar.month_name[i] for i in month_list]
input_month = input_given(data_list=month_list_name)
if input_month not in month_list_name:
    print("\nPlease enter a valid month")
    quit()
print("Month Given - "+ input_month)


month = datetime.strptime(input_month[:3], "%b").month
first_day = 1
if month == current_month:
    end_day = datetime.now().day
else:
    _, end_day = calendar.monthrange(datetime.now().year, month)
date_list = [str(datetime.now().year)+"-"+"%02d" % month+"-"+"%02d" % i for i in list(range(first_day, end_day+1))]
input_date = input_given(data_list=date_list, date_required=True)

if not input_date:
    print("\n Please enter a valid date")
    quit()
elif input_date not in valid_data_series:
    print("\n Please enter a valid date")
    quit()
else:
    print("Date Given - " + input_date)
    bar_graph = plt.figure(1)
    plot_bar_graph(plt, data_frame, input_date)
    scattered_graph = plt.figure(2)
    plot_scattered_graph(plt, data_frame, input_date)
    plt.show()