# -*- coding: utf-8 -*-#
import fileinput


def get_request_url():
    url_list = []
    for line in fileinput.input("request_url.txt"):
        url_list.append(line.strip())
    return url_list


def get_account():
    for line in fileinput.input("bohao.txt"):
        if fileinput.lineno() == 1:
            account = line.strip()
        else:
            password = line.strip()
    print(account,password)
    return account,password




if __name__ == '__main__':
    url_list = get_request_url()
    print(url_list)
