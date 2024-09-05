
Cubo Operações
Dados de entrada
DROP TABLE IF EXISTS fato_vendas;

CREATE TABLE fato_vendas (
marca VARCHAR NOT NULL,
segmento VARCHAR NOT NULL,
dia int NOT NULL,
quantidade int NOT NULL);

INSERT INTO fato_vendas (marca, segmento, dia, quantidade)
VALUES
    ('Naique', 'Premium',1 , 100),
    ('Naique', 'Premium',2,100),
    ('Naique', 'Corrida', 1, 200),
    ('Naique', 'Corrida',2, 200),
    ('Naique', 'Futebol',1, 100),
		('Naique', 'Futebol', 2, 150),
    ('Ardida', 'Premium',1, 100),
		('Ardida', 'Premium',2, 88),
    ('Ardida', 'Corrida',1, 300),
	 ('Ardida', 'Corrida',2, 400),
    ('Ardida', 'Futebol',1, 300),
	('Ardida', 'Futebol',2, 279);
​
Drill-down
SELECT
    marca,
    segmento,
    SUM (quantidade)
FROM
    fato_vendas
GROUP BY
    CUBE (marca, segmento)
ORDER BY
    marca,
    segmento;
​
Roll-up
SELECT
    segmento,
    marca,
    SUM (quantidade)
FROM
    fato_vendas
GROUP BY
    ROLLUP (marca, segmento)
ORDER BY
    marca,
    segmento;
​
Slice
SELECT
    segmento,
    SUM(quantidade)
FROM
    fato_vendas
WHERE marca = 'Naique'
GROUP BY segmento
​
Dice
SELECT
    segmento,
    marca,
    quantidade
FROM
    fato_vendas
WHERE
		marca = 'Naique' AND segmento = 'Premium'
​
Pivot
Se não existir. Mas já temos no Elephantdb
CREATE EXTENSION tablefunc;
​
SELECT *
FROM crosstab('
	SELECT
	    segmento,
	    marca,
	    SUM(quantidade)
	FROM
	    fato_vendas
	GROUP BY segmento, marca ORDER BY segmento, marca', 
  'SELECT DISTINCT marca FROM fato_vendas')
AS ct ("Segmento" text, "Naique" int, "Ardidas" int); 