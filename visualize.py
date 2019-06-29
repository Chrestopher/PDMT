import matplotlib.pyplot as plt
import pds_db as pds
import mplcursors


def plot_weight(unit="metric"):
    result = pds.get_all_pokemon_height_weight_graph(unit)
    weights = result[0]
    heights = result[1]
    names = result[2]
    weight_unit = result[3][0]
    height_unit = result[3][1]
    weight_label = "Weight(" + weight_unit + ")"
    height_label = "Height(" + height_unit + ")"

    fig, ax = plt.subplots()
    ax.scatter(weights, heights)
    ax.set_title("Pokemon " + weight_label + " vs " + height_label)

    mplcursors.cursor(ax, hover=True).connect(
        "add", lambda sel: sel.annotation.set_text(
            names[sel.target.index] + " " + str(weights[sel.target.index]) + " " + weight_unit + ", " + str(
                heights[sel.target.index]) + " " + height_unit))

    plt.xlabel(weight_label)
    plt.ylabel(height_label)

    plt.show()


if __name__ == '__main__':
    plot_weight()
