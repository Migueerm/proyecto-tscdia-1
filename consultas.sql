INSERT INTO estudiante VALUES ('001','Juan Perez','10/09/2000','23','example@example.com','12345678901');
INSERT INTO estudiante VALUES ('002','Martin Sanzhes','06/10/2002','22','example12@example.com','12945908901');
INSERT INTO estudiante VALUES ('003','Pedro Perez','03/12/2005','19','example13@example.com','12985677831');
INSERT INTO estudiante VALUES ('004','Ana López','15/05/1998','26','ana@example.com','19876543210');
INSERT INTO estudiante VALUES ('005','María Rodríguez','20/07/2001','21','maria@example.com','18765432109');
INSERT INTO estudiante VALUES ('006','Luis González','02/03/1999','23','luis@example.com','17654321098');
INSERT INTO estudiante VALUES ('007','Carla Fernández','12/11/2003','18','carla@example.com','16543210987');

INSERT INTO inscripcion VALUES ('001','11','01/03/2021','8');
INSERT INTO inscripcion VALUES ('002','12','01/03/2021','9');
INSERT INTO inscripcion VALUES ('003','13','01/03/2021','10');  
INSERT INTO inscripcion VALUES ('004','14','01/03/2021','7');
INSERT INTO inscripcion VALUES ('005','15','01/03/2021','8');
INSERT INTO inscripcion VALUES ('006','16','01/03/2021','9');
INSERT INTO inscripcion VALUES ('007','17','01/03/2021','10');


UPDATE estudiante SET Edad = '24' WHERE ID_Estudiante = '001';
UPDATE estudiante SET Edad = '23' WHERE ID_Estudiante = '005';

UPDATE inscripcion SET Nota_Final = '10' WHERE ID_Estudiante = '001' AND ID_Curso = '11';
UPDATE inscripcion SET Nota_Final = '9' WHERE ID_Estudiante = '002' AND ID_Curso = '12';
UPDATE inscripcion SET Nota_Final = '8' WHERE ID_Estudiante = '003' AND ID_Curso = '13';
UPDATE inscripcion SET Nota_Final = '7' WHERE ID_Estudiante = '004' AND ID_Curso = '14';
UPDATE inscripcion SET Nota_Final = '6' WHERE ID_Estudiante = '005' AND ID_Curso = '15';
UPDATE inscripcion SET Nota_Final = '5' WHERE ID_Estudiante = '006' AND ID_Curso = '16';
UPDATE inscripcion SET Nota_Final = '4' WHERE ID_Estudiante = '007' AND ID_Curso = '17';

DELETE FROM inscripcion WHERE ID_Estudiante = '001' AND ID_Curso = '11';
DELETE FROM inscripcion WHERE ID_Estudiante = '002' AND ID_Curso = '12';
DELETE FROM inscripcion WHERE ID_Estudiante = '003' AND ID_Curso = '13';
DELETE FROM inscripcion WHERE ID_Estudiante = '004' AND ID_Curso = '14';
DELETE FROM inscripcion WHERE ID_Estudiante = '005' AND ID_Curso = '15';
DELETE FROM inscripcion WHERE ID_Estudiante = '006' AND ID_Curso = '16';
DELETE FROM inscripcion WHERE ID_Estudiante = '007' AND ID_Curso = '17';