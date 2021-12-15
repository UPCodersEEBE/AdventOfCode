let fs = require("fs");

const inputArray = fs.readFileSync("input.dat").toString().split("\n");

let lines = [];
inputArray.forEach((line) => {
  line = line
    .split(" -> ")
    .join(",")
    .split(",")
    .map((n) => parseInt(n));

  accepted = line[0] === line[2] || line[1] === line[3];
  accepted && lines.push(line);
});

let counts = {};
lines.forEach((line) => {
  const minX = Math.min(line[0], line[2]);
  const maxX = Math.max(line[0], line[2]);
  const minY = Math.min(line[1], line[3]);
  const maxY = Math.max(line[1], line[3]);
  for (let x = minX; x <= maxX; x++) {
    for (let y = minY; y <= maxY; y++) {
      const key = `${x}:${y}`;
      counts[key] = counts[key] ? counts[key] + 1 : 1;
    }
  }
});

const result = Object.values(counts).filter((e) => e > 1);
console.log(result.length);
