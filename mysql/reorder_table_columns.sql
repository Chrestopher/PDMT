ALTER TABLE pds MODIFY name text FIRST;
ALTER TABLE pds MODIFY japanese_name text after name;
ALTER TABLE pds MODIFY pokedex_number int(11) after japanese_name;
ALTER TABLE pds MODIFY generation int(11) after pokedex_number;
ALTER TABLE pds MODIFY classification text after generation;
ALTER TABLE pds MODIFY type1 text after classification;
ALTER TABLE pds MODIFY type2 text after type1;
ALTER TABLE pds MODIFY abilities text after type2;
ALTER TABLE pds MODIFY height_m double after abilities;
ALTER TABLE pds MODIFY weight_kg double after height_m;
ALTER TABLE pds MODIFY percentage_male double after weight_kg;
ALTER TABLE pds MODIFY is_legendary double after percentage_male;
ALTER TABLE pds MODIFY is_alolan double after is_legendary;
ALTER TABLE pds MODIFY is_mega double after is_alolan;
ALTER TABLE pds MODIFY base_happiness int(11) after is_mega;
ALTER TABLE pds MODIFY base_egg_steps int(11) after base_happiness;
ALTER TABLE pds MODIFY capture_rate int(11) after base_egg_steps;
ALTER TABLE pds MODIFY experience_growth int(11) after capture_rate;
ALTER TABLE pds MODIFY base_total int(11) after experience_growth;
ALTER TABLE pds MODIFY hp int(11) after base_total;
ALTER TABLE pds MODIFY attack int(11) after hp;
ALTER TABLE pds MODIFY defense int(11) after attack;
ALTER TABLE pds MODIFY sp_attack int(11) after defense;
ALTER TABLE pds MODIFY sp_defense int(11) after sp_attack;
ALTER TABLE pds MODIFY speed int(11) after sp_defense;












