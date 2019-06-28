import matplotlib.pyplot as plt
import pds_db as pds
import mplcursors

imperial_result = pds.get_all_pokemon_height_weight_graph("imperial")
result = pds.get_all_pokemon_height_weight_graph()
imperial_weights = imperial_result[0]
imperial_heights = imperial_result[1]
weights = result[0]
heights = result[1]
names = result[2]

fig = plt.figure(
)
ax = fig.add_subplot(121)
ax.scatter(weights, heights)
ax.set_title("Pokemon Weight(kg) vs Height(m)")

mplcursors.cursor(ax, hover=True).connect(
    "add", lambda sel: sel.annotation.set_text(
        names[sel.target.index] + " " + str(weights[sel.target.index]) + " kg, " + str(
            heights[sel.target.index]) + " m"))

plt.xlabel("Weight (kg)")
plt.ylabel("Height (m)")

ax = fig.add_subplot(122)
ax.scatter(imperial_weights, imperial_heights)
ax.set_title("Pokemon Weight(lbs) vs Height(ft)")

mplcursors.cursor(ax, hover=True).connect(
    "add", lambda sel: sel.annotation.set_text(
        names[sel.target.index] + " " + str(imperial_weights[sel.target.index]) + " lbs, " + str(
            imperial_heights[sel.target.index]) + " ft"))

plt.xlabel("Weight (lbs)")
plt.ylabel("Height (ft)")
plt.tight_layout()
plt.show()
