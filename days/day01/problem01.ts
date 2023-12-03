import { readFileSync } from "fs";

const input: string[][] = readFileSync("./problem01_input.txt", "utf8").split("\n").map(cv => Array.from(cv));

let result: number = 0;

input.forEach(cv => {
	const f = cv.find(x => Number(x)) ?? "";
	const l = cv.findLast(x => Number(x)) ?? "";

	result += Number(f +l);
});


console.log(result);
