// Struct
struct Personaje {
    nombre: String,
    edad: i64,
    descripcion: String
    }
    // Struct
    struct Carro {
    placa: String,
    color: String,
    tipo: String
    }
    fn main(){
    // Construcción Struct
    let mut p1 = Personaje { nombre:"Fer".to_string(), edad:18,
    descripcion:"No hace nada".to_string() };
    let mut p2 = Personaje { nombre:"Fer".to_string(), edad:18,
    descripcion:"Maneja un carro".to_string()};
    let mut c1 = Carro { placa:"090PLO".to_string(),
    color:"gris".to_string(), tipo:"mecanico".to_string() };
    let mut c2 = Carro { placa:"P0S921".to_string(),
    color:"verde".to_string(), tipo:"automatico".to_string() };
    // Asignación Atributos
    p1.edad = 10; // Cambio aceptado
    p2.edad = 20; // Cambio aceptado
    c1.color = "cafe".to_string(); // Cambio aceptado
    c2.color = "rojo".to_string(); // Cambio aceptado
    // Acceso Atributo
    println!("{}", p1.edad); // Imprime 18
    println!("{}", c1.color); // Imprime "cafe"
    }
    