-- OPCIONAL: datos de ejemplo para ver el grafico con varios dias.
-- Uso: mysql -uroot -proot < seed_demo_busquedas.sql
-- Borrarlos:  DELETE FROM searches WHERE text LIKE '[demo]%';
USE cine_emocion;
INSERT INTO searches (text, emotion_id, created_at) VALUES
('[demo] hoy estoy triste', 2, NOW() - INTERVAL 6 DAY),
('[demo] muy triste', 2, NOW() - INTERVAL 6 DAY),
('[demo] estoy feliz', 1, NOW() - INTERVAL 5 DAY),
('[demo] estresado por examenes', 4, NOW() - INTERVAL 4 DAY),
('[demo] ansioso', 4, NOW() - INTERVAL 4 DAY),
('[demo] ansiedad', 4, NOW() - INTERVAL 4 DAY),
('[demo] feliz', 1, NOW() - INTERVAL 3 DAY),
('[demo] muy contento', 1, NOW() - INTERVAL 3 DAY),
('[demo] aburrido', 5, NOW() - INTERVAL 2 DAY),
('[demo] triste otra vez', 2, NOW() - INTERVAL 2 DAY),
('[demo] enojado', 3, NOW() - INTERVAL 1 DAY),
('[demo] romantico', 6, NOW() - INTERVAL 1 DAY),
('[demo] feliz', 1, NOW() - INTERVAL 1 DAY);
