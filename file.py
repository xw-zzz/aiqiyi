# -*- coding: utf-8 -*-#
import fileinput


def get_request_url():
    url_list = []
    for line in fileinput.input("request_url.txt"):
        url_list.append(line.strip())
    return url_list
if __name__ == '__main__':
    url_list = get_request_url()
    print(url_list)