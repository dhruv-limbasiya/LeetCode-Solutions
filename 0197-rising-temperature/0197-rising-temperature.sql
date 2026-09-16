select today.id 
from weather yesterday
join weather today
on  DATEDIFF(today.recordDate, yesterday.recordDate) = 1
where today.temperature > yesterday.temperature;        