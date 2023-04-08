DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS rooms CASCADE;

CREATE TABLE users (
    id UUID PRIMARY KEY,
    name STRING NOT NULL,
    image STRING NOT NULL,
    room UUID
);

CREATE TABLE rooms (
    id UUID PRIMARY KEY,
    code STRING NOT NULL UNIQUE,
    creator UUID
);

CREATE INDEX idx_rooms_code ON rooms (code);

ALTER TABLE users ADD FOREIGN KEY (room) REFERENCES rooms (id) ON DELETE SET NULL;
ALTER TABLE rooms ADD FOREIGN KEY (creator) REFERENCES users (id) ON DELETE SET NULL;