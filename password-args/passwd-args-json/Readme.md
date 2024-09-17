# passwd-args-json
* This folder has modules and functions which helps in
* Generating a random password 
* Encrypting username and password 
* Storing it in Json file format
* [refer](https://github.com/Srikanthkovuri/Command-Line/blob/main/password-args)
  * to generate a random password
    * password.py [refer](https://github.com/Srikanthkovuri/Command-Line/blob/main/password-args/passwordjson.py)
  * to save it in a text file
    * save.py 
  * to view the generated password
    * save.py [refer](https://github.com/Srikanthkovuri/Command-Line/blob/main/password-args/savejson.py)
* It also has a module which has a python function for
  * argument parsing through CLI
  * commands used for generation and retrieval of specific service assosciated
    * username
    * password
  * To view function for above,
    * passwdManager.py [refer](https://github.com/Srikanthkovuri/Command-Line/blob/main/password-args/passwdManagerjson.py)
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