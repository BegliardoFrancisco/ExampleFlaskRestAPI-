# Example of the first RESTAPI in Flask

#####  **clarification: "This API is a first approach to the framework, observing its main features, it does not possess persistence and is not used in any type of software product "**

------------


#### Methods & Routes
/Products:
- 'GET':  returns the list of products. if you add a path variable called "product_name" you request an individual product 
>/products/:{products_name}
- 'POST': Receive the json send by request and agreaga the product. Json.
>Example POST request json:
		`{
		"name": ExampleName ,
		 "price":  ExamplePrice ,
		 "quantity: ExampleQuantity
		 }`
		 
- 'PUT': A json is sent with the update data, and the object to be updated is referenced using a path variable called "produc_name":
> Route:  "Products/:{product_name}"
###### 		Example Data Updrade:
		`{
		"name": ExampleNameUpgrade ,
		 "price":  ExamplePriceUpgrade,
		 "quantity: ExampleQuantityUpgrade
		 }`

- 'DELETE': Using a path variable called "product_name" removes a desired product .
> Route:  "Products/:{product_name}"