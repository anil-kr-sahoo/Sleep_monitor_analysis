import numpy as np
def plot_bar_graph(plt=None, data_frame=None, input_series=None):

    if plt is not None and data_frame is not None and input_series is not None:
        bar_width = .2
        filter_referance = data_frame.loc[data_frame['Date'] == input_series]
        time_list = filter_referance['Time']
        sleep_percent_list = filter_referance['Sleep_Pecrcent']

        cal_bar = np.arange(len(time_list))
        plt.bar(time_list, sleep_percent_list, bar_width, color="r", label="Sleeping Percentage")
        plt.xlabel("Time")
        plt.ylabel("Sleeping Quality")
        plt.title("Time Vs Sleeping Quality")
        plt.xticks(time_list)
        plt.legend()
    else:
        pass