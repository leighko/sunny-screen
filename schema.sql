CREATE TABLE IF NOT EXISTS "brands" (
    "id" SERIAL PRIMARY KEY,
    "brand" VARCHAR(32) NOT NULL
);

CREATE TABLE IF NOT EXISTS "names" (
    "id" SERIAL PRIMARY KEY,
    "name" VARCHAR(32) NOT NULL UNIQUE
);

CREATE TYPE "body_parts" AS ENUM ('Face', 'Body', 'Face&Body');
CREATE TYPE "pa" AS ENUM ('+', '++', '+++', '++++');
CREATE TYPE "makeup" AS ENUM ('Chemical', 'Mineral', 'Chemical&Mineral');

CREATE TABLE IF NOT EXISTS "product_data" (
    "id" SERIAL PRIMARY KEY,
    "brand_id" INT,
    "name_id" INT,
    "use" body_parts NOT NULL, --make this a SET (instead of having the third option)
    "pa_rating" pa NOT NULL,
    "type" makeup NOT NULL, --use a set here bc i think they can be both. double check that first tho
    FOREIGN KEY("brand_id") REFERENCES "brands"("id"),
    FOREIGN KEY("name_id") REFERENCES "names"("id")
);

CREATE TABLE IF NOT EXISTS "user_data" (
    "id" SERIAL PRIMARY KEY,
    "brand_id" INT,
    "name_id" INT,
    "tried" INT NOT NULL CHECK("tried" <= 1),
    "feedback" TEXT, 
    "rating" INT, -- on a scale from 1 - 10? or 1-5 or 1-3... figure out how to implement
    FOREIGN KEY("brand_id") REFERENCES "brands"("id"),
    FOREIGN KEY("name_id") REFERENCES "names"("id")
);

CREATE TABLE IF NOT EXISTS "ingredients" (
    "id" INT PRIMARY KEY,
    "name_id" INT,
    "active" TEXT NOT NULL,
    "active_percent" INT, 
    "inactive" TEXT NOT NULL,
    FOREIGN KEY("name_id") REFERENCES "names"("id")
);