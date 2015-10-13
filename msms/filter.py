import pandas as pd

# example input data. This will probably change once we put incorporate this function into the main program
data = '/Users/student/Desktop/pubs/PUBS 2015 MS files/proteinGroups.txt'
df = pd.read_table(data, usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 18, 19, 20, 21, 38, 39, 40, 41, 42, 43, 44, 45, 68, 69, 70, 71, 88, 89, 90, 91, 92, 93, 94, 95, 118, 119, 120, 121, 138, 139, 140, 141, 142, 143, 144, 145, 160, 161, 162, 163, 164, 165, 166, 167, 176, 177, 178, 179, 196, 197, 198, 199, 200, 201, 202, 203, 226, 227, 228, 229, 246, 247, 248, 249, 250, 251, 252, 253, 268, 277, 278, 279, 280, 297, 298, 299, 300, 301, 302, 303, 304, 327, 328, 329, 330, 347, 348, 349, 350, 351, 352, 353, 354, 377, 378, 379, 380, 397, 398, 399, 400, 401, 402, 403, 404, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433], header = 0)


# Filter functions


# remove known and possible contaminants
df = df[df['Potential contaminant'] != '+']

# remove REV and CON
df = df[df['Protein IDs'].str.contains("REV") == False]
df = df[df['Protein IDs'].str.contains("CON") == False]
#print(df['Protein IDs'].str.contains("REV"))

# remove columns with low intensities, or any value that is less than 10^5
# the column name may be different
df = df[df['Intensity Pynd_AlkKO_WCL'] > 100000]
