import { readFileSync } from "fs";

const input: string[][] = readFileSync("./problem01_input.txt", "utf8").split("\n").map(cv => Array.from(cv));
const cvs: number[] = [];

input.forEach(cv => {
	const h: string[] = [];
	for(let i = 0; i < cv.length; i++) {
		if (Number(cv[i])) {
			h.push(cv[i]);
			break;
		}
	}
	for(let i = cv.length-1; i >= 0; i--) {
		if (Number(cv[i])) {
			h.push(cv[i]);
			break;
		}
	}
	cvs.push(Number(h.join("")));
});

const result = cvs.reduce((a,b) => a + b, 0);

console.log(result);
