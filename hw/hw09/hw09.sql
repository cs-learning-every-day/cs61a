CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-- copy your solution from prev hw!
-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name, size from dogs, sizes where dogs.height > sizes.min and dogs.height <= sizes.max;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT p.child from dogs as d, parents as p where p.parent = d.name order by height desc;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECt a.child as first, b.child as second 
    from parents as a, parents as b where a.parent = b.parent and a.child < b.child;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT first || ' and ' || second || ' are ' || b.size || ' siblings' 
    from siblings as a, size_of_dogs as b, size_of_dogs as c
    where a.first = b.name and a.second = c.name and b.size = c.size;