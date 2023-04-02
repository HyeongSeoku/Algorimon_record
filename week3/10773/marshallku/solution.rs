use std::io::stdin;

fn main() {
    let mut line = String::new();

    stdin().read_line(&mut line).unwrap();

    let max: usize = line.split_whitespace().collect::<Vec<&str>>()[0].parse().unwrap();
    let mut stack: Vec<usize> = vec![];
    

    for _ in 0..max {
        line = String::new();
        stdin().read_line(&mut line).unwrap();
        let value: usize = line.split_whitespace().collect::<Vec<&str>>()[0].parse().unwrap();

        if value == 0 {
            stack.remove(stack.len() - 1);
        } else {
            stack.push(value);
        }
    }

    let mut result = 0;

    for i in stack {
        result += i;
    }

    print!("{}", result);
}