import click
from smartcard.System import readers
from smartcard.util import toHexString


class AdpuCommands:
    get_uid = [0xFF, 0xCA, 0x00, 0x00, 0x00]


commands = AdpuCommands()

@click.group()
def main():
    pass


@main.command(name="test")
def sample():
    r = readers()
    print(r)

    conn = r[0].createConnection()
    conn.connect()

    data, sw1, sw2 = conn.transmit(commands.get_uid)

    print("UID={}\tstatus1={}\tstatus2={}".format(data, sw1, sw2))



if __name__ == '__main__':
    sample()