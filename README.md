# P2PChat

## Interfaces
Here we present a brief discussion about the User interface that the application provides
- Initial Interface
![enter image description here](https://github.com/ChenliangEdward/PNGDump/blob/master/P2PChat/mainWindow.png?raw=true)
### Display
___
![enter image description here](https://github.com/ChenliangEdward/PNGDump/blob/master/P2PChat/mainWindow2.png?raw=true)
- Friend Box
The friend box shows a list of friends, you can select a friend to show the message you have with that friend.

-  Messages Box
The message box shows the messages you have with the selected friend.

### Buttons
___
- **Search and Add**
This button will take the text on the input box above and query the central server to get the corresponding IP address.
- **Sign in**
This button will take the text on the input box above and register them along with the IP address to the central server. 
-  **Refresh**
This will display any new message to the message Box.
- **Send**
This button will send the text in the text input box to the selected friend.

## Internal Design
### User Database
Since each user need to store the conversation on their own, we make the user database as simple as possible. Note that the user column will only be the sender or receiver , and it will always be one of friends. The direction entry will determine whether the message is sent to the friend or from the friend.
![enter image description here](https://github.com/ChenliangEdward/PNGDump/blob/master/P2PChat/UserDB.png?raw=true)
### Programming Logic
- Initialization
Upon initialization, the program will start the PyQt User interface along with a thread that runs the socket service. It will also query the local database to get the friends' information and display them to the Friend list.   
- Send Message
After sending the message, the message will be recorded on the local database and the message box will refresh to display the new copy of chat. 

## Code Refactor & Optimization
Here are some TODO list:
- Dynamically update User IP

- Optimize thread implementation
Since we are implementing our UI with PyQt, it does not support original python threading library well. We will move to Qthread and 





