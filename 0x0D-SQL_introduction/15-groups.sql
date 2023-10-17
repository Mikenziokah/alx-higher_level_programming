-- grouping same values in the second table
SELECT score , COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score desc;
