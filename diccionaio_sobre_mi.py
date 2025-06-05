#Diccionario
yo = {

"pnombre" : "Diego",
"appaterno" : "Alarcon",

"fecha_naciomiento" : {
    "dia" : 20,
    "mes" : 2,
    "anio" : 2003
},

"signo" : "♓",
"genero" : "Masculino",
"altura" : 1.67,
"nacionalidad" : "Chile",
"colorfav" : "Azul",
"favgame" : "HuntShowdown",
"favmov" : "FightClub",
"ocupacion" : "Estudiante",
"favanim" : "Dororo",
"favser" : "BCS",

"mascotas" : {
    "nombre1" : "Cochino",
    "raza1" : "Huron",
    "nombre2" : "Arena",
    "raza2" : "Gato",
    "nombre3" : "Blu",
    "raza3" : "Perro"
},



}

#Llamar ficha
print(f"""
==========================================================      
                    {yo['pnombre']} {yo["appaterno"]} {yo["signo"]}
==========================================================
Fecha de nacimiento: {yo['fecha_naciomiento']["dia"]}-{yo['fecha_naciomiento']["mes"]}-{yo['fecha_naciomiento']["anio"]}         Nacionalidad: {yo['nacionalidad']}
==========================================================
Genero: {yo['genero']}                             Altura: {yo["altura"]}
==========================================================
Color favorito: {yo['colorfav']}          Juego favorito: {yo['favgame']}
Pelicula fav: {yo['favmov']}                  Anime fav: {yo['favanim']}
Serie fav: {yo['favser']}
==========================================================
                        Mascotas:

Nombre: {yo['mascotas']["nombre1"]}         Nombre: {yo['mascotas']["nombre2"]}          Nombre: {yo['mascotas']["nombre3"]}
Raza:   {yo['mascotas']["raza1"]}           Raza:   {yo['mascotas']["raza2"]}         Raza:   {yo['mascotas']["raza3"]}
==========================================================""")