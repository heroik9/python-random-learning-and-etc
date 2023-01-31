
def sample(funkcija):
    def sample1():
        print("kazkas 1")
        funkcija()
        print("kazkas 2")

    return sample1

@sample
def sample2():
    print("kazkas 3")

sample2()


