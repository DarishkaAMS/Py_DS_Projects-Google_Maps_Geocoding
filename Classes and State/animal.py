class Animal:
    noise = "Rrrr"

    def make_noise(self):
        print(f'I say {self.noise}')

    def set_noise(self, new_noise):
        self.noise = new_noise