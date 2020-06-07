class Puppy:
    n_puppies = 0

    def __new__(cls):
        if cls.n_puppies < 10:
            object.__new__(cls)
            cls.n_puppies += 1
