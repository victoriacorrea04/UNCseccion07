USE cine_emocion;
SET NAMES utf8mb4;
INSERT INTO movies (id, title, overview, rating, release_year, poster_url) VALUES
(31,'El club de la pelea','Un empleado insomne y un vendedor de jabón carismático fundan un club clandestino de peleas que se les va de las manos.',8.4,1999,NULL),
(32,'Los Vengadores','Un grupo de superhéroes se une para evitar que Loki invada la Tierra con un ejército alienígena.',7.7,2012,NULL),
(33,'La princesa Mononoke','Un joven guerrero se ve atrapado en la guerra entre los dioses del bosque y una aldea que explota el hierro.',8.3,1997,NULL),
(34,'Volver al futuro','Un adolescente viaja accidentalmente a 1955 en una máquina del tiempo y debe lograr que sus padres se enamoren.',8.3,1985,NULL),
(35,'El silencio de los corderos','Una joven agente del FBI pide ayuda a un brillante psiquiatra caníbal para atrapar a otro asesino en serie.',8.3,1991,NULL),
(36,'Ratatouille','Una rata con talento para la cocina se alía con un joven pinche para convertirse en chef en París.',7.8,2007,NULL),
(37,'Mi vecino Totoro','Dos hermanas se mudan al campo y conocen a los amables espíritus del bosque, entre ellos el gran Totoro.',8.1,1988,NULL),
(38,'Django desencadenado','Un esclavo liberado se asocia con un cazarrecompensas para rescatar a su esposa de un cruel plantador.',8.2,2012,NULL),
(39,'Los increíbles','Una familia de superhéroes retirados debe volver a la acción para detener a un villano.',7.7,2004,NULL),
(40,'Gran Torino','Un veterano de guerra gruñón se encariña con sus vecinos inmigrantes y los defiende de una pandilla.',8.0,2008,NULL),
(41,'Perdida','Cuando su esposa desaparece el día de su aniversario, un hombre se convierte en el principal sospechoso.',7.9,2014,NULL),
(42,'Diario de una pasión','Un joven humilde y una chica de familia rica viven un romance de verano que el tiempo pondrá a prueba.',7.8,2004,NULL),
(43,'Sueños de libertad','Un banquero condenado injustamente forja una amistad en prisión y mantiene viva la esperanza.',8.7,1994,NULL),
(44,'Monsters, Inc.','Dos monstruos que trabajan asustando niños descubren que una pequeña humana puede cambiarlo todo.',7.8,2001,NULL),
(45,'Cuestión de tiempo','Un joven descubre que puede viajar en el tiempo y lo usa para conquistar el amor y valorar la vida.',7.9,2013,NULL),
(46,'Mamma Mia!','Una novia invita en secreto a los tres posibles padres de ella a su boda en una isla griega, al ritmo de ABBA.',6.5,2008,NULL),
(47,'El gran showman','La historia de P. T. Barnum, quien fundó un espectáculo que revolucionó el mundo del circo.',7.6,2017,NULL),
(48,'Top Gun: Maverick','Tras más de treinta años de servicio, Maverick entrena a una nueva generación de pilotos para una misión imposible.',8.2,2022,NULL),
(49,'Ahora me ves','Un grupo de magos realiza atracos espectaculares durante sus shows mientras el FBI intenta atraparlos.',7.2,2013,NULL),
(50,'Alien','La tripulación de una nave comercial descubre que algo letal viaja a bordo con ellos.',8.5,1979,NULL);
INSERT INTO movie_genres (movie_id, genre_id) VALUES
(31,18),(31,53),(32,28),(32,12),(32,878),(33,16),(33,14),(33,12),
(34,12),(34,878),(34,35),(35,80),(35,53),(35,27),(36,16),(36,35),(36,10751),
(37,16),(37,14),(37,10751),(38,18),(38,28),(39,16),(39,28),(39,10751),
(40,18),(40,80),(41,9648),(41,53),(41,18),(42,10749),(42,18),(43,18),(43,80),
(44,16),(44,35),(44,10751),(45,10749),(45,35),(45,14),(46,35),(46,10402),(46,10749),
(47,18),(47,10402),(48,28),(48,18),(49,9648),(49,53),(49,80),(50,27),(50,878);
