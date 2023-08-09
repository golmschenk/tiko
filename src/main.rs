use std::error::Error;
use std::process::Command;

fn main() -> Result<(), Box<dyn Error>> {
    handle_nu();

    Ok(())
}

fn handle_nu() {
    let nu_command_string = "nu";
    if command_exists(nu_command_string) {
        println!("`{}` found.", nu_command_string);
    } else {
        println!("`{}` not found. Installing...", nu_command_string);
        install_nu();
        println!("Finished installing `{}`.", nu_command_string);
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
            false => {
                println!(
                    "Exit status of `{:?}` was unexpectedly false.\n\
                     The output of the command was:\n{:?}",
                    nu_install_command, nu_install_command.output().unwrap()
                );
                panic!()
            }
        },
        Err(error) => {
            println!(
                "Error running `{:?}`: `{:?}`.\n\
                 The output of the command was:\n{:?}",
                nu_install_command, error, nu_install_command.output().unwrap());
            panic!()
        }
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
