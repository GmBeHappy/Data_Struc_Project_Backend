
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
| `typeName'`| `string` | **Required**. Type name |
| `items` | `Object:Item` | Non Required |

#### Add item to Type

```python
  stock.getCategory('categoryName').getType('typeName').addItem('itemName', amount)
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `itemName'`| `string` | **Required**. Type name |
| `amount` | `Int` | **Required**. amount of item |




## License

[MIT](https://choosealicense.com/licenses/mit/)

