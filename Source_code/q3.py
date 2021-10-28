import matplotlib.pyplot as plt
import math
import q2


if __name__ == "__main__":
    # x axis values
    payload = [16, 32, 51]

    for sf in range(7, 13):
        y = []
        for i in payload:
            y.append(q2.calculate_time_on_air(i, sf, 1, 125))
        plt.scatter(payload, y, label="sf="+str(sf))

    # naming the x axis
    plt.xlabel('payload')
    # naming the y axis
    plt.ylabel('time on air')
    # giving a title to my graph
    # plt.title('Two lines on same graph!')

    # show a legend on the plot
    plt.legend()

    # function to show the plot
    plt.show()
