def plot_scattered_graph(plt=None, data_frame=None, input_series=None):

    if plt is not None and data_frame is not None and input_series is not None:
        filter_referance = data_frame.loc[data_frame['Date'] == input_series]
        x = filter_referance['Time']
        specific_graph(plt, filter_referance, x, "Sleep_Pecrcent")

    else:
        pass

def specific_graph(plt, filter_referance, x, variable):
    y = filter_referance[variable]
    plt.xlabel("Activity")
    plt.ylabel("Data")
    plt.scatter(x, y, color="g")
    plt.plot(x, y, color="r", label="Sleeping Percentage")
    plt.title("Time Vs Sleeping Quality")
    plt.legend()