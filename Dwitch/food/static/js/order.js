var pcart = document.querySelector('#pcart');
var ptotal = document.querySelector('#ptotal');

function addBurger(burid) {
    var burgerId = '#bur' + burid;
    var name = document.querySelector(burgerId).innerHTML;
    var radio = 'burger' + burid;
    var price = document.querySelector('input[name="' + radio + '"]:checked').value;

    pcart.innerHTML += '<li>' + name + ' ' + price + ' €</li>';

    var orders = JSON.parse(localStorage.getItem('orders')) || [];
    var total = parseFloat(localStorage.getItem('total')) || 0;

    orders.push([name, parseFloat(price)]);
    localStorage.setItem('orders', JSON.stringify(orders));
    total += parseFloat(price);
    localStorage.setItem('total', total);

    var cart = document.querySelector("#cart");
    cart.innerHTML = orders.length;

    ptotal.innerHTML = 'Total: ' + total + ' €';
}

function pshoppingCart() {
    var orders = JSON.parse(localStorage.getItem('orders')) || [];
    var total = parseFloat(localStorage.getItem('total')) || 0;
    var cartSize = orders.length;

    pcart.innerHTML = '';
    for (let i = 0; i < cartSize; i++) {
        pcart.innerHTML += '<li>' + orders[i][0] + ' ' + orders[i][1] + ' €</li>';
    }
    ptotal.innerHTML = 'Total: ' + total + ' €';
}

pshoppingCart();
