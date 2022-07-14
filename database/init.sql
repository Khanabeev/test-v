DROP TABLE IF EXISTS organizations;
CREATE TABLE organizations
(
    id          BIGSERIAL PRIMARY KEY,
    name        VARCHAR NOT NULL,
    business_id VARCHAR NOT NULL UNIQUE,
    email       VARCHAR NOT NULL
);

CREATE TYPE enum_brand AS ENUM(
    'Canyon',
    'Trek',
    'Cannondale',
    'Specialized',
    'Giant',
    'Orbea',
    'Scott',
    'Santa Cruz',
    'Cervelo'
    );

DROP TABLE IF EXISTS bikes;
CREATE TABLE bikes
(
    id            BIGSERIAL PRIMARY KEY,
    organization  INTEGER       NOT NULL,
    brand         enum_brand    NOT NULL,
    model         VARCHAR,
    price         NUMERIC(8, 2) NOT NULL,
    serial_number VARCHAR       NOT NULL UNIQUE
);
