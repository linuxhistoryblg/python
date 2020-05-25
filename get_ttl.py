# Ping and capture TTL
from subprocess import run

def ping_one(args):
    '''
    ping_one(args) : Ping a given host 1 time and return ttl.
    Expects a three item list as argument.
    Example:
    get_ttl.ping_one(['ping','-c1','192.168.1.20'])
    See: https://subinsb.com/default-device-ttl-values/
    for ttl to OS crosswalk.
    dcd
    '''
    # Call ping, capture output, decode to str, split to list
    run_output=run(args,capture_output=True).stdout.decode().split()

    # Walk thru run_output, get 'ttl=64', split and keep 64 as int
    for item in run_output:
        if item.startswith('ttl'):
            ttl = int(item.split(sep='=')[1])
    return ttl

if __name__ == '__main__':
    # Set up args
    args=['ping','-c1','192.168.1.20']
    ttl = ping_one(args)
    # Print <host> has <TTL> ttl.
    print('{} has {} ttl.'.format(args[2],ttl))
