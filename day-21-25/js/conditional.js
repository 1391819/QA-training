'use strict';

// What are the return values of the following code?

// let strictA = true;
// let strictB = 1;

// console.log(strictA == strictB); // true - value check
// console.log(strictA === strictB); // false - value and type check

// ------------------------------------

// Considering the following code, what will be the results be?

// let strictA = true;
// let strictB = 1;

// console.log(strictA != strictB); // false
// console.log(strictA !== strictB); // true

// ------------------------------------

/*

Create a IF statement that satifies the following:
	- Declare a variable age
	- Write a condition that checks if age is between 18 AND 65
	- Return a value in each case where the condition is satisfied and not satisfied.
	- Extra: Consider the case where age is less than 18 - return 'underage'.

*/

// let age = 64;

// // can be done with ifs, but I think it looks better this way
// // simple explanation:
// // 		true just to avoid strict equality === between arg and cases
// // 		if we pass age, we'd never go inside the cases since they are either true or false
// switch (true) {
// 	case age >= 18 && age <= 65:
// 		console.log('Age is between 18 and 65');
// 		break;
// 	case age < 18:
// 		console.log('Underage');
// 		break;
// 	default:
// 		console.log('Age is not between 18 and 65');
// 		break;
// }

// ------------------------------------

/*

Using ternary-if syntax, write code that checks if age is above 50.

*/

// let age = 51;

// let olderThan50 = age > 50 ? true : false;

// if (olderThan50) {
// 	console.log('Age older than 50');
// } else {
// 	console.log('Younger or equal to 50');
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
	case 0:
		console.log('Monday');
	case 1:
	case 2:
	case 3:
	case 4:
		console.log('Can be any day, Tuesday to Friday');
		break;
	case 5:
		console.log('Saturday');
		break;
	case 6:
		console.log('Sunday');
		break;
	default:
		console.log('Invalid day');
		break;
}

// ------------------------------------
