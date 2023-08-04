'use strict';

/*

Create a function that takes in 2 parameters num1 and num2 and subtracts the two numbers.

*/

function substraction(num1, num2) {
	return num1 - num2;
}

console.log(substraction(5, 2));

// ------------------------------------

/*

Create a function expression called welcome that take in name, age,gender as a parameters. The outcome should be like so:
    
    e.g. "My name is Felix Cited, i am 20 years old and of gender Male

*/

const welcome = function (name, age, gender) {
	return `My name is ${name}, I am ${age} years old and of gender ${gender}`;
};

console.log(welcome('Roberto', 24, 'male'));
// ------------------------------------

/*

Create an arrow function called powerUp that takes in two values n1 and n2. The arrow function will return the power of the two numbers.

e.g.
    n1=2, n2=3 will return 8 (2 x 2 x 2);
    n1=3, n2=3 will return 27 (3 x 3 x 3);

    hint use Math.pow()

*/

// could be done in one line but I rather keep the return keyword for readability
const powerUp = (n1, n2) => {
	return Math.pow(n1, n2);
};

let n1 = 2;
let n2 = 3;

console.log(`${n1} to the power of ${n2} is: ${powerUp(n1, n2)}`);
