import sysconfig
print(sysconfig.get_paths()["include"])
print(sysconfig.get_config_var("LIBDIR"))
