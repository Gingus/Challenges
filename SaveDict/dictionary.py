import pickle

def save_dict(name, file_path):
    """Something"""
    with open(file_path, 'wb') as file:
        pickle.dump(name, file)
        
def load_dict(file_path):
    """Something"""
    with open(file_path, 'rb') as file:
        return pickle.load(file)
