import matplotlib.pyplot as plt
import pds_db as pds
import mplcursors

weights = pds.get_all_pokemon_height_weight_graph()[0]
heights = pds.get_all_pokemon_height_weight_graph()[1]
names = pds.get_all_pokemon_height_weight_graph()[2]

fig, ax = plt.subplots()
ax.scatter(weights, heights)
ax.set_title("Pokemon Weight(kg) vs Height(m)")

mplcursors.cursor(ax, hover=True).connect(
    "add", lambda sel: sel.annotation.set_text(
        names[sel.target.index] + " " + str(weights[sel.target.index]) + " kg, " + str(
            heights[sel.target.index]) + " m"))

plt.xlabel("Weight (kg)")
plt.ylabel("Height (m)")
plt.show()
