--Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans
SELECT origin, fans as nb_fans, dense_rank() 
OVER ( order by mark desc ) 
AS 'dense_rank' FROM metal_bands;
