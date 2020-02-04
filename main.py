from utils import load_nestle_data

X_TRAIN_DIRECTORY = "data/X_train.csv"
Y_TRAIN_DIRECTORY = "data/Y_train.csv"
X_train = load_nestle_data(X_TRAIN_DIRECTORY)

print(X_train.head())

print(X_train.info())

print(X_train.describe())

Y_train = load_nestle_data(Y_TRAIN_DIRECTORY)


print(Y_train.head())

print(Y_train.info())

print(Y_train.describe())

#Identify Y missing values
Y_missing = (Y_train["y"].isna())
Y_missing_indices = Y_missing[Y_missing].index

Y_train = Y_train.drop(Y_missing_indices)
X_train = X_train.drop(Y_missing_indices)