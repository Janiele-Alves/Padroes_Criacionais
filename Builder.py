class Veiculo:
    def __init__(self, model, color, motor):
        self.model = model
        self.color = color
        self.motor = motor

class VeiculoBuilder:
    def __init__(self):
        self.model = None
        self.color = None
        self.motor = None

    def set_model(self, model):
        self.model = model
        return self

    def set_color(self, color):
        self.color = color
        return self

    def set_motor(self, motor):
        self.motor = motor
        return self

    def build(self):
        return Veiculo(self.model, self.color, self.motor)

class Diretor:
    def __init__(self, builder):
        self.builder = builder

    def construir_veiculo(self, model, color, motor):
        return self.builder.set_model(model) \
                           .set_color(color) \
                           .set_motor(motor) \
                           .build()

builder = VeiculoBuilder()
diretor = Diretor(builder)

print("*****CARRO****")

carro = diretor.construir_veiculo("Luxury car", "Black", "Motor V8")
print("Modelo:",carro.model, "\nCor:",carro.color, "\nMotor:",carro.motor)

print("*****MOTO****")

moto = diretor.construir_veiculo("Sports Motorcycle", "Red", "High Performance Engine")
print("Modelo:", moto.model, "\nCor:", moto.color, "\nMotor:", moto.motor)
