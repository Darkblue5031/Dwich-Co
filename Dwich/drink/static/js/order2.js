
var nam = document.querySelector("#name");
var price = document.querySelector("#price");
var ptotal = document.querySelector('#total');

function shoppingCart() {
    var orders = JSON.parse(localStorage.getItem('orders')) || [];
    var total = parseFloat(localStorage.getItem('total')) || 0;

    nam.innerHTML = '<h3>Nom</h3>';
    price.innerHTML = '<h3>Prix</h3>';

    for (let i = 0; i < orders.length; i++) {
        button = '<button class="del" onclick="removeBurger(' + i +')">X</button>';
        nam.innerHTML += '<h4>' + orders[i][0] + '</h4>'
        price.innerHTML += '<h4>' + orders[i][1] + ' €' + button + '</h4>'
    }
    ptotal.innerHTML = 'Total: ' + total + ' €';
}

shoppingCart();



function addbiere(burid) {
    var biereId = '#bur' + burid;
    var name = document.querySelector(biereId).innerHTML;
    var radio = 'biere' + burid;
    var price = document.querySelector('input[name="' + radio + '"]:checked').value;

    var orders = JSON.parse(localStorage.getItem('orders')) || [];
    var total = parseFloat(localStorage.getItem('total')) || 0;

    orders.push([name, parseFloat(price)]);
    localStorage.setItem('orders', JSON.stringify(orders));
    total += parseFloat(price);
    localStorage.setItem('total', total);

    var cart = document.querySelector("#cart");
    cart.innerHTML = orders.length;

    pshoppingCart();
}

function addsoft(burid) {
    var softId = '#bur' + burid;
    var name = document.querySelector(softId).innerHTML;
    var radio = 'soft' + burid;
    var price = document.querySelector('input[name="' + radio + '"]:checked').value;

    var orders = JSON.parse(localStorage.getItem('orders')) || [];
    var total = parseFloat(localStorage.getItem('total')) || 0;

    orders.push([name, parseFloat(price)]);
    localStorage.setItem('orders', JSON.stringify(orders));
    total += parseFloat(price);
    localStorage.setItem('total', total);

    var cart = document.querySelector("#cart");
    cart.innerHTML = orders.length;

    pshoppingCart();
}

function addpression(burid) {
    var pressionId = '#bur' + burid;
    var name = document.querySelector(pressionId).innerHTML;
    var radio = 'pression' + burid;
    var price = document.querySelector('input[name="' + radio + '"]:checked').value;

    var orders = JSON.parse(localStorage.getItem('orders')) || [];
    var total = parseFloat(localStorage.getItem('total')) || 0;

    orders.push([name, parseFloat(price)]);
    localStorage.setItem('orders', JSON.stringify(orders));
    total += parseFloat(price);
    localStorage.setItem('total', total);

    var cart = document.querySelector("#pcart");
    pshoppingCart();
}

function pshoppingCart() {
    var orders = JSON.parse(localStorage.getItem('orders')) || [];
    var total = parseFloat(localStorage.getItem('total')) || 0;

    pcart.innerHTML = '';
    for (let i = 0; i < orders.length; i++) {
        button = '<button class="del" onclick="removeBurger(' + i +')">X</button>';
        pcart.innerHTML += '<li>' + orders[i][0] + ' ' + orders[i][1] + ' €' + button + '</li>';
    }
    ptotal.innerHTML = 'Total: ' + total + ' €';
}

function removeBurger(n) {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    total = Number(total) - Number(orders[n][1]);
    orders.splice(n,1);
    var cart = document.querySelector("#cart");
    cart.innerHTML = orders.length;
    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('total', total);
    pshoppingCart();
}

function addcafe(burid) {
    var cafeId = '#bur' + burid;
    var name = document.querySelector(cafeId).innerHTML;
    var radio = 'cafe' + burid;
    var price = document.querySelector('input[name="' + radio + '"]:checked').value;

    var orders = JSON.parse(localStorage.getItem('orders')) || [];
    var total = parseFloat(localStorage.getItem('total')) || 0;

    orders.push([name, parseFloat(price)]);
    localStorage.setItem('orders', JSON.stringify(orders));
    total += parseFloat(price);
    localStorage.setItem('total', total);

    var cart = document.querySelector("#cart");
    cart.innerHTML = orders.length;

    pshoppingCart();
}