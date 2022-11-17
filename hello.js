const timeout = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

async function show_letter() {
  let input_string = "Hello World";
  let output_string = "";
  let letters = "abcdefghijklmnopqrstuvwxyz";

  for (let i = 0; i < input_string.length; i++) {
    const char = input_string[i];
    let iterator = letters.indexOf(char.toLowerCase());
    for (let j = 0; j <= iterator; j++) {
      const letter = letters[j];
      console.log(output_string + letter);
      await timeout(100);
    }
    output_string += char;
  }
}

show_letter();