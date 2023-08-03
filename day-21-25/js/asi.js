/*

Declare a few variables / code blocks and terminate the code appropriately.

Remove the semi-colons from the variables / code-blocks that you've written and see if there is an affect on the output.

*/

let a = 'Hello';
let b = 123213;

console.log(a);
console.log(b);

// this will put a ; at the end of a -> not what we want
// let a // missing "," after a
// b
// = 3;

// ------------------------------------

/*

Have a look at the below code and try to spot where there might be an error:

*/

function sayHello() {
	return; // ASI put a ; here -> not what we want, return value altered
	{
		('Someone says hello');
	}
}

// correct version
function sayHello() {
	return 'Someone says hello';
}

console.log(sayHello());
