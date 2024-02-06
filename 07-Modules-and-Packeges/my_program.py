from modules_and_packages import my_func
from my_main_package import some_main_script # This is how you import a module
from my_main_package.sub_package import my_sub_script # This is how you import a sub-package

my_func()

some_main_script.report_main() # This is how you call a function from a module
my_sub_script.sub_report() # This is how you call a function from a sub-package
