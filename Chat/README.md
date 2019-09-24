# Simple Chat Room

To run, first setup the server:

	1.) Find your public IP for wireless LAN adapter WiFi
		a.) On Windows, open cmd window
		b.) Type "ipconfig /all"
		c.) Scroll to "Wireless LAN adapter WiFi"
		d.) Find the field "IPv4 Address"
		e.) Copy this IP
	2.) Paste the IP in the server.py code where it says "Your IP here" and uncomment the line
		a.) This is interpreted as a String so leave the quotes on the IP!
		b.) Feel free to change the port number (number after the IP)

Next run the client on other machines (won't work if hosting server and client on same machine):
	
	1.) Use same IP from server.py to paste into client.py where stated and uncomment the line
	    a.) If you changed the port number in server, be sure to use that same port in client
	2.) If server is running from another machine, run client.py with up to 5 seperate people in chatroom
		a.) If you want more people in chat, change "s.listen(5)" to the number of connections you want to accept in server.py
	