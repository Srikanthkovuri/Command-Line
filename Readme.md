# Command Line Interface(CLI)
### hello.py
* Here, I am trying to talk with machine using
    * python interpeter
    * CLI
* 'hello.py'-> module will print **Hey! argument-you-entered** in cli
* This will print the last argument.so,
    * better to use one argument  
* now, run the following command in cli
  > **python module-name argument**
  * In this case,
  ```bash
  python hello.py Srikanth 
  ```
### numeric.py
* 'nueric.py'-> module will print **factorial-of-given-arg** in cli
* This will print the fatorial of last argument.so,
    * better to use one argument  
* now, run the following command in cli
  > **python module-name argument**
  * In this case,
  ```bash
  python numeric.py 5 
  ```
## password-args
* This folder has a sample python function 
  * to generate a random password
    * password.py 
  * to save it in a text file
    * save.py 
  * to view the generated password
    * save.py
* It also has a module which has a python function for
  * argument parsing through CLI
  * commands used for generation and retrieval of specific service assosciated
    * username
    * password
  * To view function for above,
    * passwdManager.py  
* To generate a password using cli,run below command
  ```bash
  python passwdManager.py generate -l 16 -s Gmail -u srikanth
  ```
  * generate -> subcommand
  * Here, -l -> length
  * -s -> service name
  * -u -> username
  * passwdManager.py -> module which has main function
* After successful execution of above command, we will be able to see
  * service name
  * username
  * password in a text file
* Now, to a retrieve generated password,type as below
  ```bash
  python passwdManager.py retrieve -s Gmail 
  ```
* Upon successful execution, we will be able to see
  * username
  * password 



