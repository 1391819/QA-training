'use strict';

// Ex 1

// using a for loop
// for (let a = 100; a <= 200; a++) {
// 	console.log(`a = ${a}`);
// }

// using a while loop
// let a = 100;
// while (a <= 200) {
// 	a++;
// 	console.log(`a = ${a}`);
// }

// ------------------------------------

// Ex 2

// using a for loop
// for (let a = 100; a <= 200; a++) {
// 	if (a % 2 == 0) {
// 		console.log('-');
// 	} else {
// 		console.log('*');
// 	}
// }

// using a while loop
// let a = 100;
// while (a <= 200) {
// 	if (a % 2 == 0) {
// 		console.log('-');
// 	} else {
// 		console.log('*');
// 	}
// 	a++;
// }

// ------------------------------------

// Ex 3

// for (let j = 1; j < 11; j++) {
// 	for (let k = 0; k < 10; k++) {
// 		console.log(j);
// 	}
// }

// ------------------------------------

/*

Write a switch case statement which uses the current day as its expression and matches with the relevant case. 

Criteria:
    - Omit a break statement if it is a weekday, until the last day
    - Use a default case to handle an invalid range.

*/

let day = new Date().getDay();
// console.log(day); // debug

switch (day) {
	case 1:
		console.log('Monday');
	case 2:
	case 3:
	case 4:
	case 5:
		console.log('Friday');
		break;
	case 6:
		console.log('Saturday');
		break;
	case 7:
		console.log('Sunday');
		break;
	default:
		console.log('Invalid day');
		break;
}

// ------------------------------------
