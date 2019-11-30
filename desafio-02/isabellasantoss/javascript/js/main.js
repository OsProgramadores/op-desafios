function clicou(){

var maximo = 10000;
for (var i = 2; i <= maximo; i++) {
    var primo = true;
    for (var j = 2; j <= i; j++) {
        if (((i % j) == 0) && (j != i)) {
            primo = false;
        }
    }

    if (primo) {
        document.write(i + "<br>" );

    }
}

}