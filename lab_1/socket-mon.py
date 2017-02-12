import psutil


def process_ip_port(input):
    p = '\"' + input[0] + '@' + str(input[1]) + '\"'
    return p


def process_connection(connection):
    pid = connection.pid
    laddr = connection.laddr
    raddr = connection.raddr
    status = connection.status
    out = None
    if laddr != () and raddr != ():
        out = '\"' + str(pid) + '\"' + ',' + process_ip_port(laddr) + ',' + process_ip_port(raddr) + ',' + '\"' + str(status) + '\"'
    return (pid, out)


def run():
    connections = psutil.net_connections(kind='tcp')
    conn_map = {}
    for connection in connections:
        pid, out = process_connection(connection)
        if out is not None:
            if (pid not in conn_map):
                conn_map[pid] = [out]
            else:
                conn_map[pid].append(out)
    sorted_map = sorted(conn_map.items(), key = lambda x: len(x[1]),reverse = True)
    print '"pid","laddr","raddr","status"'
    for k,v in sorted_map:
        for i in v:
            print i

if __name__ == "__main__":
    run()

