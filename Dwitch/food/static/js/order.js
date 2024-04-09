var pcart = document.querySelector('#pcart');
var ptotal = document.querySelector('#ptotal');


function addBurger(burid){
    burgerId = '#bur' + burid;
    var name = document.querySelector(burgerId).innerHTML;
    var radio = 'burger' + burid;
    var price = document.getElementsByName(radio);
    pcart.innerHTML += '<li>' + name + ' ' + price[0].value + '</li>';

    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize = orders.length;

    orders[cartSize] = [name, price];
    localStorage.setItem('orders', JSON.stringify(orders));
    total = Number(total) + Number(price);
    localStorage.setItem('total', total);

    var cart = document.querySelector("#cart")
    cart.innerHTML = orders.length;

    ptotal.innerHTML = 'Total: ' + total + ' €';
    pcart.innerHTML += '<li>' + name + ' ' + price + ' €</li>';
}
// duplication d'affichage

function pshoppingCart() {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize = orders.length;
    pcart.innerHTML = '';
    for (let i = 0; i < cartSize; i++) {
        pcart.innerHTML += '<li>' + orders[i][0] + ' ' + orders[i][1] + ': ' + orders[i][2] + ' €<li>';
    }
    ptotal.innerHTML + 'Total: ' + total + ' €';
}

pshoppingCart();