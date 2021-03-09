import collections


def print_n(s: str):
    so_list = s.split(';')
    so_dic = collections.defaultdict(list)
    n_file_set = set()
    y_file_set = set()
    for so in so_list:
        so_fils = so.split(":")
        key = so_fils[0]
        val = so_fils[1].split(",")
        so_dic[key] = [i.split() for i in val]
        for f in so_dic[key]:
            if f[1] == 'N':
                n_file_set.add(f[0])
            else:
                y_file_set.add(f[0])
    for y in y_file_set:
        if y in n_file_set:
            n_file_set.remove(y)
    for k in so_dic.keys():
        v = so_dic[k]
        index = 0
        while len(v) > 0 and index < len(v):
            if v[index][0] not in n_file_set:
                v.pop(index)
                continue
            index += 1
    result = "OUT:"
    for k in so_dic.keys():
        re = ""
        if len(so_dic[k]) != 0:
            re = f"{k}:"
            for f in so_dic[k]:
                re += f'{f[0]},'
            re = re[:-1]
        if len(re) != 0:
            re += ';'
        result += re
    if len(result) != 4:
        result = result[:-1]
    return result


if __name__ == '__main__':
    x = 'a.so:f1 N,f2 N,f3 Y,f4 N;b.so:f4 Y,f5 N'
    print_n(x)
