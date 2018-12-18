var fibonacci = function (n)
{
    if (n <= 1)
        return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

var gcd = function (a, b)
{
    var i;
    for (i = a; i > 1; i--)
    {
        if (a % i == 0 && b % i == 0)
        {
            return i;
        }
    }
}

var randomInt=function(max)
{
    var index=Math.floor(Math.random()*max);
    return index
}
    
var randomStudent = function ()
{
    return students[randomInt(students.length)];
}
