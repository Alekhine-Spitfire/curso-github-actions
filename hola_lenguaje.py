import os


def main():
    nombre = os.getenv("USERNAME")
    lenguaje = "Python"
    print(f"¡Hola, {nombre} desde GitHub!")
    print(f"Tu lenguaje favorito es: {lenguaje}")


if __name__ == "__main__":
    main()
 
