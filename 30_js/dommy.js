/* Phase III */
/* Helper Functions:
 
   changeHeading to change the HTML of the header
   changeBack to change the HTML of the header back to its default of "Hello World!"
   removeItem to remove elements-- it accesses the parentNode and then removes the child (itself)

*/

var changeHeading = function(e) {
    var h = document.getElementById("h")
    h.innerHTML = e
};
var changeBack=function(e){
    var h=document.getElementById("h")
    h.innerHTML="Hello World!"
}

var removeItem = function(e) {
    var toRemove = e.target;
    toRemove.parentNode.removeChild(toRemove);
};

/* Giving each list item the mouseover, mouseout, and click features */

var lis = document.getElementsByTagName("li");
for(var i=0; i < lis.length; i++) {
    lis[i].addEventListener('mouseover', function(e){ changeHeading(this.innerHTML);});
    lis[i].addEventListener('mouseout', changeBack);
    lis[i].addEventListener('click', removeItem);
};


var addItem=function(e){
    var list=document.getElementById("thelist");
    var item=document.createElement("li");
    item.innerHTML="CHEESE";
    item.addEventListener('lick',removeItem);
    item.addEventListener('mouseover',function(e){changeHeading(this.innerHTML);});
    item.addEventListener('mouseout',changeBack);
    list.appendChild(item);
}
var button=document.getElementById("b");
button.addEventListener('click',addItem);

var fibonacci = function (n)
{
    if (n < 2)
        return 1;
    return fibonacci(n - 1) + fibonacci(n - 2);
};

var addFib=function(e){
    var index=0;
    console.log(e);
    var list=document.getElementById("fliblist");
    var item=document.createElement("li");
    var item.innerHTML=fibonacci(index);
    list.appendChild(item);
    index++;
};
    


var fb=document.getElementById("fb");
fb.addEventListener("click",addFib);
