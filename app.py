from flask import Flask, jsonify, request


app = Flask(__name__)

from products import products

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'Tefii'})

@app.route('/products', methods= ['GET'])
def getproducts():
    return  jsonify({'products': products, 'message': 'Products list'})

@app.route('/products/<string:product_name>', methods= ['GET'])
def getproduct(product_name):

    productFound = list(filter(lambda x: x['name'] == product_name, products))

    if len(productFound) > 0 :
        return jsonify({'products': productFound[0]})
    else: 
        return jsonify({'message': 'Product not found'})

@app.route('/products', methods= ['POST'])
def addproduct():

    new_product =  {
        'name': request.json['name'],
        'product': request.json['price'],
        'quantity': request.json['quantity']
    }
    products.append(new_product)

    return jsonify({'message': 'receive new product', 'NewProduct': new_product, 'products': products})

@app.route('/products/<string:product_name>', methods= ['PUT'])
def upgradeProduct(product_name):    

    productFound = list(filter(lambda x: x['name'] == product_name, products))

    if len(productFound) > 0 :
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantity'] = request.json['quantity']
        return jsonify({'message': 'Updrade product', 'Product': productFound[0], 'products': products})
    else:

        return jsonify({'message': 'Product not found'})

@app.route('/products/<string:product_name>', methods= ['DELETE'])
def deleteproduct(product_name):
    
    productFound = list(filter(lambda x: x['name'] == product_name, products))
    
    if len(productFound) > 0 :
        products.remove(productFound[0])
        return jsonify({'message': 'Delete product', 'Delete Product': productFound[0], 'products': products})
    else:
        
        return jsonify({'message': 'Product not found'})



if  __name__ == '__main__':
    app.run(debug=True,port = 4000)