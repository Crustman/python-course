class Girls:
    def __init__(self, face, body):
        self.face = face
        self.body = body
        

    def moves(self):
        print("Great dance moves....")
    def get_make_and_model(self):
        print(f"She has a {self.face} and {self.body} body!.")

my_car = Girls("hot face", "curvy")
my_car.get_make_and_model()

my_car.moves()





        

