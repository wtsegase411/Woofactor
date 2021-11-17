import matplotlib.pyplot as plt

def two_d_visualize(progressions, progs, title):
    """
    References:
    https://matplotlib.org/3.1.1/gallery/ticks_and_spines/ticklabels_rotation.html
    https://matplotlib.org/stable/api/pyplot_summary.html#matplotlib.pyplot.plotting

    :param progressions: a two-dimensional array with float values that represent
    :param progs: a list of progressions in the data in a string format (e.g.) ['I', 'IV', 'V'])
    :param title: a string represents the title of the plot
    :return:
    """

    ticks = [i for i in range(len(progs))]


    if len(progressions) == 0:
        pass
    else:
        a_figure = plt.figure()
        axis = plt.axes()
        # X-axis ticks & labels on the top instead of on the bottom (default)
        axis.tick_params(axis='x', labelbottom=False, bottom = False, labeltop=True, top=True)
        plt.xticks(ticks, progs, rotation=60)    # labeling x-axis with each progression
        plt.xticks(fontsize=9)
        plt.yticks(ticks, progs)    # labeling y-axis with each progression
        plt.title(str(title))
        plt.colorbar()
        plt.subplots_adjust(top=0.8)    # space above the title
        plt.show()

