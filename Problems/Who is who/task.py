class Angel:
    color = "white"
    feature = "wings"
    home = "Heaven"


class Demon:
    color = "red"
    feature = "horns"
    home = "Hell"


angel = Angel()
print("""{}
{}
{}""".format(angel.color, angel.feature, angel.home))
demon = Demon()
print("""{}
{}
{}""".format(Demon.color, Demon.feature, Demon.home))
