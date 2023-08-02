/*

Create 4 different console logging statements using the following information
    - First name
    - Second name
    - Where you are from
    - And your star sign

*/

let firstName = 'Roberto';
let secondName = 'Nacu';
let place = 'United Kindom';
let starSign = 'Sagittarius';

console.log(firstName);
console.log(secondName);
console.log(place);
console.log(starSign);

// ------------------------------------

/*

Create 2 variables of your favourite car and console.log() so the output looks like
    - My Favourite car is <make> and the model is <model>

*/

let carMake = 'Audi';
let carModel = 'RS 6';

console.log(`My favourite cat is ${carMake} and the model is ${carModel}`);

// ------------------------------------

/*

Create a console.log() with a message which uses the following CSS properties:
    - Text colour to be orange
    - Text to be set to the fantasy font family.
    - Text to be bold
    - Background color to be black
    - Padding around the text to be 10px
*/

let customCSS =
	"color: orange; font-family: 'Fantasy'; font-weight: bold; background-color: black; padding: 10px;";

console.log('This is a message with %c custom CSS', customCSS);
