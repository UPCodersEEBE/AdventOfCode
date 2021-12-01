use std::fs;
use std::io;
use std::io::BufRead;
use std::io::BufReader;

fn main() -> io::Result<()> {
    let filename = "src/input.dat";
    let lines = file_to_vec(filename.to_string())?;

    let mut result = 0;
    for i in 0..lines.len() - 3 {
        let is_higher = lines[i] < lines[i + 3];
        let increment: i32 = is_higher.into();
        result += increment;
    }
    println!("Result: {}", result);

    Ok(())
}

fn file_to_vec(filename: String) -> io::Result<Vec<i32>> {
    let file_in = fs::File::open(filename)?;
    let file_reader = BufReader::new(file_in);
    Ok(file_reader
        .lines()
        .filter_map(io::Result::ok)
        .map(|s| s.parse().unwrap())
        .collect())
}
