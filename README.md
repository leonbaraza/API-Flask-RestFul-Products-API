# Flask RestFul Product API

## ROUTES
1. All Products.
```python
GET /api/products
```
⋅⋅⋅ Returns a list json objects of all products

2. One products.
```python
GET /api/products/:id
```
⋅⋅⋅ Returns a json object of a single products based on the id 

3. Creating a products.
```python
POST /api/products
```
⋅⋅⋅ Returns status code of 201 and a json object of the products created or error with status code of 400 if no such id and 500 if something goes wrong

4. Updating a products
```python
PUT /api/products/:id
```
⋅⋅⋅ Returns a json object of the products updated or error with status code of 400 if no such id and 500 if something goes wrong

5. Deleting a products
```python
DELETE /api/products/:id
```
⋅⋅⋅ Returns a json message of deletion successful or error with status code of 400 if no such id and 500 if something goes wrong