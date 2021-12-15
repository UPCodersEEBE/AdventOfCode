import fs from "fs";

let fileArray = fs.readFileSync("input.dat").toString().split("\n");

let polymer_template = fileArray[0];
const pairs: Array<string> = fileArray.slice(2, -1);

const insertStep = (text: string): string => {
  const max = text.length;
  const pairs_to_enter: Array<{ index: number; letter: string }> = [];
  for (let i = max; i > 1; i--) {
    pairs.forEach((pair) => {
      text.slice(i - 2, i) === pair.slice(0, 2) &&
        pairs_to_enter.push({ index: i, letter: pair.slice(-1) });
    });
  }

  pairs_to_enter.forEach((el) => {
    text = text.substr(0, el.index - 1) + el.letter + text.substr(el.index - 1);
  });

  return text;
};

polymer_template = insertStep(polymer_template);

for (let i = 0; i < 9; i++) {
  polymer_template = insertStep(polymer_template);
}
const letters: string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

let maxVal = 0;
let minVal = polymer_template.length;
let tot = 0;
for (let i = 0; i < letters.length; i++) {
  const count = polymer_template.split(letters[i]).length - 1;
  tot += count;
  maxVal = Math.max(maxVal, count);
  minVal = count === 0 ? minVal : Math.min(minVal, count);
}

console.log(`Result: ${maxVal - minVal}`);
