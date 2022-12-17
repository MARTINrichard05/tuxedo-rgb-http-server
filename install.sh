chown root start_rgb.service
chown root tuxedo_keyboard.py
chown root core.py
cp start_rgb.service /etc/systemd/system
mkdir /etc/rgb_http_server/
cp core.py /etc/rgb_http_server/
cp tuxedo_keyboard.py /etc/rgb_http_server/
systemctl enable start_rgb.service
systemctl start start_rgb.service
