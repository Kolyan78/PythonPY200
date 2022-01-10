1. Вынесите инициализацию атрибута `capacity_volume` в отдельный метод `init_capacity_volume`.  
Для этого необходимо установить первоначальное значение атрибуту, например `None`, и вызвать метод,  
   который будет инициализировать этот атрибут.
   
   ```python
   from typing import Union
   
   
   class Glass:
       def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
           self.capacity_volume = None
           self.init_capacity_volume(capacity_volume)
   
           ...
   ```

1. Самостоятельно инициализировать экземпляр класса `Glass` с объемом 200 и количеством жидкости 100.
1. Распечатать атрибуты экземпляр класса `Glass` `capacity_volume` и `occupied_volume`
