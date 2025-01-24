-- Tabla Athletes
CREATE TABLE IF NOT EXISTS Athletes (
    PersonName TEXT NOT NULL,
    Country TEXT NOT NULL,
    Discipline TEXT NOT NULL
);

-- Tabla Coaches
CREATE TABLE IF NOT EXISTS Coaches (
    Name TEXT NOT NULL,
    Country TEXT NOT NULL,
    Discipline TEXT NOT NULL,
    Event TEXT
);

-- Tabla EntriesGender
CREATE TABLE IF NOT EXISTS EntriesGender (
    Discipline TEXT NOT NULL,
    Female INTEGER NOT NULL,
    Male INTEGER NOT NULL,
    Total INTEGER NOT NULL
);

-- Tabla Medals
CREATE TABLE IF NOT EXISTS Medals (
    Rank INTEGER NOT NULL,
    TeamCountry TEXT NOT NULL,
    Gold INTEGER NOT NULL,
    Silver INTEGER NOT NULL,
    Bronze INTEGER NOT NULL,
    Total INTEGER NOT NULL,
    Rank_by_Total INTEGER NOT NULL
);

-- Tabla Teams
CREATE TABLE IF NOT EXISTS Teams (
    TeamName TEXT NOT NULL,
    Discipline TEXT NOT NULL,
    Country TEXT NOT NULL,
    Event TEXT NOT NULL
);
