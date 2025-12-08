INSERT INTO aerolineas(nombre_aerolinea,web_aerolinea) VALUES
('Aerolínea 1','www.aerolinea1.com'),
('Aerolínea 2','www.aerolinea2.com');

INSERT INTO aviones(cod_avion,tipo_avion,capacidad_avion,id_aerolinea) VALUES
('AV-1',1,10,1),
('AV-2',2,15,1),
('AV-3',1,10,2),
('AV-4',2,15,2);

INSERT INTO localidades(nombre_localidad,latitud,longitud) VALUES
('Santiago',-33.389260,-70.794059),
('Temuco',-38.927248,-72.646820);

INSERT INTO vuelos(fecha_hora_salida,destino,origen,cod_vuelo,id_avion,tipo_vuelo) VALUES
('2025-11-12 00:00',2,1,'AV-1-ZCO',1,1),
('2025-11-12 00:00',1,2,'AV-1-STG',2,2);