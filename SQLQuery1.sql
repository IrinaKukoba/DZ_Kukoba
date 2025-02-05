
INSERT INTO Artist (name) VALUES 
('Billie Eilish'), 
('Ed Sheeran'), 
('Dua Lipa'), 
('The Weeknd');


INSERT INTO Genre (name) VALUES 
('Pop'), 
('Hip Hop'), 
('R&B');


INSERT INTO Album (title, release_year) VALUES 
('When We All Fall Asleep, Where Do We Go?', 2019), 
('÷ (Divide)', 2017), 
('Future Nostalgia', 2020), 
('After Hours', 2020);


INSERT INTO Track (title, duration, album_id) VALUES 
('Bad Guy', '00:03:14', 1),
('Shape of You', '00:03:53', 2),
('Start Now', '00:03:03', 3), 
('Blinding Lights', '00:03:20', 4),
('Bellyache', '00:02:55', 1),
('Castle on the Hill', '00:04:21', 2);


INSERT INTO Compilation (title, release_year) VALUES 
('Billie Eilish: The Collection', 2020), 
('Ed Sheeran: Greatest Hits', 2021), 
('Dua Lipa: Complete Edition', 2021), 
('The Weeknd: The Highlights', 2021);


INSERT INTO Artist_Genre (artist_id, genre_id) VALUES 
(1, 1), -- Billie Eilish - Pop
(2, 1), -- Ed Sheeran - Pop
(3, 1), -- Dua Lipa - Pop
(4, 3); -- The Weeknd - R&B


INSERT INTO Artist_Album (artist_id, album_id) VALUES 
(1, 1), -- Billie Eilish - When We All Fall Asleep, Where Do We Go?
(2, 2), -- Ed Sheeran - ÷ (Divide)
(3, 3), -- Dua Lipa - Future Nostalgia
(4, 4); -- The Weeknd - After Hours


INSERT INTO Compilation_Track (compilation_id, track_id) VALUES 
(1, 1), -- Billie Eilish: The Collection - Bad Guy
(1, 5), -- Billie Eilish: The Collection - Bellyache
(2, 2), -- Ed Sheeran: Greatest Hits - Shape of You
(2, 6), -- Ed Sheeran: Greatest Hits - Castle on the Hill
(3, 3), -- Dua Lipa: Complete Edition - Don't Start Now
(4, 4); -- The Weeknd: The Highlights - Blinding Lights