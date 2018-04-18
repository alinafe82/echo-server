import socket
import sys
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s: %(message)s',
                    )


def client(msg, log_buffer=sys.stderr):
    logger = logging.getLogger('Echo_Client')
    logger.debug('client')
    # TODO: Replace the following line with your code which will instantiate
    #       a TCP socket with IPv4 Addressing, call the socket you make 'sock'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # can also be sock = socket.socket()
    # socket represents a socket, belongs to OS needs to be closed gracefully
    server_address = ('localhost', 10000)
    print('connecting to {0} port {1}'.format(*server_address), file=log_buffer)
    # TODO: connect your socket to the server here.

    sock.connect(server_address)
    # you can use this variable to accumulate the entire message received back
    # from the server
    received_message = '    '

    # this try/finally block exists purely to allow us to close the socket
    # when we are finished with it
    try:
        print('sending "{0}"'.format(msg), file=log_buffer)
        # TODO: send your message to the server here.
        #print('sending {!r}'.format(msg))
        sock.sendall(msg)

        # TODO: the server should be sending you back your message as a series
        #       of 16-byte chunks. Accumulate the chunks you get to build the
        #       entire reply from the server. Make sure that you have received
        #       the entire message and then you can break the loop.
        #
        #       Log each chunk you receive.  Use the print statement below to
        #       do it. This will help in debugging problems
        chunk = ''

        #logger.debug('len(msg) ->"%s"', chunk_expected)
        while len(received_message) < len(msg):
            chunk = sock.recv(16)
            print('received "{0}"'.format(chunk.decode('utf8')),
                  file=log_buffer)
            received_message += chunk.decode()

            if len(chunk) < 16:
                break

    finally:
        # TODO: after you break out of the loop receiving echoed chunks from
        #       the server you will want to close your client socket.
        print('closing socket', file=log_buffer)
        sock.close()
        # TODO: when all is said and done, you should return the entire reply
        # you received from the server as the return value of this function.
        #return ''.join(received_message)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage = '\nusage: python echo_client.py "this is my message"\n'
        print(usage, file=sys.stderr)
        sys.exit(1)

    msg = sys.argv[1]
    client(msg)
