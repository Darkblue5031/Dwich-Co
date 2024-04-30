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

function removeBurger(n) {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    total = Number(total) - Number(orders[n][1]);
    orders.splice(n,1);
    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('total', total);
    shoppingCart();
}

var note = document.querySelector('#message');

function order() {
    var msg = note.value;
    var orders = localStorage.getItem('orders');
    var total = localStorage.getItem('total');

    var url = "/order";
    var orderData = {};
    orderData['orders'] = orders;
    orderData['note'] = msg;
    orderData['total'] = total;
    $.ajax({
        url: url,
        type: "POST",
        data: orderData,
        success: function(data) {
            window.location.replace('success');
            localStorage.setItem('orders', JSON.stringify([]));
            localStorage.setItem('total', 0);
        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.log('An error occurred: ' + textStatus, errorThrown);
        }
    });
}
