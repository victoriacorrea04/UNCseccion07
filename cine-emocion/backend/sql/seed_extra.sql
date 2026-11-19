USE cine_emocion;
SET NAMES utf8mb4;
INSERT INTO movies (id, title, overview, rating, release_year, poster_url) VALUES
(21,'El Padrino','La saga de la familia Corleone, una de las más poderosas de la mafia de Nueva York.',8.7,1972,NULL),
(22,'Matrix','Un hacker descubre que la realidad es una simulación y se une a la rebelión contra las máquinas.',8.2,1999,NULL),
(23,'El caballero oscuro','Batman se enfrenta al Joker, un criminal caótico que quiere sumir Gotham en el desorden.',8.5,2008,NULL),
(24,'Toy Story','Los juguetes de Andy cobran vida cuando nadie los ve, y un vaquero rivaliza con un nuevo astronauta.',8.0,1995,NULL),
(25,'Buscando a Nemo','Un pez payaso cruza el océano para encontrar a su hijo, capturado por un buzo.',7.8,2003,NULL),
(26,'El viaje de Chihiro','Una niña queda atrapada en un mundo de espíritus y debe trabajar para salvar a sus padres.',8.5,2001,NULL),
(27,'Pulp Fiction','Historias entrelazadas de criminales de Los Ángeles: dos sicarios, un boxeador y la esposa de un gánster.',8.5,1994,NULL),
(28,'Origen','Un ladrón que roba secretos entrando en los sueños recibe la tarea de implantar una idea.',8.4,2010,NULL),
(29,'La La Land','Una aspirante a actriz y un pianista de jazz se enamoran mientras persiguen sus sueños en Los Ángeles.',7.9,2016,NULL),
(30,'Jurassic Park','Un parque con dinosaurios clonados se descontrola y los visitantes luchan por sobrevivir.',8.0,1993,NULL);
INSERT INTO movie_genres (movie_id, genre_id) VALUES
(21,80),(21,18),(22,28),(22,878),(23,28),(23,80),(23,18),(24,16),(24,35),(24,10751),
(25,16),(25,10751),(25,35),(26,16),(26,14),(26,10751),(27,80),(27,53),
(28,28),(28,878),(28,12),(29,35),(29,18),(29,10402),(29,10749),(30,12),(30,878);
