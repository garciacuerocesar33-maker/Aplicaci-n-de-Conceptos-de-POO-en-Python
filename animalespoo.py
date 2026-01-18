
# Clase base: Animal
# Esta es la clase principal de la que heredarán otras. Tiene atributos básicos y métodos.
class Animal:
    # Constructor: aquí inicializo los atributos de cada animal.
    # Uso encapsulación con __edad para que no se pueda cambiar fácilmente desde fuera.
    def __init__(self, nombre, especie):
        self.nombre = nombre  # Atributo público: el nombre del animal
        self.especie = especie  # Atributo público: la especie
        self.__edad = 0  # Atributo privado: la edad, protegido con __ para encapsulación

    # Método para obtener la edad (getter), porque es privado y no se puede acceder directamente.
    def obtener_edad(self):
        return self.__edad

    # Método para cambiar la edad (setter), con validación simple.
    def cambiar_edad(self, nueva_edad):
        if nueva_edad >= 0:
            self.__edad = nueva_edad
        else:
            print("La edad no puede ser negativa.")

    # Método básico: hacer sonido. Este se va a sobrescribir en clases derivadas (polimorfismo).
    def hacer_sonido(self):
        print(f"{self.nombre} hace un sonido genérico.")

    # Método con argumentos variables: alimentar. Usa *args para polimorfismo, aceptando diferentes comidas.
    def alimentar(self, *comidas):
        print(f"Alimentando a {self.nombre} con: {', '.join(comidas)}")


# Clase derivada: Perro
# Esta hereda de Animal, así que tiene todo lo de Animal más cosas propias.
class Perro(Animal):
    # Constructor: llamo al de la clase base con super() y añado atributos propios.
    def __init__(self, nombre, raza):
        super().__init__(nombre, "Perro")  # Herencia: uso super() para inicializar la base
        self.raza = raza  # Atributo propio: la raza del perro

    # Sobrescribo el método hacer_sonido (polimorfismo): ahora hace ladrido en lugar de sonido genérico.
    def hacer_sonido(self):
        print(f"{self.nombre} ladra: ¡Guau guau!")

    # Método propio: jugar, solo para perros.
    def jugar(self):
        print(f"{self.nombre} está jugando con una pelota.")


# Ahora, en la parte principal del programa, creo instancias y las uso para demostrar todo.
if __name__ == "__main__":
    # Creo un animal genérico
    animal_generico = Animal("Rex", "Mamífero")
    print("--- Animal Genérico ---")
    animal_generico.hacer_sonido()  # Muestra sonido genérico
    animal_generico.cambiar_edad(5)  # Cambio la edad usando el setter
    print(f"La edad de {animal_generico.nombre} es {animal_generico.obtener_edad()} años.")  # Uso getter
    animal_generico.alimentar("carne", "agua")  # Polimorfismo con múltiples argumentos

    print("\n--- Perro (heredado) ---")
    # Creo un perro, que hereda de Animal
    mi_perro = Perro("Buddy", "Labrador")
    mi_perro.hacer_sonido()  # Polimorfismo: ahora ladra
    mi_perro.cambiar_edad(3)  # Hereda el método de cambiar edad
    print(f"La edad de {mi_perro.nombre} es {mi_perro.obtener_edad()} años.")
    mi_perro.alimentar("croquetas", "hueso", "fruta")  # Polimorfismo: acepta más comidas
    mi_perro.jugar()  # Método propio del perro