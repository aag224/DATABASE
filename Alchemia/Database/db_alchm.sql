CREATE TABLE "Control" (
	"ID"	INTEGER UNIQUE,
	"Cuenta"	TEXT NOT NULL COLLATE RTRIM,
	"Clave_Reaccion"	TEXT NOT NULL COLLATE RTRIM,
	"Fecha"	TEXT NOT NULL,
	"Tipo_de_Documento"	TEXT NOT NULL,
	"Material"	TEXT,
	PRIMARY KEY("ID" AUTOINCREMENT),
	FOREIGN KEY("Clave_Reaccion") REFERENCES "Investigacion"("Clave_Reaccion"),
	FOREIGN KEY("Cuenta") REFERENCES "Identificacion"("Cuenta"))

CREATE TABLE "Identificacion" (
	"Cuenta"	TEXT UNIQUE,
	"Correo"	TEXT,
	"Numero Celular"	TEXT,
	"Nombre"	TEXT UNIQUE,
	"Carrera "	TEXT,
	"Posgrado "	TEXT,
	PRIMARY KEY("Cuenta"))

CREATE TABLE "Investigacion" (
	"Clave_Reaccion"	INTEGER UNIQUE,
	"Nombre " TEXT UNIQUE,
	"Inicio_Fin" TEXT,
	"Estatus "	TEXT,
	PRIMARY KEY("Clave_Reaccion"))

CREATE TABLE "Login_datos" (
	"ID"	INTEGER,
	"Cuenta"	INTEGER,
	"Password"	TEXT,
	PRIMARY KEY("ID" AUTOINCREMENT),
	FOREIGN KEY("Cuenta") REFERENCES "Identificacion"("Cuenta")
)
