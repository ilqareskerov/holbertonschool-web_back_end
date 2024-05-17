-- This isa a line of text
SELECT band_name, IFNULL(split, 2023) - IFNULL(formed, 0) as lifespan FROM metal_bands WHERE style LIKE "%Glam rock%";