"""
Peer believes that they have discovered a bug in the `pypdl` module, where the 'ranges' header used when performing
downloads may not properly clear when restarting a download when a custom "User-Agent" field is supplied. They also
believe this is a bug specifically in the pypdl module and don't know how to properly fix it. I've got a few days before
uni starts up again so this seemed like an interesting challenge.

They insist that the following code will reproduce the bug, but the servers used to test this aren't publicly
accessible and is still searching for another server to test this against.
"""
from pypdl import Pypdl

download_list = [
    ""              # URLs go here?
]

# custom user agent to bypass dumb "anti-bot" blocks. apparently the use of a custom user agent was how the bug
# was discovered.
dl = Pypdl(allow_reuse=True, headers={
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0"
})
dl.logger.setLevel('DEBUG')  # Enable Debug messages

for download in download_list:
    # Apparently the download also needs to be segmented as well, since that uses the 'ranges' header
    dl.start(download, block=True, segments=2)

    while dl.wait:
        print(f"Waiting for download from {download}...")

    print()

    while not dl.completed:
        print(f"Downloading from {download}...")


