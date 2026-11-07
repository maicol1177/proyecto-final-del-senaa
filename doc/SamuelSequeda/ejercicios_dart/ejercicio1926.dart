void main() {
Car car = new Car();
car.placa = "ABC123";
car.modelo = 2024;
car.auto = true;

print("Placa: ${car.placa} Modelo: ${car.modelo} Auto: ${car.auto}");

Car car2 = new Car();
car2.placa = "ABC1234";
car2.modelo = 2026;
car2.auto = true;

print("Placa: ${car2.placa} Modelo: ${car2.modelo} Auto: ${car2.auto}");

Car car3 = new Car();
car3.placa = "ABC12345";
car3.modelo = 2027;
car3.auto = true;

print("Placa: ${car3.placa} Modelo: ${car3.modelo} Auto: ${car3.auto}");

Car car4 = new Car();
car4.placa = "ABC123456";
car4.modelo = 2028;
car4.auto = true;

print("Placa: ${car4.placa} Modelo: ${car4.modelo} Auto: ${car4.auto}");

Car car5 = new Car();
car5.placa = "ABC1234567";
car5.modelo = 2029;
car5.auto = true;

print("Placa: ${car5.placa} Modelo: ${car5.modelo} Auto: ${car5.auto}");
}

class Car {
  String? placa;
  int? modelo;
  bool? auto;
}

