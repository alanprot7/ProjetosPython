# coding: utf-8

import io
import sys
import urllib.request as request

BUFFER_SIZE = 1024


def donwload_lenght(response, output, length):
    times = length // BUFFER_SIZE
    if length % BUFFER_SIZE > 0:
        times += 1

    for time in range(times):
        output.write(response.read(BUFFER_SIZE))
        print("Downloaded %d" % (((time * BUFFER_SIZE)/length)*100))


def donwload(response, output):
    total_donwloaded = 0
    while True:
        data = response.read(BUFFER_SIZE)
        total_donwloaded += len(data)
        if not data:
            break
        output.write(data)
        print("Donwloaded {bytes}".format(bytes=total_donwloaded))


def main():
    response = request.urlopen(sys.argv[1])
    output = io.FileIO("saida.zip", mode="w")

    content_length = response.getheader("Content-Length")
    if content_length:
        length = int(content_length)
        donwload_lenght(response, output, length)
    else:
        donwload(response, output)

    response.close()
    output.close()
    print("Finished")


if __name__ == "__main__":
    main()
