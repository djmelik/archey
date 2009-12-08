#!/usr/bin/env python

# Import libraries.
import subprocess
from subprocess import Popen, PIPE

# Define colors.
# Uncomment whatever color scheme you prefer.
clear = '\x1b[0m' # clear [Do NOT comment out]

# color = '\x1b[1;30m' # black
# color2 = '\x1b[0;30m' # black

# color = '\x1b[1;31m' # red 
# color2 = '\x1b[0;30m' # red

# color = '\x1b[1;32m' # green
# color2 = '\x1b[0;32m' # green

# color = '\x1b[1;33m' # yellow
# color2 = '\x1b[0;33m' # yellow

color = '\x1b[1;34m' # blue [Default]
color2 = '\x1b[0;34m' # blue [Default]

# color = '\x1b[1;35m' # magenta
# color2 = '\x1b[0;35m' # magenta

# color = '\x1b[1;36m' # cyan
# color2 = '\x1b[0;36m' # cyan

# color = '\x1b[1;37m' # white
# color2 = '\x1b[0;37m' # white

# Define arrays containing values.
list = []

# Screenshot
# Set to 'True' to enable screenshot.
screen = 'False'
def screenshot():
	subprocess.check_call(["scrot", "-cd5"])

# Find running processes.
p1 = Popen(['ps', '-A'], stdout=PIPE).communicate()[0].split('\n')
processes = [process.split()[3] for process in p1 if process]
p1 = None

# Print coloured key with normal value.
def output(key, value):
	output = '%s%s:%s %s' % (color, key, clear, value)
	list.append(output)

# Define operating system.
def os_display(): 
	arch = Popen(['uname', '-m'], stdout=PIPE).communicate()[0].rstrip('\n')
	os = 'Arch Linux %s' % (arch)
	output('OS', os)

# Define kernel.
def kernel_display():
	kernel = Popen(['uname', '-r'], stdout=PIPE).communicate()[0].rstrip('\n')
	output ('Kernel', kernel)

# Define uptime.
def uptime_display():
	p1 = Popen(['uptime'], stdout=PIPE).communicate()[0].lstrip().split(' ')
	uptime = ' '.join(p1[2:(p1.index(''))]).rstrip(',')
	output ('Uptime', uptime)

# Define battery. [Requires: acpi]
def battery_display(): 
	p1 = Popen(['acpi'], stdout=PIPE).communicate()[0].lstrip()
	battery = p1.split(' ')[3].rstrip('\n')
	output ('Battery', battery)

# Define desktop environment. 
def de_display():
	dict = {'gnome-session': 'GNOME',
		'ksmserver': 'KDE',
		'xfce-mcs-manager': 'Xfce'}
	de = 'None found'
	for key in dict.keys():
		if key in processes: de = dict[key]
	output ('DE', de)

# Define window manager.
def wm_display():
        dict = {'awesome': 'Awesome',
		'beryl': 'Beryl',
		'blackbox': 'Blackbox',
		'dwm': 'DWM',
		'enlightenment': 'Enlightenment',
                'fluxbox': 'Fluxbox',
		'fvwm': 'FVWM',
		'icewm': 'icewm',
		'kwin': 'kwin',
		'metacity': 'Metacity',
                'openbox': 'Openbox',
		'wmaker': 'Window Maker',
		'xfwm4': 'Xfwm',
		'xmonad': 'Xmonad'}  
        wm = 'None found'
        for key in dict.keys():
		if key in processes: wm = dict[key]
        output ('WM', wm)

# Define number of packages installed.
def packages_display():
	p1 = Popen(['pacman', '-Q'], stdout=PIPE)
	p2 = Popen(['wc', '-l'], stdin=p1.stdout, stdout=PIPE)
	packages = p2.communicate()[0].rstrip('\n')
	output ('Packages', packages)

# Define file system information. 
def fs_display(mount=''):
	p1 = Popen(['df', '-Th',  mount], stdout=PIPE).communicate()[0]
	part = [line for line in p1.split('\n') if line][1]
	part = part.split()[3]
	if mount == '/': mount = '/root'
	fs = mount.rpartition('/')[2].title()
   	output (fs, part)

# Values to display.
## Possible Options [Enabled by default]: 'os', 'kernel', 'uptime', 'de', 'wm', 'packages', 'fs:/'
## Possible Options [Disabled by default]: 'battery', 'fs:/MOUNT/POINT'
display = [ 'os', 'kernel', 'uptime', 'de', 'wm', 'packages', 'fs:/', 'fs:/home' ]

# Run functions found in 'display' array.
for x in display:
	call = [arg for arg in x.split(':') if arg]
	funcname=call[0] + "_display"
	func=locals()[funcname]
	if len(call) > 1:
		func(arg)
	else:
		func()

# Fill 'list' array with with blank keys. [Do NOT remove]
list.extend(['']*(13 - len(display)))

# Result.
print """%s
%s               +                
%s               #                
%s              ###               %s
%s             #####              %s
%s             ######             %s
%s            ; #####;            %s
%s           +##.#####            %s
%s          +##########           %s
%s         ######%s#####%s##;         %s
%s        ###%s############%s+        %s
%s       #%s######   #######        %s
%s     .######;     ;###;`\".      %s
%s    .#######;     ;#####.       %s
%s    #########.   .########`     %s
%s   ######'           '######    %s
%s  ;####                 ####;   
%s  ##'                     '##   
%s #'                         `#  %s                          
""" % (color, color, color, color, list[0], color, list[1], color, list[2], color, list[3], color, list[4], color, list[5], color, color2, color, list[6], color, color2, color, list[7], color, color2, list[8], color2, list[9], color2, list[10], color2, list[11], color2, list[12], color2, color2, color2, clear)

if screen == 'True': 
	screenshot()
else:
	quit
