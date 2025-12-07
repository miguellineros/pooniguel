CREATE TABLE IF NOT EXISTS aerolineas(
    id_aerolinea INTEGER NOT NULL AUTO_INCREMENT,
    nombre_aerolinea VARCHAR(25) NOT NULL,
    web_aerolinea VARCHAR(255) NULL,

    CONSTRAINT pk_aerolineas PRIMARY KEY (id_aerolinea)
);

CREATE TABLE IF NOT EXISTS aviones(
    id_avion INTEGER NOT NULL AUTO_INCREMENT, 
    cod_avion VARCHAR(10) NOT NULL, 
    tipo_avion INTEGER NOT NULL, 
    capacidad_avion INTEGER NOT NULL, 
    id_aerolinea INTEGER NOT NULL,

    CONSTRAINT pk_aviones PRIMARY KEY (id_avion),
    CONSTRAINT fk_aviones_aerolineas FOREIGN KEY (id_aerolinea)
        REFERENCES aerolineas(id_aerolinea)
);

CREATE TABLE IF NOT EXISTS localidades(
    id_localidad INTEGER NOT NULL AUTO_INCREMENT, 
    nombre_localidad VARCHAR(50) NOT NULL, 
    latitud FLOAT NULL,
    longitud FLOAT NULL,

    CONSTRAINT pk_localidades PRIMARY KEY (id_localidad)
);

CREATE TABLE IF NOT EXISTS vuelos(
    id_vuelo INTEGER NOT NULL AUTO_INCREMENT, 
    fecha_hora_salida DATETIME NOT NULL, 
    destino INTEGER NOT NULL, 
    origen INTEGER NOT NULL, 
    cod_vuelo VARCHAR(6) NOT NULL, 
    id_avion INTEGER NOT NULL,
    tipo_vuelo INTEGER NOT NULL,

    CONSTRAINT pk_vuelos PRIMARY KEY (id_vuelo),
    CONSTRAINT fk_vuelos_localidades_destino FOREIGN KEY (destino)
        REFERENCES localidades (id_localidad),
    CONSTRAINT fk_vuelos_localidades_origen FOREIGN KEY (origen)
        REFERENCES localidades (id_localidad),
    CONSTRAINT fk_vuelos_aviones FOREIGN KEY (id_avion)
        REFERENCES aviones (id_avion)
);

CREATE TABLE IF NOT EXISTS pasajeros(
    id_pasajero INTEGER NOT NULL AUTO_INCREMENT, 
    nombre_pasajero VARCHAR(100) NOT NULL, 
    num_pasaporte VARCHAR(15) NULL, 
    fecha_nacimiento DATE NULL,

    CONSTRAINT pk_pasajeros PRIMARY KEY (id_pasajero)
);

CREATE TABLE IF NOT EXISTS asientos(
    id_asiento INTEGER NOT NULL AUTO_INCREMENT, 
    id_vuelo INTEGER NOT NULL, 
    num_asiento VARCHAR(4) NOT NULL,
    categoria INTEGER NOT NULL,

    CONSTRAINT pk_asientos PRIMARY KEY (id_asiento),
    CONSTRAINT fk_asientos_vuelos FOREIGN KEY (id_vuelo)
        REFERENCES vuelos (id_vuelo)
);

CREATE TABLE IF NOT EXISTS reservas(
    id_reserva INTEGER NOT NULL AUTO_INCREMENT, 
    id_pasajero INTEGER NOT NULL, 
    id_asiento INTEGER NOT NULL, 
    
    CONSTRAINT pk_reservas PRIMARY KEY (id_reserva),
    CONSTRAINT fk_reservas_pasajeros FOREIGN KEY (id_pasajero)
        REFERENCES pasajeros (id_pasajero),
    CONSTRAINT fk_reservas_asientos FOREIGN KEY (id_asiento)
        REFERENCES asientos (id_asiento)
);