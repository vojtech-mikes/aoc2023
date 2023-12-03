import { readFileSync } from "fs";

const input: string[] = readFileSync("input.txt", "utf8").split("\n");

input.pop();
function getGameId(s: string): number {
	const id = s?.split(":")[0].match(/\d/g)?.join("");
	return Number(id);
}

function getCubes(s: string): {r: number, g: number, b: number} {
	let cubes: {r: number, g: number, b: number} = {r:0, g: 0, b: 0};
	const rawGame = s.split(":")[1].split(";");
	rawGame.forEach(gameSets => {
		const spltGameSet = gameSets.split(", ");
		spltGameSet.forEach(gameSet => {
			const [x, color] = gameSet.trimStart().split(" ");
			const n = Number.parseInt(x);
			switch (color) {
				case "red":
					cubes.r = n > cubes.r ? n : cubes.r;
				break;
				case "blue":
					cubes.b = n > cubes.b ? n : cubes.b;
				break;
				case "green":
					cubes.g = n > cubes.g ? n : cubes.g;
				break;
			}
		});
	});
	return cubes;
}

let count: number = 0;

const RED_LIMIT = 12;
const GREEN_LIMIT = 13;
const BLUE_LIMIT = 14;

input.forEach(game => {
	const gameId = getGameId(game);
	const cubes = getCubes(game);
	if (cubes.r <= RED_LIMIT && cubes.b <= BLUE_LIMIT &&  cubes.g <= GREEN_LIMIT) {
		count += gameId;
	}
});

console.log(count);
