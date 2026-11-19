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

-- Historial del usuario demo (para ver "Mis estadisticas"). Se borra con el mismo DELETE de arriba.
INSERT INTO searches (text, emotion_id, user_id, created_at)
SELECT t.texto, t.emocion, u.id, NOW() - INTERVAL t.dias DAY
FROM users u
JOIN (SELECT '[demo] triste' AS texto, 2 AS emocion, 6 AS dias
      UNION ALL SELECT '[demo] triste otra vez', 2, 5
      UNION ALL SELECT '[demo] feliz', 1, 4
      UNION ALL SELECT '[demo] romantico', 6, 3
      UNION ALL SELECT '[demo] romantico', 6, 3
      UNION ALL SELECT '[demo] estresado', 4, 2
      UNION ALL SELECT '[demo] feliz', 1, 1
      UNION ALL SELECT '[demo] feliz', 1, 1
      UNION ALL SELECT '[demo] aburrido', 5, 0) t
WHERE u.username = 'demo';
