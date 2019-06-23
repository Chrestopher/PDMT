ALTER TABLE pds MODIFY name text FIRST;
ALTER TABLE pds MODIFY pokedex_number int(11) after name;
ALTER TABLE pds MODIFY generation int(11) after pokedex_number;
ALTER TABLE pds MODIFY type1 text after generation;
ALTER TABLE pds MODIFY type2 text after type1;
ALTER TABLE pds MODIFY height_m double after type2;
ALTER TABLE pds MODIFY weight_kg double after height_m;