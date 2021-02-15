import os,sys,time,re

pid = os.getpid()

while (input != "exit"):
    if 'PS1' is os.environ:
        os.write(1, os.environ['PS1'].encode())
    else:
        os.write(1, ("$ ").encode())

        input = os.read(0,1000).decode()

        if("exit" in input):
            os.write(1,("GoodBye User!\n").encode())
            sys.exit(0)

            rc = os.fork()

            if rc < 0:
                os.write(2, 'Fork failed!\n'.encode())
                sys.exit(1)

            elif rc == 0:
                 for dir in re.split(":", os.environ['PATH']):
                     program = "%s/%s" % (dir, Input[0])

                     try:
                         os.execve(program, Input, os.environ)
                     except FileNotFoundError:
                         pass

                     os.write(2, ("Couldn't do commands! %s\n" % input[0]).encode())
                     sys.exit(1)
                     

                 else:
                     childPidCode = os.wait()
                     os.write(1, ("Parent: Child %d terminated with exit code %d\n" % childPidCode).encode())
