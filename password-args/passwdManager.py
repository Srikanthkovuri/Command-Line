"""This module has command line interaction function
"""
from argparse import ArgumentParser
from password import password_gen
from save import save_pass,view_pass

def command_line_inter():
    """This function describes argspasser
    """
    global_parser=ArgumentParser(prog='passwdManager')
    sub_parser=global_parser.add_subparsers(dest='command')
    # adding subcommand i.e generate
    arg_parser=sub_parser.add_parser("generate",help="generate a pssword using cli")
    # adding arguments
    arg_parser.add_argument(
        '-l',
        '--length',
        default=8,
        help="length should be minimum 8 characters"
    )
    arg_parser.add_argument(
        '-d',
        '--digits',
        action="store_true",
        help="minimum single Digit should be included"
    )
    arg_parser.add_argument(
        '-c',
        '--special-characters',
        action="store_true",
        help="minmium single special character should be included"
    )
    arg_parser.add_argument(
        '-u',
        '--username',
        help="for to enter a username"
    )
    arg_parser.add_argument(
        '-s',
        '--service',
        help="To enter a service name"
    )
    arg_parser.add_argument(
        '-p',
        '--password',
        help="To enter a password"
    )
    # adding subcommand i.e retrieve
    retrive_arg=sub_parser.add_parser("retrieve",help="retrieve password")
    retrive_arg.add_argument(
        '-s',
        '--service',
        help="retrieve specific password"
    )
    return global_parser.parse_args()  

def main():
    """Main function
    """
    arg_obj=command_line_inter()
    if arg_obj.command == 'generate':
        #calling function
        password=password_gen(
            length=arg_obj.length,
            digits=arg_obj.digits,
            special_char=arg_obj.special_characters
        )
        save_pass(
            service=arg_obj.service,
            username=arg_obj.username,
            password=password
        )
        print("your password was successfully saved!,use 'retrive' command to fetch")
    elif arg_obj.command == 'retrieve':
        username,password=view_pass(
            ser_name=arg_obj.service)
        print(f"username:{username}")
        print(f"password:{password}")

if __name__ == "__main__":
    main()





    
