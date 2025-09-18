"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
/* let nome declara uma nova variavel */
let nome = 'Yuri';
let matricula = 20251148060034;
console.log(nome);
console.log(matricula);
//imprimir uma frase
console.log(nome + ' possui a matricula ' + matricula);
console.log(`${nome} posssui a matricula ${matricula}`);
/* Declare as notas de 2 bimestres de um estudante,
faça o calculo e imprima o resultado da média.

Formula para o calculo da media:
(notaBim1 * 2 + notaBim2 * 3) / 5
*/
const read = require('readline-sync');
let b1 = +read.question('Bin1 ');
let b2 = +read.question('Bin2 ');
let media = ((b1 + b2 * 3) / 5);
console.log(`Media = ${media}`);
if (media >= 60) {
    console.log('Aprovado(a)');
}
else {
    console.log('Avaliação final');
}
