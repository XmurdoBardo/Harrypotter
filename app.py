from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Lista de 100 preguntas sobre Harry Potter
preguntas = [
    {
        "pregunta": "¿Cuál es el nombre del director de Hogwarts durante los primeros libros?",
        "respuestas": ["Severus Snape", "Albus Dumbledore", "Minerva McGonagall", "Rubeus Hagrid"],
        "respuesta_correcta": 1
    },
    {
        "pregunta": "¿Quién es el mejor amigo de Harry Potter?",
        "respuestas": ["Ron Weasley", "Neville Longbottom", "Draco Malfoy", "Hermione Granger"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Qué objeto es conocido como la varita del destino?",
        "respuestas": ["Varita de Saúco", "Varita de Olivo", "Varita de Sauce", "Varita de Abeto"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Qué animal es el símbolo de la casa Gryffindor?",
        "respuestas": ["Águila", "León", "Serpiente", "Tejón"],
        "respuesta_correcta": 1
    },
    {
        "pregunta": "¿Cuál es el hechizo para desarmar a un oponente?",
        "respuestas": ["Expelliarmus", "Stupefy", "Avada Kedavra", "Lumos"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Qué objeto mágico permite a Harry ver a través de la pared?",
        "respuestas": ["Espejo de Oesed", "La capa de invisibilidad", "La piedra de la resurrección", "El giratiempo"],
        "respuesta_correcta": 1
    },
    {
        "pregunta": "¿Qué tipo de criatura es Buckbeak?",
        "respuestas": ["Hipogrifo", "Dragón", "Unicornio", "Troll"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Quién es el autor de 'Los cuentos de Beedle el Bardo'?",
        "respuestas": ["J.K. Rowling", "Albus Dumbledore", "Newt Scamander", "Severus Snape"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Cuál es la posición de Harry en el equipo de Quidditch?",
        "respuestas": ["Buscador", "Golpeador", "Guardia", "Cazador"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Qué hechizo se utiliza para paralizar a alguien?",
        "respuestas": ["Stupefy", "Petrificus Totalus", "Expelliarmus", "Avada Kedavra"],
        "respuesta_correcta": 1
    },
    {
        "pregunta": "¿Quién es el fundador de la casa Slytherin?",
        "respuestas": ["Godric Gryffindor", "Salazar Slytherin", "Rowena Ravenclaw", "Helga Hufflepuff"],
        "respuesta_correcta": 1
    },
    {
        "pregunta": "¿Qué criatura mágica puede transformarse en el peor miedo de una persona?",
        "respuestas": ["Boggart", "Dementor", "Fantasma", "Espectro"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Cuál es el nombre del guardián de la prisión de Azkaban?",
        "respuestas": ["Dementores", "Grindelwald", "Bellatrix Lestrange", "Lucius Malfoy"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Qué hechizo se utiliza para crear luz?",
        "respuestas": ["Lumos", "Nox", "Incendio", "Aguamenti"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Quién es el hermano mayor de Ron Weasley?",
        "respuestas": ["Bill Weasley", "Charlie Weasley", "Percy Weasley", "George Weasley"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Cómo se llama la profesora de Transfiguración?",
        "respuestas": ["Minerva McGonagall", "Pomona Sprout", "Filius Flitwick", "Sybill Trelawney"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Qué poción permite cambiar de apariencia?",
        "respuestas": ["Poción Multijugos", "Poción de la Verdad", "Poción de Amor", "Poción de la Fuerza"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Cuál es la forma del Patronus de Harry?",
        "respuestas": ["Ciervo", "Lobo", "Perro", "Gato"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Qué criatura es Dobby?",
        "respuestas": ["Elfo doméstico", "Hada", "Duende", "Fantasma"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Cuál es el hechizo para matar?",
        "respuestas": ["Avada Kedavra", "Expelliarmus", "Crucio", "Imperio"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Cómo se llama el hermano de Harry Potter?",
        "respuestas": ["James", "Albus", "Sirius", "No tiene hermanos"],
        "respuesta_correcta": 3
    },
    {
        "pregunta": "¿Qué objeto puede revivir a los muertos?",
        "respuestas": ["La varita de saúco", "La piedra de la resurrección", "El giratiempo", "La capa de invisibilidad"],
        "respuesta_correcta": 1
    },
    {
        "pregunta": "¿Qué casa fue fundada por Godric Gryffindor?",
        "respuestas": ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Quién es el profesor de Defensa Contra las Artes Oscuras en el primer libro?",
        "respuestas": ["Quirinus Quirrell", "Severus Snape", "Remus Lupin", "Gilderoy Lockhart"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Qué planta se utiliza para curar a las personas petrificadas?",
        "respuestas": ["Mandrágora", "Cebolla", "Ajo", "Hierba de San Juan"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Cómo se llama la casa de Hermione Granger?",
        "respuestas": ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Cuál es el nombre del hermano gemelo de Ron?",
        "respuestas": ["Fred", "George", "Bill", "Charlie"],
        "respuesta_correcta": 1
    },
    {
        "pregunta": "¿Qué nombre recibe el torneo en el que participan los estudiantes de varias escuelas?",
        "respuestas": ["Torneo de los Tres Magos", "Torneo de Hogwarts", "Torneo de Quidditch", "Torneo de las Casas"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Qué objeto se usa para controlar el tiempo?",
        "respuestas": ["El giratiempo", "La piedra de la resurrección", "La varita de saúco", "La capa de invisibilidad"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Cómo se llama el espíritu que protege la casa de Gryffindor?",
        "respuestas": ["El sombrero seleccionador", "El guardián de la casa", "El fantasma de Gryffindor", "La Dama Gris"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Qué animal tiene como mascota Ron Weasley?",
        "respuestas": ["Rata", "León", "Perro", "Gato"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Cómo se llama el hechizo que hace flotar objetos?",
        "respuestas": ["Wingardium Leviosa", "Lumos", "Aguamenti", "Accio"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Quién fue el primer ministro de magia mencionado en los libros?",
        "respuestas": ["Cornelius Fudge", "Rufus Scrimgeour", "Kingsley Shacklebolt", "Dolores Umbridge"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Qué tipo de criatura es un Thestral?",
        "respuestas": ["Caballo alado", "Dragón", "Unicornio", "Caballo de la muerte"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Cuál es la forma del Patronus de Hermione?",
        "respuestas": ["Nutria", "Ciervo", "Perro", "Gato"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Qué nombre recibe la varita de Harry Potter?",
        "respuestas": ["Varita de saúco", "Varita de olivo", "Varita de sauce", "Varita de abeto"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Cuál es el nombre del duelo entre Harry y Voldemort en el cuarto libro?",
        "respuestas": ["El duelo del cementerio", "El duelo de Hogwarts", "El duelo en el Bosque Prohibido", "El duelo en el Ministerio"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Quién es el jefe de la casa de Slytherin?",
        "respuestas": ["Severus Snape", "Horace Slughorn", "Dolores Umbridge", "Lucius Malfoy"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Cómo se llama la madre de Harry Potter?",
        "respuestas": ["Lily Potter", "Molly Weasley", "Petunia Dursley", "Narcissa Malfoy"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Qué criatura puede ver el futuro?",
        "respuestas": ["Espectro", "Dementor", "Fénix", "Vidente"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Quién es el amigo de Harry que se convierte en un lobo?",
        "respuestas": ["Ron", "Hermione", "Lupin", "Neville"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Cuál es la habitación más peligrosa en Hogwarts?",
        "respuestas": ["La Cámara de los Secretos", "La sala de los menesteres", "El Bosque Prohibido", "La sala de los trofeos"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Qué tipo de planta es la Mandrágora?",
        "respuestas": ["Planta mágica", "Planta carnívora", "Planta medicinal", "Planta venenosa"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Qué forma tiene el sombrero seleccionador?",
        "respuestas": ["Sombrero", "Capa", "Capa de invisibilidad", "Sombrero de copa"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Qué hechizo se usa para abrir puertas?",
        "respuestas": ["Alohomora", "Accio", "Expelliarmus", "Lumos"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Cómo se llama el esposo de Ginny Weasley?",
        "respuestas": ["Harry Potter", "Ron Weasley", "Neville Longbottom", "Draco Malfoy"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Cuál es el nombre del hijo de Harry y Ginny?",
        "respuestas": ["James Sirius Potter", "Albus Severus Potter", "Lily Luna Potter", "Scorpius Malfoy"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Qué objeto se usa para controlar el tiempo?",
        "respuestas": ["El giratiempo", "La piedra de la resurrección", "La varita de saúco", "La capa de invisibilidad"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Quién se convierte en el nuevo director de Hogwarts después de la batalla?",
        "respuestas": ["Minerva McGonagall", "Severus Snape", "Filius Flitwick", "Albus Dumbledore"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Cómo se llama la tienda de varitas en Diagon Alley?",
        "respuestas": ["Ollivanders", "Gringotts", "Weasleys' Wizard Wheezes", "Flourish and Blotts"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Qué deporte practican los magos en el aire?",
        "respuestas": ["Quidditch", "Bolos", "Fútbol", "Cricket"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Cuál es la criatura que protege el banco Gringotts?",
        "respuestas": ["Duende", "Dragón", "Troll", "Basilisco"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Cuál es el hechizo que se usa para curar heridas?",
        "respuestas": ["Episkey", "Fidelius", "Petrificus Totalus", "Expelliarmus"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Qué planta se usa para hacer pociones de amor?",
        "respuestas": ["Rosa", "Orquídea", "Mandrágora", "Valeriana"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Cuál es el apellido de la familia de Harry?",
        "respuestas": ["Potter", "Dursley", "Weasley", "Granger"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Qué hechizo se usa para lanzar un rayo de luz?",
        "respuestas": ["Lumos", "Incendio", "Nox", "Aguamenti"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Qué personaje es conocido por su amor por los dragones?",
        "respuestas": ["Charlie Weasley", "Hagrid", "Luna Lovegood", "Neville Longbottom"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Quién es el creador de la varita de saúco?",
        "respuestas": ["Gellert Grindelwald", "Albus Dumbledore", "Salazar Slytherin", "Voldemort"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Qué hace el giratiempo?",
        "respuestas": ["Controla el tiempo", "Vuelve al pasado", "Crea ilusiones", "Viaja al futuro"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Cómo se llama la hermana de Ron?",
        "respuestas": ["Ginny", "Molly", "Fleur", "Hermione"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Quién tiene una relación con Harry durante la serie?",
        "respuestas": ["Hermione", "Ginny", "Cho Chang", "Luna"],
        "respuesta_correcta": 1
    },
    {
        "pregunta": "¿Qué se necesita para entrar en la Cámara de los Secretos?",
        "respuestas": ["Sangre de basilisco", "Conocerse a uno mismo", "Saber hablar parsel", "Hechizo especial"],
        "respuesta_correcta": 2
    },
    {
        "pregunta": "¿Qué poción se usa para curar el veneno?",
        "respuestas": ["Poción Antídoto", "Poción de Sangre", "Poción de Poder", "Poción de Amor"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Cómo se llama el fantasma de la casa de Slytherin?",
        "respuestas": ["El Barón Sanguinario", "La Dama Gris", "Nick Casi Decapitado", "El fantasma de Gryffindor"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Cuál es el hechizo que provoca la muerte?",
        "respuestas": ["Avada Kedavra", "Crucio", "Imperio", "Expelliarmus"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Qué hechizo se utiliza para hacer levitar objetos?",
        "respuestas": ["Wingardium Leviosa", "Levioso", "Accio", "Aguamenti"],
        "respuesta_correcta": 0
    },
    {
        "pregunta": "¿Quién es el autor de 'Los cuentos de Beedle el Bardo'?",
        "respuestas": ["Albus Dumbledore", "J.K. Rowling", "Severus Snape", "Gellert Grindelwald"],
        "respuesta_correcta": 1
    },
    # Agrega tantas preguntas como desees
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        puntaje = 0
        for i in range(len(preguntas)):
            respuesta_usuario = request.form.get(f'respuesta{i}')
            if respuesta_usuario is not None and int(respuesta_usuario) == preguntas[i]["respuesta_correcta"]:
                puntaje += 1
        return redirect(f'/resultado?puntaje={puntaje}')

    return render_template('index.html', preguntas=preguntas)


@app.route('/resultado')
def resultado():
    puntaje = request.args.get('puntaje', type=int)
    return render_template('resultado.html', puntaje=puntaje, total=len(preguntas))

@app.route('/podio')
def podio():
    # Aquí puedes manejar un sistema de puntuación para mostrar el podio
    return render_template('podio.html')

if __name__ == "__main__":
    app.run(debug=True)
