USE cine_emocion;
SET NAMES utf8mb4;

INSERT INTO genres (id, name) VALUES
(28,'Acción'),(12,'Aventura'),(16,'Animación'),(35,'Comedia'),(80,'Crimen'),
(18,'Drama'),(10751,'Familia'),(14,'Fantasía'),(27,'Terror'),(10402,'Música'),
(9648,'Misterio'),(10749,'Romance'),(878,'Ciencia ficción'),(53,'Suspenso');

INSERT INTO emotions (id, name, label, emoji) VALUES
(1,'feliz','Feliz','😄'),
(2,'triste','Triste','😢'),
(3,'enojado','Enojado','😠'),
(4,'ansioso','Estresado / Ansioso','😰'),
(5,'aburrido','Aburrido','😐'),
(6,'romantico','Romántico','😍');

-- Que generos recomendar para cada emocion
INSERT INTO emotion_genres (emotion_id, genre_id) VALUES
(1,35),(1,16),(1,10751),(1,10402),
(2,18),(2,10749),(2,35),
(3,28),(3,80),(3,53),
(4,35),(4,16),(4,14),
(5,12),(5,878),(5,9648),
(6,10749),(6,18);

INSERT INTO movies (id, title, overview, rating, release_year, poster_url) VALUES
(1,'Forrest Gump','La vida de un hombre sencillo de Alabama que, sin proponérselo, presencia y protagoniza los momentos clave de la historia de Estados Unidos.',8.5,1994,NULL),
(2,'Intensamente','Las emociones de una niña de once años -Alegría, Tristeza, Furia, Miedo y Asco- viven en su cabeza y se desordenan con una mudanza.',7.6,2015,NULL),
(3,'La vida es bella','Un padre usa su imaginación para proteger a su hijo del horror de un campo de concentración haciéndole creer que todo es un juego.',8.5,1997,NULL),
(4,'El Rey León','El joven león Simba debe superar la pérdida de su padre y reclamar su lugar como rey de la sabana.',8.3,1994,NULL),
(5,'Mad Max: Furia en el camino','En un desierto postapocalíptico, Furiosa y Max huyen de un tirano en una persecución brutal y sin descanso.',7.6,2015,NULL),
(6,'John Wick','Un exasesino a sueldo vuelve a la acción para vengarse de quienes le arrebataron lo que más quería.',7.4,2014,NULL),
(7,'El resplandor','Una familia cuida un hotel aislado en invierno mientras el padre cae poco a poco en la locura.',8.2,1980,NULL),
(8,'Parásitos','Una familia pobre se infiltra en la vida de una familia rica con consecuencias inesperadas.',8.5,2019,NULL),
(9,'Coco','Miguel sueña con ser músico y viaja a la Tierra de los Muertos para descubrir la historia de su familia.',8.2,2017,NULL),
(10,'Amélie','Una joven parisina decide mejorar en secreto la vida de los que la rodean mientras busca su propio amor.',7.9,2001,NULL),
(11,'Interstellar','Un grupo de astronautas viaja a través de un agujero de gusano en busca de un nuevo hogar para la humanidad.',8.4,2014,NULL),
(12,'El señor de los anillos: La comunidad del anillo','Frodo emprende un viaje para destruir un anillo todopoderoso junto a una compañía de héroes.',8.4,2001,NULL),
(13,'Up','Un anciano ata miles de globos a su casa y vuela hacia Sudamérica acompañado de un niño explorador.',7.9,2009,NULL),
(14,'Antes del amanecer','Dos jóvenes se conocen en un tren y pasan una noche caminando por Viena, conversando sobre el amor y la vida.',7.9,1995,NULL),
(15,'Whiplash','Un joven baterista se enfrenta a un profesor obsesivo que lo empuja hasta el límite.',8.4,2014,NULL),
(16,'Gladiador','Un general romano traicionado se convierte en gladiador para vengar a su familia.',8.2,2000,NULL),
(17,'Shrek','Un ogro gruñón emprende una misión para rescatar a una princesa y recuperar su pantano.',7.8,2001,NULL),
(18,'Seven','Dos detectives persiguen a un asesino en serie que basa sus crímenes en los siete pecados capitales.',8.4,1995,NULL),
(19,'Soul','Un profesor de música queda atrapado fuera de su cuerpo y descubre qué significa realmente vivir.',8.1,2020,NULL),
(20,'Titanic','Un joven artista y una chica de clase alta se enamoran a bordo del famoso transatlántico.',7.9,1997,NULL);

INSERT INTO movie_genres (movie_id, genre_id) VALUES
(1,18),(1,10749),(1,35),
(2,16),(2,35),(2,10751),
(3,35),(3,18),(3,10749),
(4,16),(4,10751),(4,18),
(5,28),(5,12),(5,878),
(6,28),(6,53),
(7,27),(7,53),
(8,35),(8,53),(8,18),
(9,16),(9,10751),(9,10402),(9,14),
(10,35),(10,10749),
(11,12),(11,18),(11,878),
(12,12),(12,14),(12,28),
(13,16),(13,12),(13,10751),(13,35),
(14,10749),(14,18),
(15,18),(15,10402),
(16,28),(16,18),(16,12),
(17,16),(17,35),(17,14),(17,10751),
(18,80),(18,9648),(18,53),
(19,16),(19,10751),(19,35),(19,10402),(19,14),
(20,18),(20,10749);
