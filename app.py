import csv


class Vehiculo:
    def __init__(self, marca, modelo, nro_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.nro_ruedas = nro_ruedas

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.nro_ruedas} ruedas"


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, nro_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"{super().__str__()}, {self.velocidad} Km/h, {self.cilindrada} cc"


class Particular(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, nro_puestos):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.nro_puestos = nro_puestos

    def __str__(self):
        return f"{super().__str__()}, Puestos: {self.nro_puestos}"


class Carga(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, carga):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return f"{super().__str__()}, Carga: {self.carga} Kg"


class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, tipo):
        super().__init__(marca, modelo, nro_ruedas)
        self.tipo = tipo

    def __str__(self):
        return f"{super().__str__()}, Tipo: {self.tipo}"


class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, nro_ruedas, tipo, motor, cuadro, nro_radios):
        super().__init__(marca, modelo, nro_ruedas, tipo)
        self.motor = motor
        self.cuadro = cuadro
        self.nro_radios = nro_radios

    def __str__(self):
        return f"{super().__str__()}, Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.nro_radios}"


def guardar_datos_csv(vehiculos):
    try:
        with open("vehiculos.csv", "w", newline="") as archivo:
            archivo_csv = csv.writer(archivo)
            for vehiculo in vehiculos:
                archivo_csv.writerow([type(vehiculo), vehiculo.__dict__])
        print("Datos guardados correctamente en vehiculos.csv")
    except Exception as e:
        print(f"Error al guardar los datos: {e}")


def leer_datos_csv():
    vehiculos = []
    try:
        with open("vehiculos.csv", "r") as archivo:
            archivo_csv = csv.reader(archivo)
            for vehiculo in archivo_csv:
                print(vehiculo)
        print("Datos leídos correctamente de vehiculos.csv")
    except FileNotFoundError:
        print("El archivo vehiculos.csv no existe.")
    except Exception as e:
        print(f"Error al leer los datos: {e}")


def menu():
    vehiculos = []

    while True:
        print("\nMenú de control de vehículos:")
        print("1. Insertar un vehículo particular")
        print("2. Insertar un vehículo de carga")
        print("3. Insertar una bicicleta")
        print("4. Insertar una motocicleta")
        print("5. Guardar vehículos en archivo CSV")
        print("6. Leer vehículos desde archivo CSV")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            marca = input("Inserte la marca del vehículo: ")
            modelo = input("Inserte el modelo del vehículo: ")
            nro_ruedas = input("Inserte el número de ruedas: ")
            velocidad = input("Inserte la velocidad en km/h: ")
            cilindrada = input("Inserte el cilindraje en cc: ")
            nro_puestos = input("Inserte el número de puestos: ")
            particular = Particular(
                marca, modelo, nro_ruedas, velocidad, cilindrada, nro_puestos
            )
            vehiculos.append(particular)
            print(f"Vehículo particular {particular} agregado correctamente.")

        elif opcion == "2":
            marca = input("Inserte la marca del vehículo de carga: ")
            modelo = input("Inserte el modelo del vehículo: ")
            nro_ruedas = input("Inserte el número de ruedas: ")
            velocidad = input("Inserte la velocidad en km/h: ")
            cilindrada = input("Inserte el cilindraje en cc: ")
            carga = input("Inserte el peso de la carga en kg: ")
            carga_vehiculo = Carga(
                marca, modelo, nro_ruedas, velocidad, cilindrada, carga
            )
            vehiculos.append(carga_vehiculo)
            print(f"Vehículo de carga {carga_vehiculo} agregado correctamente.")

        elif opcion == "3":
            marca = input("Inserte la marca de la bicicleta: ")
            modelo = input("Inserte el modelo de la bicicleta: ")
            nro_ruedas = input("Inserte el número de ruedas: ")
            tipo = input("Inserte el tipo de bicicleta (Urbana/Carrera): ")
            bicicleta = Bicicleta(marca, modelo, nro_ruedas, tipo)
            vehiculos.append(bicicleta)
            print(f"Bicicleta {bicicleta} agregada correctamente.")

        elif opcion == "4":
            marca = input("Inserte la marca de la motocicleta: ")
            modelo = input("Inserte el modelo de la motocicleta: ")
            nro_ruedas = input("Inserte el número de ruedas: ")
            tipo = input("Inserte el tipo de motocicleta (Deportiva/Urbana): ")
            motor = input("Inserte el tipo de motor (2T/4T): ")
            cuadro = input("Inserte el tipo de cuadro: ")
            nro_radios = input("Inserte el número de radios: ")
            motocicleta = Motocicleta(
                marca, modelo, nro_ruedas, tipo, motor, cuadro, nro_radios
            )
            vehiculos.append(motocicleta)
            print(f"Motocicleta {motocicleta} agregada correctamente.")

        elif opcion == "5":
            guardar_datos_csv(vehiculos)

        elif opcion == "6":
            leer_datos_csv()

        elif opcion == "7":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, seleccione nuevamente.")


if __name__ == "__main__":
    menu()
