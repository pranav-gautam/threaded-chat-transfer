# threaded-chat-transfer
In this project I created a program which can connect with another thread, and can be used to transfer messages and/or files.

First, it creates a new thread – let’s call it the writing thread. This thread takes a port number from the keyboard and then connects to that port number. After the connection (socket) is successfully established, it goes into a loop of reading a message from the keyboard and writing the message to the connection (socket). If the message is ”transfer filename”, after the message is written, the file is transmitted through the connection.

<img width="959" alt="Screenshot (37)" src="https://github.com/pranav-gautam/sample/assets/64377125/ace3febe-a975-4011-8cf7-aa3ae337fef8">

Next, it creates a ServerSocket, prints out the port number used, and listens on the socket for new connection (i.e. the accept method). When a new connection from another user arrives, the connection Socket is established. The main thread will become the so-called reading thread by listening to the connection socket. This thread attempts to read messages from the connection socket and prints the messages on the screen. If the message is “transfer filename”, it reads the file and stores locally.
