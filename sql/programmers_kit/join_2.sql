SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS JOIN ANIMAL_OUTS USING (ANIMAL_ID, NAME)
WHERE ANIMAL_INS.DATETIME > ANIMAL_OUTS.DATETIME
ORDER BY ANIMAL_INS.DATETIME
