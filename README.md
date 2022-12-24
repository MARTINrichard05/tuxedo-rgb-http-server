# tuxedo rgb http server
the code is not clean but it works \
i have an aura 15 gen 2\
it is optimised and can run in the background without any performance impact\
if you want to use it just mention me
## the goal
to control your tuxedo keyboard backlight by sending local http request, allows you to do way more than just a fixed color
## installation
just run `sudo ./install.sh` 
it will change the files's owner to prevent access from non admin user.
## usage
just send http get request on the port 6670 that looks like that (rgb 0-255) : \
`http://127.0.0.1:6670/[r,g,b]`

## usage in another project 
if you want to use this code or a part (like the lib) , just mention me in the credits

## credits
- me :)
- tuxedo (they wrote the driver for interacting with the keyboard by writing in a file)
