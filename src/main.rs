use std::error::Error;
use std::io;
use std::process::Command;

fn main() -> Result<(), Box<dyn Error>> {
    let command_to_check = "nu"; // Replace this with the command you want to check
    if command_exists(command_to_check) {
        println!("The command '{}' exists.", command_to_check);
    } else {
        println!("The command '{}' does not exist.", command_to_check);
    };

    Ok(())
}

fn command_exists(cmd: &str) -> bool {
    let mut which_command = Command::new("which");
    which_command.arg(cmd);
    match which_command.output()
    {
        Ok(output) => output.status.success(),
        Err(error) => panic!("Error running `{:?}`: {:?}", which_command, error),
    }
}
