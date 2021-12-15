let fs = require("fs");

const inputArray = fs.readFileSync("input.dat").toString().split("\n");

let lines = [];
inputArray.forEach((line) => {
  line = line
    .split(" -> ")
    .join(",")
    .split(",")
    .map((n) => parseInt(n));

  lines.push(line);
});

let counts = {};

const addDiagonal = (line) => {
  const xUphill = line[0] < line[2];
  const yUphill = line[1] < line[3];
  const xStart = line[0];
  const yStart = line[1];

  for (let i = 0; i <= Math.abs(line[2] - line[0]); i++) {
    let key = `${xStart + i * xUphill - i * !xUphill}:${
      yStart + i * yUphill - i * !yUphill
    }`;
    counts[key] = counts[key] ? counts[key] + 1 : 1;
  }
};

const addVerticalOrHorizontal = (line) => {
  const minX = Math.min(line[0], line[2]);
  const maxX = Math.max(line[0], line[2]);
  const minY = Math.min(line[1], line[3]);
  const maxY = Math.max(line[1], line[3]);

  for (let x = minX; x <= maxX; x++) {
    for (let y = minY; y <= maxY; y++) {
      counts[`${x}:${y}`] = counts[`${x}:${y}`] ? counts[`${x}:${y}`] + 1 : 1;
    }
  }
};

lines.forEach((line) => {
  const isDiagonal = !(line[0] === line[2] || line[1] === line[3]);
  isDiagonal ? addDiagonal(line) : addVerticalOrHorizontal(line);
});

const result = Object.values(counts).filter((e) => e > 1);

console.log(result.length);
