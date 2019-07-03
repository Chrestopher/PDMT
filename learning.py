from sklearn import tree
from sklearn.model_selection import train_test_split
import pds_db as pds

# features = weight, height, base total stats
# labels = legendary

weight = pds.get_all_pokemon_column("weight_kg")
height = pds.get_all_pokemon_column("height_m")
base_total = pds.get_all_pokemon_column("base_total")
names = pds.get_all_pokemon_column("pokedex_number")

features = []
for x in range(0, len(weight)):
    features.append([weight[x], height[x], base_total[x]])

labels = pds.get_all_pokemon_column("is_legendary")

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.33,
                                                                            random_state=42)

clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)
predictions = clf.predict(features_test)

print("Model made ", len(predictions), " predictions.")
for input, prediction, label in zip(features_test, predictions, labels_test):
    if prediction != label:
        name = pds.get_one_pokemon_by_labels(input[0], input[1], input[2])
        input.append(name)
        if prediction == 1.0:
            print(input, 'has been classified as a LEGENDARY and should NOT BE')
        else:
            print(input, 'has been classified as NOT A LEGENDARY and should BE')

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(labels_test, predictions)
print("Correct Predictions: ", int(round(accuracy * len(predictions))))
print("Incorrect Predictions: ", int(len(predictions) - round(accuracy * len(predictions))))
print('Machine Learning Model Accuracy: ', round(accuracy * 100, 2), '%')

from graphviz import Source

graph = Source(tree.export_graphviz(clf, out_file=None, feature_names=["Weight", "Height", "BTS"],
                                    class_names=["Not Legendary", "Legendary"]))
graph.format = 'png'
graph.render('dtree_render')
