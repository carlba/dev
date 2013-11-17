import os


def get_env_variable(env_var_name):
    if os.environ.get(env_var_name):
        return os.environ[env_var_name]

if __name__ == '__main__':
    print get_env_variable("PATH")
    print get_env_variable("prutt")

if __name__ == '__main__':
    main()