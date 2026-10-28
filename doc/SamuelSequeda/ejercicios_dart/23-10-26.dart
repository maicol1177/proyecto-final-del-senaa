Class Personaje{
    Sring? nombre;
    int? vida;
    int? ataque;
    int? defensa;
    int? velocidad;
    int? nivel;

    Personaje({
        this.nombre,
        this.vida,
        this.ataque,
        this.defensa,
        this.velocidad,
        this.nivel
    });
}

void Mostrar.estado(Personaje personaje){
    print('Nombre: ${personaje.nombre}');
    print('Vida: ${personaje.vida}');
    print('Ataque: ${personaje.ataque}');
    print('Defensa: ${personaje.defensa}');
    print('Velocidad: ${personaje.velocidad}');
    print('Nivel: ${personaje.nivel}');
}
void main(){
    Personaje personaje1 = Personaje(
        nombre: 'Guerrero',
        vida: 100,
        ataque: 20,
        defensa: 15,
        velocidad: 10,
        nivel: 1
    );

    Personaje personaje2 = Personaje(
        nombre: 'Mago',
        vida: 80,
        ataque: 25,
        defensa: 10,
        velocidad: 12,
        nivel: 1
    );

    );

    print('=== Estado del Personaje 1 ===');
    Mostrar.estado(personaje1);

    print('\n=== Estado del Personaje 2 ===');
    Mostrar.estado(personaje2);
}
void atacar (Personaje objetivo){
    if (objetivo.vida <= 0) {
        print('${objetivo.nombre} ya está derrotado.');
        return;
    }
    if (objetivo.vida <= 0) {
        print('${objetivo.nombre} Ya no puede atacar.');
    }
int dano = ataque - objetivo.defensa;
    if (dano < 1) {
        dano = 1;
    objetivo.vida -= dano;
    }
    if objetivo.vida < 0 {
        objetivo.vida = 0;
    }
    print('${objetivo.nombre} recibió $dano de daño. Vida restante: ${objetivo.vida}');
    if (objetivo.vida <= 0) {
        print('${objetivo.nombre} ha sido derrotado.');
    }
} 
void curar(Personaje objetivo){
    if (objetivo.vida <= 0) {
        print('${objetivo.nombre} ya está derrotado y no puede ser curado.');
        return;
    }
    int curacion = 20;
    objetivo.vida += curacion;
    print('${objetivo.nombre} ha sido curado en $curacion puntos de vida. Vida actual: ${objetivo.vida}');
}
personaje1.mostrar.estado();
personaje2.mostrar.estado();

personaje1.atacar(personaje2);
personaje2.mostrar.estado();

personaje2.atacar(personaje1);
personaje1.mostrar.estado();

personaje2.curar(15);
personaje2.mostrar.estado();
}
