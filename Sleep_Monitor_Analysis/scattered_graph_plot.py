def plot_scattered_graph(plt=None, data_frame=None, input_series=None):

    if plt is not None and data_frame is not None and input_series is not None:
        filter_referance = data_frame.loc[data_frame['Date'] == input_series]
        x = filter_referance['Time']
        y = filter_referance["Sleep_Pecrcent"]
        plt.xlabel("Time")
        plt.ylabel("Sleep Quality")
        plt.scatter(x, y, color="g")
        plt.plot(x, y, color="r", label="Sleeping Percentage")
        plt.title("Time Vs Sleeping Quality")
        plt.legend()
    else:
        pass