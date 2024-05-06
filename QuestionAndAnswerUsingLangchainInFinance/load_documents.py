import pickle

filename = 'faiss_index.pkl'

with open(filename, 'rb') as file:
    data = pickle.load(file)

c = 0
if isinstance(data, tuple):
    print("Loaded data is a tuple.")
    print(f"Total elements in the tuple: {len(data)}")
    # Optionally, print the type of each element in the tuple
    import faiss

    if isinstance(data[0], faiss.swigfaiss.IndexFlatL2):
        print("Faiss Index is loaded.")
        print(f"Number of vectors indexed: {data[0].ntotal}")
        # Optionally perform a sample query if you have a vector
        # vector_to_query = [0.1, 0.2, 0.3]  # Example vector
        # vector_to_query = np.array(vector_to_query).astype('float32').reshape(1, -1)
        # k = 5  # Number of nearest neighbors to retrieve
        # D, I = data[0].search(vector_to_query, k)
        # print("Distances: ", D.flatten())
        # print("Indices: ", I.flatten())

else:
    print("Loaded data is not a tuple.")

if isinstance(data[1], list):
    print("First list loaded with length:", len(data[1]))
    print("Sample of first 10 items:", data[1][:10])  # Adjust number of items to print as needed

if isinstance(data[2], list):
    print("Second list loaded with length:", len(data[2]))
    print("Sample of first 10 items:", data[2][:10])


import random

random_index = []

for i in range(40):
    num = random.randint(1, len(data[1]) - 1)
    random_index.append(num)

print(random_index)

for j in range(len(random_index)):
    print(data[2][j])
    print()

