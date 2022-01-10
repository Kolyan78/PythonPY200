# Паттерн "Фабричный метод".

1. Реализовать абстрактный класс `DriverFactoryMethod`, который будет возвращать драйвера типа `IStructureDriver` 
   с помощью метода класса `get_driver`.
   ```python
   class DriverFactoryMethod(ABC):
       @classmethod
       @abstractmethod
       def get_driver(cls) -> IStructureDriver:
           ...
   ```

1. Проанализировать реализацию класса `SimpleFileFactoryMethod` для построения драйвера `SimpleFileDriver` 
   с помощью паттерна фабричный метод.
   
1. Инициализировать `SimpleFileDriver` с помощью фабричного метода с названием по умолчанию "untitled.txt".
