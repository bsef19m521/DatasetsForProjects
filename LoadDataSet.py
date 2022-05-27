import seaborn as sns 
print(sns.get_dataset_names())
# list of all the dataset names
# ['anagrams', 'anscombe', 'attention', 'brain_networks', 'car_crashes', 'diamonds', 'dots', 'exercise', 
#  'flights', 'fmri', 'gammas', 'geyser', 'iris', 'mpg', 'penguins', 'planets', 'taxis', 'tips', 'titanic']
# to load a dataset in current working directory , we will use following load_dataset() function which takes name of dataset
datasetName = input("Enter name of dataset to load : ")
data = sns.load_dataset(datasetName)
# convert dataset to csv format and load in current working directory
data.to_csv("titanic.csv")