class Veiculo{
    private Sring model;
    private Sring color;
    private Sring motor;
}

public Veiculo(String model, String color, String motor ){
    this.model = model;
    this.color = color;
    this.motor = motor;
}

interface  VeiculoBuilder{
    VeiculoBuilder setModelo(String model);
    VeiculoBuilder setModelo(String color);
    VeiculoBuilder setModelo(String motor);
    Veiculo build();
}

class