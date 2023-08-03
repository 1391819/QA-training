// Finding JavaScript types

let a;
let b = '12345';
let c = 12345;
let d = true;
let e = { a: 'JavaScript' };

console.log(typeof a);
console.log(typeof b);
console.log(typeof c);
console.log(typeof d);
console.log(typeof e);
console.log(typeof e.a);

// ------------------------------------

// Using template literals to dynamically change the sentence

let totalMoney = 4000;
let moneyPaidSoFar = 2348;
let totalLeftToPay = totalMoney - moneyPaidSoFar;

let result = `The total bill is ${totalMoney} the remaining amount of money to be paid is ${totalLeftToPay}`;

console.log(result);
