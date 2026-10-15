import socket, os

socket1 = socket.socket()
print(socket.__dict__["socket"].__dict__)#<class 'socket.socket'>
print(socket1.fileno())
# open(socket1.fileno() )#OSError: [WinError 6] The handle is invalid


# fd =12345
# # On Unix, receiving an fd (e.g., from another process) as integer `fd`
# sock = socket.socket(fileno=fd)  # wrap it
# # or duplicate it:
# sock = socket.fromfd(fd, socket.AF_INET, socket.SOCK_STREAM)

# # To get a file-like object for a socket:
# f = sock.makefile('rb')

# # On Unix, this might work but is wrong for sockets:
# f = open(fd, 'rb')  # may work, but socket ops like seek fail
# f = sock.makefile('rb')   # returns a buffered file object
