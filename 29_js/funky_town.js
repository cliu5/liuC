var fibonacci = function (n)
{
    if (n <= 1)
        return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
};

var gcd = function (a, b)
{
    var i;
    for (i = Math.min(a, b); i > 1; i--)
    {
        if (a % i == 0 && b % i == 0)
        {
            return i;
        }
    }
};

var randomInt = function(max)
{
    var index = Math.floor(Math.random() * max);
    return index
};
    
var students = ["claire", "brian", "oliver"];

var randomStudent = function ()
{
    return students[randomInt(students.length)];
};

var fibButton = document.getElementById("fib");
var gcdButton = document.getElementById("gcd");
var randStuButton = document.getElementById("randStu");
var results = document.getElementById("result");

var display = function (toDisplay)
{
    console.log(toDisplay);
    results.innerHTML = toDisplay;
};

fibButton.addEventListener('click', function () {display(fibonacci(10))});
gcdButton.addEventListener('click', function () {display(gcd(21, 14))});
randStuButton.addEventListener('click', function () {display(randomStudent())});
