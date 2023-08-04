'use strict';

/*

1. Create an object called darthVader with the keys allegiance, weapon and sith and the values of empire, lightsabre and true. 
2. Finally log darthVader

*/

let darthVader = {
	allegiance: 'empire',
	weapon: 'lightsabre',
	sith: true,
};

console.log(darthVader);

// ------------------------------------

/*

Create the following log statements using the darthVader Object
    - Darth Vader's allegiance is to the Empire;
    - Darth Vader's weapon of choice is a lightsabre;
    - Darth Vader is a sith? true;
    - Darth Vader is a Jedi? false;

*/

console.log(`Darth Vader's allegiance is to the ${darthVader.allegiance}`);
console.log(`Darth Vader's weapon of choice is a ${darthVader.weapon}`);
console.log(`Darth Vader' is a sith? ${darthVader.sith}`);
console.log(`Darth Vader is a Jedi? ${darthVader.sith ? 'false' : 'true'}`);
console.log(`Darth Vader is a Jedi? ${!darthVader.sith}`);
// ------------------------------------

/*

Create an array with the name myArray with 2 elements hello, everyone..
    - Next print the length of the array
    - Next use the push() method to add 3 elements to the array
    - Next print the length of the array
    - Next use shift() to remove an element
    - Finally print the contents of the array using a for of loop.

*/

let myArray = ['hello', 'everyone'];

console.log(`Length of the array is ${myArray.length}`);

myArray.push('my', 'name', 'is');

console.log(`Length of the array is ${myArray.length}`);

myArray.shift();

for (let element of myArray) {
	console.log(element);
}
