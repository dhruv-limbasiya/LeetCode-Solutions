WITH filtered_stadium AS (
    SELECT id, visit_date, people
    FROM Stadium
    WHERE people >= 100
),
grouped_stadium AS (
    SELECT 
        id, 
        visit_date, 
        people,
        id - ROW_NUMBER() OVER (ORDER BY id) AS grp
    FROM filtered_stadium
)
SELECT id, visit_date, people
FROM grouped_stadium
WHERE grp IN (
    SELECT grp 
    FROM grouped_stadium 
    GROUP BY grp 
    HAVING COUNT(*) >= 3
)
ORDER BY visit_date ASC;
