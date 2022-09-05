class Remote:
    pass

class Player:
    def moveright(self):
    #     pass

    # def moveleft(self):
    #     pass

    # def movetop(self):
    #     pass

player1 = Player()
remote1 = Remote()
if(remote1.isleftpressed()):
    player1.moveright()

 