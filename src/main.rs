use std::error::Error;
use std::process::Command;

fn main() -> Result<(), Box<dyn Error>> {
    handle_nu();

    Ok(())
}

fn handle_nu() {
    let nu_command_string = "nu";
    if command_exists(nu_command_string) {
        println!("The command '{}' exists.", nu_command_string);
    } else {
        println!("The command '{}' does not exist.", nu_command_string);
        install_nu();
    };
}

fn install_nu() {
    let mut nu_install_command = Command::new("cargo");
    nu_install_command.arg("install");
    nu_install_command.arg("nu");
    nu_install_command.arg("--features=dataframe");
    match nu_install_command.output()
    {
        Ok(output) => match output.status.success() {
            true => (),
            false => panic!("Exit status of `{:?}` was unexpectedly false.", nu_install_command)
        },
        Err(error) => panic!("Error running `{:?}`: `{:?}`.", nu_install_command, error),
    }
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
