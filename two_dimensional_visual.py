import matplotlib.pyplot as plt

"""
https://matplotlib.org/3.1.1/gallery/ticks_and_spines/ticklabels_rotation.html
https://matplotlib.org/stable/api/pyplot_summary.html#matplotlib.pyplot.plotting
"""

def two_d_visualize(progressions, progs, title):
    """
    :param progressions: a list of progressions
    :param progs:
    :param title:
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
        plt.xticks(ticks, progs, rotation=45)    # labeling x-axis with each progression
        plt.yticks(ticks, progs)    # labeling y-axis with each progression
        plt.imshow(progressions)
        plt.title(str(title))
        plt.colorbar()
        plt.show()

