ALTER TABLE asientos ADD COLUMN id_pasajero INTEGER NULL;
ALTER TABLE asientos ADD CONSTRAINT fk_asientos_pasajeros FOREIGN KEY (id_pasajero)
REFERENCES pasajeros(id);