var fibonacci = function (n)
{
    if (n <= 1)
        return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
};
var fibButton = document.getElementById("fib");
var itemChange= document.getElementById("thelist");

var display = function (toDisplay)
{
    console.log(toDisplay);
    results.innerHTML = toDisplay;
};

var header= document.getElementById("h");
var changeHeader=function(newHeader)
{
    header.innerHTML=newHeader;
}
var listElement=document.getElementsByTagName("li");


itemChange.addEventListener('mouseover', function(e) {changeHeader(listElement.getAttribute(innerHTML));})
itemChange.addEventListener('mouseout',function(e){changeHeader('Hello World');})
fibButton.addEventListener('mouseout', function (click) {console.log(click);})
