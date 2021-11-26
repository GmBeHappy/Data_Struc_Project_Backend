
# Data_Struc_Project_Backend

Project : Shabu Stock Management

วิชา DATA STRUCTURES AND ALGORITHM 


## Authors

- [@GmBeHappy](https://github.com/GmBeHappy)
- [@RMAI-PLEUM](https://github.com/RMAI-PLEUM)


## Installation

Download stock.py and add to project

```python
  from stock import *
```
    
## Usage

#### Create Stock

```python
  stock = Stock("stockName",category) 
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `stockName` | `string` | **Required**. Stock name |
| `category` | `Object:Category` | Non Required |

#### Add Category to Stock

```python
  stock.addCategory("categoryName",itemType)
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `categoryName`| `string` | **Required**. Category name |
| `itemType` | `Object:Type` | Non Required |

#### Add item type to Category

```python
  stock.getCategory('categoryName').addType('typeName',items)
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `typeName`| `string` | **Required**. Type name |
| `items` | `Object:Item` | Non Required |

#### Add item to Type

```python
  stock.getCategory('categoryName').getType('typeName').addItem('itemName', amount)
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `itemName`| `string` | **Required**. Type name |
| `amount` | `Int` | **Required**. amount of item |

#### AddNewType Button

```python
  stock.getCategory('categoryName').addNewType('typeName',amount ,expHour)
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `typeName`| `string` | **Required**. Type name |
| `amount`| `Int` | **Required**. amount of item |
| `expHour`| `Int` | **Required**. expHour |
| `items` | `Int` | Non Required |

#### AddItem Button

```python
  stock.getCategory('categoryName').getType('typeName').addItem(amount)
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `itemName`| `string` | **Required**. Type name |
| `amount` | `Int` | **Required**. amount of item |

#### useItem Button
```python
  stock.getCategory('categoryName').getType('typeName').useItem(amount)
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `itemName`| `string` | **Required**. Type name |
| `amount` | `Int` | **Required**. amount of item |

#### DeleteType Button

```python
  stock.getCategory('categoryName').removeType('typeName')
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `typeName`| `string` | **Required**. Type name |
| `typeName`| `string` | **Required**. Type name |

#### clearItem Button
```python
  stock.getCategory('categoryName').getType('typeName').clearItems()
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `itemName`| `string` | **Required**. Type name |


## License

[MIT](https://choosealicense.com/licenses/mit/)

