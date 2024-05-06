CC = gcc
CFLAGS = -O2 -Wall -I .
LIB = -lpthread

all: echoclient echoservers

echoclient: echoclient.c csapp.o
	$(CC) $(CFLAGS) -o echoclient echoclient.c csapp.o $(LIB)

echoservers: echoservers.c csapp.o
	$(CC) $(CFLAGS) -o echoserver echoservers.c csapp.o $(LIB)

csapp.o: csapp.c
	$(CC) $(CFLAGS) -c csapp.c

clean:
	rm -f *.o echoclient echoserver *~