class motocicelta:
    estado = "nueva"
    motor = False
    combustible_litros = 10
    numero_ruedas = 2
    cant_repostar = None

    def __init__(self, color, matricula, marca,modelo, fecha_fabricacion, velocidad_punta,peso,cap_combustible):
        self.color = color
        self.matricula = matricula
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.marca = marca
        self.velocidad_punta = velocidad_punta
        self.peso = peso 
        self.combustible_litros = 10
        self.numero_ruedas = 2
        self.cap_combustible = cap_combustible


    def arranque(self):
        if self.motor == False:
            print("El motor ha arrancado")
        else:
            print("El motor ya estaba en marcha ¿no escuchas como ruge?")

    def detener(self):
        if self.motor :
            print("El motor se ha detenido")
        else:
            print("El motor ya estaba detenido, giras la llave y no hace nada")

    def consultaprecio(self):
        print(f"El precio de la motocicleta {self.marca}-{self.modelo} es de :${self.precio}")
    
    def cantlitros(self):
        self.cant_repostar = self.cap_combustible - self.combustible_litros
        print(f"El estanque tiene : {self.combustible_litros}L y la capaciadad es : {self.cap_combustible}\nfaltan : {self.cant_repostar}L para llenar el estanque")

    def repostar(self):
        verif = True
        while verif :
            
            repos = int(input("ingrese los litros a repostar\n"))
            if 0 < repos <= self.cant_repostar: 
                self.combustible_litros += repos
                print(f"has cargado combustible el estanque tiene: {self.combustible_litros}L")  
                verif = False
            else:
                print("catidad incorrercta , no puedes pasarte de la capacidada max de tu motocicleta")  
        

motocicelta_1 = motocicelta("rojo","bkh12","bmw","p201",2001,"180km/h","70kg",50)
motocicelta_2 = motocicelta(
    color ="verde",
    matricula ="jlk23",
    fecha_fabricacion =2003,
    modelo ="G5",
    velocidad_punta="190km/h",
    peso="82kg",
    marca="yamaha",
    cap_combustible=50,
    )
motocicelta_1.combustible_litros = 0

motocicelta_1.precio = 1_700_000

motocicelta_1.detener()

motocicelta_2.cantlitros()

motocicelta_2.repostar()

print(f"tienes : {motocicelta_2.combustible_litros}L de combustible")






