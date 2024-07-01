const apiPaths = {
    beer: '/api/beer/',
    soft: '/api/soft/',
    pression: '/api/pression/',
    coffee: '/api/coffee/',
    burger: '/api/burger/',
    dwitch: '/api/dwitch/',
    fries: '/api/fries/',
    salad: '/api/salad/',
    dessert: '/api/dessert/'
}

let cartProductElement = document.getElementById('cart-products');
let note = document.querySelector('#message');

var hours = 24;
var now = new Date().getTime();
var stepTime = localStorage.getItem('stepTime');

if (stepTime == null) {
    localStorage.setItem('stepTime', now);
}
else {
    if (now - stepTime > hours*60*60*1000) {
        localStorage.clear;
        localStorage.setItem('stepTime', now);
    }
}

var url = window.location.pathname;
url = url.split('/');
switch (url[1]) {
    case 'order':
        fillCart();
        break;
    default:
        break;
}

function fillCart() {
    let values = shoppingCart()
    let cart = values.cart
    let totalPrice = values.totalPrice
    if(cart.length == 0) return;

    cart.forEach(product => {
        console.log("TEST2",product);
        console.log("TEST3",product.length);
        console.log("TEST",product);

        let productElement = document.createElement('div');
        productElement.classList.add('product');
        productElement.innerHTML = `
            <div class="product-name">${product[0]}</div>
            <div class="product-price">${product[1]}€</div>
        `;
        cartProductElement.appendChild(productElement);
    })

    let totalElement = document.getElementById('total');
    totalElement.innerHTML = totalPrice + '€';
}

function fetchProduct(category, products) {
    let categoryPrice = 0;
    let categoryCart = [];

    let strProducts = '';
    products.forEach(productId => {
        if (products.indexOf(productId) == products.length - 1) {
            strProducts += productId;
        } else {
            strProducts += productId + ','
        }
    })
    
    fetch(apiPaths[category] + strProducts)
        .then(response => response.json())
        .then(data => {
            categoryPrice += data.price;
            categoryCart.push([data[0].nom, data[0].prix]);
        });

    return {
        categoryCart: categoryCart,
        categoryPrice: categoryPrice
    };
}            

function shoppingCart() {
    let totalPrice = 0;
    let cart = [];

    let beerInCart = JSON.parse(localStorage.getItem('beerInCart')) || [];
    let softInCart = JSON.parse(localStorage.getItem('softInCart')) || [];
    let pressionInCart = JSON.parse(localStorage.getItem('pressionInCart')) || [];
    let coffeeInCart = JSON.parse(localStorage.getItem('coffeeInCart')) || [];
    let burgerInCart = JSON.parse(localStorage.getItem('burgerInCart')) || [];
    let dwitchInCart = JSON.parse(localStorage.getItem('dwitchInCart')) || [];
    let friesInCart = JSON.parse(localStorage.getItem('friesInCart')) || [];
    let saladInCart = JSON.parse(localStorage.getItem('saladInCart')) || [];
    let dessertInCart = JSON.parse(localStorage.getItem('dessertInCart')) || [];

    let categories = ['beer', 'soft', 'pression', 'coffee', 'burger', 'dwitch', 'fries', 'salad', 'dessert'];
    let products = [beerInCart, softInCart, pressionInCart, coffeeInCart, burgerInCart, dwitchInCart, friesInCart, saladInCart, dessertInCart];

    for (let i = 0; i < categories.length; i++) {
        if(products[i].length == 0) continue;
        let categoryReponse = fetchProduct(categories[i], products[i]);
        let categoryCart = categoryReponse.categoryCart
        let categoryPrice = categoryReponse.categoryPrice
        cart.push(categoryCart);
        totalPrice += categoryPrice;
    }

    return {
        cart: cart, 
        totalPrice: totalPrice
    };
}

function addProduct(category, productId) {
    let pressionInCart = JSON.parse(localStorage.getItem(category + 'InCart')) || [];
    pressionInCart.push(parseInt(productId));
    localStorage.setItem(category + 'InCart', JSON.stringify(pressionInCart));
}

function removeProduct(category, productId) {
    let cart = JSON.parse(localStorage.getItem(category + 'InCart')) || [];
    let index = cart.indexOf(productId);
    if (index > -1) {
        cart.splice(index, 1);
    }
    localStorage.setItem(category, JSON.stringify(cart));
    shoppingCart();
}

function order() {
    var msg = note.value;
    var pickupSlotId = document.getElementById('pickup_slot').value;

    var url = "/order";
    var orderData = {};
    orderData['note'] = msg;
    orderData['pickup_slot'] = pickupSlotId;
    $.ajax({
        url: url,
        type: "POST",
        data: orderData,
        success: function(data) {
            window.location.replace('success');
        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.log('An error occurred: ' + textStatus, errorThrown);
        }
    });
}
